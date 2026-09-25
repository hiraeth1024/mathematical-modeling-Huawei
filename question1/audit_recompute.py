"""Independent raw-data audit of Question 1 quality scores.

Runs without importing code/quality_scoring.py or code/q1_pipeline.py.
"""
from __future__ import annotations

import json
import lzma
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1] / "workspace"
RAW = ROOT / "user_data/real_attachments/real_attachments/A_data_value"
FIELDS = [
    "fluency_en", "qurater", "ad_en", "fineweb_edu",
    "modernbert_cleanliness", "modernbert_reasoning",
    "modernbert_professionalism", "modernbert_readability",
    "dsir_books", "rps_lines_ending_with_terminal_punctution_mark",
    "rps_doc_num_sentences", "rps_doc_word_count",
    "rps_doc_frac_no_alph_words", "rps_doc_frac_chars_top_2gram",
    "rps_lines_uppercase_letter_fraction", "rps_doc_frac_unique_words",
    "rps_lines_numerical_chars_fraction", "dsir_math",
    "rps_doc_mean_word_length", "dsir_wiki",
    "rps_doc_frac_chars_top_3gram", "rps_doc_unigram_entropy",
]
NEGATIVE = {"rps_doc_frac_no_alph_words", "rps_doc_frac_chars_top_2gram",
            "rps_doc_frac_chars_top_3gram", "rps_lines_uppercase_letter_fraction",
            "rps_lines_numerical_chars_fraction"}
LENGTH = {"rps_doc_word_count", "rps_doc_num_sentences",
          "rps_doc_mean_word_length"}
PRRC = {k for k in FIELDS if k.startswith("modernbert_")}
DSIR = {"dsir_books", "dsir_math", "dsir_wiki"}


def decode(k, value):
    try:
        if k == "fineweb_edu":
            return float(value[0])
        if k == "qurater":
            return float(sum(value) / 4)
        if k in PRRC or k in {"ad_en", "fluency_en"}:
            logits = np.asarray(value, dtype=float)
            p = np.exp(logits - logits.max())
            p /= p.sum()
            return float(p @ (np.arange(6) / 5)) if k in PRRC else float(p[1])
        return float(value)
    except (ValueError, TypeError, IndexError):
        return np.nan


def read(rel):
    rows = []
    with lzma.open(RAW / rel, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                record = json.loads(line)
                row = {k: decode(k, record.get(k)) for k in FIELDS}
                row["domain"] = record.get("_source_domain", "?")
                rows.append(row)
    return pd.DataFrame(rows)


def transform(df, ref=None):
    """Use pandas average ranks for A1, binary searches against A1 for extensions."""
    cols, specs = {}, {} if ref is None else ref
    n = len(df) if ref is None else ref["n"]
    for k in FIELDS:
        raw = df[k].to_numpy(dtype=float)
        median = float(np.nanmedian(raw)) if ref is None else ref[k]["median"]
        x = np.where(np.isfinite(raw), raw, median)
        if k in LENGTH:
            x = np.log1p(np.maximum(x, 0))
            cap = float(np.quantile(x, .95)) if ref is None else ref[k]["cap"]
            x = np.minimum(x, cap)
        else:
            cap = None
        if k in NEGATIVE:
            x = -x
        if ref is None:
            cols[k] = (pd.Series(x).rank(method="average").to_numpy() - .5) / n
            specs[k] = {"median": median, "cap": cap, "sorted": np.sort(x)}
        else:
            ordered = ref[k]["sorted"]
            cols[k] = (np.searchsorted(ordered, x, "left") +
                       np.searchsorted(ordered, x, "right")) / (2 * n)
    specs["n"] = n
    return pd.DataFrame(cols), specs


def score(raw, ranks):
    w = np.array([1 / 24 if i < 8 else 1 / 9 if k in DSIR else 1 / 33
                  for i, k in enumerate(FIELDS)])
    assert np.isclose(w.sum(), 1)
    return ranks[FIELDS].to_numpy() @ w


def main():
    a1 = read("slimpajama_quality_signal_sample.jsonl.xz")
    ranks, ref = transform(a1)
    q = score(a1, ranks)
    expected = pd.read_csv(ROOT / "output/q1_quality_scores.csv")
    assert len(a1) == len(expected) == 51230
    assert (a1.domain.to_numpy() == expected._source_domain.to_numpy()).all()
    max_error = float(np.abs(q - expected.Q.to_numpy()).max())
    assert max_error < 1e-12, max_error
    threshold = float(np.quantile(ranks.fineweb_edu, .8))
    conflict = (ranks.fineweb_edu.to_numpy() >= threshold) & (a1.ad_en.to_numpy() < .5)
    assert np.array_equal(conflict, expected.conflict.to_numpy(dtype=bool))
    domains = pd.DataFrame({"domain": a1.domain, "q": q, "conflict": conflict})
    summary = {"A1_n": len(a1), "A1_Q_mean": float(q.mean()),
               "A1_Q0": float(domains.groupby("domain").q.mean().median()),
               "A1_conflict_n": int(conflict.sum()),
               "A1_highest_conflict_domain": str(domains.groupby("domain").conflict.mean().idxmax()),
               "max_saved_score_error": max_error, "extensions": {}}
    for tag, rel, expected_n in [
        ("A2_arxiv", "slimpajama_quality_extended/arxiv_part-6777d8857c6e-000486.jsonl.xz", 17523),
        ("A3_github", "slimpajama_quality_extended/github_part-6777d8857c6e-000275.jsonl.xz", 203752),
    ]:
        ext = read(rel)
        assert len(ext) == expected_n
        rank_ext, _ = transform(ext, ref)
        conf = ((rank_ext.fineweb_edu.to_numpy() >= threshold) &
                (ext.ad_en.to_numpy() < .5))
        summary["extensions"][tag] = {"n": len(ext), "Q": float(score(ext, rank_ext).mean()),
                                       "conflict_n": int(conf.sum())}
    saved = json.loads((ROOT / "figures/problem_1_results.json").read_text())
    assert np.isclose(summary["A1_Q0"], saved["domain_Q_median"], atol=1e-12)
    assert summary["A1_conflict_n"] == saved["conflict"]["n_conflict"]
    for tag, got in summary["extensions"].items():
        assert np.isclose(got["Q"], saved["domain_Q_extended"][tag]["Q_ext"], atol=1e-12)
        assert got["conflict_n"] == saved["conflict"]["extensions"][tag]["n_conflict"]
    out = ROOT / "output/q1_independent_audit.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
