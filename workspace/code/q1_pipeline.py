"""Full-data quality evaluation and conflict audit for Question 1."""
from __future__ import annotations

import json
import lzma

import numpy as np
import pandas as pd
from scipy import stats

import utils as u
from params import SEED
from quality_scoring import (ALL_INDICATORS, GROUPS, balanced_weights,
                             compute_q, decode_records, fit_reference,
                             normalize, reference_summary)

A1 = ("A_data_value/slimpajama_quality_signal_sample.jsonl.xz", 51230)
EXTENSIONS = [
    ("A2_arxiv", "arxiv", "A_data_value/slimpajama_quality_extended/"
     "arxiv_part-6777d8857c6e-000486.jsonl.xz", 17523),
    ("A3_github", "github", "A_data_value/slimpajama_quality_extended/"
     "github_part-6777d8857c6e-000275.jsonl.xz", 203752),
]


def read_decoded(rel: str, expected: int, *, mode: str = "softmax") -> pd.DataFrame:
    """Stream xz records, discarding content while retaining all signal rows."""
    count = 0

    def records():
        nonlocal count
        with lzma.open(u.dpath(rel), "rt", encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    count += 1
                    yield json.loads(line)

    df = decode_records(records(), mode=mode)
    if count != expected or len(df) != expected:
        raise AssertionError(f"{rel}: decoded {count}, expected {expected}")
    print(f"[Q1] decoded {rel}: {count} rows ({mode})")
    return df


def critic_weights(R: pd.DataFrame) -> dict[str, float]:
    values = R[ALL_INDICATORS].to_numpy(dtype=float)
    std = values.std(axis=0, ddof=1)
    corr = np.nan_to_num(np.corrcoef(values, rowvar=False), nan=0.0)
    strength = std * (1.0 - corr).sum(axis=1)
    strength = strength / strength.sum()
    return dict(zip(ALL_INDICATORS, strength.tolist()))


def detect_conflict(df: pd.DataFrame, R: pd.DataFrame,
                    edu_threshold: float) -> tuple[np.ndarray, dict]:
    """High education rank AND predicted advertisement (probability > 0.5)."""
    edu = R["fineweb_edu"].to_numpy(dtype=float)
    has_ad = 1.0 - df["ad_en"].to_numpy(dtype=float)
    mask = (edu >= edu_threshold) & (has_ad > 0.5)
    domains = df["_source_domain"].astype(str)
    by_domain = pd.Series(mask, index=df.index).groupby(domains).agg(["sum", "count", "mean"])
    summary = {
        "rate": float(mask.mean()), "n": int(mask.sum()),
        "spearman_education_vs_ad_probability": float(stats.spearmanr(edu, has_ad).statistic),
        "domain_rates": {name: {"n_conflict": int(row["sum"]),
                                "n": int(row["count"]), "rate": float(row["mean"])}
                         for name, row in by_domain.iterrows()},
    }
    return mask, summary


def evaluate_quality() -> tuple[dict, pd.DataFrame, dict]:
    """Compute primary scores, robustness contrasts, and A1/A2/A3 conflicts."""
    u.set_all_seeds(SEED)
    df = read_decoded(*A1)
    reference = fit_reference(df)
    R = normalize(df, reference)
    weights = balanced_weights()
    Q = compute_q(R, weights)
    df["Q"] = Q
    domains = df["_source_domain"].astype(str)
    domain_q = df.groupby(domains)["Q"].agg(["mean", "count"])
    q0 = float(domain_q["mean"].median())

    cw = critic_weights(R)
    Q_critic = compute_q(R, cw)
    Q_equal = compute_q(R, {k: 1 / len(ALL_INDICATORS) for k in ALL_INDICATORS})
    argmax_df = read_decoded(*A1, mode="argmax")
    argmax_R = normalize(argmax_df, fit_reference(argmax_df))
    Q_argmax = compute_q(argmax_R)
    def domain_tau(other):
        other_mean = pd.Series(other, index=df.index).groupby(domains).mean()
        return float(stats.kendalltau(domain_q["mean"], other_mean.loc[domain_q.index]).statistic)
    robustness = {
        "critic_sample_spearman": float(stats.spearmanr(Q, Q_critic).statistic),
        "critic_domain_kendall": domain_tau(Q_critic),
        "equal22_sample_spearman": float(stats.spearmanr(Q, Q_equal).statistic),
        "equal22_domain_kendall": domain_tau(Q_equal),
        "argmax_sample_spearman": float(stats.spearmanr(Q, Q_argmax).statistic),
        "argmax_domain_kendall": domain_tau(Q_argmax),
        "argmax_domain_Q": {k: float(v) for k, v in
                            pd.Series(Q_argmax, index=df.index).groupby(domains).mean().items()},
    }
    del argmax_df, argmax_R

    edu_threshold = float(np.quantile(R["fineweb_edu"], 0.8))
    mask, conflict_a1 = detect_conflict(df, R, edu_threshold)
    df["conflict"] = mask
    df["Q_adjusted"] = np.where(mask, .5 * Q, Q)
    base_domain = domain_q["mean"]
    adjusted_domain = df.groupby(domains)["Q_adjusted"].mean()
    sensitivity = {}
    for delta in (.3, .5, .7, 1.0):
        candidate = pd.Series(np.where(mask, delta * Q, Q), index=df.index)
        values = candidate.groupby(domains).mean().loc[base_domain.index]
        sensitivity[str(delta)] = {
            "domain_rank_kendall": float(stats.kendalltau(base_domain, values).statistic),
            "domain_Q": {k: float(v) for k, v in values.items()},
        }

    ext_q, ext_conflict = {}, {}
    for tag, domain, rel, n_exp in EXTENSIONS:
        de = read_decoded(rel, n_exp)
        Re = normalize(de, reference)
        Qe = compute_q(Re, weights)
        cmask, csum = detect_conflict(de, Re, edu_threshold)
        ext_q[tag] = {"Q_ext": float(Qe.mean()), "n": len(Qe),
                      "Q_A1_same_domain": float(base_domain[domain])}
        ext_conflict[tag] = {
            "n": len(de), "n_conflict": int(cmask.sum()),
            "rate": csum["rate"],
            "A1_same_domain_rate": conflict_a1["domain_rates"][domain]["rate"],
            "spearman_education_vs_ad_probability": csum["spearman_education_vs_ad_probability"],
        }
        print(f"[Q1] {tag}: Q={Qe.mean():.5f}, conflict={csum['rate']:.3%}")
        del de, Re, Qe

    results = {
        "_meta": u.run_meta(),
        "method": "semantic logits + A1 empirical midrank + three balanced groups",
        "scoring_definition": {
            "logits": "binary positive-class softmax; PRRC 0-5 softmax expected rating / 5",
            "qurater": "equal mean of four source ratings within one field",
            "reference": "A1 empirical midrank CDF; A2/A3 reuse A1 map",
            "length": "word count, sentence count, mean word length log1p and cap at A1 p95",
            "group_weights": {k: 1 / len(GROUPS) for k in GROUPS},
            "limitations": "construct and group weights are modeling choices, not calibrated quality probabilities",
        },
        "normalization_reference": reference_summary(reference),
        "weights": weights, "weights_critic": cw,
        "weights_sum": float(sum(weights.values())),
        "Q_stats": {"min": float(Q.min()), "max": float(Q.max()),
                    "mean": float(Q.mean()), "median": float(np.median(Q))},
        "domain_Q_A1": {k: {"Q": float(row["mean"]), "n": int(row["count"])}
                        for k, row in domain_q.iterrows()},
        "domain_Q_median": q0,
        "domain_Q_extended": ext_q,
        "robustness": robustness,
        "conflict": {
            "positive_indicator": "fineweb_edu",
            "negative_indicator": "ad_en has-ad probability",
            "rule": "A1 education percentile >= A1 p80 and P(has_ad) > 0.5",
            "tau_pos_q80": edu_threshold,
            "ad_probability_threshold": 0.5,
            "conflict_rate": conflict_a1["rate"],
            "n_conflict": conflict_a1["n"],
            "by_domain": conflict_a1["domain_rates"],
            "extensions": ext_conflict,
            "spearman_pos_vs_adcontent": conflict_a1["spearman_education_vs_ad_probability"],
            "resolution": "delta=0.5 only for a sensitivity score; primary Q and Q0 unchanged",
            "adjusted_domain_Q": {k: float(v) for k, v in adjusted_domain.items()},
            "delta_sensitivity": sensitivity,
            "kendall_tau_before_after": float(stats.kendalltau(Q, df["Q_adjusted"]).statistic),
        },
    }
    u.save_json(results, "figures/problem_1_quality_results.json")
    return results, df, reference
