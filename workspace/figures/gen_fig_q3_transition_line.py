# -*- coding: utf-8 -*-
"""fig_q3_transition_line — 最优份额随 logC 的演化与结构转移点（配方 basic #3）。

本图讲什么：在 logC∈[18,25] 的 36 点网格上求最优配置，画三项算力份额随预算的
  连续轨迹。s_Q 单调下降、s_train 单调上升、s_attn 近乎平稳；结构转移定义为
  份额对 logC 导数的峰值处（式18）并与 KKT 活跃集切换对齐，落在 logC=22.4。
  右轴叠加 |ds_Q/dlogC| 的绝对值曲线，其峰值即转移点的判据来源。
  本图是确定性优化的解轨迹，不存在重复抽样，故不画置信带——区间表达仅适用于
  随机实验，此处若加带会是虚构的不确定性。
数据来源：figures/problem_3_results.json['structural_transition']
  （logC_grid / s_train / s_Q / s_attn / d_sQ_dlogC / transition_logC）
  ← SLSQP 逐点求解，g(Q)=指数型，L_ctx=2048。
关键数值：transition_logC=22.4（C=2.51e22 FLOPs）；s_train 0.774→0.931；
  s_Q 0.173→0.005；s_attn 0.053→0.064；|ds_Q/dlogC| 峰值 0.0608。
版式：原生 6.4×4.0in，左轴份额（%），右轴导数绝对值，双轴刻度都不密集。
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, declutter_axes, auto_legend)

p3 = load("problem_3_results.json")
st = p3["structural_transition"]
lg = np.asarray(st["logC_grid"], dtype=float)
S = {"s_train": np.asarray(st["s_train"], dtype=float) * 100.0,
     "s_Q": np.asarray(st["s_Q"], dtype=float) * 100.0,
     "s_attn": np.asarray(st["s_attn"], dtype=float) * 100.0}
dsQ = np.abs(np.asarray(st["d_sQ_dlogC"], dtype=float))
tr = float(st["transition_logC"])

SER = [("s_train", cn("训练份额 $s_{train}$"), PALETTE[0], "o"),
       ("s_Q", cn("质量份额 $s_Q$"), PALETTE[2], "s"),
       ("s_attn", cn("注意力份额 $s_{attn}$"), PALETTE[1], "^")]

fig, ax = plt.subplots(figsize=(6.4, 4.0), layout="constrained")
set_paper_placement(fig)
ax2 = ax.twinx()

# 转移点竖线（先画，压在曲线下）
ax.axvline(tr, color=COLORS["down"], linestyle="--", linewidth=1.4, zorder=1,
           label=cn("结构转移 $\\log_{10}C$=%.1f" % tr))

step = max(1, len(lg) // 12)
for key, lab, col, mk in SER:
    y = S[key]
    ax.plot(lg, y, color=col, linewidth=2.0, zorder=3, label=lab)
    ax.plot(lg[::step], y[::step], mk, color=col, markersize=4.2,
            markeredgecolor="white", markeredgewidth=0.8, zorder=4, linestyle="none")
    ax.fill_between(lg, y, alpha=0.05, color=col, linewidth=0, zorder=2)

# 右轴：份额导数绝对值，峰值给出转移判据
ax2.plot(lg, dsQ, color=COLORS["ref_line"], linewidth=1.3, linestyle=":",
         zorder=2, label=cn("$|ds_Q/d\\log_{10}C|$"))
k = int(np.argmax(dsQ))
ax2.scatter([lg[k]], [dsQ[k]], s=54, marker="v", color=COLORS["ref_line"],
            edgecolors="white", linewidths=0.9, zorder=5)
# 数值统一用 COLORS['text']：ref_line 浅灰做文字只有 4.45:1，够不到 4.5:1
ax2.text(lg[k] + 0.13, dsQ[k], f"{dsQ[k]:.4f}", fontsize=8.2, va="center",
         ha="left", color=COLORS["text"], fontweight="bold")

# 端点数值（份额起止），放在曲线左右两端外侧净空
for key, _, col, _ in SER:
    y = S[key]
    ax.text(lg[0] - 0.12, y[0], f"{y[0]:.1f}", fontsize=8.0, va="center",
            ha="right", color=COLORS["text"])
    ax.text(lg[-1] + 0.12, y[-1], f"{y[-1]:.1f}", fontsize=8.0, va="center",
            ha="left", color=COLORS["text"], fontweight="bold")

# xlabel 在画布最下缘：带下标的 mathtext（$\log_{10}C$）其下标降部会伸出
# tight bbox 约 2pt 被判出界 → 这里改用中文习惯写法 lg C，不用下标
ax.set_xlabel(cn("算力预算 lg C（C 单位 FLOPs）"))
ax.set_ylabel(cn("算力份额（%）"))
ax2.set_ylabel(cn("份额导数（%/decade）"))
# 左右留白从 0.75 收到 0.42：端点数值本就在轴内，过大的留白会把 xlabel 推出页面
ax.set_xlim(lg[0] - 0.42, lg[-1] + 0.42)
ax.set_ylim(-4, 104)
ax2.set_ylim(0, float(dsQ.max()) * 1.85)
ax2.set_yticks(np.linspace(0, round(float(dsQ.max()), 2), 4))
declutter_axes(ax, grid="y")
ax2.grid(False)
ax2.spines["top"].set_visible(False)

h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
# 双轴句柄合并后交给 auto_legend 按实际净空选位（不硬写 bbox 猜坐标）
auto_legend(ax, handles=h1 + h2, labels=l1 + l2, loc="center left",
            fontsize=8.2, frameon=False, labelspacing=0.28, handlelength=1.5)

save_fig(fig, "figures/fig_q3_transition_line.pdf")
