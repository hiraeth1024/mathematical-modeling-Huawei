# -*- coding: utf-8 -*-
"""A1 seven-domain Q and fixed-reference A2/A3 extension comparisons."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from _figbase import (save_fig, set_paper_placement, COLORS,
                      load, cn, declutter_axes)

meta = load("_prep_q1.json")
p1 = load("problem_1_results.json")
A1 = meta["domain_Q_A1_ci"]
EXT = {v["domain"]: v for v in meta["domain_Q_extended_ci"].values()}
Q0 = p1["domain_Q_median"]

doms = sorted(A1, key=lambda d: A1[d]["Q"], reverse=True)
n = len(doms)

fig = plt.figure(figsize=(6.6, 5.0), layout="constrained")
fig.get_layout_engine().set(w_pad=0.25)
set_paper_placement(fig)
gs = fig.add_gridspec(2, 2, height_ratios=[0.09, 1.0],
                      width_ratios=[1.0, 0.90], hspace=0.02, wspace=0.03)
ax_leg = fig.add_subplot(gs[0, :])               # 图例独立行，避开数据点
ax_leg.axis("off")
ax = fig.add_subplot(gs[1, 0])
ax_v = fig.add_subplot(gs[1, 1], sharey=ax)      # 专用数值列
ax_v.axis("off")

C_A1, C_EX, C_EX_TEXT, C_ARROW = "#C5283D", "#F2A65A", "#B1600E", "#9B5094"
lab_done = set()
for i, d in enumerate(doms):
    a = A1[d]
    ax.hlines(i, a["lo"], a["hi"], color=C_A1, linewidth=3.4, alpha=0.30,
              capstyle="butt", zorder=2)
    ax.scatter(a["Q"], i, s=62, color=C_A1, edgecolors="white", linewidths=1.0,
               zorder=5, label=cn("抽样集 A1") if "a1" not in lab_done else None)
    lab_done.add("a1")

    e = EXT.get(d)
    if e is None:
        continue
    ax.hlines(i, min(a["Q"], e["Q"]), max(a["Q"], e["Q"]), color=C_ARROW,
              linewidth=1.7, alpha=0.85, zorder=3)
    ax.annotate("", xy=(e["Q"], i), xytext=(a["Q"], i),
                arrowprops=dict(arrowstyle="-|>", color=C_ARROW,
                                lw=1.7, shrinkA=5.5, shrinkB=5.5), zorder=4)
    ax.hlines(i, e["lo"], e["hi"], color=C_EX, linewidth=3.4, alpha=0.30,
              capstyle="butt", zorder=2)
    ax.scatter(e["Q"], i, s=62, color=C_EX, edgecolors="white", linewidths=1.0,
               zorder=5, marker="D",
               label=cn("扩展集 A2/A3") if "ex" not in lab_done else None)
    lab_done.add("ex")

ax.axvline(Q0, color=COLORS["ref_line"], linestyle="--", linewidth=1.1, zorder=1,
           label=cn("域级中位数 $Q_0$=%.4f" % Q0))

# ---- 右侧数值列：加宽并分成三栏；变化值与百分比在同栏分行 ----
COLX = (0.03, 0.38, 0.70)
ax_v.text(COLX[0], -0.62, cn("$Q_{A1}$"), fontsize=8.5, ha="left", va="bottom",
          color=C_A1, fontweight="bold", transform=ax_v.get_yaxis_transform())
ax_v.text(COLX[1], -0.62, cn("$Q_{ext}$"), fontsize=8.5, ha="left", va="bottom",
          color=C_EX_TEXT, fontweight="bold", transform=ax_v.get_yaxis_transform())
ax_v.text(COLX[2], -0.62, cn("变化"), fontsize=8.5, ha="left", va="bottom",
          color=COLORS["text"], fontweight="bold",
          transform=ax_v.get_yaxis_transform())
for i, d in enumerate(doms):
    a, e = A1[d], EXT.get(d)
    tr = ax_v.get_yaxis_transform()
    ax_v.text(COLX[0], i, f"{a['Q']:.4f}", fontsize=8.5, ha="left", va="center",
              color=C_A1, transform=tr)
    if e is None:
        ax_v.text(COLX[1], i, "—", fontsize=8.5, ha="left", va="center",
                  color=COLORS["grid"], transform=tr)
        continue
    dq = e["Q"] - a["Q"]
    ax_v.text(COLX[1], i, f"{e['Q']:.4f}", fontsize=8.5, ha="left", va="center",
              color=C_EX_TEXT, transform=tr)
    ax_v.text(COLX[2], i, f"{dq:+.4f}\n({100 * dq / a['Q']:+.2f}%)", fontsize=8.1,
              ha="left", va="center", color=COLORS["text"], fontweight="bold",
              transform=tr)

ticks = [cn(d) for d in doms]
ax.set_yticks(np.arange(n))
ax.set_yticklabels(ticks, fontsize=9)
values = [v[key] for v in A1.values() for key in ("lo", "hi")]
values += [v[key] for v in EXT.values() for key in ("lo", "hi")]
ax.set_xlim(max(0, min(values) - 0.025), min(1, max(values) + 0.025))
ax.xaxis.set_major_locator(MaxNLocator(nbins=5, prune="both"))
ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.2f}"))
ax.set_xlabel(cn("域级综合质量 $Q$（A1 分位标度）"))
ax.set_ylim(n - 0.5, -0.9)
declutter_axes(ax, grid="x")
handles, labels = ax.get_legend_handles_labels()
ax_leg.legend(handles, labels, loc="center", ncol=3, fontsize=8.2,
              frameon=False, columnspacing=1.2, handlelength=1.5)

save_fig(fig, "figures/fig_q1_domain_Q_dumbbell.pdf")
