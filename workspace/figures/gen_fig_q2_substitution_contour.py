# -*- coding: utf-8 -*-
"""固定数据量的等损失线与参考点局部替代率。数值来自当前问题二结果；图中增量为导数的局部线性近似。"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      load, cn, auto_legend, declutter_axes)

p2 = load("problem_2_results.json")
el = p2["elasticity"]
ic = el["iso_loss_contour"]
Ns = np.asarray(ic["N_grid"], dtype=float)
Qs = np.asarray(ic["Q_grid"], dtype=float)
LL = np.asarray(ic["L_surface"], dtype=float)      # shape (len(Qs), len(Ns))
ref = el["reference_point"]
slope = float(el["substitution_dN_dQ"])
dN01 = float(el["delta_N_for_deltaQ_0.1"])

QQ, NN = np.meshgrid(Qs, Ns, indexing="ij")        # 与 LL 同序

fig, ax = plt.subplots(figsize=(6.2, 4.6), layout="constrained")
set_paper_placement(fig)

levels = np.linspace(float(LL.min()), float(LL.max()), 18)
cf = ax.contourf(QQ, NN, LL, levels=levels, cmap="YlOrRd", alpha=0.88, zorder=1)
# 等值线与标注用深色：白线白字在浅 YlOrRd 区对比度不足（实测 3.81:1 < 4.5:1）；
# 标注层数取 every-5 而非 every-3，避免左下密集区 "2.72"×"2.91" 相撞
cs = ax.contour(QQ, NN, LL, levels=levels[::5], colors=[COLORS["text"]],
                linewidths=0.7, alpha=0.80, zorder=2)
# 损失刻度由右侧色条给出，避免低N密集区域的等值线数字相互遮挡。

# 参考点所在等损失线（加粗）
cs_ref = ax.contour(QQ, NN, LL, levels=[float(ref["L0"])], colors=[COLORS["text"]],
                    linewidths=1.9, zorder=4)

# 参考点切线段：dN = slope·dQ，取 ΔQ=±0.1 的线段长度
dq = 0.10
q0, n0 = float(ref["Q0"]), float(ref["N0"])
ax.plot([q0 - dq, q0 + dq], [n0 - slope * dq, n0 + slope * dq],
        color=COLORS["down"], linewidth=2.0, linestyle="--", zorder=5,
        label=cn("切线 $dN/dQ|_L$=%.3f" % slope))
ax.scatter([q0], [n0], s=92, marker="*", color=COLORS["down"],
           edgecolors="white", linewidths=1.3, zorder=6,
           label=cn("参考点 $L_0$=%.4f" % ref["L0"]))

# 替代量短锚点：ΔQ=+0.1 对应的 N 节省
ax.annotate("", xy=(q0 + dq, n0 + slope * dq), xytext=(q0, n0),
            arrowprops=dict(arrowstyle="-|>", color=COLORS["down"], lw=1.5,
                            shrinkA=4, shrinkB=0), zorder=6)
ax.annotate(cn("局部近似 $\\Delta N$=%.3f（$\\Delta Q$=0.1）" % dN01),
        xy=(q0 + dq, n0 + slope * dq), xytext=(0.60, 1.75),
        arrowprops=dict(arrowstyle="-", color=COLORS["down"], lw=0.8),
        fontsize=8.5, va="center", ha="left", fontweight="bold",
        color=COLORS["down"],
        bbox=dict(boxstyle="round,pad=0.24", facecolor="white",
                  edgecolor=COLORS["down"], alpha=0.92, linewidth=0.7), zorder=7)

ax.set_xlabel(cn("数据质量 $Q$（无量纲）"))
ax.set_ylabel(cn("模型规模 $N$（$10^9$ 参数）"))
ax.set_xlim(float(Qs.min()), float(Qs.max()))
ax.set_ylim(float(Ns.min()), float(Ns.max()))
declutter_axes(ax, grid=False)
cb = fig.colorbar(cf, ax=ax, shrink=0.94, aspect=22, pad=0.022)
cb.set_label(cn("损失 $L$（nats/token，$D$=%d$\\times10^9$ tokens）" % int(ic["D_fixed"])),
             fontsize=9)
cb.ax.tick_params(labelsize=8)
auto_legend(ax, loc="upper right", fontsize=8.5, frameon=False,
            labelspacing=0.3, handlelength=1.6)

save_fig(fig, "figures/fig_q2_substitution_contour.pdf")
