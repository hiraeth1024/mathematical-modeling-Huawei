"""Semantic decoding and fixed-reference quality scoring for A1--A3.

The 22 source fields remain 22 scoring features. A1 alone defines imputation,
length saturation, and empirical percentile references; extensions reuse them.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

LIST_INDICATORS = [
    "fluency_en", "qurater", "ad_en", "fineweb_edu",
    "modernbert_cleanliness", "modernbert_reasoning",
    "modernbert_professionalism", "modernbert_readability",
]
SCALAR_INDICATORS = [
    "dsir_books", "rps_lines_ending_with_terminal_punctution_mark",
    "rps_doc_num_sentences", "rps_doc_word_count",
    "rps_doc_frac_no_alph_words", "rps_doc_frac_chars_top_2gram",
    "rps_lines_uppercase_letter_fraction", "rps_doc_frac_unique_words",
    "rps_lines_numerical_chars_fraction", "dsir_math",
    "rps_doc_mean_word_length", "dsir_wiki",
    "rps_doc_frac_chars_top_3gram", "rps_doc_unigram_entropy",
]
ALL_INDICATORS = LIST_INDICATORS + SCALAR_INDICATORS
MODEL_INDICATORS = LIST_INDICATORS
DSIR_INDICATORS = ["dsir_books", "dsir_math", "dsir_wiki"]
STRUCTURE_INDICATORS = [x for x in SCALAR_INDICATORS if x not in DSIR_INDICATORS]
GROUPS = {"model": MODEL_INDICATORS, "dsir": DSIR_INDICATORS,
          "structure": STRUCTURE_INDICATORS}
NEGATIVE_STRUCTURE = {
    "rps_doc_frac_no_alph_words", "rps_doc_frac_chars_top_2gram",
    "rps_doc_frac_chars_top_3gram", "rps_lines_uppercase_letter_fraction",
    "rps_lines_numerical_chars_fraction",
}
SATURATED_LENGTH = {"rps_doc_word_count", "rps_doc_num_sentences",
                    "rps_doc_mean_word_length"}
PRRC = {x for x in LIST_INDICATORS if x.startswith("modernbert_")}


def _softmax(values: np.ndarray) -> np.ndarray:
    z = values - np.max(values)
    e = np.exp(z)
    return e / e.sum()


def decode_value(name: str, value, *, mode: str = "softmax") -> float:
    """Decode logits by class order; return NaN for missing/malformed values."""
    if name not in LIST_INDICATORS:
        try:
            answer = float(value)
            return answer if np.isfinite(answer) else np.nan
        except (TypeError, ValueError):
            return np.nan
    if not isinstance(value, (list, tuple)):
        return np.nan
    try:
        v = np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return np.nan
    expected = 1 if name == "fineweb_edu" else 4 if name == "qurater" else 6 if name in PRRC else 2
    if v.shape != (expected,) or not np.all(np.isfinite(v)):
        return np.nan
    if name == "fineweb_edu":
        return float(v[0])
    if name == "qurater":
        # The four ratings share one source field; equal within-field averaging
        # is an explicit modeling choice, not a claim that they are one construct.
        return float(v.mean())
    if mode == "argmax":
        return float(np.argmax(v) / 5 if name in PRRC else np.argmax(v))
    if mode != "softmax":
        raise ValueError(f"unknown decoding mode: {mode}")
    probs = _softmax(v)
    return float((probs @ (np.arange(6) / 5)) if name in PRRC else probs[1])


def decode_records(records, *, mode: str = "softmax") -> pd.DataFrame:
    rows = []
    for item in records:
        row = {name: decode_value(name, item.get(name), mode=mode)
               for name in ALL_INDICATORS}
        row["_source_domain"] = item.get("_source_domain", "?")
        rows.append(row)
    return pd.DataFrame(rows)


def _oriented(values: np.ndarray, name: str, cap: float | None) -> np.ndarray:
    x = np.asarray(values, dtype=float)
    if name in SATURATED_LENGTH:
        x = np.log1p(np.maximum(x, 0))
        if cap is not None:
            x = np.minimum(x, cap)
    if name in NEGATIVE_STRUCTURE:
        x = -x
    return x


def fit_reference(df: pd.DataFrame) -> dict:
    """Fit A1 medians, p95 length caps, and exact empirical rank references."""
    reference = {"median": {}, "cap": {}, "sorted": {}}
    for name in ALL_INDICATORS:
        raw = df[name].to_numpy(dtype=float)
        finite = raw[np.isfinite(raw)]
        if len(finite) == 0:
            raise ValueError(f"no finite values for {name}")
        median = float(np.median(finite))
        reference["median"][name] = median
        filled = np.where(np.isfinite(raw), raw, median)
        cap = (float(np.quantile(np.log1p(np.maximum(filled, 0)), .95))
               if name in SATURATED_LENGTH else None)
        reference["cap"][name] = cap
        reference["sorted"][name] = np.sort(_oriented(filled, name, cap))
    return reference


def normalize(df: pd.DataFrame, reference: dict) -> pd.DataFrame:
    """Midrank empirical CDF on A1; fixed map and clipping for A2/A3."""
    columns = {}
    for name in ALL_INDICATORS:
        x = df[name].to_numpy(dtype=float)
        x = np.where(np.isfinite(x), x, reference["median"][name])
        x = _oriented(x, name, reference["cap"][name])
        s = reference["sorted"][name]
        left = np.searchsorted(s, x, side="left")
        right = np.searchsorted(s, x, side="right")
        columns[name] = np.clip((left + right) / (2 * len(s)), 0, 1)
    return pd.DataFrame(columns, index=df.index)


def balanced_weights() -> dict[str, float]:
    """Predeclared equal group shares and equal within-group shares, not entropy weights."""
    return {name: 1 / (len(GROUPS) * len(members))
            for members in GROUPS.values() for name in members}


def compute_q(R: pd.DataFrame, weights: dict[str, float] | None = None) -> np.ndarray:
    weights = balanced_weights() if weights is None else weights
    w = np.asarray([weights[name] for name in ALL_INDICATORS])
    if not np.isclose(w.sum(), 1):
        raise ValueError("quality weights must sum to one")
    return np.clip(R[ALL_INDICATORS].to_numpy() @ w, 1e-6, 1.0)


def reference_summary(reference: dict) -> dict:
    return {name: {"median": reference["median"][name],
                   "length_cap_log1p_p95": reference["cap"][name],
                   "oriented_min": float(reference["sorted"][name][0]),
                   "oriented_max": float(reference["sorted"][name][-1])}
            for name in ALL_INDICATORS}
