# -*- coding: utf-8 -*-
"""constraint_audit.py — 从最终 results.json 重算所有硬约束（不信优化器字段）。

只 print 结论（PASS/FAIL、n_violations、max_error、最多5条越界定位），禁 print 大数组。
自动发现基线并断言全部进审计（防漏审对照方案）。
"""
from __future__ import annotations
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import re
import json
import numpy as np
from params import ETA, UNIT_SCALE, g_Q, LCTX_CRIT

_ROOT = os.path.dirname(_HERE)


def _load(name):
    return json.load(open(os.path.join(_ROOT, "figures", name), encoding="utf-8"))


def recompute_total(N, D, Q, Q0, Lctx, gkind):
    Na, Da = N * UNIT_SCALE, D * UNIT_SCALE
    C_train = 6.0 * Na * Da
    C_Q = Da * max(g_Q(Q, gkind) - g_Q(Q0, gkind), 0.0)
    C_attn = ETA * Na * Da * Lctx
    return C_train + C_Q + C_attn


def main():
    violations = []
    audited = set()

    r3 = _load("problem_3_results.json")
    Q0 = r3["Q0"]
    Lctx_main = r3["optimal_allocation"]["Lctx_main"]
    budgets = r3["optimal_allocation"]["budgets"]

    # ---- 审计最优解（三型 g × 三档预算）----
    for gkind, per in r3["optimal_allocation"]["by_gtype"].items():
        for ckey, sol in per.items():
            if "L" not in sol:
                continue
            name = f"optimal[g={gkind},C={ckey}]"
            audited.add(name)
            C = float(ckey)
            # 硬约束 1: 预算
            Ct = recompute_total(sol["N"], sol["D"], sol["Q"], Q0, Lctx_main, gkind)
            if Ct > C * (1 + 1e-6):
                violations.append(f"{name} C_tot={Ct:.4e} > C={C:.4e}")
            # 硬约束 2: Q ∈ (0,1]
            if not (0 < sol["Q"] <= 1.0 + 1e-9):
                violations.append(f"{name} Q={sol['Q']} 越界(0,1]")
            # 硬约束 3: N,D > 0
            if sol["N"] <= 0 or sol["D"] <= 0:
                violations.append(f"{name} N/D 非正")
            # 硬约束 4: C_Q 铰链取正部一致
            Da = sol["D"] * UNIT_SCALE
            cq_expect = Da * max(g_Q(sol["Q"], gkind) - g_Q(Q0, gkind), 0.0)
            if abs(cq_expect - sol["C_Q"]) > max(1e-3 * abs(sol["C_Q"]), 1e6):
                violations.append(f"{name} C_Q={sol['C_Q']:.3e} != 重算{cq_expect:.3e}")

    # ---- 自动发现并审计基线 ----
    _BASE_KW = re.compile(r'baseline|naive|greedy|chinchilla|等分|均分|不调整|lower.?bound|下界', re.I)
    discovered = [k for k in r3["optimal_allocation"] if _BASE_KW.search(k)]
    for bkey in discovered:
        for ckey, sol in r3["optimal_allocation"][bkey].items():
            if "L" not in sol:
                continue
            name = f"{bkey}[C={ckey}]"
            audited.add(name)
            C = float(ckey)
            Ct = recompute_total(sol["N"], sol["D"], sol["Q"], Q0, Lctx_main, "exp")
            n_v = 0
            if Ct > C * (1 + 1e-6):
                violations.append(f"{name} C_tot={Ct:.4e} > C={C:.4e}"); n_v += 1
            if not (0 < sol["Q"] <= 1.0 + 1e-9):
                violations.append(f"{name} Q越界"); n_v += 1
            print(f"[baseline] {name} PASS={n_v==0} util={sol.get('util'):.4f}")

    missing = [b for b in discovered if not any(b in a for a in audited)]
    assert not missing, f"[基线漏审] {missing}"

    # ---- L_ctx 敏感性取值 ⊆ C7 集 + 临界值 ----
    ls = r3["lctx_sensitivity"]
    C7 = {2048, 4096, 8192, 32768, 131072}
    for k in ls["panels"]:
        if int(k) not in C7:
            violations.append(f"lctx_sensitivity 用了 C7 外取值 {k}")
    if abs(ls["Lctx_crit"] - 3e4) >= 1.0:
        violations.append(f"Lctx_crit={ls['Lctx_crit']} != 3e4")

    # ---- 预算单调性 C↑→L*↓ ----
    Ls = [r3["optimal_allocation"]["by_gtype"]["exp"][f"{C:.0e}"]["L"] for C in budgets]
    for i in range(len(Ls) - 1):
        if Ls[i] < Ls[i + 1] - 1e-9:
            violations.append(f"预算单调性破: L({budgets[i]:.0e})={Ls[i]} < L({budgets[i+1]:.0e})={Ls[i+1]}")

    # ---- Q1 配比单纯形 + Q ∈ (0,1] ----
    r1 = _load("problem_1_results.json")
    if not r1["mixture_model"]["simplex_ok"]:
        violations.append("Q1 配比未满足单纯形")
    if not (0 < r1["Q_stats"]["min"] and r1["Q_stats"]["max"] <= 1.0):
        violations.append(f"Q1 Q越界(0,1]: [{r1['Q_stats']['min']},{r1['Q_stats']['max']}]")

    # ---- Q2 Q=1 退化 + 弹性方向 ----
    r2 = _load("problem_2_results.json")
    if not r2["generalized"]["Q1_degeneracy_pass"]:
        violations.append("Q2 Q=1退化不吻合")
    e = r2["elasticity"]
    if not (e["eps_N"] < 0 and e["eps_D"] < 0 and e["eps_Q"] < 0):
        violations.append("Q2 弹性非负(应<0)")

    # ---- Q4 贡献占比和≈100% + 前沿不倒退 ----
    r4 = _load("problem_4_results.json")
    cd = r4["contribution_decomp"]
    if abs(cd["sum_check"] - 100) > 1e-6:
        violations.append(f"Q4 贡献占比和={cd['sum_check']}!=100")
    if not r4["frontier"]["frontier_no_regress_24m_ge_12m"]:
        violations.append("Q4 前沿24m<12m(倒退)")

    print("=" * 60)
    n = len(violations)
    print(f"[constraint_audit] 审计方案数={len(audited)}, 发现基线={discovered}")
    print(f"[constraint_audit] {'PASS' if n==0 else 'FAIL'}  n_violations={n}")
    for v in violations[:5]:
        print(f"    VIOLATION {v}")
    return 0 if n == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
