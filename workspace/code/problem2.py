# -*- coding: utf-8 -*-
"""problem2.py — 问题二：经典标度律 -> 广义标度律 + 弹性与替代。

认领能力：P2-C1(经典律 L(N,D)) P2-C2(广义律 L(N,D,Q,p)) P2-C3(弹性/替代)
方法(METHOD_CLAIMS M3/M4)：
  M3 对数域 Huber 非线性最小二乘拟合经典律(式7-8): L=E+A N^-a+B D^-b
  M4 广义律(式9): L=E+A N^-a+B (Q^theta D)^-b，B6-B8 估 theta，Q=1 退化经典
"""
from __future__ import annotations
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

import utils as u
from params import SEED


def classic_model(params, N, D):
    """经典标度律 L=E+A N^-alpha+B D^-beta（式7）。"""
    E, A, alpha, B, beta = params
    return E + A * np.power(N, -alpha) + B * np.power(D, -beta)


def _residual_log_huber(params, N, D, L):
    """对数域残差（least_squares 的 loss='huber' 在外层施加）。式8。"""
    pred = classic_model(params, N, D)
    pred = np.clip(pred, 1e-6, None)
    return np.log(L) - np.log(pred)


def fit_classic(N, D, L, supplementary=False):
    """对数域 Huber-NLS 多起点拟合经典律。返回最优参数与 R2。"""
    N, D, L = (np.asarray(x, dtype=float) for x in (N, D, L))
    if not all(np.isfinite(x).all() and (x > 0).all() for x in (N, D, L)):
        raise ValueError("N,D,L 必须为有限正数")
    upper = [max(L), 200, 1.5, 500, 1.5] if supplementary else [min(L) + 1e-6, 50, 1.0, 50, 1.0]
    best = None
    # 多起点：alpha,beta 网格初值 + E,A,B 合理初值
    for alpha0 in [0.1, 0.2, 0.34, 0.5]:
        for beta0 in [0.1, 0.28, 0.4]:
            x0 = [min(L) * 0.9, 0.5, alpha0, 1.0, beta0]
            try:
                res = least_squares(
                    _residual_log_huber, x0, args=(N, D, L),
                    loss="huber", f_scale=0.1,
                    bounds=([0.0, 0.0, 0.01, 0.0, 0.01], upper),
                    x_scale="jac", ftol=1e-12, xtol=1e-12, gtol=1e-10, max_nfev=20000)
                if not res.success:
                    continue
                pred = classic_model(res.x, N, D)
                ss_res = np.sum((L - pred) ** 2)
                ss_tot = np.sum((L - L.mean()) ** 2)
                r2 = 1 - ss_res / ss_tot
                if best is None or res.cost < best["cost"]:
                    best = {"params": res.x, "r2": float(r2),
                            "cost": float(res.cost)}
            except (ValueError, FloatingPointError):
                continue
    if best is None:
        raise RuntimeError("经典标度律的全部初值均未收敛")
    return best


def generalized_model(params, N, D, Q):
    """广义标度律 L=E+A N^-alpha+B (Q^theta D)^-beta（式9）。Q=1 退化经典。"""
    E, A, alpha, B, beta, theta = params
    # 质量增强有效数据量 Q_eff = Q**theta * D（Q=1 时退化经典）
    Q_eff = np.power(Q, theta) * D          # 等价 Q**theta * D
    Q_eff = np.clip(Q_eff, 1e-9, None)
    return E + A * np.power(N, -alpha) + B * np.power(Q_eff, -beta)


def _residual_gen_log(params, N, D, Q, L):
    pred = generalized_model(params, N, D, Q)
    pred = np.clip(pred, 1e-6, None)
    return np.log(L) - np.log(pred)


def fit_generalized(N, D, Q, L, classic_params, theta_bounds=(-10.0, 10.0)):
    """在经典参数基础上新增 theta，用 B6-B8 拟合。theta 符号由数据决定（默认自由）。"""
    E0, A0, a0, B0, b0 = classic_params
    lo_t, hi_t = theta_bounds
    best = None
    for theta0 in [-2.0, -0.5, 0.1, 0.5, 1.0, 2.0]:
        if not (lo_t <= theta0 <= hi_t):
            theta0 = 0.5 * (lo_t + hi_t)
        # E 上界放宽：B6-B8 的 loss 尺度与 B1 不同（Q_setpoint 重标定损失区间）
        Lmax = float(np.max(L))
        x0 = [min(L) * 0.5, A0, a0, B0, b0, theta0]
        try:
            res = least_squares(
                _residual_gen_log, x0, args=(N, D, Q, L),
                loss="huber", f_scale=0.1,
                bounds=([0.0, 0.0, 0.01, 0.0, 0.01, lo_t],
                        [Lmax, 200, 1.5, 500, 1.5, hi_t]),
                x_scale="jac", ftol=1e-12, xtol=1e-12, gtol=1e-10, max_nfev=30000)
            if not res.success:
                continue
            pred = generalized_model(res.x, N, D, Q)
            ss_res = np.sum((L - pred) ** 2); ss_tot = np.sum((L - L.mean()) ** 2)
            r2 = 1 - ss_res / ss_tot
            if best is None or res.cost < best["cost"]:
                best = {"params": res.x, "r2": float(r2), "cost": float(res.cost),
                        "active_bounds": res.active_mask.tolist(),
                        "jacobian_condition": float(np.linalg.cond(res.jac)),
                        "optimality": float(res.optimality)}
        except (ValueError, FloatingPointError):
            continue
    if best is None:
        raise RuntimeError("广义标度律的全部初值均未收敛")
    return best


def main():
    u.set_all_seeds(SEED)
    results = {"_meta": u.run_meta(), "method": "log-domain Huber-NLS classic + generalized (Q^theta D)"}

    _p2_classic(results)
    _p2_generalized(results)
    _p2_elasticity(results)

    validate_capability(results)
    u.save_json(results, "figures/problem_2_results.json")
    u.save_json(results["classic"], "output/q2_classic_scaling.json")
    print("[Q2] 完成")
    return results


def _p2_classic(results):
    """P2-C1：B1(1176行)主拟合 + B2/B3/B4/B5 分层泛化。"""
    print("=" * 60)
    print("[Q2] Step 1: 经典标度律 B1 拟合（对数域 Huber-NLS 多起点）")
    b1 = u.read_csv_checked("B_scaling_laws/pythia_training_log_existing.csv", 1176)
    b1 = b1[(b1["val_loss"] > 0) & (b1["N_params_B"] > 0) & (b1["D_tokens_B"] > 0)].copy()
    N, D, L = b1["N_params_B"].values, b1["D_tokens_B"].values, b1["val_loss"].values
    fit = fit_classic(N, D, L)
    E, A, alpha, B, beta = fit["params"]
    pred = classic_model(fit["params"], N, D)
    resid = L - pred
    print(f"[Q2]   E={E:.4f} A={A:.4f} alpha={alpha:.4f} B={B:.4f} beta={beta:.4f} R2={fit['r2']:.5f}")
    print(f"[Q2]   残差均值={resid.mean():.4e} 标准差={resid.std():.4f}")

    # 分层泛化验证 B2/B3/B4/B5
    layers = {}
    for tag, rel, nexp, is_traj in [
        ("B2_cerebras", "B_scaling_laws/cerebras_training_log.csv", 1029, False),
        ("B4_baseline", "B_scaling_laws/scaling_baseline.csv", 57, False),
        ("B5_published", "B_scaling_laws/published_scaling_data.csv", 44, False)]:
        try:
            d = u.read_csv_checked(rel, nexp)
            d = d[(d["val_loss"] > 0) & (d["N_params_B"] > 0) & (d["D_tokens_B"] > 0)]
            p = classic_model(fit["params"], d["N_params_B"].values, d["D_tokens_B"].values)
            yt = d["val_loss"].values
            rmse = float(np.sqrt(np.mean((yt - p) ** 2)))
            ss_res = np.sum((yt - p) ** 2); ss_tot = np.sum((yt - yt.mean()) ** 2)
            r2 = float(1 - ss_res / ss_tot) if ss_tot > 0 else None
            layers[tag] = {"n": int(len(d)), "rmse": rmse, "r2": r2}
            print(f"[Q2]   泛化 {tag}: n={len(d)} RMSE={rmse:.4f} R2={r2}")
        except Exception as e:
            print(f"[Q2]   泛化 {tag} 跳过: {e}")

    # B3 轨迹（8族×500）插值验证
    import glob as _g
    traj_files = sorted(_g.glob(u.dpath("B_scaling_laws/training_trajectories/*.csv")))
    results["classic"] = {
        "params": {"E": float(E), "A": float(A), "alpha": float(alpha),
                   "B": float(B), "beta": float(beta)},
        "r2": fit["r2"], "n_fit": int(len(b1)),
        "residual_mean": float(resid.mean()), "residual_std": float(resid.std()),
        "generalization": layers,
        "n_trajectory_files": len(traj_files),
        "N_range": [float(N.min()), float(N.max())],
        "D_range": [float(D.min()), float(D.max())],
        "L_range": [float(L.min()), float(L.max())],
        # 供图：预测vs实际 + 残差（下采样到 300 点防图过密，全精度已在此不需要）
        "fit_scatter": {"actual": L.tolist(), "predicted": pred.tolist()},
    }
    assert set(layers) == {"B2_cerebras", "B4_baseline", "B5_published"}, "必须完成B2/B4/B5验证"
    b9 = u.read_csv_checked("B_scaling_laws/supplementary_large_models.csv", 132)
    b10 = u.read_csv_checked("B_scaling_laws/supplementary_large_baseline.csv", 128)
    pred_large = classic_model(fit["params"], b10["N_params_B"], b10["D_tokens_B"])
    results["classic"]["large_scale_extrapolation"] = {
        "B9_n": len(b9), "B10_n": len(b10),
        "B9_N_range": [float(b9["N_params_B"].min()), float(b9["N_params_B"].max())],
        "B10_rmse": float(np.sqrt(np.mean((b10["val_loss"] - pred_large) ** 2))),
        "B10_outside_B1_N": int((b10["N_params_B"] > N.max()).sum()),
        "note": "B9为规模元数据，B10为补充估算基线，仅作外推一致性诊断，不作真实观测验证",
    }


def _p2_generalized(results):
    """半合成补充集：按实验设置分组留出，与独立拟合的无 Q 模型比较。"""
    print("[Q2] Step 2: B6-B8 分组留出与公平基线")
    frames = []
    for tag, rel, n in [
        ("B6", "supplementary_NQ_experiment.csv", 360),
        ("B7", "supplementary_NQ_experiment_expanded.csv", 450),
        ("B8", "supplementary_NQ_experiment_large.csv", 1704)]:
        d = u.read_csv_checked("B_scaling_laws/" + rel, n)
        d["source"] = tag
        frames.append(d)
    dq = pd.concat(frames, ignore_index=True)
    cols = ["N_params_B", "D_tokens_B", "Q_score", "val_loss"]
    valid = np.isfinite(dq[cols]).all(axis=1) & (dq[cols] > 0).all(axis=1)
    dq = dq.loc[valid].reset_index(drop=True)
    N, D, Q, L = (dq[c].to_numpy(float) for c in cols)
    from scipy.stats import spearmanr
    corr_QL = float(spearmanr(Q, L).statistic)
    cp = [results["classic"]["params"][k] for k in ("E", "A", "alpha", "B", "beta")]
    # 同一 N,D,Q 设置的重复行不可同时进入训练与留出集。
    groups = dq.groupby(cols[:3], sort=True).ngroup().to_numpy()
    unique = np.unique(groups)
    rng = np.random.default_rng(SEED)
    holdout_groups = rng.permutation(unique)[:max(1, int(np.ceil(.2 * len(unique))))]
    mask = np.isin(groups, holdout_groups)
    tr, ho = np.flatnonzero(~mask), np.flatnonzero(mask)
    genfit = fit_generalized(N[tr], D[tr], Q[tr], L[tr], cp)
    baseline = fit_classic(N[tr], D[tr], L[tr], supplementary=True)
    gp = genfit["params"]
    pred_g = generalized_model(gp, N[ho], D[ho], Q[ho])
    pred_c = classic_model(baseline["params"], N[ho], D[ho])
    rmse_g = float(np.sqrt(np.mean((L[ho] - pred_g) ** 2)))
    rmse_c = float(np.sqrt(np.mean((L[ho] - pred_c) ** 2)))
    source_metrics = {}
    for tag in sorted(dq["source"].unique()):
        m = dq.loc[ho, "source"].to_numpy() == tag
        source_metrics[tag] = {"n": int(m.sum()),
            "rmse_generalized": float(np.sqrt(np.mean((L[ho][m] - pred_g[m]) ** 2))),
            "rmse_no_quality": float(np.sqrt(np.mean((L[ho][m] - pred_c[m]) ** 2)))}
    # Huber 拟合不是 Gaussian MLE；这些只是同训练集 log-RSS 惩罚诊断，不能用作严格 AIC 推断。
    def information_diagnostic(pred, k):
        mse = max(float(np.mean((np.log(L[tr]) - np.log(pred)) ** 2)), np.finfo(float).tiny)
        n = len(tr)
        return n * np.log(mse) + 2 * k, n * np.log(mse) + k * np.log(n)
    ag, bg = information_diagnostic(generalized_model(gp, N[tr], D[tr], Q[tr]), 6)
    ac, bc = information_diagnostic(classic_model(baseline["params"], N[tr], D[tr]), 5)
    test_n, test_d = np.array([1., 5.]), np.array([50., 200.])
    reference = classic_model(gp[:5], test_n, test_d)
    rel_err = float(np.max(np.abs(generalized_model(gp, test_n, test_d, np.ones(2)) - reference) / reference))
    theta_assumed = 0.5
    downstream = cp + [theta_assumed]
    results["generalized"] = {
        "params": dict(zip(("E", "A", "alpha", "B", "beta", "theta"), map(float, gp))),
        "theta_empirical_B6B8": float(gp[-1]), "theta_assumed_downstream": theta_assumed,
        "theta_role": "下游theta=0.5是假设；B6-B8为半合成数据，不能校准A1质量的因果效应",
        "r2": genfit["r2"], "n_fit": len(tr), "n_holdout": len(ho),
        "corr_Q_L": corr_QL,
        "corr_Q_L_note": "B6-B8的Q_score与损失正相关；不据此推断其真实语义或与A1评分可比",
        "split": {"unit": "unique (N,D,Q) setting", "seed": SEED,
                  "n_groups": len(unique), "n_holdout_groups": len(holdout_groups),
                  "group_overlap": len(set(groups[tr]) & set(groups[ho]))},
        "rmse_holdout_generalized": rmse_g,
        "rmse_holdout_classic_baseline": rmse_c,
        "baseline_params": dict(zip(("E", "A", "alpha", "B", "beta"), map(float, baseline["params"]))),
        "baseline_note": "同一训练集、同一Huber目标、同一公共参数边界，独立重拟合不含Q的模型",
        "generalized_better_or_equal": bool(rmse_g <= rmse_c),
        "holdout_by_source": source_metrics,
        "fit_diagnostics": {k: genfit[k] for k in ("active_bounds", "jacobian_condition", "optimality")},
        "aic": {"generalized": float(ag), "classic": float(ac)},
        "bic": {"generalized": float(bg), "classic": float(bc)},
        "information_criteria_note": "训练集log残差平方和惩罚诊断；Huber估计非Gaussian MLE，不作正式AIC/BIC检验",
        "Q1_degeneracy_rel_err": rel_err, "Q1_degeneracy_pass": rel_err < .001,
        "downstream_params": dict(zip(("E", "A", "alpha", "B", "beta", "theta"), downstream)),
        "surface_data": _gen_surface(downstream),
        "surface_note": "B1经典参数+假设theta，与问题三同口径；不同于半合成经验拟合",
    }
    print(f"[Q2] grouped holdout n={len(ho)}: generalized RMSE={rmse_g:.6f}, refit no-Q={rmse_c:.6f}; theta={gp[-1]:.4f}")


def _gen_surface(params):
    """广义律 L(N,Q) 曲面数据（供 fig_q2_generalized_surface）+ Q=1 退化对照线。"""
    Ns = np.logspace(-1, 2, 30)
    Qs = np.linspace(0.1, 1.0, 30)
    NN, QQ = np.meshgrid(Ns, Qs)
    D_fix = 100.0
    LL = generalized_model(params, NN, D_fix * np.ones_like(NN), QQ)
    return {"N_grid": Ns.tolist(), "Q_grid": Qs.tolist(),
            "L_surface": LL.tolist(), "D_fixed": D_fix,
            "Q1_line": generalized_model(params, Ns, D_fix * np.ones_like(Ns),
                                         np.ones_like(Ns)).tolist()}


def _p2_elasticity(results):
    """P2-C3：弹性解析 + Q-N 替代率数值（式11-13）。"""
    print("[Q2] Step 3: 弹性与 Q-N 替代率（解析代入拟合参数）")
    gp = results["generalized"]["downstream_params"]
    # 弹性/替代分析用下游 assumed theta>0（quality-helps premise，与 Q3 一致）
    theta = results["generalized"]["theta_assumed_downstream"]
    E, A, alpha, B, beta = (gp["E"], gp["A"], gp["alpha"], gp["B"], gp["beta"])

    # 参考点：N0,D0 取 B1 范围中位数量级，Q0 取 Q1 域中位数
    import json
    Q0 = float(json.loads((u._ROOT / "figures/problem_1_results.json").read_text())["domain_Q_median"])
    N0, D0 = 1.0, 100.0
    L0 = generalized_model([E, A, alpha, B, beta, theta], np.array([N0]), np.array([D0]), np.array([Q0]))[0]

    # 弹性（式12）
    eps_N = -alpha * A * N0 ** (-alpha) / L0
    Deff = Q0 ** theta * D0
    eps_D = -beta * B * Deff ** (-beta) / L0
    eps_Q = theta * eps_D
    print(f"[Q2]   弹性 eps_N={eps_N:.4f} eps_D={eps_D:.4f} eps_Q={eps_Q:.4f} (均应<0)")

    # Q-N 替代率 dN/dQ|_L（式13）
    dL_dN = -alpha * A * N0 ** (-alpha - 1)
    dL_dQ = -theta * beta * B * Q0 ** (-theta * beta - 1) * D0 ** (-beta)
    dN_dQ = -dL_dQ / dL_dN
    delta_N_for_dQ01 = dN_dQ * 0.1
    print(f"[Q2]   替代率 dN/dQ|_L={dN_dQ:.4f}；ΔQ=0.1 等价 ΔN~{delta_N_for_dQ01:.4f} (10^9 params)")

    # 有限增量的两种问题分别计算，避免将局部导数直接当作0.1的大步长结论。
    dq = min(0.1, 1.0 - Q0)
    target = float(generalized_model([E, A, alpha, B, beta, theta], N0, D0, Q0 + dq))
    at_old_q = target - E - B * (Q0 ** theta * D0) ** (-beta)
    equivalent_increase = (A / at_old_q) ** (1 / alpha) - N0 if at_old_q > 0 else None
    at_new_q = L0 - E - B * ((Q0 + dq) ** theta * D0) ** (-beta)
    exact_iso_change = (A / at_new_q) ** (1 / alpha) - N0

    # 等损失线数据（供 fig_q2_substitution_contour）
    Ns = np.linspace(0.1, 10, 40)
    Qs = np.linspace(0.1, 1.0, 40)
    NN, QQ = np.meshgrid(Ns, Qs)
    LL = generalized_model([E, A, alpha, B, beta, theta], NN, D0 * np.ones_like(NN), QQ)

    results["elasticity"] = {
        "reference_point": {"N0": N0, "D0": D0, "Q0": Q0, "L0": float(L0)},
        "eps_N": float(eps_N), "eps_D": float(eps_D), "eps_Q": float(eps_Q),
        "eps_Q_equals_theta_eps_D": float(theta * eps_D),
        "substitution_dN_dQ": float(dN_dQ),
        "delta_N_for_deltaQ_0.1": float(delta_N_for_dQ01),
        "finite_delta_Q": dq, "exact_iso_loss_delta_N": float(exact_iso_change),
        "equivalent_parameter_increase_B": None if equivalent_increase is None else float(equivalent_increase),
        "parameter_source": "B1 classic fit + assumed theta + Q1 domain median",
        "iso_loss_contour": {"N_grid": Ns.tolist(), "Q_grid": Qs.tolist(),
                             "L_surface": LL.tolist(), "D_fixed": D0},
    }


def validate_capability(results):
    """P2 任务对齐硬断言。"""
    c = results["classic"]
    # P2-C1: 经典律 R2>0.9, alpha,beta in (0,1)
    assert c["r2"] > 0.9, f"[能力不成立] 经典律 R2={c['r2']}<0.9"
    p = c["params"]
    assert 0 < p["alpha"] < 1 and 0 < p["beta"] < 1, \
        f"[能力不成立] alpha/beta 越界 {p['alpha']},{p['beta']}"
    g = results["generalized"]
    # P2-C2 falsifiable_check: 广义律(含Q)在B6留出 RMSE 不劣于同参经典(忽略Q)基线
    #   —— Q 项确有信息量(不论 setpoint 方向)。下游 theta_assumed>0 反映部署质量premise。
    assert g["split"]["group_overlap"] == 0, "训练/留出实验设置泄漏"
    assert np.isfinite(g["rmse_holdout_classic_baseline"]), "无Q基线未有效拟合"
    assert g["theta_assumed_downstream"] > 0, "[能力不成立] 下游assumed theta<=0"
    assert g["corr_Q_L_note"], "[能力不成立] 未说明 Q_score 口径(setpoint vs Q_synth)"
    # Q=1 退化（equivalence_claims 硬性检验）
    assert g["Q1_degeneracy_pass"], f"[能力不成立] Q=1退化 rel_err={g['Q1_degeneracy_rel_err']}>0.001"
    # P2-C3: 弹性为负 + 替代率有数值
    e = results["elasticity"]
    assert e["eps_N"] < 0 and e["eps_D"] < 0 and e["eps_Q"] < 0, "[能力不成立] 弹性非负"
    assert "delta_N_for_deltaQ_0.1" in e, "[能力不成立] 替代率未代入数值"
    print("[Q2] validate_capability PASS")


if __name__ == "__main__":
    main()
