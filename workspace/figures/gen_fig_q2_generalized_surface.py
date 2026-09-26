
# -*- coding: utf-8 -*-
"""广义损失曲面：B1 经典参数与假设 theta，数据来自当前 problem_2_results.json 的 surface_data。与问题三使用相同参数口径。"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  注册 3d 投影

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      load, cn)

p2 = load("problem_2_results.json")
g = p2["generalized"]
sd = g["surface_data"]
Ns = np.asarray(sd["N_grid"], dtype=float)
Qs = np.asarray(sd["Q_grid"], dtype=float)
LL = np.asarray(sd["L_surface"], dtype=float)      # shape (len(Qs), len(Ns))
Q1 = np.asarray(sd["Q1_line"], dtype=float)
D_fix = float(sd["D_fixed"])

# 横轴取 log10(N)：N 跨 3 个数量级，线性轴会把小模型全挤在一侧
lgN = np.log10(Ns)
XX, YY = np.meshgrid(lgN, Qs)

# 原生画布收窄到 5.6in：3D 轴 + 色条 + 图例行在 6.5in 上会被论文缩到 <0.9，
# 把 8.5pt 的刻度压到 7.2pt。收窄后缩放比接近 1，字号不再腰斩。
fig = plt.figure(figsize=(5.6, 4.0))
set_paper_placement(fig)
# 图例占独立行：3D 曲面铺满数据区，任何图内位置都会压住曲面
gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 0.075], hspace=0.01)
ax = fig.add_subplot(gs[0, 0], projection="3d")
ax_leg = fig.add_subplot(gs[1, 0])
ax_leg.axis("off")

surf = ax.plot_surface(XX, YY, LL, cmap="YlOrRd", alpha=0.88, edgecolor="none",
                       antialiased=True, rstride=1, cstride=1)
z_off = float(LL.min() - (LL.max() - LL.min()) * 0.28)
ax.contour(XX, YY, LL, zdir="z", offset=z_off, cmap="YlOrRd", alpha=0.55, levels=12)

# Q=1 退化对照线（= 经典律 L(N,D)）
ax.plot(lgN, np.ones_like(lgN), Q1, color=COLORS["text"], linewidth=2.0,
        zorder=10, label=cn("$Q$=1 退化线（经典律）"))

# 参考点：Q2 弹性分析所用 (N=1, Q=0.5)
ref = p2["elasticity"]["reference_point"]
if abs(ref["D0"] - D_fix) < 1e-9:
    ax.scatter([np.log10(ref["N0"])], [ref["Q0"]], [ref["L0"]], s=54,
               color=COLORS["down"], edgecolors="white", linewidths=1.2,
               depthshade=False, zorder=12,
               label=cn("弹性参考点 $L_0$=%.3f" % ref["L0"]))

# labelpad 拉开轴名与刻度：实测 "log10 N" 会压住 "-1.0" 刻度
ax.set_xlabel(cn("$\\log_{10} N$（$10^9$ 参数）"), labelpad=13)
ax.set_ylabel(cn("数据质量 $Q$（无量纲）"), labelpad=10)
ax.set_zlabel(cn("损失 $L$（nats/token）"), labelpad=9)
ax.set_zlim(z_off, float(LL.max()))
ax.set_xticks([-1, 0, 1, 2])
ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax.view_init(elev=24, azim=-131)
ax.tick_params(labelsize=9, pad=1.5)
h, l = ax.get_legend_handles_labels()
ax_leg.legend(h, l, loc="center", ncol=2, fontsize=8.5, frameon=False,
              labelspacing=0.3, handlelength=1.5, columnspacing=2.0)
cb = fig.colorbar(surf, ax=ax, shrink=0.60, aspect=16, pad=0.10)
cb.set_label(cn("$L$（nats/token）"), fontsize=9)
cb.ax.tick_params(labelsize=8)

save_fig(fig, "figures/fig_q2_generalized_surface.pdf")
