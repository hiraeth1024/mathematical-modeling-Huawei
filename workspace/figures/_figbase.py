# -*- coding: utf-8 -*-
"""figures/_figbase.py — 数据图公共引导：路径注入 + 结果载入 + 口径函数。

所有 gen_fig_*.py 统一 `from _figbase import ...`，把样板收敛到一处，避免十几份
脚本各写各的导入与各算一套口径。数据一律来自 figures/*.json（comp-code 产物）
与 figures/_prep_*.{json,npz}（本步骤按同口径重算的文档级中间量），不硬编码数值。
"""
from __future__ import annotations
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from _utils.plot_utils import (setup_style, save_fig, set_paper_placement,  # noqa: E402
                               PALETTE, PALETTE_LIGHT, COLORS, _lighten,
                               auto_legend, smart_labels, dynamic_limits,
                               declutter_axes, uncertainty_band,
                               draw_vector_heatmap, shared_legend,
                               consolidate_shared_legends)

setup_style()


def load(name):
    """按 figures/ → output/ 顺序找结果文件（JSON）。"""
    for base in (HERE, os.path.join(ROOT, "output")):
        p = os.path.join(base, name)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                return json.load(fh)
    raise FileNotFoundError(name)


def load_npz(name):
    p = os.path.join(HERE, name)
    if not os.path.exists(p):
        raise FileNotFoundError(p)
    return np.load(p, allow_pickle=True)


def panel(ax, tag):
    """子图角标 (a)(b)(c) — 紧贴左上，不是整图标题。"""
    ax.set_title(tag, fontsize=11, fontweight="bold", loc="left", pad=3)


_GLYPH_FIX = (("⇒", "→"), ("≫", r"$\gg$"), ("⛔", "【校核】"), ("✔", "√"), ("⚠", "【注】"))


def cn(s):
    """中文/符号标签兜底：雅黑缺字会渲染成空白方框。"""
    s = str(s)
    for bad, good in _GLYPH_FIX:
        s = s.replace(bad, good)
    return s


def log_floor(vals, eps=1e-6):
    """对数轴零值地板：贴真实最小值下方半个数量级，避免写死常量撑爆量程。"""
    real = np.asarray(vals, dtype=float)
    real = real[np.isfinite(real) & (real > eps)]
    if real.size == 0:
        return eps
    return 10.0 ** (np.floor(np.log10(real.min())) - 0.5)


# ---- 标度律（与 code/problem2.py、code/problem3.py 同式，不另立口径）----
def generalized_loss(params, N, D, Q):
    """广义标度律 L(N,D,Q) = E + A·N^(-α) + B·(Q^θ·D)^(-β)。"""
    E, A, alpha, B, beta, theta = params
    N = np.asarray(N, dtype=float)
    D = np.asarray(D, dtype=float)
    Q = np.asarray(Q, dtype=float)
    return E + A * N ** (-alpha) + B * (Q ** theta * D) ** (-beta)


def elasticities(params, N, D, Q):
    """式12 弹性：ε_N, ε_D, ε_Q = θ·ε_D（均为 ∂lnL/∂ln·，应 < 0）。"""
    E, A, alpha, B, beta, theta = params
    L = float(generalized_loss(params, N, D, Q))
    eps_N = -alpha * A * N ** (-alpha) / L
    Deff = Q ** theta * D
    eps_D = -beta * B * Deff ** (-beta) / L
    return {"L": L, "eps_N": float(eps_N), "eps_D": float(eps_D),
            "eps_Q": float(theta * eps_D)}


def fmt_pow10(c):
    """算力预算 1e22 → LaTeX $10^{22}$。"""
    return r"$10^{%d}$" % int(round(np.log10(float(c))))
