# -*- coding: utf-8 -*-
"""Generate the Q3 assumption-sensitivity table from computed JSON."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "q3_assumption_sensitivity.json").read_text(encoding="utf-8"))
labels = {
    "baseline": "基准",
    "Q0_minus20pct": "$Q_0$ 降 20\\%",
    "Q0_plus20pct": "$Q_0$ 升 20\\%",
    "theta_0.2": "$\\theta=0.2$",
    "theta_0.8": "$\\theta=0.8$",
}
lines = [
    r"\begin{table}[!htbp]",
    r"  \centering",
    r"  \caption{质量基线与指数扰动下的候选最优质量}",
    r"  \label{tab:q3-assumption-sensitivity}",
    r"  \songti\zihao{-4}",
    r"  \begin{tabular}{lrrrrr}",
    r"    \toprule",
    r"    情景 & $Q_0$ & $\theta$ & $Q^\ast_{10^{19}}$ & $Q^\ast_{10^{22}}$ & $Q^\ast_{10^{24}}$ \\",
    r"    \midrule",
]
for key, label in labels.items():
    scenario = data["scenarios"][key]
    q = [scenario["by_budget"][f"{budget:.0e}"]["Q"] for budget in data["budgets_flops"]]
    lines.append(
        f"    {label} & {scenario['Q0']:.4f} & {scenario['theta']:.1f}"
        f" & {q[0]:.3f} & {q[1]:.3f} & {q[2]:.3f} \\\\"
    )
lines += [r"    \bottomrule", r"  \end{tabular}", r"\end{table}"]
path = HERE / "TABLE_q3_sensitivity.tex"
path.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Saved: {path}")
