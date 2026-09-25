# -*- coding: utf-8 -*-
"""fig_q4_bridge_scatter — Loss→Benchmark 桥接的分层散点+回归（配方 competition #26）。

本图讲什么：式23 单调 sigmoid 把验证损失 L 映到能力分 Cap，按可比性分层拟合：
  High 层（同模型同验证集，n=7）L 区间窄、残差带 ±0.281；Medium 层（不同验证集
  近似对齐，n=68）残差带 ±9.115，宽了一个量级。两层都满足单调递减，但残差带宽
  差异说明"跨验证集对齐"本身是前沿外推的主要误差来源——问题四的前沿结论必须把
  这条桥接不确定性计入。右侧/顶部边际密度显示两层的 L 与 Cap 覆盖范围并不重合。
数据来源：figures/problem_4_results.json['bridge']['strata_by_comparability']
  （各层 scatter.loss / scatter.cap / scatter.pred + params + residual_std）
  ← C6 loss_benchmark_bridge_expanded.csv 全量 75 行。
关键数值：High n=7, R²=0.403, σ=0.281, L∈[2.093,2.598]；
  Medium n=68, R²=0.356, σ=9.115, L∈[1.650,2.840]；两层均单调递减。
版式：原生 6.2×5.6in，主图 + 顶/右边际密度；High 层样本仅 7 点，边际用地毯线
  而非 KDE（7 点估密度不可靠）。
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, auto_legend, declutter_axes,
                      uncertainty_band)

br = load("problem_4_results.json")["bridge"]
strata = br["strata_by_comparability"]
order = sorted(strata, key=lambda k: -strata[k]["n"])     # 样本多的先画（在底层）

SHORT = {}
for k in strata:
    SHORT[k] = cn("High 层（同模型同验证集）") if k.lower().startswith("high") \
        else cn("Medium 层（跨验证集近似）")
COL = {order[0]: PALETTE[0], order[-1]: PALETTE[2]}
MK = {order[0]: "o", order[-1]: "D"}


def sigmoid(L, Smax, a, L0, c):
    return c + Smax / (1.0 + np.exp(a * (np.asarray(L, float) - L0)))


fig = plt.figure(figsize=(6.2, 5.6), layout="constrained")
set_paper_placement(fig)
gs = fig.add_gridspec(2, 2, width_ratios=[4.2, 1.0], height_ratios=[1.0, 4.2],
                      hspace=0.04, wspace=0.04)
ax = fig.add_subplot(gs[1, 0])
ax_t = fig.add_subplot(gs[0, 0], sharex=ax)
ax_r = fig.add_subplot(gs[1, 1], sharey=ax)

for key in order:
    s = strata[key]
    sc = s["scatter"]
    loss = np.asarray(sc["loss"], dtype=float)
    cap = np.asarray(sc["cap"], dtype=float)
    p = s["params"]
    col, mk = COL[key], MK[key]

    grid = np.linspace(float(s["L_range"][0]), float(s["L_range"][1]), 160)
    fit = sigmoid(grid, p["Smax"], p["a"], p["L0"], p["c"])
    sd = float(s["residual_std"])
    uncertainty_band(ax, grid, fit - sd, fit + sd, color=col, alpha=0.16,
                     label=cn("%s 残差带 $\\pm\\sigma$" % SHORT[key].split("（")[0]))
    ax.plot(grid, fit, color=col, linewidth=1.9, zorder=4,
            label=cn("sigmoid 拟合 R$^2$=%.3f" % s["r2"]))
    ax.scatter(loss, cap, s=34, marker=mk, alpha=0.72, color=col,
               edgecolors="white", linewidths=0.6, zorder=5,
               label=cn("%s n=%d" % (SHORT[key], s["n"])))

    # 边际：样本充足用 KDE，样本过少用地毯线
    if len(loss) >= 20:
        gx = np.linspace(loss.min() - 0.06, loss.max() + 0.06, 220)
        gy = np.linspace(cap.min() - 1.5, cap.max() + 1.5, 220)
        kx, ky = gaussian_kde(loss)(gx), gaussian_kde(cap)(gy)
        ax_t.fill_between(gx, kx, color=_lighten(col, 0.5), alpha=0.70, linewidth=0)
        ax_t.plot(gx, kx, color=col, linewidth=1.1)
        ax_r.fill_betweenx(gy, ky, color=_lighten(col, 0.5), alpha=0.70, linewidth=0)
        ax_r.plot(ky, gy, color=col, linewidth=1.1)
    else:
        for v in loss:
            ax_t.axvline(v, ymin=0.10, ymax=0.75, color=col, linewidth=1.0, alpha=0.85)
        for v in cap:
            ax_r.axhline(v, xmin=0.10, xmax=0.75, color=col, linewidth=1.0, alpha=0.85)

ax.set_xlabel(cn("验证损失 $L$（nats/token）"))
ax.set_ylabel(cn("综合能力 Cap（六维均分，0-100）"))
declutter_axes(ax, grid="both")
auto_legend(ax, loc="upper right", fontsize=8.0, frameon=False,
            labelspacing=0.26, handlelength=1.4)

for a, horiz in ((ax_t, True), (ax_r, False)):
    if horiz:
        a.set_yticks([])
        plt.setp(a.get_xticklabels(), visible=False)
        a.spines["left"].set_visible(False)
    else:
        a.set_xticks([])
        plt.setp(a.get_yticklabels(), visible=False)
        a.spines["bottom"].set_visible(False)
    a.spines["top"].set_visible(False)
    a.spines["right"].set_visible(False)
    a.grid(False)

save_fig(fig, "figures/fig_q4_bridge_scatter.pdf")
