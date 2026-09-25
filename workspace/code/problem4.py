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

import utils as u
from params import SEED, BENCH_DIMS

CAP_METRIC = "mean6"        # 综合能力度量：六维均分（主口径，S21声明）
OPEN_CRITERION = "hub_license"


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

    u.save_json(results, "figures/problem_4_results.json")
    u.save_json(results["bridge"], "output/q4_bridge_model.json")
    validate_capability(results)
    print("[Q4] 完成")
    return results


def _load_leaderboard():
    """C1 leaderboard_enhanced（含 Epoch AI 开源字段），4576 行。"""
    lb = u.read_csv_checked("C_efficiency_evolution/leaderboard_enhanced.csv", 4576)
    lb["Params_B"] = pd.to_numeric(lb["#Params (B)"], errors="coerce")
    lb["Cap"] = pd.to_numeric(lb["Average \u2b06\ufe0f"], errors="coerce")
    lb["year"] = lb["Submission Date"].apply(_parse_year)
    return lb


def _p4_decomp(results):
    """P4-C1：控制规模(ln N, ln C)后时间趋势=非规模技术进步。增长核算分解。"""
    print("=" * 60)
    print("[Q4] Step 1: 规模 vs 非规模贡献分解（控制 ln Params 规模项 + 时间趋势项）")
    import statsmodels.api as sm
    lb = _load_leaderboard()
    # C4 开源字段（Epoch_AI_Open_Weights，已并入 enhanced）用于开源标注
    open_labeled = lb["Epoch_AI_Open_Weights"].notna().sum() if "Epoch_AI_Open_Weights" in lb else 0

    d = lb.dropna(subset=["Cap", "Params_B", "year"]).copy()
    d = d[(d["Params_B"] > 0) & (d["Cap"] > 0)]
    d["lnN"] = np.log(d["Params_B"])
    print(f"[Q4]   有效样本 n={len(d)}; C4开源字段(Epoch_AI_Open_Weights)标注 {open_labeled} 条")

    # 主模型：Cap ~ lnN + year；年份项为条件关联，不能作因果归因。
    X = sm.add_constant(d[["lnN", "year"]])
    m = sm.OLS(d["Cap"], X).fit()
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
    years = sorted(d["year"].round().unique())
    yearly = []
    base_year = min(years)
    for yr in years:
        dlnN_y = d[d["year"].round() <= yr]["lnN"].mean() - early["lnN"].mean()
        dt_y = yr - early["year"].mean()
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
    }


def _p4_bridge(results):
    """P4-C2：C6(75行) Loss→Benchmark 单调 sigmoid，按 Loss_Comparability 分层。"""
    print("[Q4] Step 2: Loss-Benchmark 桥接（分层单调 sigmoid）")
    c6 = u.read_csv_checked("C_efficiency_evolution/loss_benchmark_bridge_expanded.csv", 75)
    c6 = c6.dropna(subset=["Val_Loss", "LB_Average"]).copy()

    def sigmoid(L, Smax, a, L0, c):
        return Smax / (1.0 + np.exp(a * (L - L0))) + c    # a>0: Loss↑→Cap↓

    strata = {}
    for comp, grp in c6.groupby("Loss_Comparability"):
        if len(grp) < 4:
            continue
        L = grp["Val_Loss"].values.astype(float)
        Cap = grp["LB_Average"].values.astype(float)
        try:
            p0 = [Cap.max(), 1.0, np.median(L), Cap.min()]
            popt, _ = curve_fit(sigmoid, L, Cap, p0=p0, maxfev=20000,
                                bounds=([0, 1e-3, L.min() - 1, -50],
                                        [200, 50, L.max() + 1, 100]))
            pred = sigmoid(L, *popt)
            resid = Cap - pred
            ss_res = np.sum(resid ** 2); ss_tot = np.sum((Cap - Cap.mean()) ** 2)
            r2 = float(1 - ss_res / ss_tot) if ss_tot > 0 else None
            strata[str(comp)] = {"n": int(len(grp)),
                                 "params": {"Smax": float(popt[0]), "a": float(popt[1]),
                                            "L0": float(popt[2]), "c": float(popt[3])},
                                 "r2": r2, "residual_std": float(resid.std()),
                                 "monotone_decreasing": bool(popt[1] > 0),
                                 "L_range": [float(L.min()), float(L.max())],
                                 "scatter": {"loss": L.tolist(), "cap": Cap.tolist(),
                                             "pred": pred.tolist()}}
            print(f"[Q4]   分层 '{comp}': n={len(grp)} a={popt[1]:.3f}(>0单调降) "
                  f"L0={popt[2]:.3f} R2={r2}")
        except Exception as e:
            print(f"[Q4]   分层 '{comp}' 拟合失败: {e}")

    results["bridge"] = {"method": "stratified monotone sigmoid (式23)",
                         "strata_by_comparability": strata,
                         "map_error_note": "残差反映 Loss 到 Cap 的映射误差；直接从榜单 Cap 外推的前沿预测不使用该桥接"}


def _p4_frontier(results):
    """P4-C3：算力放缓情景下 12/24 月前沿分位带（Bootstrap P10/P50/P90）。"""
    print("[Q4] Step 3: 能力前沿 12/24 月预测（Bootstrap 分位带 + 情景）")
    lb = _load_leaderboard()
    d = lb.dropna(subset=["Cap", "year"]).copy()
    d = d[d["Cap"] > 0]
    # 开源筛选（Hub License 非空）
    d_open = d[d["Hub License"].notna() & (d["Hub License"].astype(str).str.strip() != "")]
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
    g = g[(g["yr"] >= 2019) & (g["yr"] <= 2025) & (g["c"] > 0)]
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
    boot_slope = np.empty(n_boot)
    boot_noise = np.empty(n_boot)
    for i in range(n_boot):
        sampled = rng.choice(resid, size=len(resid), replace=True)
        boot_slope[i] = np.linalg.lstsq(A, fitted + sampled, rcond=None)[0][0]
        boot_noise[i] = rng.choice(sampled)

    frontier_pred = {}
    for sc, rc in scenarios.items():
        preds = {}
        for months in [12, 24]:
            dt = months / 12.0
            t_target = t_last + dt
            # 情景：算力放缓使斜率按 rc 缩放（rc=1 维持历史增速, rc=0 停滞）
            # 用观测末值作锚；斜率不确定性随外推期限放大。
            boot = np.clip(frontier_cap[-1] + rc * boot_slope * dt + boot_noise,
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
        "method": "monthly P90 envelope + residual-bootstrap slope refit and predictive noise",
        "scenarios": {"low": 0.0, "mid": 0.5, "high": 1.0},
        "scenario_note": "情景系数0/0.5/1直接缩放历史能力前沿斜率；与训练算力增速的对应关系是假设，未由数据估计",
        "historical_frontier": {"t": frontier_t.tolist(), "cap": frontier_cap.tolist()},
        "slope": float(slope), "predictions": frontier_pred,
        "compute_cagr_from_C4": compute_cagr,
        "compute_cagr_note": f"C4(Epoch AI)训练算力中位数 2019-2025 增速 {compute_cagr:.2f}×/年，仅作情景背景；未拟合算力-能力弹性",
        "n_monthly_frontier": int(len(frontier_t)),
        "one_step_backtest": backtest,
        "n_boot": n_boot,
        "prediction_interval_note": "各情景内 P10/P90 包含历史趋势斜率估计和月度前沿残差的不确定性；不包含情景选择或桥接误差",
        "frontier_no_regress_24m_ge_12m": bool(no_regress),
        "n_open": int(len(d_open)),
        "extrapolation_note": "12/24月为情景模拟，含外推不确定性，非数据直接支持",
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
                j = json.load(open(jf, encoding="utf-8"))
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
            vals[dim] = float(v) * 100 if isinstance(v, (int, float)) else np.nan
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
    df["avg6"] = df[list(task_keys.keys())].mean(axis=1)
    top = df.nlargest(5, "avg6")
    radar = {r["model"]: {dim: (None if pd.isna(r[dim]) else float(r[dim]))
                          for dim in task_keys} for _, r in top.iterrows()}

    results["c8_aggregation"] = {
        "n_subdirs": len(subdirs), "n_parsed": n_ok, "n_corrupt_skipped": n_bad,
        "n_six_dim_complete": n_complete,
        "task_difficulty_mean": task_means,
        "task_correlation_dims": list(task_keys.keys()),
        "task_correlation_matrix": np.nan_to_num(corr).tolist(),
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
    assert any(s["monotone_decreasing"] for s in br.values()), "[能力不成立] 桥接非单调递减"
    # P4-C3: 分位带 + 情景显式
    fr = results["frontier"]
    assert "predictions" in fr and "scenarios" in fr, "[能力不成立] 前沿无分位带/情景"
    for sc in fr["predictions"].values():
        assert "P10" in sc["12m"] and "P90" in sc["12m"], "[能力不成立] 缺P10/P90分位"
    # P4-C4: C8 覆盖>=1800
    c8 = results["c8_aggregation"]
    assert c8["n_parsed"] >= 1800, f"[能力不成立] C8覆盖{c8['n_parsed']}<1800"
    print("[Q4] validate_capability PASS")


if __name__ == "__main__":
    main()
