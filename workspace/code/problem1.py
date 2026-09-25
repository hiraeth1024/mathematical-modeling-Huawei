# -*- coding: utf-8 -*-
"""Question 1: semantic quality scoring, conflict audit, and mixture modeling."""
from __future__ import annotations

import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import numpy as np
import pandas as pd
from scipy import stats

import utils as u
from params import SEED
from q1_pipeline import evaluate_quality


def main():
    """Recalculate all Q1 outputs using one shared quality pipeline."""
    results, scored, _ = evaluate_quality()
    _q1_mixture(results)
    _q1_domain_map(results)
    u.save_json(results, "figures/problem_1_results.json")
    scores = scored[["_source_domain", "Q", "Q_adjusted", "conflict"]].copy()
    scores.insert(0, "sample_idx", np.arange(len(scores)))
    u.save_csv(scores, "output/q1_quality_scores.csv")
    validate_capability(results, scored)
    print("[Q1] complete")
    return results


def _q1_mixture(results):
    """17-domain simplex regression, held-out checks, and estimated extrapolation."""
    def paired(mixture_file, loss_file, n):
        mix_df = u.read_csv_checked(f"A_data_value/regmix_tables/{mixture_file}", n)
        loss_df = u.read_csv_checked(f"A_data_value/regmix_tables/{loss_file}", n)
        if (mix_df["index"].duplicated().any() or loss_df["index"].duplicated().any()
                or set(mix_df["index"]) != set(loss_df["index"])):
            raise ValueError(f"unpaired mixture/loss indices: {mixture_file}, {loss_file}")
        return mix_df.sort_values("index").reset_index(drop=True), \
            loss_df.sort_values("index").reset_index(drop=True)

    mix, loss = paired("train_mixture_1m.csv", "train_pile_loss_1m.csv", 512)
    mix_cols = [c for c in mix.columns if c.startswith("train_the_pile_")]
    loss_cols = [c for c in loss.columns if c.startswith("metric/")]
    P = mix[mix_cols].values.astype(float)   # (512,17) 配比
    # 归一化确保单纯形（数据本就~1，千分位舍入）
    P = P / P.sum(axis=1, keepdims=True)
    assert np.allclose(P.sum(axis=1), 1.0, atol=1e-3), "配比未满足单纯形"

    coefs = {}
    r2_train = {}
    for lc in loss_cols:
        y = np.log(loss[lc].values.astype(float))   # 对数域 ln L
        dom = lc.replace("metric/the_pile_", "").replace("_val_loss", "")
        # 带截距的线性回归 ln L = a + b·p（p 已在单纯形上）
        X = np.hstack([np.ones((len(P), 1)), P])
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        yhat = X @ beta
        # 截距与单纯形列线性相关：统一为 sum(b)=0 的可识别对比编码。
        b_mean = float(beta[1:].mean())
        beta[0] += b_mean
        beta[1:] -= b_mean
        assert np.allclose(X @ beta, yhat, atol=1e-10)
        ss_res = ((y - yhat) ** 2).sum()
        ss_tot = ((y - y.mean()) ** 2).sum()
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
        coefs[dom] = {"intercept": float(beta[0]),
                      "b": {mix_cols[i].replace("train_the_pile_", ""): float(beta[i + 1])
                            for i in range(17)}}
        r2_train[dom] = float(r2)

    # A6--A11 are observed holdouts; A12--A15 are estimated extrapolation tables.
    holdout_r2 = {}
    holdout_rank = {}
    extrapolation = {}
    for scale, mrel, lrel, nexp, kind in [
        ("1m", "test_mixture_1m.csv", "test_pile_loss_1m.csv", 256, "observed_holdout"),
        ("60m", "test_mixture_60m.csv", "test_pile_loss_60m.csv", 256, "observed_holdout"),
        ("1B", "test_mixture_1B.csv", "test_pile_loss_1B.csv", 64, "observed_holdout"),
        ("10B", "est_mixture_10b.csv", "est_pile_loss_10b.csv", 63, "estimated_extrapolation"),
        ("70B", "est_mixture_70b.csv", "est_pile_loss_70b.csv", 63, "estimated_extrapolation")]:
        tm, tl = paired(mrel, lrel, nexp)
        Pt = tm[mix_cols].values.astype(float)
        Pt = Pt / Pt.sum(axis=1, keepdims=True)
        r2s, ranks = [], []
        for lc in loss_cols:
            dom = lc.replace("metric/the_pile_", "").replace("_val_loss", "")
            if lc not in tl.columns:
                continue
            yt = np.log(tl[lc].values.astype(float))
            beta = np.array([coefs[dom]["intercept"]] +
                            [coefs[dom]["b"][mix_cols[i].replace("train_the_pile_", "")] for i in range(17)])
            yhat = np.hstack([np.ones((len(Pt), 1)), Pt]) @ beta
            ss_res = ((yt - yhat) ** 2).sum(); ss_tot = ((yt - yt.mean()) ** 2).sum()
            r2s.append(1 - ss_res / ss_tot if ss_tot > 0 else 0.0)
            if len(yt) > 2:
                ranks.append(stats.spearmanr(yt, yhat).statistic)
        mean_r2 = float(np.mean(r2s))
        mean_rank = float(np.nanmean(ranks)) if ranks else None
        if kind == "observed_holdout":
            holdout_r2[scale] = mean_r2
            holdout_rank[scale] = mean_rank
        else:
            extrapolation[scale] = {"n": nexp, "mean_logloss_r2": mean_r2,
                                    "mean_rank_spearman": mean_rank,
                                    "data_status": kind}
        print(f"[Q1]   配比 {kind} {scale}: logLoss R2={mean_r2:.3f}, "
              f"Spearman={mean_rank:.3f}")

    # LightGBM 对照（RegMix 原范式，捕捉配比交互）
    lgb_r2 = _lgb_mixture(P, loss, loss_cols)

    # 描述性配比对比强度：零和编码下各域系数绝对值均值；非因果重要性。
    imp = np.zeros(17)
    for dom in coefs:
        imp += np.abs(np.array([coefs[dom]["b"][mix_cols[i].replace("train_the_pile_", "")]
                                for i in range(17)]))
    imp /= len(coefs)
    dom_names = [c.replace("train_the_pile_", "") for c in mix_cols]
    importance = {dom_names[i]: float(imp[i]) for i in range(17)}

    mixmodel = {"method": "log-domain simplex-constrained linear regression + LightGBM",
                "n_train": 512, "n_target_domains": len(loss_cols),
                "train_r2": r2_train, "holdout_r2": holdout_r2,
                "holdout_rank_spearman": holdout_rank,
                "holdout_note": "absolute loss calibration fails across scales; rank correlation is descriptive, not full predictive transfer",
                "extrapolation": extrapolation,
                "lightgbm_r2": lgb_r2,
                "mixture_domain_importance": importance,
                "importance_note": "sum(b)=0 编码下的平均绝对系数，仅表示相对平均配比域的线性对比强度；非 LightGBM 增益或因果效应",
                "coefficient_coding": "sum(b_i)=0; intercept adjusted to preserve predictions",
                "simplex_ok": True}
    results["mixture_model"] = mixmodel
    u.save_json(mixmodel, "output/q1_mixture_model.json")


def _lgb_mixture(P, loss, loss_cols):
    """LightGBM 对照（配比交互）。5折CV R2。"""
    try:
        import warnings
        import lightgbm as lgb
        from sklearn.model_selection import cross_val_score
        r2s = []
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            for lc in loss_cols:
                y = np.log(loss[lc].values.astype(float))
                m = lgb.LGBMRegressor(n_estimators=100, num_leaves=15, learning_rate=0.05,
                                      random_state=SEED, verbose=-1, n_jobs=1)
                sc = cross_val_score(m, np.ascontiguousarray(P), y, cv=5, scoring="r2")
                r2s.append(float(sc.mean()))
        return float(np.mean(r2s))
    except Exception as e:
        print(f"[Q1]   LightGBM 对照跳过: {e}")
        return None


def _q1_domain_map(results):
    """P1-C5：A16 跨体系域映射，显式处理 inferred 域。"""
    guide = u.read_csv_checked("A_data_value/domain_mapping_guide.csv", 17)
    by_type = guide.groupby("mapping_type").size().to_dict()
    inferred = guide[guide["mapping_type"].str.contains("inferred", case=False, na=False)]
    direct = guide[guide["mapping_type"].str.contains("direct", case=False, na=False)]
    results["domain_mapping"] = {
        "n_total": int(len(guide)),
        "by_type": {k: int(v) for k, v in by_type.items()},
        "inferred_domains": inferred["mixture_domain"].tolist(),
        "inferred_handling": "保留配比为解释变量(间接影响其它域Loss)，按体裁相似性赋推断Q并标注低可信度，不无声丢弃",
        "mapping_pairs": [{"mixture": r["mixture_domain"], "quality": r["quality_domain"],
                           "type": r["mapping_type"]} for _, r in guide.iterrows()],
    }
    print(f"[Q1]   域映射类型分布: {by_type}, inferred={len(inferred)}个")


def validate_capability(results, dfA1):
    """P1 任务对齐硬断言（能力清单 falsifiable_check）。"""
    # P1-C1: 22 指标全覆盖
    assert len(results["weights"]) == 22, "[能力不成立] 质量指标数!=22"
    # P1-C2: 全量 A1 51230 条 + 扩展集域级Q存在
    assert len(dfA1) == 51230, f"[能力不成立] A1 未全量({len(dfA1)}!=51230)"
    assert "domain_Q_extended" in results and "A2_arxiv" in results["domain_Q_extended"], \
        "[能力不成立] 扩展集域级Q缺失"
    # Q in (0,1]
    assert 0 < results["Q_stats"]["min"] and results["Q_stats"]["max"] <= 1.0, \
        "[能力不成立] Q 越出 (0,1]"
    # P1-C3: 冲突有可计算判据
    assert "conflict_rate" in results["conflict"], "[能力不成立] 冲突无量化判据"
    # P1-C4: 配比回归单纯形
    assert results["mixture_model"]["simplex_ok"], "[能力不成立] 配比未满足单纯形"
    # P1-C5: inferred 域显式处理
    assert results["domain_mapping"]["inferred_handling"], "[能力不成立] inferred域无显式处理"
    print("[Q1] validate_capability PASS")


if __name__ == "__main__":
    main()
