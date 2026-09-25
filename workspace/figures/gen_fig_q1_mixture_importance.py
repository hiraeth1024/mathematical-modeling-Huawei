# -*- coding: utf-8 -*-
"""fig_q1_mixture_importance — 17 域配比对 Loss 的重要性棒棒糖图（配方 advanced #1）。

本图讲什么：RegMix 512 组配方上线性模型的零和编码系数平均绝对值。
  数值表示相对平均配比域的模型内对比强度，不能作因果解释。同时用标记形状区分
  该域能否映射到问题一的质量指标体系：direct/near_direct 的 Q 可直接取用，
  inferred 的 Q 只能按体裁相似性推断、可信度低——高重要性却只能推断 Q 的域
  （如 enron_emails）是配比-质量联合建模的主要不确定性来源。
数据来源：output/q1_mixture_model.json['mixture_domain_importance'] ←
  A4 train_mixture_1m(512) + A5 train_pile_loss_1m(512)；映射类型来自
  figures/problem_1_results.json['domain_mapping']['mapping_pairs'](A16)。
关键数值：LightGBM 对照 R²=0.977；线性配比回归 13 域训练 R² 0.496~0.786；
  重要性中位数作参考线；17 域中 direct 3 / near_direct 3 / inferred 11。
版式：原生 6.4×5.0in，17 行类别，横向棒棒糖。
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt

from _figbase import (save_fig, set_paper_placement, PALETTE, COLORS,
                      _lighten, load, cn, auto_legend, declutter_axes)

mm = load("q1_mixture_model.json")
p1 = load("problem_1_results.json")
imp = mm["mixture_domain_importance"]
mtype = {d["mixture"]: d["type"] for d in p1["domain_mapping"]["mapping_pairs"]}

items = sorted(imp.items(), key=lambda kv: kv[1], reverse=True)
names = [k for k, _ in items]
vals = np.array([v for _, v in items], dtype=float)
n = len(names)
med = float(np.median(vals))

STYLE = {"direct": ("o", PALETTE[0], cn("直接对应")),
         "near_direct": ("s", PALETTE[2], cn("近似对应")),
         "inferred": ("^", PALETTE[1], cn("推断映射"))}

fig, ax = plt.subplots(figsize=(6.4, 5.0), layout="constrained")
set_paper_placement(fig)
y = np.arange(n)

ax.axvline(med, color=COLORS["ref_line"], linestyle=":", linewidth=1.1, zorder=1,
           label=cn("重要性中位数 %.3f" % med))

seen = set()
for i, (nm, v) in enumerate(zip(names, vals)):
    t = mtype.get(nm, "inferred")
    mk, col, lg = STYLE[t]
    ax.hlines(i, 0, v, color=_lighten(col, 0.35), linewidth=2.3,
              capstyle="round", zorder=2)
    ax.scatter(v, i, s=76, color=col, marker=mk, edgecolors="white",
               linewidths=1.1, zorder=4, label=lg if t not in seen else None)
    seen.add(t)
    ax.text(v + vals.max() * 0.055, i, f"{v:.3f}", va="center", ha="left",
            fontsize=8.5, fontweight="bold" if i < 3 else "normal",
            color=COLORS["text"])

ax.set_yticks(y)
ax.set_yticklabels([cn(s) for s in names], fontsize=8.5)
ax.set_xlabel(cn("零和编码下的平均绝对系数（非因果）"))
ax.set_xlim(0, vals.max() * 1.22)
ax.set_ylim(n - 0.5, -0.7)
declutter_axes(ax, grid="x")
auto_legend(ax, loc="lower right", fontsize=8.5, frameon=False,
            labelspacing=0.3, handlelength=1.4)

save_fig(fig, "figures/fig_q1_mixture_importance.pdf")
