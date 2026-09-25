# -*- coding: utf-8 -*-
"""fig_q2_elasticity_diverging — 各因素损失弹性发散柱状图（配方 advanced #20）。

本图讲什么：式12 弹性 ε_x=∂lnL/∂ln x 在 4 个工作点上的对照。三个因素全部落在
  零线左侧（增投都降损），但量级排序稳定为 |ε_D|>|ε_N|>|ε_Q|，且恒有恒等式
  ε_Q=θ·ε_D（θ=0.5）——即质量的降损杠杆只有数据的一半。随工作点沿 N 增大，
  三条弹性同步收缩，对应幂律的边际收益递减。
数据来源：figures/problem_2_results.json['generalized']['params'] +
  ['theta_assumed_downstream'] 解析代入（同 code/problem2.py::_p2_elasticity 式12）；
  参考工作点 (N=1,D=100,Q=0.5) 的三个 ε 与已发布值逐一断言一致。
关键数值：参考点 ε_N=-0.0657, ε_D=-0.0860, ε_Q=-0.0430；θ=0.5；
  工作点沿 B1 数据域 (N 0.07~12, D 0.13~300) 取 4 档，Q 固定 0.5 保证可比。
版式：原生 6.2×4.2in，3 组 × 4 工作点 = 12 根横条，零线居右。
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, elasticities, auto_legend,
                      declutter_axes)

p2 = load("problem_2_results.json")
gp = p2["generalized"]["params"]
theta = float(p2["generalized"]["theta_assumed_downstream"])
params = [gp["E"], gp["A"], gp["alpha"], gp["B"], gp["beta"], theta]
ref = p2["elasticity"]["reference_point"]
Q_FIX = float(ref["Q0"])

# 工作点：参考点 + 沿 B1 数据域的小/中/大三档（Q 固定，保证三组弹性可比）
POINTS = [(0.1, 2.0, cn("小 $N$=0.1")),
          (1.0, 20.0, cn("中 $N$=1, $D$=20")),
          (float(ref["N0"]), float(ref["D0"]), cn("参考点 $N$=1, $D$=100")),
          (10.0, 200.0, cn("大 $N$=10"))]

rows = [elasticities(params, N, D, Q_FIX) for N, D, _ in POINTS]

# 硬断言：参考工作点必须复现已发布弹性
k_ref = next(i for i, (N, D, _) in enumerate(POINTS)
             if abs(N - ref["N0"]) < 1e-12 and abs(D - ref["D0"]) < 1e-12)
for key in ("eps_N", "eps_D", "eps_Q"):
    assert abs(rows[k_ref][key] - p2["elasticity"][key]) < 1e-12, \
        f"[口径不一致] {key} 与已发布不符"

FACTORS = [("eps_D", cn("数据量 $\\varepsilon_D$"), PALETTE[0]),
           ("eps_N", cn("模型规模 $\\varepsilon_N$"), PALETTE[2]),
           ("eps_Q", cn("数据质量 $\\varepsilon_Q$"), PALETTE[1])]

fig, ax = plt.subplots(figsize=(6.2, 4.2), layout="constrained")
set_paper_placement(fig)

n_pt = len(POINTS)
h = 0.20
group_y = np.arange(len(FACTORS)) * 1.25
vmin = min(r[k] for r in rows for k, _, _ in FACTORS)

ax.axvspan(vmin * 1.30, 0, color=COLORS["up"], alpha=0.05, zorder=0)
ax.axvline(0.0, color=COLORS["text"], linewidth=1.2, zorder=4)

alphas = np.linspace(0.30, 0.68, n_pt)
for gi, (key, glab, col) in enumerate(FACTORS):
    for pi, r in enumerate(rows):
        yy = group_y[gi] + (pi - (n_pt - 1) / 2.0) * h
        is_ref = pi == k_ref
        ax.barh(yy, r[key], height=h * 0.86,
                color=_lighten(col, float(1.0 - alphas[pi])),
                edgecolor=col, linewidth=1.8 if is_ref else 0.9, zorder=3,
                label=POINTS[pi][2] if gi == 0 else None)
        ax.text(r[key] - abs(vmin) * 0.016, yy, f"{r[key]:.4f}",
                va="center", ha="right", fontsize=8.2,
                fontweight="bold" if is_ref else "normal", color=COLORS["text"])

ax.set_yticks(group_y)
ax.set_yticklabels([g[1] for g in FACTORS], fontsize=9.5)
ax.set_xlabel(cn("损失弹性 $\\varepsilon=\\partial \\ln L/\\partial \\ln x$（无量纲）"))
ax.set_xlim(vmin * 1.34, abs(vmin) * 0.10)
ax.set_ylim(group_y[-1] + 0.62, group_y[0] - 0.62)
declutter_axes(ax, grid="x")

# 方向锚点与恒等式都进图例，不在绘图区放浮动文字框（12 根柱占满，图内无净空）
from matplotlib.lines import Line2D
extra = [Line2D([], [], linestyle="none", marker="", label=cn("← 降损更强")),
         Line2D([], [], linestyle="none", marker="",
                label=cn("$\\varepsilon_Q=\\theta\\varepsilon_D$, $\\theta$=%.1f" % theta))]
h, l = ax.get_legend_handles_labels()
auto_legend(ax, handles=h + extra, labels=l + [e.get_label() for e in extra],
            loc="upper left", fontsize=8.2, frameon=False,
            labelspacing=0.28, handlelength=1.3, ncol=2,
            title=cn("工作点（$Q$=%.1f 固定）" % Q_FIX), title_fontsize=8.2)

save_fig(fig, "figures/fig_q2_elasticity_diverging.pdf")
