# -*- coding: utf-8 -*-
"""月度 P90 与三情景预测分位带。曲线由拟合末期水平出发，预测仅表示历史样本末期后的条件情景；数值读取当前问题四结果。"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, auto_legend, declutter_axes,
                      uncertainty_band)

fr = load("problem_4_results.json")["frontier"]
hist_t = np.asarray(fr["historical_frontier"]["t"], dtype=float)
hist_c = np.asarray(fr["historical_frontier"]["cap"], dtype=float)
pred = fr["predictions"]
scen = fr["scenarios"]

ORDER = [("high", cn("维持（斜率×1.0）"), PALETTE[0]),
         ("mid", cn("放缓（斜率×0.5）"), PALETTE[2]),
         ("low", cn("停滞（斜率×0.0）"), PALETTE[1])]

t0, c0 = float(hist_t[-1]), float(hist_c[-1])
anchor = float(fr["fitted_anchor"])

fig, ax = plt.subplots(figsize=(6.4, 4.3), layout="constrained")
set_paper_placement(fig)

# 历史段
ax.plot(hist_t, hist_c, "o-", color=COLORS["text"], linewidth=1.9, markersize=4.4,
        markeredgecolor="white", markeredgewidth=0.8, zorder=6,
        label=cn("历史 P90 前沿 n=%d" % len(hist_t)))
ax.scatter([t0], [c0], s=66, color=COLORS["text"], edgecolors="white",
           linewidths=1.0, zorder=7)

ax.axvline(t0, color=COLORS["ref_line"], linestyle=":", linewidth=1.1, zorder=2,
           label=cn("预测起点 %.2f" % t0))

for key, lab, col in ORDER:
    d = pred[key]
    tt = np.array([t0, float(d["12m"]["t_target"]), float(d["24m"]["t_target"])])
    p50 = np.array([anchor, float(d["12m"]["P50"]), float(d["24m"]["P50"])])
    p10 = np.array([anchor, float(d["12m"]["P10"]), float(d["24m"]["P10"])])
    p90 = np.array([anchor, float(d["12m"]["P90"]), float(d["24m"]["P90"])])
    uncertainty_band(ax, tt, p10, p90, color=col, alpha=0.22, zorder=3,
                     label=cn("%s P10-P90" % lab))
    ax.plot(tt, p50, "--", color=col, linewidth=1.9, zorder=5)
    ax.scatter(tt[1:], p50[1:], s=40, color=col, edgecolors="white",
               linewidths=0.9, zorder=6)
    ax.text(tt[-1] + 0.035, p50[-1], f"{p50[-1]:.1f}", fontsize=8.4, va="center",
            ha="left", color=col, fontweight="bold")

# 12/24 月刻度锚点
for k, off in (("12m", 0), ("24m", 1)):
    t_k = float(pred["mid"][k]["t_target"])
    ax.axvline(t_k, color=COLORS["grid"], linestyle="-", linewidth=0.6,
               alpha=0.55, zorder=1)

ax.set_xlabel(cn("时间（年，小数）"))
ax.set_ylabel(cn("能力前沿 Cap（六维均分，0-100）"))
ax.set_xlim(hist_t[0] - 0.05, float(pred["high"]["24m"]["t_target"]) + 0.30)
declutter_axes(ax, grid="y")
auto_legend(ax, loc="upper left", fontsize=8.0, frameon=False,
            labelspacing=0.26, handlelength=1.5, ncol=2)

save_fig(fig, "figures/fig_q4_frontier_fan.pdf")
