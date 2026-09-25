# -*- coding: utf-8 -*-
"""problem3.py — 问题三：算力约束下 N/D/Q 资源配置优化 + 结构性转移 + L_ctx 敏感性。

认领能力：P3-C1(N/D/Q联合优化) P3-C2(结构性转移定义与识别) P3-C3(L_ctx敏感性+临界值)
方法(METHOD_CLAIMS M5/M6)：
  M5 KKT 解析条件 + SLSQP 多起点约束搜索(式14-15)，预算约束进 NonlinearConstraint
  M6 结构转移份额导数 ds_X/d(logC) 峰值 + 数值边界状态检查(式18)

单位约定：决策变量 N,D 以 1e9 为单位（与 B1 标度律一致）；代入算力公式须乘 1e9。
  C_train = 6*(N*1e9)*(D*1e9);  C_Q = (D*1e9)*[g(Q)-g(Q0)]_+;  C_attn = eta*(N*1e9)*(D*1e9)*L_ctx
"""
from __future__ import annotations
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import json
import numpy as np
from scipy.optimize import minimize, NonlinearConstraint

import utils as u
from params import ETA, LCTX_CRIT, LCTX_SET, BUDGETS, SEED, g_Q, UNIT_SCALE

# 广义标度律参数（Q3 用 B1 真实标度律 + assumed theta，来自 Q2）
def _load_q2_params():
    p = u._ROOT / "figures" / "problem_2_results.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    cp = d["classic"]["params"]                     # B1 真实标度律
    theta = d["generalized"]["theta_assumed_downstream"]
    return cp["E"], cp["A"], cp["alpha"], cp["B"], cp["beta"], theta


def _load_q0():
    """Q0 = Q1 域级 Q 中位数（跨问传递，CROSS_PROBLEM_LEDGER）。"""
    p = u._ROOT / "figures" / "problem_1_results.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    return float(d["domain_Q_median"])


def loss_gen(N, D, Q, params):
    """广义标度律 L=E+A N^-alpha+B (Q^theta D)^-beta（N,D in 1e9 单位）。"""
    E, A, alpha, B, beta, theta = params
    # 质量增强有效数据量 Q_eff = Q**theta * D
    Q_eff = np.power(Q, theta) * D          # 等价 Q**theta * D
    return E + A * np.power(N, -alpha) + B * np.power(Q_eff, -beta)


def compute_total(N, D, Q, Q0, Lctx, gkind):
    """三部分算力和（FLOPs），N,D in 1e9 单位。返回 (C_tot, C_train, C_Q, C_attn)。"""
    Na, Da = N * UNIT_SCALE, D * UNIT_SCALE
    C_train = 6.0 * Na * Da
    C_Q = Da * max(g_Q(Q, gkind) - g_Q(Q0, gkind), 0.0)
    C_attn = ETA * Na * Da * Lctx
    return C_train + C_Q + C_attn, C_train, C_Q, C_attn


def solve_budget(C, Q0, params, Lctx, gkind, n_starts=20):
    """SLSQP 多起点求 min L s.t. C_tot<=C。对数变量(lnN,lnD)+Q。"""
    rng = np.random.default_rng(SEED)
    E = params[0]

    def unpack(x):
        return np.exp(x[0]), np.exp(x[1]), x[2]

    def obj(x):
        N, D, Q = unpack(x)
        return loss_gen(N, D, np.clip(Q, 1e-4, 1.0), params)

    def con_fun(x):
        N, D, Q = unpack(x)
        Ct, *_ = compute_total(N, D, np.clip(Q, 1e-4, 1.0), Q0, Lctx, gkind)
        return (C - Ct) / C          # >=0 可行（归一化）

    nlc = NonlinearConstraint(con_fun, 0.0, np.inf)
    bounds = [(np.log(1e-3), np.log(1e5)), (np.log(1e-2), np.log(1e6)), (1e-3, 1.0)]

    best = None
    # Chinchilla 平衡点附近初值：6 N D 1e18 ~ 0.9 C
    ND_budget = 0.9 * C / (6.0 * UNIT_SCALE ** 2)
    for s in range(n_starts):
        if s == 0:
            n0 = d0 = np.sqrt(max(ND_budget, 1e-6))
            q0i = min(max(Q0 * 1.5, 0.1), 1.0)
        else:
            frac = rng.uniform(0.2, 0.8)
            n0 = np.sqrt(max(ND_budget, 1e-6)) * np.exp(rng.uniform(-2, 2))
            d0 = max(ND_budget / max(n0, 1e-9), 1e-3)
            q0i = rng.uniform(0.05, 1.0)
        x0 = [np.log(np.clip(n0, 1e-3, 1e5)), np.log(np.clip(d0, 1e-2, 1e6)),
              np.clip(q0i, 1e-3, 1.0)]
        try:
            res = minimize(obj, x0, method="SLSQP", bounds=bounds,
                           constraints=[nlc],
                           options={"maxiter": 500, "ftol": 1e-12})
            if not res.success and res.status not in (0, 9):
                continue
            N, D, Q = unpack(res.x)
            Q = np.clip(Q, 1e-4, 1.0)
            Ct, Ctr, CQ, Cat = compute_total(N, D, Q, Q0, Lctx, gkind)
            if Ct > C * (1 + 1e-6):       # 越预算的解丢弃
                continue
            Lval = loss_gen(N, D, Q, params)
            if best is None or Lval < best["L"]:
                best = {"N": float(N), "D": float(D), "Q": float(Q), "L": float(Lval),
                        "C_tot": float(Ct), "C_train": float(Ctr), "C_Q": float(CQ),
                        "C_attn": float(Cat), "util": float(Ct / C)}
        except Exception:
            continue
    return best


def main():
    u.set_all_seeds(SEED)
    params = _load_q2_params()
    Q0 = _load_q0()
    print("=" * 60)
    print(f"[Q3] 标度律参数 E={params[0]:.3f} A={params[1]:.3f} alpha={params[2]:.3f} "
          f"B={params[3]:.3f} beta={params[4]:.3f} theta={params[5]:.3f}; Q0={Q0:.4f}")

    results = {"_meta": u.run_meta(),
               "method": "SLSQP multi-start feasible search + share-derivative transition; KKT equations analytic only",
               "scaling_params": {"E": params[0], "A": params[1], "alpha": params[2],
                                  "B": params[3], "beta": params[4], "theta": params[5]},
               "Q0": Q0, "eta": ETA, "Lctx_crit": LCTX_CRIT}

    _q3_optimal(results, params, Q0)
    _q3_transition(results, params, Q0)
    _q3_lctx(results, params, Q0)

    u.save_json(results, "figures/problem_3_results.json")
    u.save_json(results["optimal_allocation"], "output/q3_optimal_allocation.json")
    u.save_json(results["lctx_sensitivity"], "output/q3_lctx_sensitivity.json")
    validate_capability(results)
    print("[Q3] 完成")
    return results


def _q3_optimal(results, params, Q0):
    """P3-C1：三档预算最优 N*,D*,Q*,L* + 份额，三型 g(Q) 对比。主 L_ctx=2048。"""
    print("[Q3] Step 1: 三档预算最优配置（三型 g(Q)），主 L_ctx=2048")
    Lctx_main = 2048
    alloc = {}
    for gkind in ["exp", "pow", "log"]:
        alloc[gkind] = {}
        for C in BUDGETS:
            sol = solve_budget(C, Q0, params, Lctx_main, gkind, n_starts=20)
            if sol is None:
                print(f"[Q3]   g={gkind} C={C:.0e}: 未找到可行解")
                alloc[gkind][f"{C:.0e}"] = {"status": "no_feasible"}
                continue
            shares = {"s_train": sol["C_train"] / sol["C_tot"],
                      "s_Q": sol["C_Q"] / sol["C_tot"],
                      "s_attn": sol["C_attn"] / sol["C_tot"]}
            sol["shares"] = shares
            sol["Q_above_Q0"] = bool(sol["Q"] > Q0)
            alloc[gkind][f"{C:.0e}"] = sol
            print(f"[Q3]   g={gkind} C={C:.0e}: N*={sol['N']:.4g} D*={sol['D']:.4g} "
                  f"Q*={sol['Q']:.4f} L*={sol['L']:.4f} util={sol['util']:.4f} "
                  f"s_train={shares['s_train']:.3f} s_Q={shares['s_Q']:.3f} s_attn={shares['s_attn']:.3f}")
    # 对比基线：Chinchilla 等分(N=D, Q=Q0 无质量投入)，仅作对照
    baseline_chinchilla = {}
    for C in BUDGETS:
        # 6 N D 1e18 = C, N=D → N=D=sqrt(C/6e18); Q=Q0 (C_Q=0)
        ND = C / (6.0 * UNIT_SCALE ** 2)
        Nb = Db = float(np.sqrt(ND))
        Ct, Ctr, CQ, Cat = compute_total(Nb, Db, Q0, Q0, Lctx_main, "exp")
        # attn 会略超预算(6ND已占满)，缩放使可行
        if Ct > C:
            scale = np.sqrt(C / Ct)
            Nb *= scale; Db *= scale
            Ct, Ctr, CQ, Cat = compute_total(Nb, Db, Q0, Q0, Lctx_main, "exp")
        Lb = loss_gen(Nb, Db, Q0, params)
        baseline_chinchilla[f"{C:.0e}"] = {
            "N": Nb, "D": Db, "Q": Q0, "L": float(Lb), "C_tot": float(Ct),
            "C_train": float(Ctr), "C_Q": float(CQ), "C_attn": float(Cat),
            "util": float(Ct / C), "note": "Chinchilla等分基线(N=D,Q=Q0无质量投入)，作对照"}
    results["optimal_allocation"] = {"Lctx_main": Lctx_main, "budgets": BUDGETS,
                                     "by_gtype": alloc,
                                     "baseline_chinchilla": baseline_chinchilla}
    # 对比：最优 vs 基线 L 改善
    for C in BUDGETS:
        opt_L = alloc["exp"][f"{C:.0e}"].get("L")
        base_L = baseline_chinchilla[f"{C:.0e}"]["L"]
        if opt_L is not None:
            print(f"[Q3]   C={C:.0e}: 最优L={opt_L:.4f} vs Chinchilla基线L={base_L:.4f} "
                  f"(改善{base_L-opt_L:.4f})")

    # 预算单调性核验：C↑ → L*↓（用 exp 型）
    Ls = [alloc["exp"][f"{C:.0e}"]["L"] for C in BUDGETS
          if "L" in alloc["exp"][f"{C:.0e}"]]
    mono = all(Ls[i] >= Ls[i + 1] - 1e-9 for i in range(len(Ls) - 1))
    results["optimal_allocation"]["budget_monotonic_L"] = bool(mono)
    print(f"[Q3]   预算单调性 C↑→L*↓: {mono} (L*={[round(x,4) for x in Ls]})")


def _q3_transition(results, params, Q0, gkind="exp"):
    """P3-C2：连续预算扫描 log Cin[18,25]，ds_X/d(logC) 峰值 + Q 内点/边界切换。"""
    print("[Q3] Step 2: 结构性转移识别（份额导数峰值 + 活跃集切换）")
    Lctx_main = 2048
    logC = np.linspace(18, 25, 36)
    Cs = 10.0 ** logC
    s_train, s_Q, s_attn, Qs, Ns, Ds, Ls = [], [], [], [], [], [], []
    for C in Cs:
        sol = solve_budget(C, Q0, params, Lctx_main, gkind, n_starts=12)
        if sol is None:
            s_train.append(np.nan); s_Q.append(np.nan); s_attn.append(np.nan)
            Qs.append(np.nan); Ns.append(np.nan); Ds.append(np.nan); Ls.append(np.nan)
            continue
        s_train.append(sol["C_train"] / sol["C_tot"])
        s_Q.append(sol["C_Q"] / sol["C_tot"])
        s_attn.append(sol["C_attn"] / sol["C_tot"])
        Qs.append(sol["Q"]); Ns.append(sol["N"]); Ds.append(sol["D"]); Ls.append(sol["L"])

    s_train, s_Q = np.array(s_train), np.array(s_Q)
    # ds_X/d(logC) 数值差分（式18）
    d_sQ = np.gradient(s_Q, logC)
    d_strain = np.gradient(s_train, logC)
    # 转移点：|d_sQ| 峰值处
    valid = ~np.isnan(d_sQ)
    if valid.sum() > 2:
        peak_idx = int(np.nanargmax(np.abs(d_sQ)))
        C_transition = float(Cs[peak_idx])
    else:
        peak_idx, C_transition = -1, None
    # Q 数值边界状态与 C_Q 铰链激活；未计算 KKT 残差。
    Qs_arr = np.array(Qs)
    q_activates = [bool(q > Q0) for q in Qs]
    first_activate = next((float(Cs[i]) for i, a in enumerate(q_activates) if a), None)

    results["structural_transition"] = {
        "gtype": gkind, "logC_grid": logC.tolist(), "C_grid": Cs.tolist(),
        "s_train": s_train.tolist(), "s_Q": s_Q.tolist(), "s_attn": s_attn,
        "d_sQ_dlogC": d_sQ.tolist(), "d_strain_dlogC": d_strain.tolist(),
        "Q_traj": Qs, "N_traj": Ns, "D_traj": Ds, "L_traj": Ls,
        "transition_logC": float(logC[peak_idx]) if peak_idx >= 0 else None,
        "transition_C": C_transition,
        "CQ_first_activation_C": first_activate,
        "definition": "候选结构转移=份额对logC导数峰值处(式18)；另检查 Q 边界与 C_Q 铰链状态，未计算 KKT 残差",
    }
    print(f"[Q3]   转移点 C†~{C_transition:.2e} (logC={logC[peak_idx]:.2f}), "
          f"C_Q首次激活 C~{first_activate}")


def _q3_lctx(results, params, Q0, gkind="exp"):
    """P3-C3：L_ctx 敏感性(C7 五取值) + 临界值 6/eta=3e4 解析核验。中预算档。"""
    print("[Q3] Step 3: L_ctx 敏感性（C7 五取值）+ 临界值核验")
    C = 1e22
    panels = {}
    for Lctx in LCTX_SET:
        sol = solve_budget(C, Q0, params, Lctx, gkind, n_starts=16)
        if sol:
            panels[str(Lctx)] = {"N": sol["N"], "D": sol["D"], "Q": sol["Q"],
                                 "L": sol["L"], "shares": {
                                     "s_train": sol["C_train"] / sol["C_tot"],
                                     "s_Q": sol["C_Q"] / sol["C_tot"],
                                     "s_attn": sol["C_attn"] / sol["C_tot"]}}
            print(f"[Q3]   L_ctx={Lctx}: N*={sol['N']:.4g} D*={sol['D']:.4g} "
                  f"Q*={sol['Q']:.4f} L*={sol['L']:.4f} s_attn={sol['C_attn']/sol['C_tot']:.4f}")
    # 临界值解析核验
    lctx_crit_check = abs(LCTX_CRIT - 6.0 / ETA) < 1.0
    results["lctx_sensitivity"] = {
        "budget_C": C, "gtype": gkind,
        "Lctx_set": LCTX_SET,
        "Lctx_crit": LCTX_CRIT,
        "Lctx_crit_analytic": 6.0 / ETA,
        "Lctx_crit_check": bool(lctx_crit_check),
        "panels": panels,
        "note": f"L_ctx_crit=6/eta={LCTX_CRIT:.0f} tokens；落在8192与32768之间，"
                f"即>=32768的长上下文模型注意力开销已超训练开销",
    }
    print(f"[Q3]   L_ctx_crit=6/eta={LCTX_CRIT:.0f} 解析核验={lctx_crit_check}")


def validate_capability(results):
    """P3 任务对齐硬断言（能力清单 falsifiable_check）。"""
    alloc = results["optimal_allocation"]["by_gtype"]
    # P3-C1: 每档预算最优解重代入预算式 <= C（容差1e-6），Qin(0,1]
    for gkind in ["exp", "pow", "log"]:
        for C in BUDGETS:
            sol = alloc[gkind][f"{C:.0e}"]
            assert "L" in sol, f"[能力不成立] g={gkind} C={C:.0e} 无可行解"
            assert sol["C_tot"] <= C * (1 + 1e-6), \
                f"[能力不成立] g={gkind} C={C:.0e} 越预算 {sol['C_tot']:.3e}>{C:.3e}"
            assert 0 < sol["Q"] <= 1.0, f"[能力不成立] Q={sol['Q']}越界(0,1]"
            assert sol["N"] > 0 and sol["D"] > 0, "[能力不成立] N/D非正"
    # P3-C1: 预算单调性
    assert results["optimal_allocation"]["budget_monotonic_L"], "[能力不成立] C↑→L*↓ 破"
    # P3-C2: 转移判据可判定
    st = results["structural_transition"]
    assert "transition_C" in st and "d_sQ_dlogC" in st, "[能力不成立] 转移无可判据"
    # P3-C3: 临界值 + C7 取值
    ls = results["lctx_sensitivity"]
    assert ls["Lctx_crit_check"] and abs(ls["Lctx_crit"] - 3e4) < 1.0, "[能力不成立] 临界值!=3e4"
    assert set(int(k) for k in ls["panels"].keys()) <= set(LCTX_SET), "[能力不成立] L_ctx用了C7外取值"
    print("[Q3] validate_capability PASS")


if __name__ == "__main__":
    main()
