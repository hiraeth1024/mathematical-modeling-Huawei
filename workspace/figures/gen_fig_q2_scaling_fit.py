# -*- coding: utf-8 -*-
"""fig_q2_scaling_fit — 经典标度律拟合优度 [2-panel]（配方 competition #4）。

本图讲什么：
  (a) 经典律 L=E+A·N^(-α)+B·D^(-β) 在 B1 pythia 逐 checkpoint 拟合集（n=1176）
      上的预测 vs 实际，45° 线为完美拟合。三个外部集（B2 cerebras / B4 baseline /
      B5 published）的泛化 RMSE 不叠在图内，已移入 TABLE_q2_scaling——"拟合集近乎
      无残差"与"跨来源泛化明显退化"是两件事，须一起看。
  (b) 拟合残差分布与正态拟合：残差标准差 1.47e-4 nats/token，量级远小于 L 本身
      （2.09~4.74），确认对数域 Huber-NLS 已收敛到数据的确定性结构。
数据来源：figures/problem_2_results.json['classic']（fit_scatter / r2 /
  residual_std / generalization）← B1 8 个轨迹文件全量。
关键数值：R²=0.9999998；E=1.6898, A=0.3540, α=0.3400, B=1.2403, β=0.2799；
  泛化 RMSE：B5 published 0.198 (R²=0.731) < B4 baseline 0.293 (R²=0.605)
  < B2 cerebras 1.243 (R²=-5.07)。
版式：原生 5.9×6.0in，上下 2 panel（高度比 2.6:1），面板各自独立坐标含义。
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, gaussian_kde

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, panel, auto_legend, declutter_axes)

p2 = load("problem_2_results.json")
cl = p2["classic"]
act = np.asarray(cl["fit_scatter"]["actual"], dtype=float)
prd = np.asarray(cl["fit_scatter"]["predicted"], dtype=float)
res = prd - act
gen = cl["generalization"]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5.9, 6.0), layout="constrained",
                               height_ratios=[2.6, 1.0])
set_paper_placement(fig)

# ---- (a) 预测 vs 实际 ----
panel(ax1, "(a)")
lo, hi = float(min(act.min(), prd.min())), float(max(act.max(), prd.max()))
pad = (hi - lo) * 0.05
lo, hi = lo - pad, hi + pad

xy = np.vstack([act, prd])
kde = gaussian_kde(xy)
gx = np.linspace(lo, hi, 90)
GX, GY = np.meshgrid(gx, gx)
ZZ = kde(np.vstack([GX.ravel(), GY.ravel()])).reshape(GX.shape)
ax1.contourf(GX, GY, ZZ, levels=8, cmap="Blues", alpha=0.20, zorder=0)

ax1.plot([lo, hi], [lo, hi], "--", color=COLORS["down"], linewidth=1.2,
         zorder=3, label=cn("完美拟合线"))
ax1.scatter(act, prd, s=14, alpha=0.45, color=PALETTE[0], edgecolors="white",
            linewidths=0.25, zorder=2, rasterized=True,
            label=cn("B1 拟合集 n=%d" % cl["n_fit"]))

ax1.text(0.045, 0.955,
         "R$^2$=%.7f, RMSE=%.2e" % (cl["r2"], float(np.sqrt((res ** 2).mean()))),
         transform=ax1.transAxes, fontsize=9, va="top", ha="left",
         bbox=dict(boxstyle="round,pad=0.26", facecolor="white",
                   edgecolor=PALETTE[0], alpha=0.92, linewidth=0.8))

ax1.set_xlabel(cn("实际损失 $L$（nats/token）"))
ax1.set_ylabel(cn("预测损失 $\\hat{L}$（nats/token）"))
ax1.set_xlim(lo, hi)
ax1.set_ylim(lo, hi)
declutter_axes(ax1, grid="both")
auto_legend(ax1, loc="upper center", fontsize=8.5, frameon=False,
            labelspacing=0.3, handlelength=1.5)

# ---- (b) 残差分布 ----
panel(ax2, "(b)")
ax2.hist(res, bins=40, density=True, color=_lighten(PALETTE[0], 0.45),
         edgecolor=PALETTE[0], linewidth=0.7, alpha=0.80, zorder=2)
xr = np.linspace(res.min(), res.max(), 240)
ax2.plot(xr, norm.pdf(xr, res.mean(), res.std()), color=PALETTE[2],
         linewidth=1.8, zorder=3,
         label=cn("正态拟合 $\\sigma$=%.2e" % res.std()))
ax2.axvline(0.0, color=COLORS["ref_line"], linestyle="--", linewidth=1.0, zorder=1)
ax2.set_xlabel(cn("拟合残差 $\\hat{L}-L$（nats/token）"))
ax2.set_ylabel(cn("概率密度"))
declutter_axes(ax2, grid="y")
ax2.ticklabel_format(axis="x", style="sci", scilimits=(0, 0), useMathText=True)
auto_legend(ax2, loc="upper right", fontsize=8.5, frameon=False,
            labelspacing=0.3, handlelength=1.5)

save_fig(fig, "figures/fig_q2_scaling_fit.pdf")
