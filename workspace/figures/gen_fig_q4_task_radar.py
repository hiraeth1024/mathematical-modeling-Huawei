# -*- coding: utf-8 -*-
"""fig_q4_task_radar — 前沿模型逐任务六维能力雷达图（配方 competition #5）。

本图讲什么：C8 逐任务聚合（1860 个可解析目录，1854 个六维完整）里 Top-5 前沿
  模型在六个 Benchmark 上的剖面，叠加全样本任务均值作基准多边形。六维并非齐涨：
  MATH 与 GPQA 是所有前沿模型的共同短板（全样本均值 11.4 / 29.8），而 BBH 与
  MMLU-PRO 已接近饱和——说明问题四的"综合能力"单一均分口径会掩盖任务间的
  结构差异，前沿外推需按任务分别看。
数据来源：figures/problem_4_results.json['c8_aggregation']
  （top5_frontier_radar + task_difficulty_mean + task_correlation_dims）
  ← C8 detailed_results 1863 个子目录，7 个损坏目录已跳过。
关键数值：全样本均值 IFEval 40.2 / BBH 47.5 / MATH 11.4 / GPQA 29.8 /
  MUSR 40.0 / MMLU-PRO 32.0；Top-5 的 MATH 跨度 39.3~58.9。
版式：原生 6.2×5.0in，极坐标；5 个模型 + 1 条基准线共 6 条，模型名截断到 ≤18
  显示宽，图例在专用 GridSpec 列避免压住多边形。
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      load, cn)

c8 = load("problem_4_results.json")["c8_aggregation"]
dims = list(c8["task_correlation_dims"])
top5 = c8["top5_frontier_radar"]
mean6 = c8["task_difficulty_mean"]

# 模型名压缩：去掉组织前缀，保留版本标识
def short_name(k):
    s = k.split("_", 1)[-1] if "_" in k else k
    s = s.replace("instruct-", "").replace("-instruct", "")
    return s if len(s) <= 20 else s[:19] + "…"


names = list(top5.keys())
N = len(dims)
ang = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
ang_c = ang + [ang[0]]

fig = plt.figure(figsize=(6.2, 5.0), layout="constrained")
set_paper_placement(fig)
gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 0.40], wspace=0.02)
ax = fig.add_subplot(gs[0, 0], projection="polar")
ax_leg = fig.add_subplot(gs[0, 1])
ax_leg.axis("off")

R_MAX = 100.0
ax.set_ylim(0, R_MAX * 1.06)
rings = [20, 40, 60, 80, 100]
th = np.linspace(0, 2 * np.pi, 160)
for k, r in enumerate(rings):
    if k % 2 == 0:
        ax.fill_between(th, rings[k - 1] if k > 0 else 0, r, alpha=0.025,
                        color=PALETTE[0], zorder=0)
    ax.plot(th, [r] * len(th), color=COLORS["grid"], linewidth=0.5, zorder=1)
ax.set_yticks(rings)
# 半径刻度用 COLORS['text']：grid 浅灰做文字只有 3.4:1，够不到 4.5:1
ax.set_yticklabels([str(r) for r in rings], fontsize=8.0, color=COLORS["text"])
ax.set_xticks(ang)
ax.set_xticklabels([cn(d) for d in dims], fontsize=9.5, color=COLORS["text"])
ax.tick_params(axis="x", pad=13)

# 基准多边形：全样本任务均值
base = [float(mean6[d]) for d in dims]
ax.plot(ang_c, base + [base[0]], color=COLORS["text"], linewidth=1.9,
        linestyle="--", zorder=5, label=cn("全样本均值 n=%d" % c8["n_six_dim_complete"]))
ax.fill(ang_c, base + [base[0]], color=COLORS["text"], alpha=0.06, zorder=2)

for i, k in enumerate(names):
    vals = [float(top5[k][d]) for d in dims]
    col = PALETTE[i % len(PALETTE)]
    ax.plot(ang_c, vals + [vals[0]], color=col, linewidth=1.5, alpha=0.90,
            zorder=4, label=cn(short_name(k)))
    ax.fill(ang_c, vals + [vals[0]], color=col, alpha=0.045, zorder=3)

# 基准值数值锚点（每个维度一个，放在轴外圈内侧，不压多边形）
for a, v in zip(ang, base):
    ax.text(a, R_MAX * 1.045, f"{v:.1f}", ha="center", va="center", fontsize=8.0,
            color=COLORS["text"],
            bbox=dict(boxstyle="round,pad=0.14", facecolor="white",
                      edgecolor="none", alpha=0.88))

h, l = ax.get_legend_handles_labels()
ax_leg.legend(h, l, loc="center left", fontsize=8.0, frameon=False,
              labelspacing=0.45, handlelength=1.5,
              title=cn("C8 Top-5 前沿模型"), title_fontsize=8.2)

save_fig(fig, "figures/fig_q4_task_radar.pdf")
