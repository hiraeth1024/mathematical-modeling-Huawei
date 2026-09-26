# -*- coding: utf-8 -*-
"""规模与年份项的描述性回归分解。累计曲线使用累计样本的平均规模和平均提交年份，模型增量不等于因果贡献。"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, panel, declutter_axes)

pre = load("_prep_q4.json")
p4 = load("problem_4_results.json")["contribution_decomp"]
m = pre["monthly"]
t = np.array([r["t"] for r in m], dtype=float)
f_s = np.array([r["delta_f_scale"] for r in m], dtype=float)
h_n = np.array([r["delta_h_nonscale"] for r in m], dtype=float)
tot = np.array([r["delta_total"] for r in m], dtype=float)
sc_p = np.array([r["scale_pct"] for r in m], dtype=float)
ns_p = np.array([r["nonscale_pct"] for r in m], dtype=float)
t1 = float(pre["window"]["t1"])

C_S, C_N = PALETTE[1], PALETTE[0]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.2, 5.4), layout="constrained",
                               sharex=True, height_ratios=[1.0, 1.0])
set_paper_placement(fig)

# ---- (a) 绝对贡献（能力点）----
panel(ax1, "(a)")
ax1.axhline(0.0, color=COLORS["text"], linewidth=1.0, zorder=2)
ax1.fill_between(t, 0, h_n, color=_lighten(C_N, 0.45), alpha=0.80, linewidth=0,
                 zorder=1, label=cn("非规模项 $\\Delta h$"))
ax1.fill_between(t, f_s, 0, color=_lighten(C_S, 0.45), alpha=0.80, linewidth=0,
                 zorder=1, label=cn("规模项 $\\Delta f$"))
ax1.plot(t, h_n, "o-", color=C_N, linewidth=1.7, markersize=4.2,
         markeredgecolor="white", markeredgewidth=0.8, zorder=4)
ax1.plot(t, f_s, "s-", color=C_S, linewidth=1.7, markersize=4.2,
         markeredgecolor="white", markeredgewidth=0.8, zorder=4)
ax1.plot(t, tot, "^--", color=COLORS["text"], linewidth=1.5, markersize=4.0,
         markeredgecolor="white", markeredgewidth=0.7, zorder=5,
         label=cn("合计 $\\Delta f+\\Delta h$"))
for y, col in ((h_n, C_N), (f_s, C_S), (tot, COLORS["text"])):
    ax1.text(t[-1] + 0.012, y[-1], f"{y[-1]:+.2f}", fontsize=8.2, va="center",
             ha="left", color=col, fontweight="bold")
ax1.set_ylabel(cn("能力贡献（六维均分，点）"), fontsize=9.5)
declutter_axes(ax1, grid="y")
ax1.legend(loc="center left", fontsize=8.2, frameon=False,
           labelspacing=0.28, handlelength=1.4)

# ---- (b) 占比 ----
panel(ax2, "(b)")
ax2.axhline(0.0, color=COLORS["text"], linewidth=1.0, zorder=3)
ax2.axhline(100.0, color=COLORS["ref_line"], linestyle=":", linewidth=1.1,
            zorder=3, label=cn("100% 参考线"))
ax2.fill_between(t, 0, ns_p, color=_lighten(C_N, 0.45), alpha=0.75, linewidth=0,
                 zorder=1)
ax2.fill_between(t, sc_p, 0, color=_lighten(C_S, 0.45), alpha=0.75, linewidth=0,
                 zorder=1)
ax2.plot(t, ns_p, "o-", color=C_N, linewidth=1.7, markersize=4.2,
         markeredgecolor="white", markeredgewidth=0.8, zorder=4,
         label=cn("非规模占比"))
ax2.plot(t, sc_p, "s-", color=C_S, linewidth=1.7, markersize=4.2,
         markeredgecolor="white", markeredgewidth=0.8, zorder=4,
         label=cn("规模占比"))
# 窗口口径的已发布结果作校核点
ax2.scatter([t1], [p4["scale_pct"]], s=76, marker="*", color=COLORS["down"],
            edgecolors="white", linewidths=1.0, zorder=6,
            label=cn("窗口口径 %.1f%%" % p4["scale_pct"]))
for y, col in ((ns_p, C_N), (sc_p, C_S)):
    ax2.text(t[-1] + 0.012, y[-1], f"{y[-1]:+.1f}%", fontsize=8.2, va="center",
             ha="left", color=col, fontweight="bold")
# 保留首期近零分母产生的极端占比，用明确标注的对称对数轴展示全范围。
ax2.set_yscale("symlog", linthresh=100, linscale=1.0)
ticks = [-10000, -100, 0, 100, 10000]
ax2.set_yticks(ticks)
ax2.set_yticklabels(["−10000", "−100", "0", "100", "10000"], fontsize=8)
ax2.set_ylabel(cn("贡献占比（%，对称对数轴）"), fontsize=9.5)
ax2.set_xlabel(cn("提交时间（年，小数）"))
declutter_axes(ax2, grid="y")
ax2.legend(loc="center left", fontsize=8.2, frameon=False,
           labelspacing=0.28, handlelength=1.4, ncol=2)

for ax in (ax1, ax2):
    ax.set_xlim(t[0] - 0.02, t[-1] + 0.075)
    ax.set_xticks(t[::2])
    ax.set_xticklabels([f"{v:.2f}" for v in t[::2]], fontsize=8.5)

save_fig(fig, "figures/fig_q4_contribution_decomp.pdf")
