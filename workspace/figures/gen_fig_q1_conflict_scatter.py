# -*- coding: utf-8 -*-
"""A1 education percentile versus decoded probability of an advertisement."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, load_npz, cn, auto_legend, declutter_axes)

z = load_npz("_prep_q1.npz")
meta = load("_prep_q1.json")
p1 = load("problem_1_results.json")
fe = np.asarray(z["fe"], dtype=float)
ad = np.asarray(z["ad_raw"], dtype=float)
conf = np.asarray(z["conflict"], dtype=bool)
c = meta["conflict"]
tau_p, tau_m = c["tau_pos_q80"], c["ad_probability_threshold"]

fig = plt.figure(figsize=(6.2, 5.6), layout="constrained")
set_paper_placement(fig)
gs = fig.add_gridspec(2, 2, width_ratios=[4.2, 1.0], height_ratios=[1.0, 4.2],
                      hspace=0.04, wspace=0.04)
ax = fig.add_subplot(gs[1, 0])
ax_t = fig.add_subplot(gs[0, 0], sharex=ax)
ax_r = fig.add_subplot(gs[1, 1], sharey=ax)

# 冲突区底色（先画，压在散点下）
ax.axhspan(tau_m, 1.02, xmin=0, xmax=1, color=_lighten(COLORS["down"], 0.85),
           alpha=0.30, zorder=0)
ax.add_patch(plt.Rectangle((tau_p, tau_m), 1.02 - tau_p, 1.02 - tau_m,
                           facecolor=_lighten(COLORS["down"], 0.55), alpha=0.45,
                           edgecolor=COLORS["down"], linewidth=1.1, zorder=1))

# 非冲突样本（栅格化，保持 PDF 体积可控）
ax.scatter(fe[~conf], ad[~conf], s=2.0, alpha=0.10, color=PALETTE[0],
           linewidths=0, rasterized=True, zorder=2)
# 冲突样本高亮
ax.scatter(fe[conf], ad[conf], s=3.2, alpha=0.38, color=COLORS["down"],
           linewidths=0, rasterized=True, zorder=3,
           label=cn("冲突样本 n=%d" % c["n"]))

# 分位阈值线（短锚点标签进图例，线上不重复塞字）
ax.axvline(tau_p, color=COLORS["ref_line"], linestyle="--", linewidth=1.0,
           zorder=4, label=cn("教育价值 0.8 分位 %.2f" % tau_p))
ax.axhline(tau_m, color=COLORS["ref_line"], linestyle=":", linewidth=1.0,
           zorder=4, label=cn("判为含广告的概率阈值 %.2f" % tau_m))

ax.text(0.985, 0.975, "%.2f%%" % (100 * c["rate"]), transform=ax.transAxes,
        ha="right", va="top", fontsize=10, fontweight="bold",
        color=COLORS["down"],
        bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                  edgecolor=COLORS["down"], alpha=0.92, linewidth=0.7))

ax.set_xlabel(cn("教育价值 fineweb_edu（A1 分位）"))
ax.set_ylabel(cn("含广告概率 1-P(无广告)"))
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)
declutter_axes(ax, grid="both")
auto_legend(ax, loc="lower left", fontsize=8, frameon=False,
            labelspacing=0.3, handlelength=1.4)

# 边际密度：全体 vs 冲突子集（子样本估 KDE，5 万点全量估计过慢且形状一致）
rng = np.random.default_rng(42)
sub = rng.choice(len(fe), size=8000, replace=False)
xx = np.linspace(0, 1, 300)
for a, data, dsub, col, horiz in ((ax_t, fe, fe[conf], PALETTE[0], True),
                                  (ax_r, ad, ad[conf], PALETTE[0], False)):
    k_all = gaussian_kde(data[sub])(xx)
    k_cf = gaussian_kde(dsub)(xx)
    if horiz:
        a.fill_between(xx, k_all, color=_lighten(col, 0.5), alpha=0.75, linewidth=0)
        a.plot(xx, k_all, color=col, linewidth=1.1)
        a.plot(xx, k_cf, color=COLORS["down"], linewidth=1.1, linestyle="--")
        a.set_yticks([])
        plt.setp(a.get_xticklabels(), visible=False)
    else:
        a.fill_betweenx(xx, k_all, color=_lighten(col, 0.5), alpha=0.75, linewidth=0)
        a.plot(k_all, xx, color=col, linewidth=1.1)
        a.plot(k_cf, xx, color=COLORS["down"], linewidth=1.1, linestyle="--")
        a.set_xticks([])
        plt.setp(a.get_yticklabels(), visible=False)
    for s in ("top", "right", "left" if horiz else "bottom"):
        a.spines[s].set_visible(False)
    a.grid(False)

save_fig(fig, "figures/fig_q1_conflict_scatter.pdf")
