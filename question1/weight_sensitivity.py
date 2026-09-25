"""Audit Q1 weights without changing the published primary scoring rule."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "workspace/code"))
from q1_pipeline import A1, read_decoded  # noqa: E402
from quality_scoring import GROUPS, fit_reference, normalize  # noqa: E402


def main():
    published = json.loads((ROOT / "workspace/figures/problem_1_results.json").read_text())
    df = read_decoded(*A1)
    R = normalize(df, fit_reference(df))
    domain = df["_source_domain"].astype(str)
    group_means = pd.DataFrame({name: R[fields].mean(axis=1)
                                for name, fields in GROUPS.items()})
    by_domain = group_means.groupby(domain).mean().sort_index()
    base = by_domain.mean(axis=1)
    assert np.allclose(base.values,
                       [published["domain_Q_A1"][d]["Q"] for d in by_domain.index])

    global_critic = published["weights_critic"]
    grouped_weights = {k: global_critic[k] /
                       sum(global_critic[v] for v in fields) / len(GROUPS)
                       for fields in GROUPS.values() for k in fields}
    grouped_score = sum(R[k].to_numpy() * w for k, w in grouped_weights.items())
    grouped_domain = pd.Series(grouped_score).groupby(domain).mean().loc[base.index]

    scenarios = []
    for m in np.arange(.2, .501, .05):
        for dsir in np.arange(.2, .501, .05):
            structure = 1.0 - m - dsir
            if not .2 - 1e-9 <= structure <= .5 + 1e-9:
                continue
            q = by_domain["model"] * m + by_domain["dsir"] * dsir + \
                by_domain["structure"] * structure
            scenarios.append({"group_weights": {"model": round(float(m), 2),
                                                 "dsir": round(float(dsir), 2),
                                                 "structure": round(float(structure), 2)},
                              "domain_kendall": float(stats.kendalltau(base, q).statistic),
                              "Q0": float(q.median()), "highest": str(q.idxmax()),
                              "lowest": str(q.idxmin())})
    result = {
        "primary": {"group_weights": {name: 1/3 for name in GROUPS},
                    "Q0": float(base.median())},
        "grouped_critic": {"Q0": float(grouped_domain.median()),
                           "domain_kendall": float(stats.kendalltau(base, grouped_domain).statistic),
                           "sample_spearman": float(stats.spearmanr(
                               group_means.mean(axis=1), grouped_score).statistic),
                           "weights": grouped_weights},
        "group_weight_grid": {"min_weight": .2, "max_weight": .5, "step": .05,
                              "n_scenarios": len(scenarios),
                              "min_domain_kendall": min(x["domain_kendall"] for x in scenarios),
                              "min_Q0": min(x["Q0"] for x in scenarios),
                              "max_Q0": max(x["Q0"] for x in scenarios),
                              "highest_counts": pd.Series([x["highest"] for x in scenarios]).value_counts().to_dict(),
                              "lowest_counts": pd.Series([x["lowest"] for x in scenarios]).value_counts().to_dict()},
        "scenarios": scenarios,
    }
    path = ROOT / "workspace/output/q1_weight_sensitivity.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: {j: v for j, v in d.items() if j != "weights"}
                      for k, d in result.items() if k != "scenarios"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
