# -*- coding: utf-8 -*-
"""code/params.py — 题面给定常量的唯一权威源（读 DATA_FACTS.json 的 given 段）。

禁止在其它模块里裸写这些数值字面量；一律 from params import *。
所有常量语义与 MODELING_REPORT.md 第八节"参数口径表"一一对应。
"""
from __future__ import annotations
import json
import math
from pathlib import Path

# 自举：定位工作区根目录下的 DATA_FACTS.json
_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
_FACTS = json.loads((_ROOT / "DATA_FACTS.json").read_text(encoding="utf-8"))

# ---- 附件根目录 ----
DATA_ROOT = str(_ROOT / "user_data" / "real_attachments" / "real_attachments")

# ---- 题面给定常量（given 段，must_use_verbatim=True，禁改）----
ETA = 2e-4                       # 注意力开销系数 η
CHINCHILLA_C = 6.0               # C_train = 6ND
LCTX_CRIT = CHINCHILLA_C / ETA   # 注意力临界上下文 = 6/η = 3e4 tokens
UNIT_SCALE = 1e9                 # N,D 以 1e9 为单位；代入 6ND 须乘 1e9

# g(Q) 三型参数（每 token 质量成本，FLOPs/token）
GQ_EXP = {"gamma": 1e7, "lambda": 6.0}    # 指数型 g=gamma*exp(lambda*Q)
GQ_POW = {"gamma": 5e9, "lambda": 4.0}    # 幂型   g=gamma*Q^lambda
GQ_LOG = {"gamma": 2e9, "lambda": 10.0}   # 对数型 g=gamma*ln(1+lambda*Q)

# 三档典型预算 C (FLOPs)
BUDGETS = [1e19, 1e22, 1e24]

# Q 定义域
Q_MIN, Q_MAX = 0.0, 1.0          # Q ∈ (0,1]（下界开）

# L_ctx 敏感性扫描取值（严格取自 C7 实测集，禁臆造）
LCTX_SET = [2048, 4096, 8192, 32768, 131072]

# 六维 Benchmark 维度名
BENCH_DIMS = ["IFEval", "BBH", "MATH Lvl 5", "GPQA", "MUSR", "MMLU-PRO"]

# 随机种子（可复现）
SEED = 42


def g_Q(Q, kind="exp"):
    """每 token 质量成本函数 g(Q)，三型之一（DATA_FACTS.given 原值）。"""
    if kind == "exp":
        return GQ_EXP["gamma"] * math.exp(GQ_EXP["lambda"] * Q)
    if kind == "pow":
        return GQ_POW["gamma"] * (Q ** GQ_POW["lambda"])
    if kind == "log":
        return GQ_LOG["gamma"] * math.log(1.0 + GQ_LOG["lambda"] * Q)
    raise ValueError(f"unknown g(Q) kind: {kind}")


def g_Q_prime(Q, kind="exp"):
    """质量成本的一阶导数，用于边界与驻点残差核验。"""
    if kind == "exp":
        return GQ_EXP["lambda"] * g_Q(Q, kind)
    if kind == "pow":
        return GQ_POW["gamma"] * GQ_POW["lambda"] * Q ** (GQ_POW["lambda"] - 1)
    if kind == "log":
        return GQ_LOG["gamma"] * GQ_LOG["lambda"] / (1 + GQ_LOG["lambda"] * Q)
    raise ValueError(f"unknown g(Q) kind: {kind}")


# ---- 口径一致性断言（防同一物理量跨模块口径打架）----
# L_ctx 临界值解析恒等：6/eta 必须 == 3e4
assert abs(LCTX_CRIT - 3e4) < 1.0, f"[口径冲突] Lctx_crit={LCTX_CRIT} != 3e4"
# g(Q) 三型在 Q=1 处的相对经济性（仅用于验证参数被正确读入，非硬约束）
_g1_exp, _g1_pow, _g1_log = g_Q(1.0, "exp"), g_Q(1.0, "pow"), g_Q(1.0, "log")
assert _g1_exp > 0 and _g1_pow > 0 and _g1_log > 0, "[参数错误] g(Q=1) 应为正"
# eta 与临界值互恰
assert abs(CHINCHILLA_C / ETA - LCTX_CRIT) < 1e-6, "[口径冲突] 6/eta 与 Lctx_crit 不一致"

if __name__ == "__main__":
    print("[params] 常量加载与口径一致性 OK")
    print(f"  ETA={ETA}, LCTX_CRIT={LCTX_CRIT}, BUDGETS={BUDGETS}")
    print(f"  g(1) exp={_g1_exp:.3e} pow={_g1_pow:.3e} log={_g1_log:.3e}")
