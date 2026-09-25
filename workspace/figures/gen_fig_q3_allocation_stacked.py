# -*- coding: utf-8 -*-
"""fig_q3_allocation_stacked — 三档预算下的算力份额堆叠柱状图（配方 basic #2）。

本图讲什么：C∈{1e19,1e22,1e24} FLOPs 三档预算、三种质量成本函数 g(Q)（指数/幂/
  对数）下的最优算力分配结构 C_train:C_Q:C_attn，并列 Chinchilla 等分基线
  （N=D、Q=Q0、无质量投入）作对照。随预算上升，质量投入份额 s_Q 单调收缩、训练
  份额 s_train 扩张；三种 g(Q) 形式下方向一致，说明结构性结论对成本函数形式不
  敏感。柱顶数字为该配置达到的最优损失 L*。
数据来源：figures/problem_3_results.json['optimal_allocation']（by_gtype 的
  shares/L + baseline_chinchilla）← SLSQP 多起点 + KKT 校验，L_ctx=2048。
关键数值：exp 型 s_Q 从 14.34%(1e19) → 8.57%(1e22) → 1.51%(1e24)；
  对应 L* 3.098 → 2.151 → 1.914；基线 1e22 的 L=2.424 劣于最优 2.151。
版式：原生 6.6×4.5in；顶部 GridSpec 专用行放公共图例，主轴双层 x 轴（柱=方案、
  组=预算），柱顶 L* 竖排数值留 28% 净空，互不遮挡。
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, fmt_pow10, declutter_axes)

p3 = load("problem_3_results.json")
oa = p3["optimal_allocation"]
budgets = list(oa["budgets"])
bkeys = list(oa["by_gtype"]["exp"].keys())


def bkey(c):
    for k in bkeys:
        if abs(float(k) - float(c)) / float(c) < 1e-9:
            return k
    raise KeyError(c)


SCHEMES = [("exp", cn("指数")), ("pow", cn("幂")), ("log", cn("对数")),
           ("baseline", cn("基线"))]
COMP = [("s_train", cn("训练 $C_{train}$"), PALETTE[0]),
        ("s_Q", cn("质量 $C_Q$"), PALETTE[2]),
        ("s_attn", cn("注意力 $C_{attn}$"), PALETTE[1])]

fig = plt.figure(figsize=(6.6, 4.5), layout="constrained")
set_paper_placement(fig)
gs = fig.add_gridspec(2, 1, height_ratios=[0.065, 1.0], hspace=0.02)
ax_leg = fig.add_subplot(gs[0])
ax_leg.axis("off")
ax = fig.add_subplot(gs[1])

W = 0.195
bars, centers = [], []
for bi, c in enumerate(budgets):
    k = bkey(c)
    centers.append(bi)
    for si, (g, _) in enumerate(SCHEMES):
        x = bi + (si - (len(SCHEMES) - 1) / 2.0) * W
        if g == "baseline":
            d = oa["baseline_chinchilla"][k]
            tot = float(d["C_tot"])
            sh = {"s_train": d["C_train"] / tot, "s_Q": d["C_Q"] / tot,
                  "s_attn": d["C_attn"] / tot}
        else:
            d = oa["by_gtype"][g][k]
            sh = d["shares"]
        bars.append((x, sh, float(d["L"])))

for x, sh, Lstar in bars:
    bottom = 0.0
    for key, _, col in COMP:
        v = 100.0 * float(sh[key])
        ax.bar(x, v, W * 0.88, bottom=bottom, color=_lighten(col, 0.38),
               edgecolor=col, linewidth=1.0, zorder=2)
        if v > 6.0:
            ax.text(x, bottom + v / 2.0, f"{v:.1f}", ha="center", va="center",
                    fontsize=8.0, fontweight="bold", color=COLORS["text"])
        bottom += v
    ax.text(x, 102.5, f"{Lstar:.3f}", ha="center", va="bottom", fontsize=8.0,
            fontweight="bold", color=COLORS["text"], rotation=90)

# 双层 x 轴：主刻度=方案（柱位），次刻度=预算（组心），不需要方案图例
ax.set_xticks([b[0] for b in bars])
ax.set_xticklabels([lab for _ in budgets for _, lab in SCHEMES], fontsize=8.0)
ax.set_xticks(centers, minor=True)
ax.set_xticklabels([cn("$C$=%s FLOPs" % fmt_pow10(c)) for c in budgets],
                   minor=True, fontsize=9.5)
ax.tick_params(axis="x", which="minor", pad=17, length=0)
ax.tick_params(axis="x", which="major", length=2)

ax.set_ylabel(cn("算力份额（%）"))
ax.set_ylim(0, 128)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_xlim(-0.55, len(budgets) - 0.45)
declutter_axes(ax, grid="y")

handles = [Patch(facecolor=_lighten(c, 0.38), edgecolor=c, label=l)
           for _, l, c in COMP]
ax_leg.legend(handles=handles, loc="center", ncol=3, fontsize=8.6, frameon=False,
              labelspacing=0.28, handlelength=1.4, columnspacing=1.6,
              title=cn("柱顶数值 = 最优损失 $L^*$（nats/token）"), title_fontsize=8.2)

save_fig(fig, "figures/fig_q3_allocation_stacked.pdf")
