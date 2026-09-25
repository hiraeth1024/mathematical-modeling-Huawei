# -*- coding: utf-8 -*-
"""Clustered Spearman correlations of the 22 semantically decoded A1 quality signals.

The plot retains its original layout; the scoring method uses balanced groups.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import squareform

from _figbase import (save_fig, set_paper_placement, COLORS, PALETTE,
                      load, load_npz, cn, declutter_axes)

z = load_npz("_prep_q1.npz")
meta = load("_prep_q1.json")
corr = np.asarray(z["corr"], dtype=float)
labels = [cn(s) for s in meta["short_labels"]]
n = corr.shape[0]

# 层次聚类：d = 1 - ρ（正相关越强越近），average linkage
dist = 1.0 - corr
np.fill_diagonal(dist, 0.0)
dist = (dist + dist.T) / 2.0
Z = linkage(squareform(np.clip(dist, 0.0, 2.0), checks=False), method="average")
N_CL = 4
cl = fcluster(Z, N_CL, criterion="maxclust")

fig = plt.figure(figsize=(6.4, 6.3), layout="constrained")
set_paper_placement(fig)
gs = fig.add_gridspec(2, 2, height_ratios=[0.16, 1.0], width_ratios=[1.0, 0.045],
                      hspace=0.02, wspace=0.03)

# 顶部列树状图：与热力图同列 → 等宽；xlim 按 scipy 叶节点坐标 5+10i 对齐格心
ax_d = fig.add_subplot(gs[0, 0])
dn = dendrogram(Z, ax=ax_d, no_labels=True,
                color_threshold=Z[-N_CL + 1, 2],
                above_threshold_color=COLORS["ref_line"])
order = dn["leaves"]
ax_d.set_xlim(0, 10 * n)
ax_d.set_axis_off()

ax = fig.add_subplot(gs[1, 0])
ax_cb = fig.add_subplot(gs[1, 1])
M = corr[np.ix_(order, order)]
lab = [labels[i] for i in order]

# 本图不在格内写数值（484 格写满会糊成一片，精确值见 TABLE_q1_weights 与正文），
# 故用 pcolormesh：PDF 里同样是矢量网格，且与规划的"聚类热力图"图型一致。
# 带数值的热力图才必须走 draw_vector_heatmap（需要按格背景判字色对比度）。
im = ax.pcolormesh(np.arange(n + 1), np.arange(n + 1), M, cmap="coolwarm",
                   vmin=-1.0, vmax=1.0, edgecolors="white", linewidth=0.25)
ax.set_aspect("equal")
ax.invert_yaxis()
cb = fig.colorbar(im, cax=ax_cb)
cb.set_label(cn("Spearman 相关系数 ρ"), fontsize=9)
cb.ax.tick_params(labelsize=8)
cb.outline.set_linewidth(0.7)

ax.set_xticks(np.arange(n) + 0.5)
ax.set_yticks(np.arange(n) + 0.5)
# 22 列的格宽只有 ~0.2in，斜排标签的包围盒必相撞（实测 35°/52° 下
# "2gram重复"×"3gram重复" 都压在一起）→ 竖排：横向只占一个字高，恰好放得下
ax.set_xticklabels(lab, rotation=90, ha="center", va="top")
ax.set_yticklabels(lab)
declutter_axes(ax, grid=False)

# 聚类分界白线（行列同序，簇块沿对角线）；pcolormesh 下格 i 占 [i, i+1]，
# 故分界线落在整数 k 上（不是 k-0.5）
cl_ord = [cl[i] for i in order]
for k in range(1, n):
    if cl_ord[k] != cl_ord[k - 1]:
        ax.axvline(k, color="white", linewidth=2.0)
        ax.axhline(k, color="white", linewidth=2.0)

# 簇编号短锚点（给簇起名，不下判断）
bounds = [0] + [k for k in range(1, n) if cl_ord[k] != cl_ord[k - 1]] + [n]
for j in range(len(bounds) - 1):
    mid = (bounds[j] + bounds[j + 1]) / 2.0
    ax.text(mid, -0.55, f"C{j + 1}", ha="center", va="bottom",
            fontsize=9, fontweight="bold", color=PALETTE[j % len(PALETTE)])
ax.set_xlim(0, n)
ax.set_ylim(n, -0.9)

ax.tick_params(axis="both", labelsize=8.5, length=0)
ax.set_xlabel(cn("质量指标（方向统一后，越高越好）"))
ax.set_ylabel(cn("质量指标"))

save_fig(fig, "figures/fig_q1_quality_corr.pdf")
