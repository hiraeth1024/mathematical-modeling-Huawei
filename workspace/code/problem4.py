# -*- coding: utf-8 -*-
"""problem4.py — 问题四：规模/非规模贡献分解 + Loss-Benchmark 桥接 + 前沿预测 + C8聚合。

认领能力：P4-C1(规模vs非规模分离) P4-C2(Loss-Benchmark桥接) P4-C3(12/24月前沿+不确定性) P4-C4(C8逐任务聚合)
方法(METHOD_CLAIMS M7/M8/M9)：
  M7 分层单调 sigmoid 桥接(式23，按 Loss_Comparability 分层)
  M8 趋势残差 Bootstrap 前沿预测分位带(式24, P10/P50/P90)
  M9 C8 逐任务聚合(>=1800目录, 遍历 detailed_results/ JSON)
"""
from __future__ import annotations
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import json
import glob
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.special import expit
from types import SimpleNamespace

import utils as u
from params import SEED, BENCH_DIMS

CAP_METRIC = "mean6"        # 综合能力度量：六维均分（主口径，S21声明）
OPEN_CRITERION = "named_hub_license_excluding_explicit_closed_weights"


def _fit_ols(d, columns):
    """中心化年份改善条件数，并用 HC3 标准误描述异方差。"""
    x = d[columns].astype(float).copy()
    center = float(x["year"].mean()) if "year" in x else 0.0
    if "year" in x:
        x["year"] -= center
    X = np.column_stack([np.ones(len(x)), x.to_numpy()])
    y = d["Cap"].to_numpy(float)
    coef = np.linalg.lstsq(X, y, rcond=None)[0]
    resid = y - X @ coef
    inverse = np.linalg.pinv(X.T @ X)
    leverage = np.einsum("ij,jk,ik->i", X, inverse, X)
    weighted = X * (resid / np.maximum(1 - leverage, 1e-10))[:, None]
    cov = inverse @ (weighted.T @ weighted) @ inverse
    names = ["const"] + columns
    transform = np.eye(len(names))
    if "year" in names:
        transform[0, names.index("year")] = -center
    coef, cov = transform @ coef, transform @ cov @ transform.T
    return SimpleNamespace(params=pd.Series(coef, index=names),
                           hc3_se=dict(zip(names, np.sqrt(np.maximum(np.diag(cov), 0)))),
                           rsquared=float(1 - np.sum(resid ** 2) / np.sum((y - y.mean()) ** 2)))


def _model_type(value):
    s = str(value).lower()
    if "chat" in s or "fine-tuned" in s:
        return "chat_finetuned"
    if "pretrained" in s:
        return "pretrained"
    if "merge" in s or "moerge" in s:
        return "merged"
    return "other"


def _open_mask(d):
    licenses = d["Hub License"].fillna("").astype(str).str.strip().str.lower()
    closed = d["Epoch_AI_Open_Weights"].fillna("").astype(str).str.lower().eq("no")
    return ~licenses.isin(["", "other", "unknown", "none", "nan"]) & ~closed


def _parse_year(s):
    """日期 → 年份小数。容错混合类型。"""
    try:
        d = pd.to_datetime(s, errors="coerce")
        if pd.isna(d):
            return np.nan
        return d.year + (d.dayofyear - 1) / 365.25
    except Exception:
        return np.nan


def main():
    u.set_all_seeds(SEED)
    results = {"_meta": u.run_meta(),
               "method": "growth-accounting decomp + stratified sigmoid bridge + bootstrap frontier + C8 per-task",
               "cap_metric": CAP_METRIC, "open_criterion": OPEN_CRITERION,
               "capability_definition": "六维Benchmark均分(IFEval,BBH,MATH,GPQA,MUSR,MMLU-PRO)"}

    _p4_decomp(results)
    _p4_bridge(results)
    _p4_frontier(results)
    _p4_c8(results)

    validate_capability(results)
    u.save_json(results, "figures/problem_4_results.json")
    u.save_json(results["bridge"], "output/q4_bridge_model.json")
    print("[Q4] 完成")
    return results


def _load_leaderboard():
    """C1 leaderboard_enhanced（含 Epoch AI 开源字段），4576 行。"""
    lb = u.read_csv_checked("C_efficiency_evolution/leaderboard_enhanced.csv", 4576)
    lb["Params_B"] = pd.to_numeric(lb["#Params (B)"], errors="coerce")
    scores = lb[BENCH_DIMS].apply(pd.to_numeric, errors="coerce")
    lb["Cap"] = scores.mean(axis=1).where(scores.notna().all(axis=1))
    lb["year"] = lb["Submission Date"].apply(_parse_year)
    lb["model_type"] = lb["Type"].apply(_model_type)
    return lb


def _p4_decomp(results):
    """P4-C1：控制规模(ln N, ln C)后时间趋势=非规模技术进步。增长核算分解。"""
    print("=" * 60)
    print("[Q4] Step 1: 规模 vs 非规模贡献分解（控制 ln Params 规模项 + 时间趋势项）")
    lb = _load_leaderboard()
    # C4 开源字段（Epoch_AI_Open_Weights，已并入 enhanced）用于开源标注
    open_labeled = lb["Epoch_AI_Open_Weights"].notna().sum() if "Epoch_AI_Open_Weights" in lb else 0

    d = lb.dropna(subset=["Cap", "Params_B", "year"]).copy()
    d = d[(d["Params_B"] > 0) & (d["Cap"] > 0)]
    d["lnN"] = np.log(d["Params_B"])
    print(f"[Q4]   有效样本 n={len(d)}; C4开源字段(Epoch_AI_Open_Weights)标注 {open_labeled} 条")

    # 主模型：Cap ~ lnN + year；年份项为条件关联，不能作因果归因。
    m = _fit_ols(d, ["lnN", "year"])
    b_N, c_t = m.params["lnN"], m.params["year"]
    print(f"[Q4]   Cap ~ {m.params['const']:.2f} + {b_N:.3f}·lnN + {c_t:.3f}·year, R2={m.rsquared:.3f}")

    # 增长核算：早期与晚期样本均值的回归项分解。
    t0, t1 = d["year"].quantile(0.1), d["year"].quantile(0.9)
    early = d[d["year"] <= t0]; late = d[d["year"] >= t1]
    dCap_obs = late["Cap"].mean() - early["Cap"].mean()
    dlnN = late["lnN"].mean() - early["lnN"].mean()
    dt = late["year"].mean() - early["year"].mean()
    df_scale = b_N * dlnN
    dh_time = c_t * dt
    total = df_scale + dh_time
    scale_pct = 100 * df_scale / total if total != 0 else np.nan
    nonscale_pct = 100 * dh_time / total if total != 0 else np.nan
    print(f"[Q4]   观测ΔCap={dCap_obs:.3f}; Δf(规模)={df_scale:.3f} Δh(非规模)={dh_time:.3f} "
          f"→ 规模%={scale_pct:.1f} 非规模%={nonscale_pct:.1f}")
    print(f"[Q4]   窗口内平均参数规模 ΔlnN={dlnN:.3f}"
          f"{'(下降→本回归规模项增量为负)' if dlnN<0 else ''}")

    # 逐年贡献演化（供 fig_q4_contribution_decomp 堆叠面积图）
    years = sorted(np.floor(d["year"]).unique())
    yearly = []
    base_year = min(years)
    for yr in years:
        cumulative = d[np.floor(d["year"]) <= yr]
        dlnN_y = cumulative["lnN"].mean() - early["lnN"].mean()
        dt_y = cumulative["year"].mean() - early["year"].mean()
        f_y = b_N * dlnN_y; h_y = c_t * dt_y
        tot_y = f_y + h_y
        if abs(tot_y) > 1e-9:
            yearly.append({"year": float(yr), "scale_pct": float(100 * f_y / tot_y),
                           "nonscale_pct": float(100 * h_y / tot_y)})

    results["contribution_decomp"] = {
        "model": "Cap ~ lnN + year (OLS)", "r2": float(m.rsquared),
        "b_lnN": float(b_N), "c_year": float(c_t),
        "window": {"t0": float(t0), "t1": float(t1)},
        "delta_Cap_observed": float(dCap_obs),
        "delta_lnN_window": float(dlnN),
        "delta_f_scale": float(df_scale), "delta_h_nonscale": float(dh_time),
        "scale_pct": float(scale_pct), "nonscale_pct": float(nonscale_pct),
        "sum_check": float(scale_pct + nonscale_pct),
        "interpretation": ("年份系数={:.1f} 点/年是控制参数量后的条件关联；"
                           "窗口 ΔlnN={:.2f}，份额为模型拟合增量之比，不能解释为因果贡献".format(c_t, dlnN)),
        "open_field_source": "Epoch_AI_Open_Weights (C4)", "n_open_labeled": int(open_labeled),
        "yearly_evolution": yearly, "n": int(len(d)),
        "hc3_standard_errors": m.hc3_se,
        "unexplained_window_change": float(dCap_obs - total),
    }
    # 模型类型构成可能与时间混杂：保留主描述模型，并加入显式类型控制的敏感性模型。
    indicators = pd.get_dummies(d["model_type"], prefix="type", drop_first=True, dtype=float)
    controlled = pd.concat([d, indicators], axis=1)
    adjusted = _fit_ols(controlled, ["lnN", "year"] + list(indicators.columns))
    results["contribution_decomp"]["type_controlled_sensitivity"] = {
        "counts": d["model_type"].value_counts().to_dict(),
        "coefficients": adjusted.params.to_dict(), "r2": adjusted.rsquared,
        "hc3_standard_errors": adjusted.hc3_se,
        "note": "类型固定效应敏感性；年份系数仍是条件关联，HC3未校正模型家族聚类",
    }


def _fit_bridge(L, cap):
    """0<=下渐近线<=上渐近线<=100；expit 避免指数溢出。"""
    def sigmoid(x, ratio, a, L0, c):
        return c + (100 - c) * ratio * expit(a * (L0 - x))
    bounds = ([0, 1e-3, L.min() - 1, 0], [1, 50, L.max() + 1, 100])
    best = None
    for a0 in (0.5, 2.0, 8.0):
        p0 = [0.8, a0, np.median(L), max(0, cap.min() * .5)]
        try:
            par, cov = curve_fit(sigmoid, L, cap, p0=p0, bounds=bounds, maxfev=20000)
        except (RuntimeError, ValueError):
            continue
        pred = sigmoid(L, *par)
        cost = np.sum((cap - pred) ** 2)
        if best is None or cost < best[0]:
            best = (cost, par, pred)
    if best is None:
        raise RuntimeError("桥接的全部初值均未收敛")
    _, par, pred = best
    ratio, a, L0, c = par
    return {"Smax": float((100 - c) * ratio), "a": float(a),
            "L0": float(L0), "c": float(c)}, pred


def _p4_bridge(results):
    """可比性分层拟合与逐点留一检验；不混用不同层的损失标度。"""
    print("[Q4] Step 2: bounded bridge and leave-one-out validation")
    c6 = u.read_csv_checked("C_efficiency_evolution/loss_benchmark_bridge_expanded.csv", 75)
    c6 = c6.dropna(subset=["Val_Loss", "LB_Average"]).copy()
    strata = {}
    for comp, grp in c6.groupby("Loss_Comparability"):
        if len(grp) < 5:
            continue
        L, cap = grp["Val_Loss"].to_numpy(float), grp["LB_Average"].to_numpy(float)
        par, pred = _fit_bridge(L, cap)
        held = []
        for i in range(len(L)):
            mask = np.arange(len(L)) != i
            fitted, _ = _fit_bridge(L[mask], cap[mask])
            held.append(fitted["c"] + fitted["Smax"] * expit(fitted["a"] * (fitted["L0"] - L[i])))
        held = np.asarray(held)
        strata[str(comp)] = {
            "n": len(grp), "params": par,
            "r2": float(1 - np.sum((cap - pred) ** 2) / np.sum((cap - cap.mean()) ** 2)),
            "residual_std": float(np.std(cap - pred)),
            "loocv_rmse": float(np.sqrt(np.mean((cap - held) ** 2))),
            "loocv_mae": float(np.mean(np.abs(cap - held))),
            "loocv_mean_baseline_rmse": float(np.sqrt(np.mean((cap - (cap.sum() - cap) / (len(cap) - 1)) ** 2))),
            "monotone_decreasing": par["a"] > 0 and par["Smax"] >= 0,
            "bounded_0_100": 0 <= par["c"] <= par["c"] + par["Smax"] <= 100 + 1e-9,
            "L_range": [float(L.min()), float(L.max())],
            "scatter": {"loss": L.tolist(), "cap": cap.tolist(), "pred": pred.tolist()},
        }
        print(f"[Q4] bridge {comp}: R2={strata[str(comp)]['r2']:.4f}, LOO RMSE={strata[str(comp)]['loocv_rmse']:.3f}")
    results["bridge"] = {"method": "stratified bounded monotone sigmoid + LOOCV",
                         "strata_by_comparability": strata,
                         "map_error_note": "留一误差仅描述本层数据，不能证明跨验证集可迁移；榜单前沿未经过桥接"}


def _p4_frontier(results):
    """P4-C3：算力放缓情景下 12/24 月前沿分位带（Bootstrap P10/P50/P90）。"""
    print("[Q4] Step 3: 能力前沿 12/24 月预测（Bootstrap 分位带 + 情景）")
    lb = _load_leaderboard()
    d = lb.dropna(subset=["Cap", "year"]).copy()
    d = d[d["Cap"] > 0]
    # 开源筛选（Hub License 非空）
    d_open = d.loc[_open_mask(d)].copy()
    print(f"[Q4]   开源模型 n={len(d_open)}/{len(d)}")

    # 前沿：逐时间窗 P90 上包络
    d_open = d_open[d_open["year"].notna()]
    ymin, ymax = d_open["year"].min(), d_open["year"].max()
    # 月度分箱前沿
    bins = np.arange(np.floor(ymin), np.ceil(ymax) + 1 / 12, 1 / 12)
    frontier_t, frontier_cap = [], []
    for i in range(len(bins) - 1):
        m = (d_open["year"] >= bins[i]) & (d_open["year"] < bins[i + 1])
        if m.sum() >= 2:
            frontier_t.append(float((bins[i] + bins[i + 1]) / 2))
            frontier_cap.append(float(d_open[m]["Cap"].quantile(0.9)))
    frontier_t = np.array(frontier_t); frontier_cap = np.array(frontier_cap)

    # C4(epoch) 真实历史算力增速：median compute by year, 估 CAGR
    ep = u.read_csv_checked("C_efficiency_evolution/epoch_all_ai_models.csv", 3523)
    ep["c"] = pd.to_numeric(ep["Training compute (FLOP)"], errors="coerce")
    ep["yr"] = pd.to_datetime(ep["Publication date"], errors="coerce").dt.year
    g = ep.dropna(subset=["c", "yr"])
    g = g[(g["yr"] >= 2019) & (g["yr"] <= 2025) & (g["c"] > 0)
          & g["Domain"].fillna("").str.contains("Language", regex=False)
          & g["Open model weights?"].eq("Yes")].copy()
    yr_med = g.groupby("yr")["c"].median()
    # log-linear CAGR
    yrs_c = yr_med.index.values.astype(float)
    log_c = np.log10(yr_med.values)
    cagr_slope = np.polyfit(yrs_c, log_c, 1)[0]     # log10 FLOPs/year
    compute_cagr = float(10 ** cagr_slope)
    print(f"[Q4]   C4历史算力增速: {compute_cagr:.2f}×/年 (log10斜率={cagr_slope:.3f})")

    # 线性趋势 + 残差自助重拟合，外推 12/24 月
    rng = np.random.default_rng(SEED)
    t_last = frontier_t.max()
    # 情景=相对历史算力增速的比例（0停滞/0.5放缓/1维持历史增速），显式声明
    scenarios = {"low": 0.0, "mid": 0.5, "high": 1.0}
    # 历史前沿线性斜率
    if len(frontier_t) < 4:
        raise ValueError("有效月度前沿点不足，不能进行趋势自助拟合")
    A = np.vstack([frontier_t - t_last, np.ones_like(frontier_t)]).T
    slope, intercept = np.linalg.lstsq(A, frontier_cap, rcond=None)[0]
    fitted = A @ np.array([slope, intercept])
    resid = frontier_cap - fitted
    resid -= resid.mean()
    # 扩展窗口一步（月）滚动检验；与“末值延续”基线对照。
    backtest_pred, backtest_naive, backtest_obs = [], [], []
    for i in range(5, len(frontier_t)):
        A_i = np.vstack([frontier_t[:i] - frontier_t[i - 1],
                         np.ones(i)]).T
        slope_i, anchor_i = np.linalg.lstsq(A_i, frontier_cap[:i], rcond=None)[0]
        backtest_pred.append(anchor_i + slope_i * (frontier_t[i] - frontier_t[i - 1]))
        backtest_naive.append(frontier_cap[i - 1])
        backtest_obs.append(frontier_cap[i])
    if not backtest_obs:
        raise ValueError("有效月度前沿点不足，不能进行一步滚动检验")
    bt_pred = np.asarray(backtest_pred)
    bt_naive = np.asarray(backtest_naive)
    bt_obs = np.asarray(backtest_obs)
    backtest = {
        "protocol": "expanding-window one-step-ahead; initial 5 monthly points",
        "n_forecasts": int(len(bt_obs)),
        "trend_mae": float(np.mean(np.abs(bt_pred - bt_obs))),
        "trend_rmse": float(np.sqrt(np.mean((bt_pred - bt_obs) ** 2))),
        "trend_bias": float(np.mean(bt_pred - bt_obs)),
        "last_value_mae": float(np.mean(np.abs(bt_naive - bt_obs))),
    }
    print(f"[Q4]   一步滚动检验 n={backtest['n_forecasts']}: 趋势 MAE={backtest['trend_mae']:.2f}, "
          f"末值延续 MAE={backtest['last_value_mae']:.2f}")
    n_boot = 2000
    boot_anchor = np.empty(n_boot)
    boot_slope = np.empty(n_boot)
    boot_noise = np.empty(n_boot)
    for i in range(n_boot):
        sampled = rng.choice(resid, size=len(resid), replace=True)
        boot_slope[i], boot_anchor[i] = np.linalg.lstsq(A, fitted + sampled, rcond=None)[0]
        boot_noise[i] = rng.choice(resid)

    frontier_pred = {}
    for sc, rc in scenarios.items():
        preds = {}
        for months in [12, 24]:
            dt = months / 12.0
            t_target = t_last + dt
            # 情景：算力放缓使斜率按 rc 缩放（rc=1 维持历史增速, rc=0 停滞）
            # 与滚动检验一致，使用拟合末期水平并保留截距/斜率协方差。
            boot = np.clip(boot_anchor + rc * boot_slope * dt + boot_noise,
                           0.0, 100.0)
            preds[f"{months}m"] = {"P10": float(np.percentile(boot, 10)),
                                   "P50": float(np.percentile(boot, 50)),
                                   "P90": float(np.percentile(boot, 90)),
                                   "t_target": float(t_target)}
        frontier_pred[sc] = preds
        print(f"[Q4]   情景 {sc}(rc={rc}): 12m P50={preds['12m']['P50']:.2f} "
              f"24m P50={preds['24m']['P50']:.2f}")

    # 前沿不倒退核验（mid 情景 24m>=12m）
    mid = frontier_pred["mid"]
    no_regress = mid["24m"]["P50"] >= mid["12m"]["P50"]

    results["frontier"] = {
        "method": "monthly P90 + joint intercept/slope residual bootstrap + independent predictive noise",
        "scenarios": {"low": 0.0, "mid": 0.5, "high": 1.0},
        "scenario_note": "情景系数0/0.5/1直接缩放历史能力前沿斜率；与训练算力增速的对应关系是假设，未由数据估计",
        "historical_frontier": {"t": frontier_t.tolist(), "cap": frontier_cap.tolist()},
        "slope": float(slope), "fitted_anchor": float(intercept), "predictions": frontier_pred,
        "time_axis": "Submission Date, monthly bins; targets relative to last observed month",
        "open_selection": {"rule": OPEN_CRITERION, "type_counts": d_open["model_type"].value_counts().to_dict(),
                           "explicit_open_weights": int(d_open["Epoch_AI_Open_Weights"].eq("Yes").sum()),
                           "note": "有明确名称的许可证且未明确标注关闭权重；未逐项核验许可证条款，不等于严格开源认证"},
        "compute_cagr_from_C4": compute_cagr,
        "compute_sample": {"domain": "Language", "open_weights": "Yes", "n": len(g),
                           "yearly_n": {str(int(k)): int(v) for k,v in g.groupby("yr").size().items()},
                           "n_with_training_data_size": int(pd.to_numeric(g["Training dataset size (total)"], errors="coerce").notna().sum())},
        "compute_cagr_note": f"C4(Epoch AI)开放权重语言模型训练算力中位数 2019-2025 增速 {compute_cagr:.2f}×/年，仅作情景背景；未拟合算力-能力弹性",
        "n_monthly_frontier": int(len(frontier_t)),
        "one_step_backtest": backtest,
        "n_boot": n_boot,
        "prediction_interval_note": "各情景内 P10/P90 包含趋势截距、斜率联合估计和独立月度预测残差的不确定性；不包含情景选择或桥接误差",
        "frontier_no_regress_24m_ge_12m": bool(no_regress),
        "n_open": int(len(d_open)),
        "extrapolation_note": "12/24月为情景模拟，含外推不确定性，非数据直接支持",
    }
    type_frontiers = {}
    for kind, part in d_open.groupby("model_type"):
        ts, ys, counts = [], [], []
        for i in range(len(bins) - 1):
            vals = part.loc[(part["year"] >= bins[i]) & (part["year"] < bins[i + 1]), "Cap"]
            if len(vals) >= 2:
                ts.append(float((bins[i] + bins[i + 1]) / 2))
                ys.append(float(vals.quantile(.9)))
                counts.append(len(vals))
        type_frontiers[kind] = {"n": len(part), "t": ts, "cap": ys, "monthly_n": counts,
                                "slope": float(np.polyfit(np.asarray(ts) - ts[-1], ys, 1)[0]) if len(ts) >= 4 else None}
    results["frontier"]["by_model_type"] = type_frontiers
    c3 = u.read_csv_checked("C_efficiency_evolution/leaderboard_extended_timeseries.csv", 4599)
    history = c3[c3["Source"].ne("Open LLM Leaderboard")].copy()
    scores = pd.to_numeric(history["Average"], errors="coerce")
    years = pd.to_numeric(history["Year"], errors="coerce")
    results["historical_C3_check"] = {
        "n": len(c3), "source_counts": c3["Source"].value_counts().to_dict(),
        "historical_n": len(history), "historical_year_range": [float(years.min()), float(years.max())],
        "historical_score_range": [float(scores.min()), float(scores.max())],
        "note": "C3混合榜单与论文历史记录；年份粒度、评测版本与许可证缺失，单独报告覆盖而不混入月度主预测",
    }
    print(f"[Q4]   前沿不倒退(24m>=12m, mid): {no_regress}")


def _p4_c8(results):
    """P4-C4：C8 detailed_results 逐任务聚合（>=1800 目录，六维基准）。"""
    print("[Q4] Step 4: C8 逐任务聚合（遍历 detailed_results/ JSON）")
    dr = u.dpath("C_efficiency_evolution/detailed_results")
    subdirs = [d for d in sorted(os.listdir(dr)) if os.path.isdir(os.path.join(dr, d))]
    print(f"[Q4]   detailed_results 子目录数={len(subdirs)}")

    # 六维任务键映射
    task_keys = {"IFEval": "leaderboard_ifeval", "BBH": "leaderboard_bbh",
                 "MATH": "leaderboard_math_hard", "GPQA": "leaderboard_gpqa",
                 "MUSR": "leaderboard_musr", "MMLU-PRO": "leaderboard_mmlu_pro"}
    metric_pref = {"leaderboard_ifeval": "prompt_level_strict_acc,none",
                   "leaderboard_bbh": "acc_norm,none",
                   "leaderboard_math_hard": "exact_match,none",
                   "leaderboard_gpqa": "acc_norm,none",
                   "leaderboard_musr": "acc_norm,none",
                   "leaderboard_mmlu_pro": "acc,none"}

    rows = []
    n_ok, n_bad, n_complete = 0, 0, 0
    for sub in subdirs:
        jfiles = sorted(glob.glob(os.path.join(dr, sub, "*.json")))
        if not jfiles:
            continue
        # 取最新可解析记录（按文件名时间戳，文件名含 ISO 时间）
        parsed = None
        for jf in sorted(jfiles, reverse=True):
            try:
                with open(jf, encoding="utf-8") as stream:
                    j = json.load(stream)
                if not isinstance(j, dict) or not isinstance(j.get("results"), dict):
                    n_bad += 1
                    continue
                parsed = j
                break
            except Exception:
                n_bad += 1
                continue
        if parsed is None:
            n_bad += 1
            continue
        r = parsed.get("results", {})
        row = {"model": sub}
        vals = {}
        for dim, tk in task_keys.items():
            node = r.get(tk, {})
            key = metric_pref[tk]
            v = node.get(key)
            vals[dim] = float(v) * 100 if isinstance(v, (int, float)) and not isinstance(v, bool) and np.isfinite(v) and 0 <= v <= 1 else np.nan
        row.update(vals)
        row["date"] = parsed.get("date")
        if all(not np.isnan(vals[dim]) for dim in task_keys):
            n_complete += 1
        rows.append(row)
        n_ok += 1

    df = pd.DataFrame(rows)
    u.save_csv(df, "output/q4_task_aggregation.csv")
    print(f"[Q4]   解析成功 {n_ok} 目录, 损坏跳过 {n_bad}, 六维完整 {n_complete}")

    # 逐任务分析：各基准难度（平均分）+ 任务间相关矩阵
    task_means = {dim: float(df[dim].mean()) for dim in task_keys if dim in df}
    corr = df[list(task_keys.keys())].corr().values
    # 前沿模型（Average 最高 top-1）六维（供雷达图）
    df["avg6"] = df[list(task_keys.keys())].mean(axis=1).where(df[list(task_keys.keys())].notna().all(axis=1))
    top = df.dropna(subset=["avg6"]).nlargest(5, "avg6")
    radar = {r["model"]: {dim: (None if pd.isna(r[dim]) else float(r[dim]))
                          for dim in task_keys} for _, r in top.iterrows()}

    results["c8_aggregation"] = {
        "n_subdirs": len(subdirs), "n_parsed": n_ok, "n_corrupt_skipped": n_bad,
        "n_six_dim_complete": n_complete,
        "task_difficulty_mean": task_means,
        "task_correlation_dims": list(task_keys.keys()),
        "task_correlation_matrix": [[float(v) if np.isfinite(v) else None for v in row] for row in corr],
        "ranking_rule": "六维完整才参与均分排名；任务原始分数未按榜单机会水平归一化",
        "n_excluded_from_ranking": int(df["avg6"].isna().sum()),
        "top5_frontier_radar": radar,
        "coverage_note": f"覆盖 {n_ok} 可解析目录(>=1800要求), 六维完整 {n_complete}",
    }


def validate_capability(results):
    """P4 任务对齐硬断言（能力清单 falsifiable_check）。"""
    # P4-C1: 规模控制 + 占比和~100%
    cd = results["contribution_decomp"]
    assert abs(cd["sum_check"] - 100) < 1e-6, f"[能力不成立] 贡献占比和={cd['sum_check']}!=100"
    assert "b_lnN" in cd, "[能力不成立] 未控制规模变量"
    # P4-C2: 分层 + 单调
    br = results["bridge"]["strata_by_comparability"]
    assert len(br) >= 1, "[能力不成立] 桥接无分层"
    assert all(s["monotone_decreasing"] and s["bounded_0_100"] for s in br.values()), "[能力不成立] 桥接非单调递减"
    # P4-C3: 分位带 + 情景显式
    fr = results["frontier"]
    assert "predictions" in fr and "scenarios" in fr, "[能力不成立] 前沿无分位带/情景"
    for sc in fr["predictions"].values():
        for horizon in ("12m", "24m"):
            q = sc[horizon]
            assert 0 <= q["P10"] <= q["P50"] <= q["P90"] <= 100, "前沿分位数越界/倒序"
    # P4-C4: C8 覆盖>=1800
    c8 = results["c8_aggregation"]
    assert c8["n_parsed"] >= 1800, f"[能力不成立] C8覆盖{c8['n_parsed']}<1800"
    print("[Q4] validate_capability PASS")


if __name__ == "__main__":
    main()
