# -*- coding: utf-8 -*-
"""prep_q4_decomp.py — 把问题四的规模/非规模贡献分解细化到月度网格。

problem_4_results.json 里的 yearly_evolution 只有 2024/2025 两个点，画不出
堆叠面积图的演化形状。本脚本沿用 problem4.py::_p4_decomp 的同一个 OLS 模型
（Cap ~ lnN + year）与同一个增长核算恒等式，只把评估时点从"整年"换成"月末
累计"，不重新拟合第二套系数：

  Δf_scale(t)    = b_lnN · [ mean(lnN | year<=t) - mean(lnN | 早期窗口) ]
  Δh_nonscale(t) = c_year · [ mean(year | year<=t) - mean(year | 早期窗口) ]
  占比(t)        = 100 · Δ· / (Δf + Δh)

系数 b_lnN / c_year / 早期窗口由重新拟合复现并对已发布值硬断言，保证与论文
正文数字同源。输出 figures/_prep_q4.json。
"""
from __future__ import annotations
import json
import os
import sys

import numpy as np
import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
_CODE = os.path.join(_ROOT, "code")
for p in (_ROOT, _CODE):
    if p not in sys.path:
        sys.path.insert(0, p)

import utils as u                      # noqa: E402
from problem4 import _load_leaderboard, _fit_ols  # noqa: E402
from params import SEED                # noqa: E402

OUT_JSON = os.path.join(_HERE, "_prep_q4.json")


def main():
    u.set_all_seeds(SEED)
    published = json.loads(
        open(os.path.join(_HERE, "problem_4_results.json"), encoding="utf-8").read()
    )["contribution_decomp"]

    lb = _load_leaderboard()

    d = lb.dropna(subset=["Cap", "Params_B", "year"]).copy()
    d = d[(d["Params_B"] > 0) & (d["Cap"] > 0)]
    d["lnN"] = np.log(d["Params_B"])

    m = _fit_ols(d, ["lnN", "year"])
    b_N, c_t = float(m.params["lnN"]), float(m.params["year"])

    # 硬断言：复现的系数/样本量必须与已发布结果一致（同一模型，不是第二套拟合）
    assert abs(b_N - published["b_lnN"]) < 1e-9, f"b_lnN 不符 {b_N} vs {published['b_lnN']}"
    assert abs(c_t - published["c_year"]) < 1e-9, f"c_year 不符 {c_t} vs {published['c_year']}"
    assert abs(float(m.rsquared) - published["r2"]) < 1e-9, "R2 不符"
    assert int(len(d)) == published["n"], f"样本量不符 {len(d)} vs {published['n']}"
    print(f"[prep-q4] OLS 复现一致 ✓ b_lnN={b_N:.4f} c_year={c_t:.4f} "
          f"R2={m.rsquared:.4f} n={len(d)}")

    t0, t1 = float(d["year"].quantile(0.1)), float(d["year"].quantile(0.9))
    assert abs(t0 - published["window"]["t0"]) < 1e-9, "早期窗口 t0 不符"
    assert abs(t1 - published["window"]["t1"]) < 1e-9, "晚期窗口 t1 不符"
    early = d[d["year"] <= t0]
    lnN_early = float(early["lnN"].mean())
    year_early = float(early["year"].mean())

    # 月度网格：早期窗口右端 → 样本最晚时点
    t_lo, t_hi = t0, float(d["year"].max())
    grid = np.arange(np.ceil(t_lo * 12) / 12.0, t_hi + 1e-9, 1.0 / 12.0)

    rows = []
    for t in grid:
        sub = d[d["year"] <= t]
        if len(sub) < 30:            # 累计样本太少时占比噪声主导，不出点
            continue
        f_t = b_N * (float(sub["lnN"].mean()) - lnN_early)
        h_t = c_t * (float(sub["year"].mean()) - year_early)
        tot = f_t + h_t
        if abs(tot) < 1e-9:
            continue
        rows.append({
            "t": float(t),
            "n_cum": int(len(sub)),
            "delta_f_scale": float(f_t),
            "delta_h_nonscale": float(h_t),
            "delta_total": float(tot),
            "scale_pct": float(100.0 * f_t / tot),
            "nonscale_pct": float(100.0 * h_t / tot),
            "mean_lnN_cum": float(sub["lnN"].mean()),
            "mean_year_cum": float(sub["year"].mean()),
        })
    assert rows, "月度网格为空"

    # 与已发布的窗口口径结果对账（晚期窗口均值处应还原 scale_pct）
    late = d[d["year"] >= t1]
    f_w = b_N * (float(late["lnN"].mean()) - lnN_early)
    h_w = c_t * (float(late["year"].mean()) - year_early)
    scale_pct_w = 100.0 * f_w / (f_w + h_w)
    assert abs(scale_pct_w - published["scale_pct"]) < 1e-6, \
        f"窗口口径 scale_pct 不符 {scale_pct_w} vs {published['scale_pct']}"
    print(f"[prep-q4] 窗口口径复现一致 ✓ scale_pct={scale_pct_w:.3f}%")

    out = {
        "model": published["model"],
        "b_lnN": b_N, "c_year": c_t, "r2": float(m.rsquared), "n": int(len(d)),
        "window": {"t0": t0, "t1": t1,
                   "lnN_early": lnN_early, "year_early": year_early},
        "grid_note": "月度网格 = 累计到 t 的样本均值 lnN 代入同一增长核算恒等式；"
                     "系数与早期窗口基准均与 problem_4_results.json 同源",
        "monthly": rows,
        "window_checkpoint": {"scale_pct": scale_pct_w,
                              "nonscale_pct": 100.0 - scale_pct_w},
        "source": "C1 leaderboard_enhanced.csv 全量 4576 行（有效样本 %d）" % len(d),
        "seed": SEED,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
    print(f"[prep-q4] 写出 {OUT_JSON}（{len(rows)} 个月度点）")


if __name__ == "__main__":
    main()
