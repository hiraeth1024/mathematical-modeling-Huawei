# -*- coding: utf-8 -*-
"""gen_latex_includes.py — 生成 figures/latex_includes.tex。

每图一个 [!htbp] 受控浮动块。caption 只写短标题（中文 ≤20 字），统计口径、结论、数据
来源全部留给论文正文——这样 caption 不会变成小字号段落，正文也能完整解释证据。
宽度按各图实际长宽比分档：越接近方形/越高，越要收窄，否则一张图吃掉整页高度。
"""
from __future__ import annotations
import os

import fitz

HERE = os.path.dirname(os.path.abspath(__file__))

# (文件名, 短标题 ≤20 汉字, LaTeX label 后缀)
FIGS = [
    ("fig_q1_quality_corr", "质量指标相关性聚类热力图", "q1_quality_corr"),
    ("fig_q1_conflict_scatter", "教育价值与广告含量的冲突区", "q1_conflict_scatter"),
    ("fig_q1_domain_Q_dumbbell", "抽样集与扩展集域级质量对照", "q1_domain_Q"),
    ("fig_q1_mixture_importance", "各域配比对损失的重要性排序", "q1_mixture_imp"),
    ("fig_q2_scaling_fit", "经典标度律拟合优度与残差", "q2_scaling_fit"),
    ("fig_q2_generalized_surface", "广义标度律损失曲面", "q2_gen_surface"),
    ("fig_q2_elasticity_diverging", "各因素损失弹性对照", "q2_elasticity"),
    ("fig_q2_substitution_contour", "等损失线与质量规模替代", "q2_substitution"),
    ("fig_q3_allocation_stacked", "三档预算下的算力份额构成", "q3_allocation"),
    ("fig_q3_transition_line", "最优份额演化与结构转移点", "q3_transition"),
    ("fig_q3_lctx_panels", "最优配置随上下文长度的变化", "q3_lctx"),
    ("fig_q4_contribution_decomp", "规模与非规模贡献分解", "q4_contribution"),
    ("fig_q4_bridge_scatter", "损失到能力的分层桥接", "q4_bridge"),
    ("fig_q4_frontier_fan", "能力前沿情景预测区间", "q4_frontier"),
    ("fig_q4_task_radar", "前沿模型逐任务能力剖面", "q4_task_radar"),
]


def width_fraction(ar):
    """按长宽比 (h/w) 分档选 \\textwidth 比例：越高越收窄，避免独占整页。"""
    if ar <= 0.62:
        return 1.00
    if ar <= 0.72:
        return 0.95
    if ar <= 0.82:
        return 0.88
    if ar <= 0.92:
        return 0.80
    return 0.74


lines = [
    "% figures/latex_includes.tex —— 由 figures/gen_latex_includes.py 生成",
    "% 使用 [!htbp] 受控浮动，允许 LaTeX 回填页面空白。",
    "% caption 只写短标题；口径/结论/数据来源写进正文。",
    "",
]
missing = []
for name, cap, lab in FIGS:
    pdf = os.path.join(HERE, name + ".pdf")
    if not os.path.exists(pdf):
        missing.append(name)
        continue
    with fitz.open(pdf) as d:
        r = d[0].rect
        ar = r.height / r.width
    wf = width_fraction(ar)
    lines += [
        r"\begin{figure}[!htbp]",
        r"  \centering",
        r"  \includegraphics[width=%.2f\textwidth]{figures/%s.pdf}" % (wf, name),
        r"  \caption{%s}" % cap,
        r"  \label{fig:%s}" % lab,
        r"\end{figure}",
        "",
    ]

out = os.path.join(HERE, "latex_includes.tex")
with open(out, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print(f"Saved: figures/latex_includes.tex ({os.path.getsize(out)} bytes), "
      f"{len(FIGS) - len(missing)}/{len(FIGS)} 图")
if missing:
    raise SystemExit("缺图: " + ", ".join(missing))
