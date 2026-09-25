# -*- coding: utf-8 -*-
"""fig_q3_lctx_panels — 最优配置随上下文长度的敏感性 [4-panel]（配方 basic #12）。

本图讲什么：固定预算 C=1e22 FLOPs、g(Q)=指数型，把 L_ctx 从 2048 扫到 131072
  （C7 实际取值集合），看最优解如何被注意力开销挤压：
  (a) N* 与 D* 同步下降（算力被 C_attn 抽走）；
  (b) Q* 反而上升并顶到上界 1.0（质量是相对更便宜的降损手段）；
  (c) 最优损失 L* 单调恶化；
  (d) 三项份额重组，s_attn 从 5.8% 涨到 77.6% 并在 L_ctx≥32768 时超过 s_train。
  各面板竖线为解析临界值 L_ctx^crit=6/η=30000 tokens，恰落在 8192 与 32768 之间。
数据来源：figures/problem_3_results.json['lctx_sensitivity']（panels 5 点 +
  Lctx_crit）← 与 output/q3_lctx_sensitivity.json 同源，SLSQP 逐点求解。
关键数值：N* 5.516→2.553；D* 258.6→115.9；Q* 0.968→1.0；L* 2.151→2.275；
  s_attn 5.84%→77.58%；L_ctx^crit=30000（解析=数值，check 通过）。
版式：原生 5.9×5.4in，2×2 面板；各面板纵轴含义不同故分别标注，横轴同为
  L_ctx（对数）只在下排标注。
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, panel, declutter_axes, fmt_pow10)

p3 = load("problem_3_results.json")
ls = p3["lctx_sensitivity"]
keys = sorted(ls["panels"], key=lambda k: int(k))
L = np.array([int(k) for k in keys], dtype=float)
P = [ls["panels"][k] for k in keys]
crit = float(ls["Lctx_crit"])
C_bud = float(ls["budget_C"])

fig = plt.figure(figsize=(5.9, 5.7), layout="constrained")
set_paper_placement(fig)
# 顶部独立行放四面板共用的判据线图例；面板各自的系列图例留在面板内
gs = fig.add_gridspec(3, 2, height_ratios=[0.055, 1.0, 1.0], hspace=0.03,
                      wspace=0.04)
ax_leg = fig.add_subplot(gs[0, :])
ax_leg.axis("off")
axes = np.empty((2, 2), dtype=object)
for r in range(2):
    for c in range(2):
        axes[r, c] = fig.add_subplot(gs[r + 1, c])

SINGLE = [
    ("(a)", [("N", cn("$N^*$（$10^9$ 参数）"), PALETTE[0], "o"),
             ("D", cn("$D^*$（$10^9$ tokens）"), PALETTE[2], "s")],
     cn("最优规模 $N^*$ / $D^*$"), True),
    ("(b)", [("Q", cn("$Q^*$"), PALETTE[1], "D")], cn("最优质量 $Q^*$（无量纲）"), False),
    ("(c)", [("L", cn("$L^*$"), PALETTE[0], "^")],
     cn("最优损失 $L^*$（nats/token）"), False),
]

for idx, (tag, series, ylab, logy) in enumerate(SINGLE):
    ax = axes.flat[idx]
    panel(ax, tag)
    ax.axvline(crit, color=COLORS["down"], linestyle="--", linewidth=1.2, zorder=1)
    for key, lab, col, mk in series:
        y = np.array([float(p[key]) for p in P])
        ax.plot(L, y, mk + "-", color=col, linewidth=1.8, markersize=4.6,
                markeredgecolor="white", markeredgewidth=0.8, zorder=3, label=lab)
        ax.fill_between(L, y, y.min() * 0.90 if logy else 0, alpha=0.05,
                        color=col, linewidth=0, zorder=2)
        # 数值统一用 COLORS['text']：浅色系列色做文字达不到 4.5:1 对比度
        ax.text(L[-1], y[-1], f"  {y[-1]:.3g}", fontsize=8.0, va="center",
                ha="left", color=COLORS["text"], fontweight="bold")
    ax.set_xscale("log", base=2)
    if logy:
        ax.set_yscale("log")
    ax.set_ylabel(ylab, fontsize=9)
    declutter_axes(ax, grid="y")
    if len(series) > 1:
        ax.legend(loc="lower left", fontsize=8.0, frameon=False,
                  labelspacing=0.25, handlelength=1.3)

# (d) 份额重组
ax = axes.flat[3]
panel(ax, "(d)")
ax.axvline(crit, color=COLORS["down"], linestyle="--", linewidth=1.2, zorder=1)
SH = [("s_train", cn("$s_{train}$"), PALETTE[0], "o"),
      ("s_Q", cn("$s_Q$"), PALETTE[2], "s"),
      ("s_attn", cn("$s_{attn}$"), PALETTE[1], "^")]
for key, lab, col, mk in SH:
    y = np.array([100.0 * float(p["shares"][key]) for p in P])
    ax.plot(L, y, mk + "-", color=col, linewidth=1.8, markersize=4.6,
            markeredgecolor="white", markeredgewidth=0.8, zorder=3, label=lab)
ax.set_xscale("log", base=2)
ax.set_ylabel(cn("算力份额（%）"), fontsize=9)
ax.set_ylim(-4, 104)
declutter_axes(ax, grid="y")
ax.legend(loc="center left", fontsize=8.0, frameon=False,
          labelspacing=0.25, handlelength=1.3)

for ax in axes.flat:
    ax.set_xlim(L.min() / 1.55, L.max() * 1.55)
    ax.set_xticks(L)
    ax.set_xticklabels([f"{int(v) // 1024}K" if v >= 1024 else str(int(v))
                        for v in L], fontsize=8)
    ax.tick_params(axis="both", labelsize=8)
for ax in axes[1, :]:
    ax.set_xlabel(cn("上下文长度 $L_{ctx}$（tokens）"), fontsize=9)
for ax in axes[0, :]:
    plt.setp(ax.get_xticklabels(), visible=False)

# 临界值是四面板共用的判据线 → 顶部独立行图例，面板内不放旋转浮动文字
from matplotlib.lines import Line2D
# 标签避开"同时带上下标"的 mathtext（下标与上标会被判为重叠文字块）
ax_leg.legend(handles=[Line2D([], [], linestyle="--", color=COLORS["down"],
                              linewidth=1.2,
                              label=cn("注意力临界 $L_{ctx}$=%d tokens" % int(crit)))],
              loc="center", fontsize=8.5, frameon=False, handlelength=1.8,
              title=cn("$C$=%s FLOPs，$g(Q)$ 指数型" % fmt_pow10(C_bud)),
              title_fontsize=8.5)

save_fig(fig, "figures/fig_q3_lctx_panels.pdf")
