# -*- coding: utf-8 -*-
"""gen_tables.py — 生成论文表格（booktabs 三线表，PDF 模式 .tex）。

五张表，全部从 figures/*.json 与 figures/_prep_*.json 读数，不硬编码：
  TABLE_q1_weights      22 指标三组平衡权重 vs CRITIC 权重对照
  TABLE_q1_domain_Q     七域 Q 与 bootstrap 区间（描述性统计）
  TABLE_q2_scaling      经典/广义标度律参数 + 拟合与泛化优度（主结果表）
  TABLE_q3_allocation   三档预算 × 三种 g(Q) 最优配置 + 等数值基线\\newline $N=D$
  TABLE_q4_frontier     12/24 月能力前沿三情景分位数

表注只写短标题（≤20 汉字）；统计口径/重复次数/数据来源写进论文正文。
"""
from __future__ import annotations
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    for base in (HERE, os.path.join(os.path.dirname(HERE), "output")):
        p = os.path.join(base, name)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                return json.load(fh)
    raise FileNotFoundError(name)


def write(lines, name):
    p = os.path.join(HERE, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"Saved: figures/{name} ({os.path.getsize(p)} bytes)")


def esc(s):
    return str(s).replace("_", r"\_").replace("%", r"\%").replace("&", r"\&")


p1 = load("problem_1_results.json")
p2 = load("problem_2_results.json")
p3 = load("problem_3_results.json")
p4 = load("problem_4_results.json")
pre1 = load("_prep_q1.json")

# ===================== TABLE_q1_weights =====================
w_main, w_c = p1["weights"], p1["weights_critic"]
short = dict(zip(pre1["indicators"], pre1["short_labels"]))
items = sorted(w_main, key=lambda k: -w_main[k])
half = (len(items) + 1) // 2
L = [r"\begin{table}[!htbp]", r"  \centering",
     r"  \caption{三组平衡主权重与 CRITIC 对照}", r"  \label{tab:q1_weights}",
     r"  \songti\zihao{-4}",
     r"  \setlength{\tabcolsep}{4pt}",
     r"  \begin{tabular}{rlcc@{\hspace{1em}}rlcc}", r"    \toprule",
     r"    \# & 指标 & 主权重 $w_j$ & CRITIC & \# & 指标 & 主权重 $w_j$ & CRITIC \\",
     r"    \midrule"]
for i in range(half):
    a = items[i]
    row = f"    {i + 1} & {esc(short[a])} & {w_main[a]:.4f} & {w_c[a]:.4f}"
    j = i + half
    if j < len(items):
        b = items[j]
        row += f" & {j + 1} & {esc(short[b])} & {w_main[b]:.4f} & {w_c[b]:.4f} \\\\"
    else:
        row += r" & & & & \\"
    L.append(row)
L += [r"    \midrule",
      r"    \multicolumn{4}{l}{合计 $\sum_j w_j$} & \multicolumn{4}{r}{%.6f} \\"
      % p1["weights_sum"],
      r"    \bottomrule", r"  \end{tabular}", r"\end{table}"]
write(L, "TABLE_q1_weights.tex")

# ===================== TABLE_q1_domain_Q =====================
ci = pre1["domain_Q_A1_ci"]
ext = {v["domain"]: v for v in pre1["domain_Q_extended_ci"].values()}
doms = sorted(ci, key=lambda d: -ci[d]["Q"])
qs = p1["Q_stats"]
L = [r"\begin{table}[!htbp]", r"  \centering",
     r"  \caption{域级综合质量统计}", r"  \label{tab:q1_domain_Q}",
     r"  \songti\zihao{-4}",
     r"  \begin{tabular}{lrccrc}", r"    \toprule",
     r"    域 & $n_{A1}$ & $Q_{A1}$ & 95\% 区间 & $n_{ext}$ & $Q_{ext}$ \\",
     r"    \midrule"]
for d in doms:
    a = ci[d]
    e = ext.get(d)
    L.append("    %s & %d & %.5f & [%.5f, %.5f] & %s & %s \\\\" % (
        esc(d), a["n"], a["Q"], a["lo"], a["hi"],
        f"{e['n']}" if e else "--", f"{e['Q']:.5f}" if e else "--"))
L += [r"    \midrule",
      r"    全样本 & %d & %.5f & -- & -- & -- \\" % (
          pre1["n_docs_A1"], qs["mean"]),
      r"    \bottomrule", r"  \end{tabular}", r"\end{table}"]
write(L, "TABLE_q1_domain_Q.tex")

# ===================== TABLE_q2_scaling =====================
cp, gp = p2["classic"]["params"], p2["generalized"]["params"]
g, c = p2["generalized"], p2["classic"]
gen = c["generalization"]
L = [r"\begin{table}[!htbp]", r"  \centering",
     r"  \caption{标度律参数与拟合优度}", r"  \label{tab:q2_scaling}",
     r"  \songti\zihao{-4}",
     r"  \begin{tabular}{lrr}", r"    \toprule",
     r"    项 & 经典律 $L(N,D)$ & 广义律 $L(N,D,Q)$ \\", r"    \midrule",
     r"    \multicolumn{3}{l}{参数} \\"]
for k, sym in (("E", r"$E$"), ("A", r"$A$"), ("alpha", r"$\alpha$"),
               ("B", r"$B$"), ("beta", r"$\beta$")):
    L.append(f"    \\quad {sym} & {cp[k]:.4f} & {gp[k]:.4f} \\\\")
L += [r"    \quad $\theta$ (经验) & -- & %.3f \\" % g["theta_empirical_B6B8"],
      r"    \quad $\theta$ (下游取用) & -- & %.2f \\" % g["theta_assumed_downstream"],
      r"    \midrule", r"    \multicolumn{3}{l}{拟合} \\",
      r"    \quad 样本量 $n$ & %d & %d \\" % (c["n_fit"], g["n_fit"]),
      r"    \quad $R^2$ & %.7f & %.4f \\" % (c["r2"], g["r2"]),
      r"    \quad 残差标准差 & %.3e & -- \\" % c["residual_std"],
      r"    \midrule", r"    \multicolumn{3}{l}{留出/外部集 RMSE} \\",
      r"    \quad B6--B8 分组留出 ($n$=%d) & %.4f & %.4f \\" % (
          g["n_holdout"], g["rmse_holdout_classic_baseline"],
          g["rmse_holdout_generalized"])]
for k in sorted(gen, key=lambda k: gen[k]["rmse"]):
    v = gen[k]
    L.append("    \\quad %s ($n$=%d) & %.4f & -- \\\\" % (
        esc(k.split("_", 1)[1]), v["n"], v["rmse"]))
L += [r"    \midrule", r"    \multicolumn{3}{l}{参考点弹性} \\"]
el = p2["elasticity"]
for k, sym in (("eps_N", r"$\varepsilon_N$"), ("eps_D", r"$\varepsilon_D$"),
               ("eps_Q", r"$\varepsilon_Q$")):
    L.append(f"    \\quad {sym} & -- & {el[k]:.4f} \\\\")
L += [r"    \quad $dN/dQ|_L$ & -- & %.4f \\" % el["substitution_dN_dQ"],
      r"    \bottomrule", r"  \end{tabular}", r"\end{table}"]
write(L, "TABLE_q2_scaling.tex")

# ===================== TABLE_q3_allocation =====================
oa = p3["optimal_allocation"]
bkeys = list(oa["by_gtype"]["exp"].keys())
GT = [("exp", "指数型"), ("pow", "幂型"), ("log", "对数型")]
# 保持小四号宋体：窄列间距与方案名称换行代替整表缩放。
L = [r"\begin{table}[!htbp]", r"  \centering",
     r"  \caption{三档预算下的最优算力配置}", r"  \label{tab:q3_allocation}",
     r"  \songti\zihao{-4}",
     r"  \setlength{\tabcolsep}{4pt}",
     r"  \begin{tabular}{@{}l>{\raggedright\arraybackslash}p{2.4cm}rrrrrrr@{}}", r"    \toprule",
     r"    $C$ (FLOPs) & $g(Q)$ & $N^*$ & $D^*$ & $Q^*$ & $L^*$ "
     r"& $s_{train}$ & $s_Q$ & $s_{attn}$ \\", r"    \midrule"]
for bi, k in enumerate(bkeys):
    expo = int(round(__import__("math").log10(float(k))))
    for gi, (gt, glab) in enumerate(GT):
        d = oa["by_gtype"][gt][k]
        s = d["shares"]
        head = r"$10^{%d}$" % expo if gi == 0 else ""
        L.append("    %s & %s & %.3f & %.1f & %.4f & %.4f & %.4f & %.4f & %.4f \\\\"
                 % (head, glab, d["N"], d["D"], d["Q"], d["L"],
                    s["s_train"], s["s_Q"], s["s_attn"]))
    b = oa["baseline_chinchilla"][k]
    tot = float(b["C_tot"])
    L.append("    & 等数值基线\\newline $N=D$ & %.3f & %.1f & %.4f & %.4f & %.4f & %.4f & %.4f \\\\"
             % (b["N"], b["D"], b["Q"], b["L"],
                b["C_train"] / tot, b["C_Q"] / tot, b["C_attn"] / tot))
    fixed = oa["baseline_fixed_quality"][k]
    total = fixed["C_tot"]
    L.append("    & 固定质量\\newline 最优基线 & %.3f & %.1f & %.4f & %.4f & %.4f & %.4f & %.4f "
             % (fixed["N"], fixed["D"], fixed["Q"], fixed["L"],
                fixed["C_train"] / total, fixed["C_Q"] / total, fixed["C_attn"] / total)
             + r"\\")
    if bi < len(bkeys) - 1:
        L.append(r"    \midrule")
L += [r"    \bottomrule", r"  \end{tabular}", r"\end{table}"]
write(L, "TABLE_q3_allocation.tex")

# ===================== TABLE_q4_frontier =====================
fr = p4["frontier"]
SC = [("high", "维持", 1.0), ("mid", "放缓", 0.5), ("low", "停滞", 0.0)]
L = [r"\begin{table}[!htbp]", r"  \centering",
     r"  \caption{能力前沿情景预测分位数}", r"  \label{tab:q4_frontier}",
     r"  \songti\zihao{-4}",
     r"  \begin{tabular}{llrrrr}", r"    \toprule",
     r"    情景 & 斜率系数 & 期限 & P10 & P50 & P90 \\", r"    \midrule"]
for key, lab, mult in SC:
    for hi, h in enumerate(("12m", "24m")):
        d = fr["predictions"][key][h]
        L.append("    %s & %s & %s & %.2f & %.2f & %.2f \\\\" % (
            lab if hi == 0 else "", ("%.1f" % mult) if hi == 0 else "",
            h.replace("m", " 月"), d["P10"], d["P50"], d["P90"]))
    L.append(r"    \addlinespace[2pt]")
hf = fr["historical_frontier"]
L += [r"    \midrule",
      r"    历史末值 & -- & %.2f & \multicolumn{3}{r}{%.2f} \\" % (
          hf["t"][-1], hf["cap"][-1]),
      r"    历史斜率 & -- & -- & \multicolumn{3}{r}{%.2f 点/年} \\" % fr["slope"],
      r"    \bottomrule", r"  \end{tabular}", r"\end{table}"]
write(L, "TABLE_q4_frontier.tex")

print("\n全部表格生成完成（5 张，booktabs 三线表，PDF 模式 .tex）")
