# -*- coding: utf-8 -*-
"""fig_q4_frontier_fan — 能力前沿 12/24 月情景预测扇形图（配方 advanced #27）。

本图讲什么：历史段是 C1 上按月取的 P90 能力前沿包络（10 个点，2024.46~2025.21，
  斜率 19.68 点/年）；预测段按三档能力斜率假设外推，画 bootstrap P10-P90 分位带
  与 P50 中位线。low=0、mid=0.5、high=1；这不是从算力增速估计的弹性。
  low 档的 12/24 月预测分布相同。
数据来源：figures/problem_4_results.json['frontier']（historical_frontier /
  slope / predictions 的 P10/P50/P90 / scenarios）← C1 4576 行；
  C4 历史算力中位数增速 5.10×/年仅作背景，n_open=2813。
关键数值：12 月 P50：low 41.52 / mid 51.38 / high 61.28；
  24 月 P50：low 41.52 / mid 61.28 / high 81.02；历史末值 41.75。
版式：原生 6.4×4.3in；预测段只有 12/24 月两个锚点，故用分段线性连接并明确
  标注"情景模拟含外推不确定性、非数据直接支持"。
"""
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
    p50 = np.array([c0, float(d["12m"]["P50"]), float(d["24m"]["P50"])])
    p10 = np.array([c0, float(d["12m"]["P10"]), float(d["24m"]["P10"])])
    p90 = np.array([c0, float(d["12m"]["P90"]), float(d["24m"]["P90"])])
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
