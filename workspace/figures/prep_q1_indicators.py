# -*- coding: utf-8 -*-
"""Prepare Q1 figures from the shared semantic scoring and conflict functions."""
from __future__ import annotations

import json
import os
import sys

import numpy as np
from scipy import stats

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
_CODE = os.path.join(_ROOT, "code")
for path in (_ROOT, _CODE):
    if path not in sys.path:
        sys.path.insert(0, path)

from params import SEED  # noqa: E402
from q1_pipeline import A1, EXTENSIONS, detect_conflict, read_decoded  # noqa: E402
from quality_scoring import (ALL_INDICATORS, balanced_weights, compute_q,  # noqa: E402
                             fit_reference, normalize)  # noqa: E402

OUT_NPZ = os.path.join(_HERE, "_prep_q1.npz")
OUT_JSON = os.path.join(_HERE, "_prep_q1.json")
SHORT = {
    "fluency_en": "流畅度", "qurater": "QuRater", "ad_en": "无广告概率",
    "fineweb_edu": "教育价值", "modernbert_cleanliness": "整洁度",
    "modernbert_reasoning": "推理性", "modernbert_professionalism": "专业性",
    "modernbert_readability": "可读性", "dsir_books": "DSIR书籍",
    "rps_lines_ending_with_terminal_punctution_mark": "句末标点",
    "rps_doc_num_sentences": "句子数", "rps_doc_word_count": "词数",
    "rps_doc_frac_no_alph_words": "非字母词占比",
    "rps_doc_frac_chars_top_2gram": "2gram重复",
    "rps_lines_uppercase_letter_fraction": "大写占比",
    "rps_doc_frac_unique_words": "唯一词占比",
    "rps_lines_numerical_chars_fraction": "数字占比",
    "dsir_math": "DSIR数学", "rps_doc_mean_word_length": "平均词长",
    "dsir_wiki": "DSIR维基", "rps_doc_frac_chars_top_3gram": "3gram重复",
    "rps_doc_unigram_entropy": "unigram熵",
}


def bootstrap_ci(x, n_boot=2000, level=.95, seed=SEED):
    rng = np.random.default_rng(seed)
    x = np.asarray(x, dtype=float)
    n = len(x)
    means = np.empty(n_boot)
    for start in range(0, n_boot, 16):
        stop = min(start + 16, n_boot)
        idx = rng.integers(0, n, size=(stop - start, n))
        means[start:stop] = x[idx].mean(axis=1)
    alpha = (1 - level) / 2
    return float(x.mean()), float(np.quantile(means, alpha)), \
        float(np.quantile(means, 1 - alpha)), n


def main():
    with open(os.path.join(_HERE, "problem_1_results.json"), encoding="utf-8") as fh:
        published = json.load(fh)
    df = read_decoded(*A1)
    ref = fit_reference(df)
    R = normalize(df, ref)
    weights = balanced_weights()
    assert weights == published["weights"], "primary weight mismatch"
    Q = compute_q(R, weights)
    assert abs(Q.mean() - published["Q_stats"]["mean"]) < 1e-12
    domain = df["_source_domain"].to_numpy(dtype=str)
    corr = np.asarray(stats.spearmanr(R.values).statistic, dtype=float)
    assert corr.shape == (22, 22)
    np.fill_diagonal(corr, 1.0)

    edu = R["fineweb_edu"].to_numpy(dtype=float)
    has_ad = 1.0 - df["ad_en"].to_numpy(dtype=float)
    threshold = published["conflict"]["tau_pos_q80"]
    mask, conflict = detect_conflict(df, R, threshold)
    assert int(mask.sum()) == published["conflict"]["n_conflict"]
    assert abs(conflict["rate"] - published["conflict"]["conflict_rate"]) < 1e-12

    domain_ci = {}
    for name in sorted(set(domain)):
        mean, lo, hi, n = bootstrap_ci(Q[domain == name])
        assert abs(mean - published["domain_Q_A1"][name]["Q"]) < 1e-12
        domain_ci[name] = {"Q": mean, "lo": lo, "hi": hi, "n": n}

    extension_ci = {}
    for tag, name, rel, count in EXTENSIONS:
        de = read_decoded(rel, count)
        Re = normalize(de, ref)
        qe = compute_q(Re, weights)
        mean, lo, hi, n = bootstrap_ci(qe)
        assert abs(mean - published["domain_Q_extended"][tag]["Q_ext"]) < 1e-12
        extension_ci[tag] = {"domain": name, "Q": mean, "lo": lo,
                             "hi": hi, "n": n}
        del de, Re, qe

    np.savez_compressed(OUT_NPZ, corr=corr, fe=edu.astype(np.float32),
                        ad_raw=has_ad.astype(np.float32), conflict=mask,
                        Q=Q.astype(np.float32), domain=domain)
    meta = {
        "source": "A1 51230 + A2 17523 + A3 203752; all records",
        "pipeline": published["method"],
        "indicators": ALL_INDICATORS,
        "short_labels": [SHORT[name] for name in ALL_INDICATORS],
        "corr_method": "Spearman on A1 semantic, oriented percentile scores",
        "n_docs_A1": len(Q),
        "conflict": {
            "tau_pos_q80": threshold,
            "ad_probability_threshold": .5,
            "rate": conflict["rate"], "n": conflict["n"],
            "spearman_fe_vs_ad": conflict["spearman_education_vs_ad_probability"],
        },
        "domain_Q_A1_ci": domain_ci,
        "domain_Q_extended_ci": extension_ci,
        "bootstrap": {"n_boot": 2000, "level": .95, "seed": SEED,
                      "definition": "within-domain document bootstrap of mean Q"},
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=2)
    print(f"[prep-q1] saved {OUT_NPZ} and {OUT_JSON}")


if __name__ == "__main__":
    main()
