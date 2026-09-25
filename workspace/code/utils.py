# -*- coding: utf-8 -*-
"""code/utils.py — 公共工具：路径自举、随机种子、数据摄入核验、结果保存。"""
from __future__ import annotations

# 自举模块路径（让 sibling import 不依赖调用方式）
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import json
import glob
import lzma
import random
from pathlib import Path

import numpy as np
import pandas as pd

from params import DATA_ROOT, SEED

_ROOT = Path(_HERE).parent


def set_all_seeds(seed: int = SEED):
    """固定所有随机源（可复现，第十一章）。"""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)


def dpath(rel: str) -> str:
    """附件相对路径 → 绝对路径。"""
    return os.path.join(DATA_ROOT, rel)


def _load_profile() -> dict:
    p = _ROOT / "DATA_PROFILE.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8")).get("files", {})
    return {}


_PROFILE = _load_profile()


def read_csv_checked(rel: str, expect_rows: int | None = None, **kw) -> pd.DataFrame:
    """读 CSV 并核对行数（对照 DATA_PROFILE.json，防静默截断）。"""
    df = pd.read_csv(dpath(rel), low_memory=False, **kw)
    prof = _PROFILE.get(rel.replace("/", os.sep)) or _PROFILE.get(rel)
    if prof and "total_rows" in prof and expect_rows is None:
        expect_rows = prof["total_rows"]
    if expect_rows is not None and len(df) != expect_rows:
        raise AssertionError(
            f"[摄入不全] {rel} 实读 {len(df)} 行 != 建档 {expect_rows} 行——"
            f"多半被截断，检查读取范围。")
    print(f"[data_ingest] {rel} 全量 {len(df)} 行已核对")
    return df


def read_jsonl_xz(rel: str, expect_rows: int | None = None):
    """逐行读 jsonl.xz（不抽样），核对行数。返回 list[dict]。"""
    recs = []
    with lzma.open(dpath(rel), "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                recs.append(json.loads(line))
    prof = _PROFILE.get(rel.replace("/", os.sep)) or _PROFILE.get(rel)
    if prof and "total_rows" in prof and expect_rows is None:
        expect_rows = prof["total_rows"]
    if expect_rows is not None and len(recs) != expect_rows:
        raise AssertionError(
            f"[摄入不全] {rel} 实读 {len(recs)} 行 != 建档 {expect_rows} 行")
    print(f"[data_ingest] {rel} 全量 {len(recs)} 行已核对")
    return recs


def save_json(obj, path: str):
    """原子保存 JSON（供 paper-figure / 审计读取）。"""
    p = _ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=_json_default),
                   encoding="utf-8")
    tmp.replace(p)
    print(f"[save] {path} ({p.stat().st_size} bytes)")


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.bool_,)):
        return bool(o)
    raise TypeError(f"not serializable: {type(o)}")


def save_csv(df: pd.DataFrame, path: str):
    p = _ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False, encoding="utf-8-sig")
    print(f"[save] {path} ({p.stat().st_size} bytes, {len(df)} rows)")


def run_meta() -> dict:
    """运行元信息（seed + 库版本），写入结果 JSON 头部。"""
    import scipy
    return {
        "seed": SEED,
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "pandas": pd.__version__,
    }


# ---- 单纯形投影（配比约束 sum p = 1, p >= 0）----
def simplex_projection(v: np.ndarray) -> np.ndarray:
    """欧氏投影到概率单纯形 {p: p>=0, sum p = 1}（Duchi et al. 2008）。"""
    v = np.asarray(v, dtype=float)
    n = len(v)
    u = np.sort(v)[::-1]
    css = np.cumsum(u)
    rho = np.nonzero(u * np.arange(1, n + 1) > (css - 1))[0][-1]
    theta = (css[rho] - 1) / (rho + 1.0)
    return np.maximum(v - theta, 0.0)


def softmax(z: np.ndarray) -> np.ndarray:
    """softmax 参数化单纯形（sum=1, >0）。"""
    z = np.asarray(z, dtype=float)
    e = np.exp(z - z.max())
    return e / e.sum()


if __name__ == "__main__":
    set_all_seeds()
    print("[utils] OK. meta:", run_meta())
    # 单纯形投影自检
    p = simplex_projection(np.array([0.5, 0.3, 0.9, -0.2]))
    assert abs(p.sum() - 1) < 1e-9 and (p >= 0).all()
    print("[utils] simplex_projection OK, sum=", p.sum())
