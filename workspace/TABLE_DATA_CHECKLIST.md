# TABLE 数据真实性核对清单（paper-figure 步骤）

**JSON 源**: all_results.json, problem_1_results.json, problem_2_results.json, problem_3_results.json, problem_4_results.json
**JSON 数据条目**: 1540
**TABLE 文件**: 5 个

---

## 核心规则

**表格数字须能由结果数据复算；允许单位换算、舍入、差值、比值与统计区间，保留推导依据。**

paper-figure 步骤的设计是从 JSON 数据**渲染**出 TABLE 文件
（用 `_utils/stats_utils.py` 的 `regression_table()` / `descriptive_table()` 等函数，
或者读 JSON 后用 Python 脚本生成）。

**TABLE 中出现 JSON 没有的数字 = 编造**，必须用真实 JSON 数据重新生成对应表格。

---

## 自检步骤

1. **逐个打开 figures/TABLE_*.tex|md**，识别每个表格里的数字单元格
2. **对每个数字**，对照下方 JSON 数据清单：
   - ✅ 能精确匹配（含合理的精度截断如 `0.94` ↔ `0.93724`）→ 真实
   - 未直接匹配 JSON：先查推导、单位和舍入；仍无依据则标记待确认，不能直接认定编造或删除整张表，
     用真实 JSON 数据重新生成（推荐：`python3 -c "from _utils.stats_utils import descriptive_table; ..."`）
3. **跳过非数据型数字**：列号 `(1)(2)(3)`、列宽 `width=10cm`、LaTeX 字号 `\zihao{5}` 等格式标记中的数字
4. **修完所有 TABLE 后**，写自证标记：

   ```bash
   touch figures/TABLE_DATA_CHECK_PASSED.txt
   ```

   下一轮检查看到此标记会跳过自检循环。

**禁止**：禁止改 JSON 让数字"对得上"、禁止编造解释、禁止保留疑似编造的 TABLE。

**特别提示**：如果 JSON 中确实没有支撑某张表所需的数据（比如表格规划里有「数据集统计特征」但 JSON 只存了模型对比结果），说明 paper-analysis 步骤遗漏了该数据。应该：(a) 删除这张表 + 改写论文规划中关于这张表的引用；或 (b) 临时跑一段 Python 从原始数据重算并补到 JSON，再生成 TABLE。**不能**直接保留编造的数字。

---

## TABLE 文件全文

### `figures/TABLE_q1_domain_Q.tex` (831 字节)

```latex
\begin{table}[H]
  \centering
  \caption{域级综合质量统计}
  \label{tab:q1_domain_Q}
  \small
  \begin{tabular}{lrccrc}
    \toprule
    域 & $n_{A1}$ & $Q_{A1}$ & 95\% 区间 & $n_{ext}$ & $Q_{ext}$ \\
    \midrule
    book & 171 & 0.22722 & [0.20941, 0.24573] & -- & -- \\
    c4 & 10000 & 0.09766 & [0.09756, 0.09776] & -- & -- \\
    commoncrawl & 9640 & 0.07985 & [0.07964, 0.08005] & -- & -- \\
    arxiv & 1419 & 0.07893 & [0.07829, 0.07960] & 17523 & 0.09330 \\
    wikipedia & 10000 & 0.07647 & [0.07631, 0.07662] & -- & -- \\
    stackexchange & 10000 & 0.07212 & [0.07193, 0.07230] & -- & -- \\
    github & 10000 & 0.07090 & [0.07074, 0.07108] & 203752 & 0.07292 \\
    \midrule
    全样本 & 51230 & 0.07988 & [0.03847, 0.79560] & -- & -- \\
    \bottomrule
  \end{tabular}
\end{table}
```

### `figures/TABLE_q1_weights.tex` (1271 字节)

```latex
\begin{table}[H]
  \centering
  \caption{质量指标客观权重对照}
  \label{tab:q1_weights}
  \small
  \begin{tabular}{rlcc@{\hspace{2.2em}}rlcc}
    \toprule
    \# & 指标 & 熵权 $w_j$ & CRITIC & \# & 指标 & 熵权 $w_j$ & CRITIC \\
    \midrule
    1 & 词数 & 0.4192 & 0.0055 & 12 & 可读性 & 0.0076 & 0.0535 \\
    2 & 句子数 & 0.3988 & 0.0082 & 13 & 整洁度 & 0.0072 & 0.0566 \\
    3 & 句末标点 & 0.0367 & 0.1356 & 14 & 非字母词占比 & 0.0065 & 0.0643 \\
    4 & 平均词长 & 0.0301 & 0.0156 & 15 & 大写占比 & 0.0056 & 0.0762 \\
    5 & 流畅度 & 0.0146 & 0.0742 & 16 & unigram熵 & 0.0043 & 0.0533 \\
    6 & 广告含量 & 0.0143 & 0.0687 & 17 & 数字占比 & 0.0004 & 0.0251 \\
    7 & 推理性 & 0.0129 & 0.0625 & 18 & 2gram重复 & 0.0001 & 0.0143 \\
    8 & 唯一词占比 & 0.0119 & 0.0786 & 19 & 3gram重复 & 0.0001 & 0.0095 \\
    9 & 教育价值 & 0.0117 & 0.0623 & 20 & DSIR书籍 & 0.0000 & 0.0055 \\
    10 & 专业性 & 0.0093 & 0.0574 & 21 & DSIR维基 & 0.0000 & 0.0047 \\
    11 & QuRater & 0.0087 & 0.0644 & 22 & DSIR数学 & 0.0000 & 0.0039 \\
    \midrule
    \multicolumn{4}{l}{合计 $\sum_j w_j$} & \multicolumn{4}{r}{1.000000} \\
    \bottomrule
  \end{tabular}
\end{table}
```

### `figures/TABLE_q2_scaling.tex` (1364 字节)

```latex
\begin{table}[H]
  \centering
  \caption{标度律参数与拟合优度}
  \label{tab:q2_scaling}
  \small
  \begin{tabular}{lrr}
    \toprule
    项 & 经典律 $L(N,D)$ & 广义律 $L(N,D,Q)$ \\
    \midrule
    \multicolumn{3}{l}{\textit{参数}} \\
    \quad $E$ & 1.6898 & 0.2163 \\
    \quad $A$ & 0.3540 & 0.5311 \\
    \quad $\alpha$ & 0.3400 & 0.3090 \\
    \quad $B$ & 1.2403 & 2.9534 \\
    \quad $\beta$ & 0.2799 & 0.1228 \\
    \quad $\theta$ (经验) & -- & -10.000 \\
    \quad $\theta$ (下游取用) & -- & 0.50 \\
    \midrule
    \multicolumn{3}{l}{\textit{拟合}} \\
    \quad 样本量 $n$ & 1176 & 2012 \\
    \quad $R^2$ & 0.9999998 & 0.3389 \\
    \quad 残差标准差 & 1.466e-04 & -- \\
    \quad AIC & -31.6 & -1842.7 \\
    \quad BIC & -2.5 & -1807.8 \\
    \midrule
    \multicolumn{3}{l}{\textit{留出/外部集 RMSE}} \\
    \quad B6 留出 ($n$=502) & 0.9713 & 0.6879 \\
    \quad published ($n$=44) & 0.1976 & -- \\
    \quad baseline ($n$=57) & 0.2927 & -- \\
    \quad cerebras ($n$=1029) & 1.2431 & -- \\
    \midrule
    \multicolumn{3}{l}{\textit{参考点弹性}} \\
    \quad $\varepsilon_N$ & -- & -0.0657 \\
    \quad $\varepsilon_D$ & -- & -0.0860 \\
    \quad $\varepsilon_Q$ & -- & -0.0430 \\
    \quad $dN/dQ|_L$ & -- & -1.3097 \\
    \bottomrule
  \end{tabular}
\end{table}
```

### `figures/TABLE_q3_allocation.tex` (1409 字节)

```latex
\begin{table}[H]
  \centering
  \caption{三档预算下的最优算力配置}
  \label{tab:q3_allocation}
  \small
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{llrrrrrrr}
    \toprule
    $C$ (FLOPs) & $g(Q)$ & $N^*$ & $D^*$ & $Q^*$ & $L^*$ & $s_{train}$ & $s_Q$ & $s_{attn}$ \\
    \midrule
    $10^{19}$ & 指数型 & 0.231 & 5.8 & 0.5456 & 3.0984 & 0.8018 & 0.1434 & 0.0547 \\
     & 幂型 & 0.215 & 6.3 & 0.4456 & 3.1147 & 0.8192 & 0.1249 & 0.0559 \\
     & 对数型 & 0.521 & 1.4 & 1.0000 & 3.2528 & 0.4482 & 0.5212 & 0.0306 \\
    & Chinchilla 基线 & 1.249 & 1.2 & 0.0789 & 3.6807 & 0.9361 & 0.0000 & 0.0639 \\
    \midrule
    $10^{22}$ & 指数型 & 5.516 & 258.6 & 0.9680 & 2.1511 & 0.8559 & 0.0857 & 0.0584 \\
     & 幂型 & 5.798 & 237.2 & 1.0000 & 2.1530 & 0.8251 & 0.1186 & 0.0563 \\
     & 对数型 & 5.600 & 253.0 & 1.0000 & 2.1505 & 0.8501 & 0.0919 & 0.0580 \\
    & Chinchilla 基线 & 39.499 & 39.5 & 0.0789 & 2.4236 & 0.9361 & 0.0000 & 0.0639 \\
    \midrule
    $10^{24}$ & 指数型 & 40.770 & 3768.7 & 1.0000 & 1.9139 & 0.9219 & 0.0151 & 0.0629 \\
     & 幂型 & 40.942 & 3739.4 & 1.0000 & 1.9141 & 0.9186 & 0.0187 & 0.0627 \\
     & 对数型 & 40.703 & 3780.4 & 1.0000 & 1.9139 & 0.9232 & 0.0137 & 0.0630 \\
    & Chinchilla 基线 & 394.989 & 395.0 & 0.0789 & 2.0682 & 0.9361 & 0.0000 & 0.0639 \\
    \bottomrule
  \end{tabular}
  }
\end{table}
```

### `figures/TABLE_q4_frontier.tex` (789 字节)

```latex
\begin{table}[H]
  \centering
  \caption{能力前沿情景预测分位数}
  \label{tab:q4_frontier}
  \small
  \begin{tabular}{llrrrr}
    \toprule
    情景 & 斜率系数 & 期限 & P10 & P50 & P90 \\
    \midrule
    维持 & 1.0 & 12 月 & 61.03 & 62.52 & 67.39 \\
     &  & 24 月 & 80.09 & 81.94 & 87.07 \\
    \addlinespace[2pt]
    放缓 & 0.5 & 12 月 & 51.19 & 52.68 & 54.96 \\
     &  & 24 月 & 60.41 & 62.26 & 64.52 \\
    \addlinespace[2pt]
    停滞 & 0.0 & 12 月 & 40.73 & 42.84 & 47.71 \\
     &  & 24 月 & 40.73 & 42.84 & 44.84 \\
    \addlinespace[2pt]
    \midrule
    历史末值 & -- & 2025.21 & \multicolumn{3}{r}{41.75} \\
    历史斜率 & -- & -- & \multicolumn{3}{r}{19.68 点/年} \\
    \bottomrule
  \end{tabular}
\end{table}
```

---

## JSON 真实数据完整清单

### `all_results.json`（778 条）

| 数据路径 | 数值 |
|---|---|
| `_meta.seed` | 42 |
| `_meta.python` | `3.11.9` |
| `_meta.numpy` | `2.4.6` |
| `_meta.scipy` | `1.17.1` |
| `_meta.pandas` | `2.3.3` |
| `problem_1._meta.seed` | 42 |
| `problem_1._meta.python` | `3.11.9` |
| `problem_1._meta.numpy` | `2.4.6` |
| `problem_1._meta.scipy` | `1.17.1` |
| `problem_1._meta.pandas` | `2.3.3` |
| `problem_1.method` | `entropy_weight + simplex_regression` |
| `problem_1.weights.fluency_en` | 0.0146247 |
| `problem_1.weights.qurater` | 0.008666 |
| `problem_1.weights.ad_en` | 0.0143205 |
| `problem_1.weights.fineweb_edu` | 0.0117222 |
| `problem_1.weights.modernbert_cleanliness` | 0.007218 |
| `problem_1.weights.modernbert_reasoning` | 0.0128978 |
| `problem_1.weights.modernbert_professionalism` | 0.00931 |
| `problem_1.weights.modernbert_readability` | 0.007585 |
| `problem_1.weights.dsir_books` | 2.023e-05 |
| `problem_1.weights.rps_lines_ending_with_terminal_punctution_mark` | 0.0366953 |
| `problem_1.weights.rps_doc_num_sentences` | 0.398791 |
| `problem_1.weights.rps_doc_word_count` | 0.41917 |
| `problem_1.weights.rps_doc_frac_no_alph_words` | 0.006465 |
| `problem_1.weights.rps_doc_frac_chars_top_2gram` | 0.0001278 |
| `problem_1.weights.rps_lines_uppercase_letter_fraction` | 0.00556 |
| `problem_1.weights.rps_doc_frac_unique_words` | 0.011894 |
| `problem_1.weights.rps_lines_numerical_chars_fraction` | 0.0004423 |
| `problem_1.weights.dsir_math` | 1.024e-05 |
| `problem_1.weights.rps_doc_mean_word_length` | 0.030113 |
| `problem_1.weights.dsir_wiki` | 1.487e-05 |
| `problem_1.weights.rps_doc_frac_chars_top_3gram` | 5.728e-05 |
| `problem_1.weights.rps_doc_unigram_entropy` | 0.004297 |
| `problem_1.weights_critic.fluency_en` | 0.0742438 |
| `problem_1.weights_critic.qurater` | 0.0644344 |
| `problem_1.weights_critic.ad_en` | 0.0687191 |
| `problem_1.weights_critic.fineweb_edu` | 0.0622748 |
| `problem_1.weights_critic.modernbert_cleanliness` | 0.0565963 |
| `problem_1.weights_critic.modernbert_reasoning` | 0.0625461 |
| `problem_1.weights_critic.modernbert_professionalism` | 0.0573819 |
| `problem_1.weights_critic.modernbert_readability` | 0.0534822 |
| `problem_1.weights_critic.dsir_books` | 0.005516 |
| `problem_1.weights_critic.rps_lines_ending_with_terminal_punctution_mark` | 0.135597 |
| `problem_1.weights_critic.rps_doc_num_sentences` | 0.008175 |
| `problem_1.weights_critic.rps_doc_word_count` | 0.005542 |
| `problem_1.weights_critic.rps_doc_frac_no_alph_words` | 0.0643314 |
| `problem_1.weights_critic.rps_doc_frac_chars_top_2gram` | 0.0142926 |
| `problem_1.weights_critic.rps_lines_uppercase_letter_fraction` | 0.0762167 |
| `problem_1.weights_critic.rps_doc_frac_unique_words` | 0.0785672 |
| `problem_1.weights_critic.rps_lines_numerical_chars_fraction` | 0.0251127 |
| `problem_1.weights_critic.dsir_math` | 0.003856 |
| `problem_1.weights_critic.rps_doc_mean_word_length` | 0.0156062 |
| `problem_1.weights_critic.dsir_wiki` | 0.004702 |
| `problem_1.weights_critic.rps_doc_frac_chars_top_3gram` | 0.009496 |
| `problem_1.weights_critic.rps_doc_unigram_entropy` | 0.0533119 |
| `problem_1.weights_sum` | 1 |
| `problem_1.Q_stats.min` | 0.0384654 |
| `problem_1.Q_stats.max` | 0.795602 |
| `problem_1.Q_stats.mean` | 0.0798766 |
| `problem_1.Q_stats.median` | 0.0777438 |
| `problem_1.method_agreement.kendall_tau_entropy_critic` | 0.826574 |
| `problem_1.method_agreement.kendall_tau_entropy_pca` | 0.801909 |
| `problem_1.domain_Q_A1.arxiv.Q` | 0.0789294 |
| `problem_1.domain_Q_A1.arxiv.n` | 1419 |
| `problem_1.domain_Q_A1.book.Q` | 0.227218 |
| `problem_1.domain_Q_A1.book.n` | 171 |
| `problem_1.domain_Q_A1.c4.Q` | 0.097659 |
| `problem_1.domain_Q_A1.c4.n` | 10000 |
| `problem_1.domain_Q_A1.commoncrawl.Q` | 0.079846 |
| `problem_1.domain_Q_A1.commoncrawl.n` | 9640 |
| `problem_1.domain_Q_A1.github.Q` | 0.0709034 |
| `problem_1.domain_Q_A1.github.n` | 10000 |
| `problem_1.domain_Q_A1.stackexchange.Q` | 0.072122 |
| `problem_1.domain_Q_A1.stackexchange.n` | 10000 |
| `problem_1.domain_Q_A1.wikipedia.Q` | 0.0764665 |
| `problem_1.domain_Q_A1.wikipedia.n` | 10000 |
| `problem_1.domain_Q_median` | 0.0789294 |
| `problem_1.domain_Q_extended.A2_arxiv.Q_ext` | 0.0933028 |
| `problem_1.domain_Q_extended.A2_arxiv.n` | 17523 |
| `problem_1.domain_Q_extended.A2_arxiv.Q_A1_same_domain` | 0.0789294 |
| `problem_1.domain_Q_extended.A3_github.Q_ext` | 0.0729202 |
| `problem_1.domain_Q_extended.A3_github.n` | 203752 |
| `problem_1.domain_Q_extended.A3_github.Q_A1_same_domain` | 0.0709034 |
| `problem_1.conflict.positive_indicator` | `fineweb_edu` |
| `problem_1.conflict.negative_indicator` | `ad_en` |
| `problem_1.conflict.spearman_pos_vs_adcontent` | 0.139308 |
| `problem_1.conflict.conflict_rate` | 0.0496194 |
| `problem_1.conflict.n_conflict` | 2542 |
| `problem_1.conflict.resolution` | `降权 delta=0.5 + 稳健聚合` |
| `problem_1.conflict.kendall_tau_before_after` | 0.932026 |
| `problem_1.mixture_model.method` | `log-domain simplex-constrained linear regression + LightGBM` |
| `problem_1.mixture_model.n_train` | 512 |
| `problem_1.mixture_model.n_target_domains` | 13 |
| `problem_1.mixture_model.train_r2.arxiv` | 0.586098 |
| `problem_1.mixture_model.train_r2.freelaw` | 0.667298 |
| `problem_1.mixture_model.train_r2.pubmed_central` | 0.60095 |
| `problem_1.mixture_model.train_r2.wikipedia_en` | 0.733503 |
| `problem_1.mixture_model.train_r2.dm_mathematics` | 0.495573 |
| `problem_1.mixture_model.train_r2.github` | 0.639096 |
| `problem_1.mixture_model.train_r2.stackexchange` | 0.623649 |
| `problem_1.mixture_model.train_r2.gutenberg_pg_19` | 0.723126 |
| `problem_1.mixture_model.train_r2.pile_cc` | 0.786129 |
| `problem_1.mixture_model.train_r2.ubuntu_irc` | 0.614876 |
| `problem_1.mixture_model.train_r2.hackernews` | 0.692505 |
| `problem_1.mixture_model.train_r2.pubmed_abstracts` | 0.785364 |
| `problem_1.mixture_model.train_r2.uspto_backgrounds` | 0.771354 |
| `problem_1.mixture_model.holdout_r2.1m` | 0.663909 |
| `problem_1.mixture_model.holdout_r2.60m` | -5.38686 |
| `problem_1.mixture_model.holdout_r2.1B` | -265.29 |
| `problem_1.mixture_model.holdout_rank_spearman.1m` | 0.843892 |
| `problem_1.mixture_model.holdout_rank_spearman.60m` | 0.842117 |
| `problem_1.mixture_model.holdout_rank_spearman.1B` | 0.736415 |
| `problem_1.mixture_model.holdout_note` | `绝对R2跨尺度退化是真实现象(Loss量级随模型规模移动)；RegMix声称的跨尺度可迁移性由配比排序Spea...` |
| `problem_1.mixture_model.lightgbm_r2` | 0.976743 |
| `problem_1.mixture_model.mixture_domain_importance.arxiv` | 0.381073 |
| `problem_1.mixture_model.mixture_domain_importance.freelaw` | 0.365129 |
| `problem_1.mixture_model.mixture_domain_importance.nih_exporter` | 0.214986 |
| `problem_1.mixture_model.mixture_domain_importance.pubmed_central` | 0.345101 |
| `problem_1.mixture_model.mixture_domain_importance.wikipedia_en` | 0.315878 |
| `problem_1.mixture_model.mixture_domain_importance.dm_mathematics` | 0.58719 |
| `problem_1.mixture_model.mixture_domain_importance.github` | 0.350591 |
| `problem_1.mixture_model.mixture_domain_importance.philpapers` | 0.49983 |
| `problem_1.mixture_model.mixture_domain_importance.stackexchange` | 0.285686 |
| `problem_1.mixture_model.mixture_domain_importance.enron_emails` | 1.06851 |
| `problem_1.mixture_model.mixture_domain_importance.gutenberg_pg_19` | 0.289332 |
| `problem_1.mixture_model.mixture_domain_importance.pile_cc` | 0.293384 |
| `problem_1.mixture_model.mixture_domain_importance.ubuntu_irc` | 0.313162 |
| `problem_1.mixture_model.mixture_domain_importance.europarl` | 0.21502 |
| `problem_1.mixture_model.mixture_domain_importance.hackernews` | 0.181038 |
| `problem_1.mixture_model.mixture_domain_importance.pubmed_abstracts` | 0.30723 |
| `problem_1.mixture_model.mixture_domain_importance.uspto_backgrounds` | 0.347687 |
| `problem_1.mixture_model.simplex_ok` | True |
| `problem_1.domain_mapping.n_total` | 17 |
| `problem_1.domain_mapping.by_type.direct` | 3 |
| `problem_1.domain_mapping.by_type.inferred` | 11 |
| `problem_1.domain_mapping.by_type.near_direct` | 3 |
| `problem_1.domain_mapping.inferred_domains[0]` | `dm_mathematics` |
| `problem_1.domain_mapping.inferred_domains[1]` | `freelaw` |
| `problem_1.domain_mapping.inferred_domains[2]` | `nih_exporter` |
| `problem_1.domain_mapping.inferred_domains[10]` | `uspto_backgrounds` |
| `problem_1.domain_mapping.inferred_domains[...]` | `<7 项省略>` |
| `problem_1.domain_mapping.inferred_handling` | `保留配比为解释变量(间接影响其它域Loss)，按体裁相似性赋推断Q并标注低可信度，不无声丢弃` |
| `problem_1.domain_mapping.mapping_pairs[0].mixture` | `arxiv` |
| `problem_1.domain_mapping.mapping_pairs[0].quality` | `arxiv` |
| `problem_1.domain_mapping.mapping_pairs[0].type` | `direct` |
| `problem_1.domain_mapping.mapping_pairs[1].mixture` | `github` |
| `problem_1.domain_mapping.mapping_pairs[1].quality` | `github` |
| `problem_1.domain_mapping.mapping_pairs[1].type` | `direct` |
| `problem_1.domain_mapping.mapping_pairs[2].mixture` | `stackexchange` |
| `problem_1.domain_mapping.mapping_pairs[2].quality` | `stackexchange` |
| `problem_1.domain_mapping.mapping_pairs[2].type` | `direct` |
| `problem_1.domain_mapping.mapping_pairs[16].mixture` | `uspto_backgrounds` |
| `problem_1.domain_mapping.mapping_pairs[16].quality` | `(none)` |
| `problem_1.domain_mapping.mapping_pairs[16].type` | `inferred` |
| `problem_1.domain_mapping.mapping_pairs[...]` | `<13 项省略>` |
| `problem_2._meta.seed` | 42 |
| `problem_2._meta.python` | `3.11.9` |
| `problem_2._meta.numpy` | `2.4.6` |
| `problem_2._meta.scipy` | `1.17.1` |
| `problem_2._meta.pandas` | `2.3.3` |
| `problem_2.method` | `log-domain Huber-NLS classic + generalized (Q^theta D)` |
| `problem_2.classic.params.E` | 1.68984 |
| `problem_2.classic.params.A` | 0.353969 |
| `problem_2.classic.params.alpha` | 0.339985 |
| `problem_2.classic.params.B` | 1.24027 |
| `problem_2.classic.params.beta` | 0.279892 |
| `problem_2.classic.r2` | 1 |
| `problem_2.classic.n_fit` | 1176 |
| `problem_2.classic.residual_mean` | -4.996e-08 |
| `problem_2.classic.residual_std` | 0.0001466 |
| `problem_2.classic.generalization.B2_cerebras.n` | 1029 |
| `problem_2.classic.generalization.B2_cerebras.rmse` | 1.24308 |
| `problem_2.classic.generalization.B2_cerebras.r2` | -5.07275 |
| `problem_2.classic.generalization.B4_baseline.n` | 57 |
| `problem_2.classic.generalization.B4_baseline.rmse` | 0.292665 |
| `problem_2.classic.generalization.B4_baseline.r2` | 0.60451 |
| `problem_2.classic.generalization.B5_published.n` | 44 |
| `problem_2.classic.generalization.B5_published.rmse` | 0.197598 |
| `problem_2.classic.generalization.B5_published.r2` | 0.73055 |
| `problem_2.classic.n_trajectory_files` | 8 |
| `problem_2.classic.N_range[0]` | 0.070542 |
| `problem_2.classic.N_range[1]` | 11.9658 |
| `problem_2.classic.D_range[0]` | 0.134 |
| `problem_2.classic.D_range[1]` | 299.893 |
| `problem_2.classic.L_range[0]` | 2.0933 |
| `problem_2.classic.L_range[1]` | 4.7388 |
| `problem_2.classic.fit_scatter.actual[0]` | 4.7388 |
| `problem_2.classic.fit_scatter.actual[1]` | 4.3541 |
| `problem_2.classic.fit_scatter.actual[2]` | 4.0384 |
| `problem_2.classic.fit_scatter.actual[1175]` | 2.0933 |
| `problem_2.classic.fit_scatter.actual[...]` | `<1172 项省略>` |
| `problem_2.classic.fit_scatter.predicted[0]` | 4.73864 |
| `problem_2.classic.fit_scatter.predicted[1]` | 4.35475 |
| `problem_2.classic.fit_scatter.predicted[2]` | 4.03779 |
| `problem_2.classic.fit_scatter.predicted[1175]` | 2.09338 |
| `problem_2.classic.fit_scatter.predicted[...]` | `<1172 项省略>` |
| `problem_2.generalized.params.E` | 0.216297 |
| `problem_2.generalized.params.A` | 0.531097 |
| `problem_2.generalized.params.alpha` | 0.309038 |
| `problem_2.generalized.params.B` | 2.95341 |
| `problem_2.generalized.params.beta` | 0.122774 |
| `problem_2.generalized.params.theta` | -10 |
| `problem_2.generalized.theta_empirical_B6B8` | -10 |
| `problem_2.generalized.theta_assumed_downstream` | 0.5 |
| `problem_2.generalized.theta_role` | `assumed (下游Q3/Q4). B6-B8经验theta仅描述setpoint数据, 见corr_Q_L说明` |
| `problem_2.generalized.r2` | 0.338887 |
| `problem_2.generalized.n_fit` | 2012 |
| `problem_2.generalized.n_holdout` | 502 |
| `problem_2.generalized.corr_Q_L` | 0.445888 |
| `problem_2.generalized.corr_Q_L_note` | `B6-B8 Q_score为实验setpoint(重标定损失), 与Q_synth部署质量口径不同(报告表⑩明确区分)` |
| `problem_2.generalized.rmse_holdout_generalized` | 0.687874 |
| `problem_2.generalized.rmse_holdout_classic_baseline` | 0.97128 |
| `problem_2.generalized.generalized_better_or_equal` | True |
| `problem_2.generalized.aic.generalized` | -1843 |
| `problem_2.generalized.aic.classic` | -31.632 |
| `problem_2.generalized.bic.generalized` | -1808 |
| `problem_2.generalized.bic.classic` | -2.48386 |
| `problem_2.generalized.Q1_degeneracy_rel_err` | 0 |
| `problem_2.generalized.Q1_degeneracy_pass` | True |
| `problem_2.generalized.surface_data.N_grid[0]` | 0.1 |
| `problem_2.generalized.surface_data.N_grid[1]` | 0.126896 |
| `problem_2.generalized.surface_data.N_grid[2]` | 0.161026 |
| `problem_2.generalized.surface_data.N_grid[29]` | 100 |
| `problem_2.generalized.surface_data.N_grid[...]` | `<26 项省略>` |
| `problem_2.generalized.surface_data.Q_grid[0]` | 0.1 |
| `problem_2.generalized.surface_data.Q_grid[1]` | 0.131034 |
| `problem_2.generalized.surface_data.Q_grid[2]` | 0.162069 |
| `problem_2.generalized.surface_data.Q_grid[29]` | 1 |
| `problem_2.generalized.surface_data.Q_grid[...]` | `<26 项省略>` |
| `problem_2.generalized.surface_data.L_surface[0][0]` | 3.23095 |
| `problem_2.generalized.surface_data.L_surface[0][1]` | 3.15417 |
| `problem_2.generalized.surface_data.L_surface[0][2]` | 3.08283 |
| `problem_2.generalized.surface_data.L_surface[0][29]` | 2.27696 |
| `problem_2.generalized.surface_data.L_surface[0][...]` | `<26 项省略>` |
| `problem_2.generalized.surface_data.L_surface[1][0]` | 3.19915 |
| `problem_2.generalized.surface_data.L_surface[1][1]` | 3.12236 |
| `problem_2.generalized.surface_data.L_surface[1][2]` | 3.05103 |
| `problem_2.generalized.surface_data.L_surface[1][29]` | 2.24515 |
| `problem_2.generalized.surface_data.L_surface[1][...]` | `<26 项省略>` |
| `problem_2.generalized.surface_data.L_surface[2][0]` | 3.1745 |
| `problem_2.generalized.surface_data.L_surface[2][1]` | 3.09772 |
| `problem_2.generalized.surface_data.L_surface[2][2]` | 3.02638 |
| `problem_2.generalized.surface_data.L_surface[2][29]` | 2.22051 |
| `problem_2.generalized.surface_data.L_surface[2][...]` | `<26 项省略>` |
| `problem_2.generalized.surface_data.L_surface[29][0]` | 2.9762 |
| `problem_2.generalized.surface_data.L_surface[29][1]` | 2.89941 |
| `problem_2.generalized.surface_data.L_surface[29][2]` | 2.82808 |
| `problem_2.generalized.surface_data.L_surface[29][29]` | 2.0222 |
| `problem_2.generalized.surface_data.L_surface[29][...]` | `<26 项省略>` |
| `problem_2.generalized.surface_data.L_surface[...]` | `<26 项省略>` |
| `problem_2.generalized.surface_data.D_fixed` | 100 |
| `problem_2.generalized.surface_data.Q1_line[0]` | 2.9762 |
| `problem_2.generalized.surface_data.Q1_line[1]` | 2.89941 |
| `problem_2.generalized.surface_data.Q1_line[2]` | 2.82808 |
| `problem_2.generalized.surface_data.Q1_line[29]` | 2.0222 |
| `problem_2.generalized.surface_data.Q1_line[...]` | `<26 项省略>` |
| `problem_2.elasticity.reference_point.N0` | 1 |
| `problem_2.elasticity.reference_point.D0` | 100 |
| `problem_2.elasticity.reference_point.Q0` | 0.5 |
| `problem_2.elasticity.reference_point.L0` | 2.49827 |
| `problem_2.elasticity.eps_N` | -0.0656971 |
| `problem_2.elasticity.eps_D` | -0.0860441 |
| `problem_2.elasticity.eps_Q` | -0.043022 |
| `problem_2.elasticity.eps_Q_equals_theta_eps_D` | -0.043022 |
| `problem_2.elasticity.substitution_dN_dQ` | -1.30971 |
| `problem_2.elasticity.delta_N_for_deltaQ_0.1` | -0.130971 |
| `problem_2.elasticity.iso_loss_contour.N_grid[0]` | 0.1 |
| `problem_2.elasticity.iso_loss_contour.N_grid[1]` | 0.353846 |
| `problem_2.elasticity.iso_loss_contour.N_grid[2]` | 0.607692 |
| `problem_2.elasticity.iso_loss_contour.N_grid[39]` | 10 |
| `problem_2.elasticity.iso_loss_contour.N_grid[...]` | `<36 项省略>` |
| `problem_2.elasticity.iso_loss_contour.Q_grid[0]` | 0.1 |
| `problem_2.elasticity.iso_loss_contour.Q_grid[1]` | 0.123077 |
| `problem_2.elasticity.iso_loss_contour.Q_grid[2]` | 0.146154 |
| `problem_2.elasticity.iso_loss_contour.Q_grid[39]` | 1 |
| `problem_2.elasticity.iso_loss_contour.Q_grid[...]` | `<36 项省略>` |
| `problem_2.elasticity.iso_loss_contour.L_surface[0][0]` | 3.23095 |
| `problem_2.elasticity.iso_loss_contour.L_surface[0][1]` | 2.88115 |
| `problem_2.elasticity.iso_loss_contour.L_surface[0][2]` | 2.76846 |
| `problem_2.elasticity.iso_loss_contour.L_surface[0][39]` | 2.40969 |
| `problem_2.elasticity.iso_loss_contour.L_surface[0][...]` | `<36 项省略>` |
| `problem_2.elasticity.iso_loss_contour.L_surface[1][0]` | 3.20647 |
| `problem_2.elasticity.iso_loss_contour.L_surface[1][1]` | 2.85667 |
| `problem_2.elasticity.iso_loss_contour.L_surface[1][2]` | 2.74399 |
| `problem_2.elasticity.iso_loss_contour.L_surface[1][39]` | 2.38521 |
| `problem_2.elasticity.iso_loss_contour.L_surface[1][...]` | `<36 项省略>` |
| `problem_2.elasticity.iso_loss_contour.L_surface[2][0]` | 3.18645 |
| `problem_2.elasticity.iso_loss_contour.L_surface[2][1]` | 2.83665 |
| `problem_2.elasticity.iso_loss_contour.L_surface[2][2]` | 2.72396 |
| `problem_2.elasticity.iso_loss_contour.L_surface[2][39]` | 2.36518 |
| `problem_2.elasticity.iso_loss_contour.L_surface[2][...]` | `<36 项省略>` |
| `problem_2.elasticity.iso_loss_contour.L_surface[39][0]` | 2.9762 |
| `problem_2.elasticity.iso_loss_contour.L_surface[39][1]` | 2.6264 |
| `problem_2.elasticity.iso_loss_contour.L_surface[39][2]` | 2.51371 |
| `problem_2.elasticity.iso_loss_contour.L_surface[39][39]` | 2.15493 |
| `problem_2.elasticity.iso_loss_contour.L_surface[39][...]` | `<36 项省略>` |
| `problem_2.elasticity.iso_loss_contour.L_surface[...]` | `<36 项省略>` |
| `problem_2.elasticity.iso_loss_contour.D_fixed` | 100 |
| `problem_3._meta.seed` | 42 |
| `problem_3._meta.python` | `3.11.9` |
| `problem_3._meta.numpy` | `2.4.6` |
| `problem_3._meta.scipy` | `1.17.1` |
| `problem_3._meta.pandas` | `2.3.3` |
| `problem_3.method` | `SLSQP multi-start + KKT + share-derivative transition` |
| `problem_3.scaling_params.E` | 1.68984 |
| `problem_3.scaling_params.A` | 0.353969 |
| `problem_3.scaling_params.alpha` | 0.339985 |
| `problem_3.scaling_params.B` | 1.24027 |
| `problem_3.scaling_params.beta` | 0.279892 |
| `problem_3.scaling_params.theta` | 0.5 |
| `problem_3.Q0` | 0.0789294 |
| `problem_3.eta` | 0.0002 |
| `problem_3.Lctx_crit` | 3e+04 |
| `problem_3.optimal_allocation.Lctx_main` | 2048 |
| `problem_3.optimal_allocation.budgets[0]` | 1e+19 |
| `problem_3.optimal_allocation.budgets[1]` | 1e+22 |
| `problem_3.optimal_allocation.budgets[2]` | 1e+24 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.N` | 0.231058 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.D` | 5.78365 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.Q` | 0.54561 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.L` | 3.09838 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.C_tot` | 1e+19 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.C_train` | 8.018e+18 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.C_Q` | 1.434e+18 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.C_attn` | 5.474e+17 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.shares.s_train` | 0.801816 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.shares.s_Q` | 0.143447 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.shares.s_attn` | 0.0547373 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+19.Q_above_Q0` | True |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.N` | 5.51552 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.D` | 258.632 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.Q` | 0.96796 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.L` | 2.15107 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.C_tot` | 1e+22 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.C_train` | 8.559e+21 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.C_Q` | 8.568e+20 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.C_attn` | 5.843e+20 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.shares.s_train` | 0.855895 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.shares.s_Q` | 0.0856764 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.shares.s_attn` | 0.0584291 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+22.Q_above_Q0` | True |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.N` | 40.7704 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.D` | 3769 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.Q` | 1 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.L` | 1.91393 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.C_tot` | 1e+24 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.C_train` | 9.219e+23 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.C_Q` | 1.514e+22 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.C_attn` | 6.294e+22 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.shares.s_train` | 0.92192 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.shares.s_Q` | 0.0151437 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.shares.s_attn` | 0.0629364 |
| `problem_3.optimal_allocation.by_gtype.exp.1e+24.Q_above_Q0` | True |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.N` | 0.2153 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.D` | 6.34152 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.Q` | 0.445591 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.L` | 3.11466 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.C_tot` | 1e+19 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.C_train` | 8.192e+18 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.C_Q` | 1.249e+18 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.C_attn` | 5.592e+17 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.shares.s_train` | 0.819199 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.shares.s_Q` | 0.124877 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.shares.s_attn` | 0.055924 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+19.Q_above_Q0` | True |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.N` | 5.79793 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.D` | 237.179 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.Q` | 1 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.L` | 2.15296 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.C_tot` | 1e+22 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.C_train` | 8.251e+21 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.C_Q` | 1.186e+21 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.C_attn` | 5.633e+20 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.shares.s_train` | 0.825089 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.shares.s_Q` | 0.118585 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.shares.s_attn` | 0.0563261 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+22.Q_above_Q0` | True |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.N` | 40.9419 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.D` | 3739 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.Q` | 1 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.L` | 1.91406 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.C_tot` | 1e+24 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.C_train` | 9.186e+23 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.C_Q` | 1.87e+22 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.C_attn` | 6.271e+22 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.shares.s_train` | 0.918594 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.shares.s_Q` | 0.0186964 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.shares.s_attn` | 0.0627094 |
| `problem_3.optimal_allocation.by_gtype.pow.1e+24.Q_above_Q0` | True |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.N` | 0.520637 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.D` | 1.43488 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.Q` | 1 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.L` | 3.25281 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.C_tot` | 1e+19 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.C_train` | 4.482e+18 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.C_Q` | 5.212e+18 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.C_attn` | 3.06e+17 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.shares.s_train` | 0.448231 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.shares.s_Q` | 0.52117 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.shares.s_attn` | 0.0305992 |
| `problem_3.optimal_allocation.by_gtype.log.1e+19.Q_above_Q0` | True |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.N` | 5.60039 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.D` | 252.983 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.Q` | 1 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.L` | 2.15047 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.C_tot` | 1e+22 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.C_train` | 8.501e+21 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.C_Q` | 9.189e+20 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.C_attn` | 5.803e+20 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.shares.s_train` | 0.850081 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.shares.s_Q` | 0.0918871 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.shares.s_attn` | 0.0580322 |
| `problem_3.optimal_allocation.by_gtype.log.1e+22.Q_above_Q0` | True |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.N` | 40.7026 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.D` | 3780 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.Q` | 1 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.L` | 1.91388 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.C_tot` | 1e+24 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.C_train` | 9.232e+23 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.C_Q` | 1.373e+22 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.C_attn` | 6.303e+22 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.util` | 1 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.shares.s_train` | 0.923242 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.shares.s_Q` | 0.0137311 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.shares.s_attn` | 0.0630267 |
| `problem_3.optimal_allocation.by_gtype.log.1e+24.Q_above_Q0` | True |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.N` | 1.24906 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.D` | 1.24906 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.Q` | 0.0789294 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.L` | 3.68072 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.C_tot` | 1e+19 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.C_train` | 9.361e+18 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.C_Q` | 0 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.C_attn` | 6.39e+17 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.util` | 1 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+19.note` | `Chinchilla等分基线(N=D,Q=Q0无质量投入)，作对照` |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.N` | 39.4989 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.D` | 39.4989 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.Q` | 0.0789294 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.L` | 2.42364 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.C_tot` | 1e+22 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.C_train` | 9.361e+21 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.C_Q` | 0 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.C_attn` | 6.39e+20 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.util` | 1 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+22.note` | `Chinchilla等分基线(N=D,Q=Q0无质量投入)，作对照` |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.N` | 394.989 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.D` | 394.989 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.Q` | 0.0789294 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.L` | 2.06816 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.C_tot` | 1e+24 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.C_train` | 9.361e+23 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.C_Q` | 0 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.C_attn` | 6.39e+22 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.util` | 1 |
| `problem_3.optimal_allocation.baseline_chinchilla.1e+24.note` | `Chinchilla等分基线(N=D,Q=Q0无质量投入)，作对照` |
| `problem_3.optimal_allocation.budget_monotonic_L` | True |
| `problem_3.structural_transition.gtype` | `exp` |
| `problem_3.structural_transition.logC_grid[0]` | 18 |
| `problem_3.structural_transition.logC_grid[1]` | 18.2 |
| `problem_3.structural_transition.logC_grid[2]` | 18.4 |
| `problem_3.structural_transition.logC_grid[35]` | 25 |
| `problem_3.structural_transition.logC_grid[...]` | `<32 项省略>` |
| `problem_3.structural_transition.C_grid[0]` | 1e+18 |
| `problem_3.structural_transition.C_grid[1]` | 1.585e+18 |
| `problem_3.structural_transition.C_grid[2]` | 2.512e+18 |
| `problem_3.structural_transition.C_grid[35]` | 1e+25 |
| `problem_3.structural_transition.C_grid[...]` | `<32 项省略>` |
| `problem_3.structural_transition.s_train[0]` | 0.774129 |
| `problem_3.structural_transition.s_train[1]` | 0.779972 |
| `problem_3.structural_transition.s_train[2]` | 0.785692 |
| `problem_3.structural_transition.s_train[35]` | 0.930977 |
| `problem_3.structural_transition.s_train[...]` | `<32 项省略>` |
| `problem_3.structural_transition.s_Q[0]` | 0.173024 |
| `problem_3.structural_transition.s_Q[1]` | 0.166782 |
| `problem_3.structural_transition.s_Q[2]` | 0.160671 |
| `problem_3.structural_transition.s_Q[35]` | 0.005469 |
| `problem_3.structural_transition.s_Q[...]` | `<32 项省略>` |
| `problem_3.structural_transition.s_attn[0]` | 0.0528472 |
| `problem_3.structural_transition.s_attn[1]` | 0.0532461 |
| `problem_3.structural_transition.s_attn[2]` | 0.0536366 |
| `problem_3.structural_transition.s_attn[35]` | 0.0635547 |
| `problem_3.structural_transition.s_attn[...]` | `<32 项省略>` |
| `problem_3.structural_transition.d_sQ_dlogC[0]` | -0.0312104 |
| `problem_3.structural_transition.d_sQ_dlogC[1]` | -0.0308821 |
| `problem_3.structural_transition.d_sQ_dlogC[2]` | -0.030132 |
| `problem_3.structural_transition.d_sQ_dlogC[35]` | -0.006229 |
| `problem_3.structural_transition.d_sQ_dlogC[...]` | `<32 项省略>` |
| `problem_3.structural_transition.d_strain_dlogC[0]` | 0.029216 |
| `problem_3.structural_transition.d_strain_dlogC[1]` | 0.0289086 |
| `problem_3.structural_transition.d_strain_dlogC[2]` | 0.0282064 |
| `problem_3.structural_transition.d_strain_dlogC[35]` | 0.005831 |
| `problem_3.structural_transition.d_strain_dlogC[...]` | `<32 项省略>` |
| `problem_3.structural_transition.Q_traj[0]` | 0.419047 |
| `problem_3.structural_transition.Q_traj[1]` | 0.443636 |
| `problem_3.structural_transition.Q_traj[2]` | 0.468596 |
| `problem_3.structural_transition.Q_traj[35]` | 1 |
| `problem_3.structural_transition.Q_traj[...]` | `<32 项省略>` |
| `problem_3.structural_transition.N_traj[0]` | 0.080176 |
| `problem_3.structural_transition.N_traj[1]` | 0.0991168 |
| `problem_3.structural_transition.N_traj[2]` | 0.122499 |
| `problem_3.structural_transition.N_traj[35]` | 114.01 |
| `problem_3.structural_transition.N_traj[...]` | `<32 项省略>` |
| `problem_3.structural_transition.D_traj[0]` | 1.60923 |
| `problem_3.structural_transition.D_traj[1]` | 2.07865 |
| `problem_3.structural_transition.D_traj[2]` | 2.68515 |
| `problem_3.structural_transition.D_traj[35]` | 1.361e+04 |
| `problem_3.structural_transition.D_traj[...]` | `<32 项省略>` |
| `problem_3.structural_transition.L_traj[0]` | 3.75079 |
| `problem_3.structural_transition.L_traj[1]` | 3.59887 |
| `problem_3.structural_transition.L_traj[2]` | 3.45856 |
| `problem_3.structural_transition.L_traj[35]` | 1.84697 |
| `problem_3.structural_transition.L_traj[...]` | `<32 项省略>` |
| `problem_3.structural_transition.transition_logC` | 22.4 |
| `problem_3.structural_transition.transition_C` | 2.512e+22 |
| `problem_3.structural_transition.CQ_first_activation_C` | 1e+18 |
| `problem_3.structural_transition.definition` | `结构转移=份额对logC导数峰值处(式18) + KKT活跃集切换(Q内点↔边界, C_Q铰链激活)` |
| `problem_3.lctx_sensitivity.budget_C` | 1e+22 |
| `problem_3.lctx_sensitivity.gtype` | `exp` |
| `problem_3.lctx_sensitivity.Lctx_set[0]` | 2048 |
| `problem_3.lctx_sensitivity.Lctx_set[1]` | 4096 |
| `problem_3.lctx_sensitivity.Lctx_set[2]` | 8192 |
| `problem_3.lctx_sensitivity.Lctx_set[3]` | 32768 |
| `problem_3.lctx_sensitivity.Lctx_set[4]` | 131072 |
| `problem_3.lctx_sensitivity.Lctx_crit` | 3e+04 |
| `problem_3.lctx_sensitivity.Lctx_crit_analytic` | 3e+04 |
| `problem_3.lctx_sensitivity.Lctx_crit_check` | True |
| `problem_3.lctx_sensitivity.panels.2048.N` | 5.51552 |
| `problem_3.lctx_sensitivity.panels.2048.D` | 258.632 |
| `problem_3.lctx_sensitivity.panels.2048.Q` | 0.96796 |
| `problem_3.lctx_sensitivity.panels.2048.L` | 2.15107 |
| `problem_3.lctx_sensitivity.panels.2048.shares.s_train` | 0.855895 |
| `problem_3.lctx_sensitivity.panels.2048.shares.s_Q` | 0.0856764 |
| `problem_3.lctx_sensitivity.panels.2048.shares.s_attn` | 0.0584291 |
| `problem_3.lctx_sensitivity.panels.4096.N` | 5.36661 |
| `problem_3.lctx_sensitivity.panels.4096.D` | 249.956 |
| `problem_3.lctx_sensitivity.panels.4096.Q` | 0.972814 |
| `problem_3.lctx_sensitivity.panels.4096.L` | 2.15526 |
| `problem_3.lctx_sensitivity.panels.4096.shares.s_train` | 0.80485 |
| `problem_3.lctx_sensitivity.panels.4096.shares.s_Q` | 0.0852608 |
| `problem_3.lctx_sensitivity.panels.4096.shares.s_attn` | 0.109889 |
| `problem_3.lctx_sensitivity.panels.8192.N` | 5.10425 |
| `problem_3.lctx_sensitivity.panels.8192.D` | 234.812 |
| `problem_3.lctx_sensitivity.panels.8192.Q` | 0.981713 |
| `problem_3.lctx_sensitivity.panels.8192.L` | 2.16304 |
| `problem_3.lctx_sensitivity.panels.8192.shares.s_train` | 0.719123 |
| `problem_3.lctx_sensitivity.panels.8192.shares.s_Q` | 0.0845086 |
| `problem_3.lctx_sensitivity.panels.8192.shares.s_attn` | 0.196368 |
| `problem_3.lctx_sensitivity.panels.32768.N` | 4.03879 |
| `problem_3.lctx_sensitivity.panels.32768.D` | 182.75 |
| `problem_3.lctx_sensitivity.panels.32768.Q` | 1 |
| `problem_3.lctx_sensitivity.panels.32768.L` | 2.19875 |
| `problem_3.lctx_sensitivity.panels.32768.shares.s_train` | 0.442853 |
| `problem_3.lctx_sensitivity.panels.32768.shares.s_Q` | 0.0734332 |
| `problem_3.lctx_sensitivity.panels.32768.shares.s_attn` | 0.483714 |
| `problem_3.lctx_sensitivity.panels.131072.N` | 2.55291 |
| `problem_3.lctx_sensitivity.panels.131072.D` | 115.93 |
| `problem_3.lctx_sensitivity.panels.131072.Q` | 1 |
| `problem_3.lctx_sensitivity.panels.131072.L` | 2.27514 |
| `problem_3.lctx_sensitivity.panels.131072.shares.s_train` | 0.177576 |
| `problem_3.lctx_sensitivity.panels.131072.shares.s_Q` | 0.0465834 |
| `problem_3.lctx_sensitivity.panels.131072.shares.s_attn` | 0.775841 |
| `problem_3.lctx_sensitivity.note` | `L_ctx_crit=6/eta=30000 tokens；落在8192与32768之间，即>=32768的长...` |
| `problem_4._meta.seed` | 42 |
| `problem_4._meta.python` | `3.11.9` |
| `problem_4._meta.numpy` | `2.4.6` |
| `problem_4._meta.scipy` | `1.17.1` |
| `problem_4._meta.pandas` | `2.3.3` |
| `problem_4.method` | `growth-accounting decomp + stratified sigmoid bridge + ...` |
| `problem_4.cap_metric` | `mean6` |
| `problem_4.open_criterion` | `hub_license` |
| `problem_4.capability_definition` | `六维Benchmark均分(IFEval,BBH,MATH,GPQA,MUSR,MMLU-PRO)` |
| `problem_4.contribution_decomp.model` | `Cap ~ lnN + year (OLS)` |
| `problem_4.contribution_decomp.r2` | 0.461658 |
| `problem_4.contribution_decomp.b_lnN` | 6.26623 |
| `problem_4.contribution_decomp.c_year` | 12.1419 |
| `problem_4.contribution_decomp.window.t0` | 2025 |
| `problem_4.contribution_decomp.window.t1` | 2025 |
| `problem_4.contribution_decomp.delta_Cap_observed` | 6.74324 |
| `problem_4.contribution_decomp.delta_lnN_window` | -0.273096 |
| `problem_4.contribution_decomp.delta_f_scale` | -1.71128 |
| `problem_4.contribution_decomp.delta_h_nonscale` | 8.54611 |
| `problem_4.contribution_decomp.scale_pct` | -25.0377 |
| `problem_4.contribution_decomp.nonscale_pct` | 125.038 |
| `problem_4.contribution_decomp.sum_check` | 100 |
| `problem_4.contribution_decomp.interpretation` | `2024-2025 窗口内，同规模下年度能力提升 c_year=12.1 点/年(非规模算法进步)；而平均参数...` |
| `problem_4.contribution_decomp.open_field_source` | `Epoch_AI_Open_Weights (C4)` |
| `problem_4.contribution_decomp.n_open_labeled` | 443 |
| `problem_4.contribution_decomp.yearly_evolution[0].year` | 2024 |
| `problem_4.contribution_decomp.yearly_evolution[0].scale_pct` | -0.390055 |
| `problem_4.contribution_decomp.yearly_evolution[0].nonscale_pct` | 100.39 |
| `problem_4.contribution_decomp.yearly_evolution[1].year` | 2025 |
| `problem_4.contribution_decomp.yearly_evolution[1].scale_pct` | -38.4328 |
| `problem_4.contribution_decomp.yearly_evolution[1].nonscale_pct` | 138.433 |
| `problem_4.contribution_decomp.n` | 4561 |
| `problem_4.bridge.method` | `stratified monotone sigmoid (式23)` |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).n` | 7 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).params.Smax` | 0.908066 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).params.a` | 18.6189 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).params.L0` | 2.13359 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).params.c` | 5.44904 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).r2` | 0.402881 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).residual_std` | 0.281131 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).monotone_decreasing` | True |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).L_range[0]` | 2.0933 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).L_range[1]` | 2.5978 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[0]` | 2.5978 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[1]` | 2.4209 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[2]` | 2.2904 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[6]` | 2.0933 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[...]` | `<3 项省略>` |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[0]` | 5.73039 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[1]` | 5.22707 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[2]` | 5.07027 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[6]` | 6.05984 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[...]` | `<3 项省略>` |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[0]` | 5.4492 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[1]` | 5.45333 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[2]` | 5.49552 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[6]` | 6.0658 |
| `problem_4.bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[...]` | `<3 项省略>` |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).n` | 68 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).params.Smax` | 15.4138 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).params.a` | 50 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).params.L0` | 2.21636 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).params.c` | 9.91298 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).r2` | 0.356452 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).residual_std` | 9.1149 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).monotone_decreasing` | True |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).L_range[0]` | 1.65 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).L_range[1]` | 2.84 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[0]` | 1.76 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[1]` | 1.75 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[2]` | 1.76 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[67]` | 2.25 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[...]` | `<64 项省略>` |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[0]` | 13.6269 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[1]` | 8.80636 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[2]` | 14.4209 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[67]` | 5.11657 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[...]` | `<64 项省略>` |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[0]` | 25.3268 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[1]` | 25.3268 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[2]` | 25.3268 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[67]` | 12.33 |
| `problem_4.bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[...]` | `<64 项省略>` |
| `problem_4.bridge.map_error_note` | `残差带宽反映映射误差，前沿结论须计入桥接不确定性` |
| `problem_4.frontier.method` | `P90 envelope + linear trend + bootstrap quantile band` |
| `problem_4.frontier.scenarios.low` | 0 |
| `problem_4.frontier.scenarios.mid` | 0.5 |
| `problem_4.frontier.scenarios.high` | 1 |
| `problem_4.frontier.scenario_note` | `算力增速档=相对历史前沿斜率的比例(0停滞/0.5放缓/1维持)，显式情景假设` |
| `problem_4.frontier.historical_frontier.t[0]` | 2024 |
| `problem_4.frontier.historical_frontier.t[1]` | 2025 |
| `problem_4.frontier.historical_frontier.t[2]` | 2025 |
| `problem_4.frontier.historical_frontier.t[9]` | 2025 |
| `problem_4.frontier.historical_frontier.t[...]` | `<6 项省略>` |
| `problem_4.frontier.historical_frontier.cap[0]` | 25.9748 |
| `problem_4.frontier.historical_frontier.cap[1]` | 28.2266 |
| `problem_4.frontier.historical_frontier.cap[2]` | 36.2308 |
| `problem_4.frontier.historical_frontier.cap[9]` | 41.7462 |
| `problem_4.frontier.historical_frontier.cap[...]` | `<6 项省略>` |
| `problem_4.frontier.slope` | 19.6791 |
| `problem_4.frontier.predictions.low.12m.P10` | 40.7341 |
| `problem_4.frontier.predictions.low.12m.P50` | 42.8404 |
| `problem_4.frontier.predictions.low.12m.P90` | 47.7103 |
| `problem_4.frontier.predictions.low.12m.t_target` | 2026 |
| `problem_4.frontier.predictions.low.24m.P10` | 40.7341 |
| `problem_4.frontier.predictions.low.24m.P50` | 42.8404 |
| `problem_4.frontier.predictions.low.24m.P90` | 44.8379 |
| `problem_4.frontier.predictions.low.24m.t_target` | 2027 |
| `problem_4.frontier.predictions.mid.12m.P10` | 51.1856 |
| `problem_4.frontier.predictions.mid.12m.P50` | 52.6799 |
| `problem_4.frontier.predictions.mid.12m.P90` | 54.9647 |
| `problem_4.frontier.predictions.mid.12m.t_target` | 2026 |
| `problem_4.frontier.predictions.mid.24m.P10` | 60.4132 |
| `problem_4.frontier.predictions.mid.24m.P50` | 62.2567 |
| `problem_4.frontier.predictions.mid.24m.P90` | 64.517 |
| `problem_4.frontier.predictions.mid.24m.t_target` | 2027 |
| `problem_4.frontier.predictions.high.12m.P10` | 61.0252 |
| `problem_4.frontier.predictions.high.12m.P50` | 62.5195 |
| `problem_4.frontier.predictions.high.12m.P90` | 67.3894 |
| `problem_4.frontier.predictions.high.12m.t_target` | 2026 |
| `problem_4.frontier.predictions.high.24m.P10` | 80.0923 |
| `problem_4.frontier.predictions.high.24m.P50` | 81.9358 |
| `problem_4.frontier.predictions.high.24m.P90` | 87.0685 |
| `problem_4.frontier.predictions.high.24m.t_target` | 2027 |
| `problem_4.frontier.compute_cagr_from_C4` | 5.09583 |
| `problem_4.frontier.compute_cagr_note` | `C4(Epoch AI)历史训练算力中位数 2019-2025 增速 5.10×/年，情景 low/mid/h...` |
| `problem_4.frontier.frontier_no_regress_24m_ge_12m` | True |
| `problem_4.frontier.n_open` | 2813 |
| `problem_4.frontier.extrapolation_note` | `12/24月为情景模拟，含外推不确定性，非数据直接支持` |
| `problem_4.c8_aggregation.n_subdirs` | 1863 |
| `problem_4.c8_aggregation.n_parsed` | 1860 |
| `problem_4.c8_aggregation.n_corrupt_skipped` | 7 |
| `problem_4.c8_aggregation.n_six_dim_complete` | 1854 |
| `problem_4.c8_aggregation.task_difficulty_mean.IFEval` | 40.1569 |
| `problem_4.c8_aggregation.task_difficulty_mean.BBH` | 47.4859 |
| `problem_4.c8_aggregation.task_difficulty_mean.MATH` | 11.3835 |
| `problem_4.c8_aggregation.task_difficulty_mean.GPQA` | 29.8035 |
| `problem_4.c8_aggregation.task_difficulty_mean.MUSR` | 39.9605 |
| `problem_4.c8_aggregation.task_difficulty_mean.MMLU-PRO` | 31.9917 |
| `problem_4.c8_aggregation.task_correlation_dims[0]` | `IFEval` |
| `problem_4.c8_aggregation.task_correlation_dims[1]` | `BBH` |
| `problem_4.c8_aggregation.task_correlation_dims[2]` | `MATH` |
| `problem_4.c8_aggregation.task_correlation_dims[5]` | `MMLU-PRO` |
| `problem_4.c8_aggregation.task_correlation_dims[...]` | `<2 项省略>` |
| `problem_4.c8_aggregation.task_correlation_matrix[0][0]` | 1 |
| `problem_4.c8_aggregation.task_correlation_matrix[0][1]` | 0.645455 |
| `problem_4.c8_aggregation.task_correlation_matrix[0][2]` | 0.490114 |
| `problem_4.c8_aggregation.task_correlation_matrix[0][5]` | 0.654209 |
| `problem_4.c8_aggregation.task_correlation_matrix[0][...]` | `<2 项省略>` |
| `problem_4.c8_aggregation.task_correlation_matrix[1][0]` | 0.645455 |
| `problem_4.c8_aggregation.task_correlation_matrix[1][1]` | 1 |
| `problem_4.c8_aggregation.task_correlation_matrix[1][2]` | 0.632933 |
| `problem_4.c8_aggregation.task_correlation_matrix[1][5]` | 0.968998 |
| `problem_4.c8_aggregation.task_correlation_matrix[1][...]` | `<2 项省略>` |
| `problem_4.c8_aggregation.task_correlation_matrix[2][0]` | 0.490114 |
| `problem_4.c8_aggregation.task_correlation_matrix[2][1]` | 0.632933 |
| `problem_4.c8_aggregation.task_correlation_matrix[2][2]` | 1 |
| `problem_4.c8_aggregation.task_correlation_matrix[2][5]` | 0.680869 |
| `problem_4.c8_aggregation.task_correlation_matrix[2][...]` | `<2 项省略>` |
| `problem_4.c8_aggregation.task_correlation_matrix[5][0]` | 0.654209 |
| `problem_4.c8_aggregation.task_correlation_matrix[5][1]` | 0.968998 |
| `problem_4.c8_aggregation.task_correlation_matrix[5][2]` | 0.680869 |
| `problem_4.c8_aggregation.task_correlation_matrix[5][5]` | 1 |
| `problem_4.c8_aggregation.task_correlation_matrix[5][...]` | `<2 项省略>` |
| `problem_4.c8_aggregation.task_correlation_matrix[...]` | `<2 项省略>` |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.IFEval` | 77.0795 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.BBH` | 72.9734 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.MATH` | 40.3323 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.GPQA` | 40.2685 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.MUSR` | 60.0529 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.MMLU-PRO` | 73.0303 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.IFEval` | 77.8189 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.BBH` | 72.8346 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.MATH` | 39.2749 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.GPQA` | 39.5973 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.MUSR` | 58.7302 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.MMLU-PRO` | 71.8501 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.IFEval` | 76.525 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.BBH` | 72.5916 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.MATH` | 40.71 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.GPQA` | 40.2685 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.MUSR` | 57.5397 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.MMLU-PRO` | 70.0216 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.IFEval` | 81.8854 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.BBH` | 72.6089 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.MATH` | 58.9124 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.GPQA` | 35.906 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.MUSR` | 41.9312 |
| `problem_4.c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.MMLU-PRO` | 56.1752 |
| `problem_4.c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.IFEval` | 72.4584 |
| `problem_4.c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.BBH` | 72.9214 |
| `problem_4.c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.MATH` | 48.3384 |
| `problem_4.c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.GPQA` | 41.6107 |
| `problem_4.c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.MUSR` | 46.6931 |
| `problem_4.c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.MMLU-PRO` | 61.4528 |
| `problem_4.c8_aggregation.coverage_note` | `覆盖 1860 可解析目录(>=1800要求), 六维完整 1854` |
| `cross_problem_ledger_observed.Q1_domain_Q_median` | 0.0789294 |
| `cross_problem_ledger_observed.Q2_scaling_params.E` | 1.68984 |
| `cross_problem_ledger_observed.Q2_scaling_params.A` | 0.353969 |
| `cross_problem_ledger_observed.Q2_scaling_params.alpha` | 0.339985 |
| `cross_problem_ledger_observed.Q2_scaling_params.B` | 1.24027 |
| `cross_problem_ledger_observed.Q2_scaling_params.beta` | 0.279892 |
| `cross_problem_ledger_observed.Q2_theta_assumed` | 0.5 |
| `cross_problem_ledger_observed.Q3_L_optimal_per_budget.1e+19` | 3.09838 |
| `cross_problem_ledger_observed.Q3_L_optimal_per_budget.1e+22` | 2.15107 |
| `cross_problem_ledger_observed.Q3_L_optimal_per_budget.1e+24` | 1.91393 |
| `cross_problem_ledger_observed.Q3_Q0_from_Q1` | 0.0789294 |

### `problem_1_results.json`（150 条）

| 数据路径 | 数值 |
|---|---|
| `_meta.seed` | 42 |
| `_meta.python` | `3.11.9` |
| `_meta.numpy` | `2.4.6` |
| `_meta.scipy` | `1.17.1` |
| `_meta.pandas` | `2.3.3` |
| `method` | `entropy_weight + simplex_regression` |
| `weights.fluency_en` | 0.0146247 |
| `weights.qurater` | 0.008666 |
| `weights.ad_en` | 0.0143205 |
| `weights.fineweb_edu` | 0.0117222 |
| `weights.modernbert_cleanliness` | 0.007218 |
| `weights.modernbert_reasoning` | 0.0128978 |
| `weights.modernbert_professionalism` | 0.00931 |
| `weights.modernbert_readability` | 0.007585 |
| `weights.dsir_books` | 2.023e-05 |
| `weights.rps_lines_ending_with_terminal_punctution_mark` | 0.0366953 |
| `weights.rps_doc_num_sentences` | 0.398791 |
| `weights.rps_doc_word_count` | 0.41917 |
| `weights.rps_doc_frac_no_alph_words` | 0.006465 |
| `weights.rps_doc_frac_chars_top_2gram` | 0.0001278 |
| `weights.rps_lines_uppercase_letter_fraction` | 0.00556 |
| `weights.rps_doc_frac_unique_words` | 0.011894 |
| `weights.rps_lines_numerical_chars_fraction` | 0.0004423 |
| `weights.dsir_math` | 1.024e-05 |
| `weights.rps_doc_mean_word_length` | 0.030113 |
| `weights.dsir_wiki` | 1.487e-05 |
| `weights.rps_doc_frac_chars_top_3gram` | 5.728e-05 |
| `weights.rps_doc_unigram_entropy` | 0.004297 |
| `weights_critic.fluency_en` | 0.0742438 |
| `weights_critic.qurater` | 0.0644344 |
| `weights_critic.ad_en` | 0.0687191 |
| `weights_critic.fineweb_edu` | 0.0622748 |
| `weights_critic.modernbert_cleanliness` | 0.0565963 |
| `weights_critic.modernbert_reasoning` | 0.0625461 |
| `weights_critic.modernbert_professionalism` | 0.0573819 |
| `weights_critic.modernbert_readability` | 0.0534822 |
| `weights_critic.dsir_books` | 0.005516 |
| `weights_critic.rps_lines_ending_with_terminal_punctution_mark` | 0.135597 |
| `weights_critic.rps_doc_num_sentences` | 0.008175 |
| `weights_critic.rps_doc_word_count` | 0.005542 |
| `weights_critic.rps_doc_frac_no_alph_words` | 0.0643314 |
| `weights_critic.rps_doc_frac_chars_top_2gram` | 0.0142926 |
| `weights_critic.rps_lines_uppercase_letter_fraction` | 0.0762167 |
| `weights_critic.rps_doc_frac_unique_words` | 0.0785672 |
| `weights_critic.rps_lines_numerical_chars_fraction` | 0.0251127 |
| `weights_critic.dsir_math` | 0.003856 |
| `weights_critic.rps_doc_mean_word_length` | 0.0156062 |
| `weights_critic.dsir_wiki` | 0.004702 |
| `weights_critic.rps_doc_frac_chars_top_3gram` | 0.009496 |
| `weights_critic.rps_doc_unigram_entropy` | 0.0533119 |
| `weights_sum` | 1 |
| `Q_stats.min` | 0.0384654 |
| `Q_stats.max` | 0.795602 |
| `Q_stats.mean` | 0.0798766 |
| `Q_stats.median` | 0.0777438 |
| `method_agreement.kendall_tau_entropy_critic` | 0.826574 |
| `method_agreement.kendall_tau_entropy_pca` | 0.801909 |
| `domain_Q_A1.arxiv.Q` | 0.0789294 |
| `domain_Q_A1.arxiv.n` | 1419 |
| `domain_Q_A1.book.Q` | 0.227218 |
| `domain_Q_A1.book.n` | 171 |
| `domain_Q_A1.c4.Q` | 0.097659 |
| `domain_Q_A1.c4.n` | 10000 |
| `domain_Q_A1.commoncrawl.Q` | 0.079846 |
| `domain_Q_A1.commoncrawl.n` | 9640 |
| `domain_Q_A1.github.Q` | 0.0709034 |
| `domain_Q_A1.github.n` | 10000 |
| `domain_Q_A1.stackexchange.Q` | 0.072122 |
| `domain_Q_A1.stackexchange.n` | 10000 |
| `domain_Q_A1.wikipedia.Q` | 0.0764665 |
| `domain_Q_A1.wikipedia.n` | 10000 |
| `domain_Q_median` | 0.0789294 |
| `domain_Q_extended.A2_arxiv.Q_ext` | 0.0933028 |
| `domain_Q_extended.A2_arxiv.n` | 17523 |
| `domain_Q_extended.A2_arxiv.Q_A1_same_domain` | 0.0789294 |
| `domain_Q_extended.A3_github.Q_ext` | 0.0729202 |
| `domain_Q_extended.A3_github.n` | 203752 |
| `domain_Q_extended.A3_github.Q_A1_same_domain` | 0.0709034 |
| `conflict.positive_indicator` | `fineweb_edu` |
| `conflict.negative_indicator` | `ad_en` |
| `conflict.spearman_pos_vs_adcontent` | 0.139308 |
| `conflict.conflict_rate` | 0.0496194 |
| `conflict.n_conflict` | 2542 |
| `conflict.resolution` | `降权 delta=0.5 + 稳健聚合` |
| `conflict.kendall_tau_before_after` | 0.932026 |
| `mixture_model.method` | `log-domain simplex-constrained linear regression + LightGBM` |
| `mixture_model.n_train` | 512 |
| `mixture_model.n_target_domains` | 13 |
| `mixture_model.train_r2.arxiv` | 0.586098 |
| `mixture_model.train_r2.freelaw` | 0.667298 |
| `mixture_model.train_r2.pubmed_central` | 0.60095 |
| `mixture_model.train_r2.wikipedia_en` | 0.733503 |
| `mixture_model.train_r2.dm_mathematics` | 0.495573 |
| `mixture_model.train_r2.github` | 0.639096 |
| `mixture_model.train_r2.stackexchange` | 0.623649 |
| `mixture_model.train_r2.gutenberg_pg_19` | 0.723126 |
| `mixture_model.train_r2.pile_cc` | 0.786129 |
| `mixture_model.train_r2.ubuntu_irc` | 0.614876 |
| `mixture_model.train_r2.hackernews` | 0.692505 |
| `mixture_model.train_r2.pubmed_abstracts` | 0.785364 |
| `mixture_model.train_r2.uspto_backgrounds` | 0.771354 |
| `mixture_model.holdout_r2.1m` | 0.663909 |
| `mixture_model.holdout_r2.60m` | -5.38686 |
| `mixture_model.holdout_r2.1B` | -265.29 |
| `mixture_model.holdout_rank_spearman.1m` | 0.843892 |
| `mixture_model.holdout_rank_spearman.60m` | 0.842117 |
| `mixture_model.holdout_rank_spearman.1B` | 0.736415 |
| `mixture_model.holdout_note` | `绝对R2跨尺度退化是真实现象(Loss量级随模型规模移动)；RegMix声称的跨尺度可迁移性由配比排序Spea...` |
| `mixture_model.lightgbm_r2` | 0.976743 |
| `mixture_model.mixture_domain_importance.arxiv` | 0.381073 |
| `mixture_model.mixture_domain_importance.freelaw` | 0.365129 |
| `mixture_model.mixture_domain_importance.nih_exporter` | 0.214986 |
| `mixture_model.mixture_domain_importance.pubmed_central` | 0.345101 |
| `mixture_model.mixture_domain_importance.wikipedia_en` | 0.315878 |
| `mixture_model.mixture_domain_importance.dm_mathematics` | 0.58719 |
| `mixture_model.mixture_domain_importance.github` | 0.350591 |
| `mixture_model.mixture_domain_importance.philpapers` | 0.49983 |
| `mixture_model.mixture_domain_importance.stackexchange` | 0.285686 |
| `mixture_model.mixture_domain_importance.enron_emails` | 1.06851 |
| `mixture_model.mixture_domain_importance.gutenberg_pg_19` | 0.289332 |
| `mixture_model.mixture_domain_importance.pile_cc` | 0.293384 |
| `mixture_model.mixture_domain_importance.ubuntu_irc` | 0.313162 |
| `mixture_model.mixture_domain_importance.europarl` | 0.21502 |
| `mixture_model.mixture_domain_importance.hackernews` | 0.181038 |
| `mixture_model.mixture_domain_importance.pubmed_abstracts` | 0.30723 |
| `mixture_model.mixture_domain_importance.uspto_backgrounds` | 0.347687 |
| `mixture_model.simplex_ok` | True |
| `domain_mapping.n_total` | 17 |
| `domain_mapping.by_type.direct` | 3 |
| `domain_mapping.by_type.inferred` | 11 |
| `domain_mapping.by_type.near_direct` | 3 |
| `domain_mapping.inferred_domains[0]` | `dm_mathematics` |
| `domain_mapping.inferred_domains[1]` | `freelaw` |
| `domain_mapping.inferred_domains[2]` | `nih_exporter` |
| `domain_mapping.inferred_domains[10]` | `uspto_backgrounds` |
| `domain_mapping.inferred_domains[...]` | `<7 项省略>` |
| `domain_mapping.inferred_handling` | `保留配比为解释变量(间接影响其它域Loss)，按体裁相似性赋推断Q并标注低可信度，不无声丢弃` |
| `domain_mapping.mapping_pairs[0].mixture` | `arxiv` |
| `domain_mapping.mapping_pairs[0].quality` | `arxiv` |
| `domain_mapping.mapping_pairs[0].type` | `direct` |
| `domain_mapping.mapping_pairs[1].mixture` | `github` |
| `domain_mapping.mapping_pairs[1].quality` | `github` |
| `domain_mapping.mapping_pairs[1].type` | `direct` |
| `domain_mapping.mapping_pairs[2].mixture` | `stackexchange` |
| `domain_mapping.mapping_pairs[2].quality` | `stackexchange` |
| `domain_mapping.mapping_pairs[2].type` | `direct` |
| `domain_mapping.mapping_pairs[16].mixture` | `uspto_backgrounds` |
| `domain_mapping.mapping_pairs[16].quality` | `(none)` |
| `domain_mapping.mapping_pairs[16].type` | `inferred` |
| `domain_mapping.mapping_pairs[...]` | `<13 项省略>` |

### `problem_2_results.json`（143 条）

| 数据路径 | 数值 |
|---|---|
| `_meta.seed` | 42 |
| `_meta.python` | `3.11.9` |
| `_meta.numpy` | `2.4.6` |
| `_meta.scipy` | `1.17.1` |
| `_meta.pandas` | `2.3.3` |
| `method` | `log-domain Huber-NLS classic + generalized (Q^theta D)` |
| `classic.params.E` | 1.68984 |
| `classic.params.A` | 0.353969 |
| `classic.params.alpha` | 0.339985 |
| `classic.params.B` | 1.24027 |
| `classic.params.beta` | 0.279892 |
| `classic.r2` | 1 |
| `classic.n_fit` | 1176 |
| `classic.residual_mean` | -4.996e-08 |
| `classic.residual_std` | 0.0001466 |
| `classic.generalization.B2_cerebras.n` | 1029 |
| `classic.generalization.B2_cerebras.rmse` | 1.24308 |
| `classic.generalization.B2_cerebras.r2` | -5.07275 |
| `classic.generalization.B4_baseline.n` | 57 |
| `classic.generalization.B4_baseline.rmse` | 0.292665 |
| `classic.generalization.B4_baseline.r2` | 0.60451 |
| `classic.generalization.B5_published.n` | 44 |
| `classic.generalization.B5_published.rmse` | 0.197598 |
| `classic.generalization.B5_published.r2` | 0.73055 |
| `classic.n_trajectory_files` | 8 |
| `classic.N_range[0]` | 0.070542 |
| `classic.N_range[1]` | 11.9658 |
| `classic.D_range[0]` | 0.134 |
| `classic.D_range[1]` | 299.893 |
| `classic.L_range[0]` | 2.0933 |
| `classic.L_range[1]` | 4.7388 |
| `classic.fit_scatter.actual[0]` | 4.7388 |
| `classic.fit_scatter.actual[1]` | 4.3541 |
| `classic.fit_scatter.actual[2]` | 4.0384 |
| `classic.fit_scatter.actual[1175]` | 2.0933 |
| `classic.fit_scatter.actual[...]` | `<1172 项省略>` |
| `classic.fit_scatter.predicted[0]` | 4.73864 |
| `classic.fit_scatter.predicted[1]` | 4.35475 |
| `classic.fit_scatter.predicted[2]` | 4.03779 |
| `classic.fit_scatter.predicted[1175]` | 2.09338 |
| `classic.fit_scatter.predicted[...]` | `<1172 项省略>` |
| `generalized.params.E` | 0.216297 |
| `generalized.params.A` | 0.531097 |
| `generalized.params.alpha` | 0.309038 |
| `generalized.params.B` | 2.95341 |
| `generalized.params.beta` | 0.122774 |
| `generalized.params.theta` | -10 |
| `generalized.theta_empirical_B6B8` | -10 |
| `generalized.theta_assumed_downstream` | 0.5 |
| `generalized.theta_role` | `assumed (下游Q3/Q4). B6-B8经验theta仅描述setpoint数据, 见corr_Q_L说明` |
| `generalized.r2` | 0.338887 |
| `generalized.n_fit` | 2012 |
| `generalized.n_holdout` | 502 |
| `generalized.corr_Q_L` | 0.445888 |
| `generalized.corr_Q_L_note` | `B6-B8 Q_score为实验setpoint(重标定损失), 与Q_synth部署质量口径不同(报告表⑩明确区分)` |
| `generalized.rmse_holdout_generalized` | 0.687874 |
| `generalized.rmse_holdout_classic_baseline` | 0.97128 |
| `generalized.generalized_better_or_equal` | True |
| `generalized.aic.generalized` | -1843 |
| `generalized.aic.classic` | -31.632 |
| `generalized.bic.generalized` | -1808 |
| `generalized.bic.classic` | -2.48386 |
| `generalized.Q1_degeneracy_rel_err` | 0 |
| `generalized.Q1_degeneracy_pass` | True |
| `generalized.surface_data.N_grid[0]` | 0.1 |
| `generalized.surface_data.N_grid[1]` | 0.126896 |
| `generalized.surface_data.N_grid[2]` | 0.161026 |
| `generalized.surface_data.N_grid[29]` | 100 |
| `generalized.surface_data.N_grid[...]` | `<26 项省略>` |
| `generalized.surface_data.Q_grid[0]` | 0.1 |
| `generalized.surface_data.Q_grid[1]` | 0.131034 |
| `generalized.surface_data.Q_grid[2]` | 0.162069 |
| `generalized.surface_data.Q_grid[29]` | 1 |
| `generalized.surface_data.Q_grid[...]` | `<26 项省略>` |
| `generalized.surface_data.L_surface[0][0]` | 3.23095 |
| `generalized.surface_data.L_surface[0][1]` | 3.15417 |
| `generalized.surface_data.L_surface[0][2]` | 3.08283 |
| `generalized.surface_data.L_surface[0][29]` | 2.27696 |
| `generalized.surface_data.L_surface[0][...]` | `<26 项省略>` |
| `generalized.surface_data.L_surface[1][0]` | 3.19915 |
| `generalized.surface_data.L_surface[1][1]` | 3.12236 |
| `generalized.surface_data.L_surface[1][2]` | 3.05103 |
| `generalized.surface_data.L_surface[1][29]` | 2.24515 |
| `generalized.surface_data.L_surface[1][...]` | `<26 项省略>` |
| `generalized.surface_data.L_surface[2][0]` | 3.1745 |
| `generalized.surface_data.L_surface[2][1]` | 3.09772 |
| `generalized.surface_data.L_surface[2][2]` | 3.02638 |
| `generalized.surface_data.L_surface[2][29]` | 2.22051 |
| `generalized.surface_data.L_surface[2][...]` | `<26 项省略>` |
| `generalized.surface_data.L_surface[29][0]` | 2.9762 |
| `generalized.surface_data.L_surface[29][1]` | 2.89941 |
| `generalized.surface_data.L_surface[29][2]` | 2.82808 |
| `generalized.surface_data.L_surface[29][29]` | 2.0222 |
| `generalized.surface_data.L_surface[29][...]` | `<26 项省略>` |
| `generalized.surface_data.L_surface[...]` | `<26 项省略>` |
| `generalized.surface_data.D_fixed` | 100 |
| `generalized.surface_data.Q1_line[0]` | 2.9762 |
| `generalized.surface_data.Q1_line[1]` | 2.89941 |
| `generalized.surface_data.Q1_line[2]` | 2.82808 |
| `generalized.surface_data.Q1_line[29]` | 2.0222 |
| `generalized.surface_data.Q1_line[...]` | `<26 项省略>` |
| `elasticity.reference_point.N0` | 1 |
| `elasticity.reference_point.D0` | 100 |
| `elasticity.reference_point.Q0` | 0.5 |
| `elasticity.reference_point.L0` | 2.49827 |
| `elasticity.eps_N` | -0.0656971 |
| `elasticity.eps_D` | -0.0860441 |
| `elasticity.eps_Q` | -0.043022 |
| `elasticity.eps_Q_equals_theta_eps_D` | -0.043022 |
| `elasticity.substitution_dN_dQ` | -1.30971 |
| `elasticity.delta_N_for_deltaQ_0.1` | -0.130971 |
| `elasticity.iso_loss_contour.N_grid[0]` | 0.1 |
| `elasticity.iso_loss_contour.N_grid[1]` | 0.353846 |
| `elasticity.iso_loss_contour.N_grid[2]` | 0.607692 |
| `elasticity.iso_loss_contour.N_grid[39]` | 10 |
| `elasticity.iso_loss_contour.N_grid[...]` | `<36 项省略>` |
| `elasticity.iso_loss_contour.Q_grid[0]` | 0.1 |
| `elasticity.iso_loss_contour.Q_grid[1]` | 0.123077 |
| `elasticity.iso_loss_contour.Q_grid[2]` | 0.146154 |
| `elasticity.iso_loss_contour.Q_grid[39]` | 1 |
| `elasticity.iso_loss_contour.Q_grid[...]` | `<36 项省略>` |
| `elasticity.iso_loss_contour.L_surface[0][0]` | 3.23095 |
| `elasticity.iso_loss_contour.L_surface[0][1]` | 2.88115 |
| `elasticity.iso_loss_contour.L_surface[0][2]` | 2.76846 |
| `elasticity.iso_loss_contour.L_surface[0][39]` | 2.40969 |
| `elasticity.iso_loss_contour.L_surface[0][...]` | `<36 项省略>` |
| `elasticity.iso_loss_contour.L_surface[1][0]` | 3.20647 |
| `elasticity.iso_loss_contour.L_surface[1][1]` | 2.85667 |
| `elasticity.iso_loss_contour.L_surface[1][2]` | 2.74399 |
| `elasticity.iso_loss_contour.L_surface[1][39]` | 2.38521 |
| `elasticity.iso_loss_contour.L_surface[1][...]` | `<36 项省略>` |
| `elasticity.iso_loss_contour.L_surface[2][0]` | 3.18645 |
| `elasticity.iso_loss_contour.L_surface[2][1]` | 2.83665 |
| `elasticity.iso_loss_contour.L_surface[2][2]` | 2.72396 |
| `elasticity.iso_loss_contour.L_surface[2][39]` | 2.36518 |
| `elasticity.iso_loss_contour.L_surface[2][...]` | `<36 项省略>` |
| `elasticity.iso_loss_contour.L_surface[39][0]` | 2.9762 |
| `elasticity.iso_loss_contour.L_surface[39][1]` | 2.6264 |
| `elasticity.iso_loss_contour.L_surface[39][2]` | 2.51371 |
| `elasticity.iso_loss_contour.L_surface[39][39]` | 2.15493 |
| `elasticity.iso_loss_contour.L_surface[39][...]` | `<36 项省略>` |
| `elasticity.iso_loss_contour.L_surface[...]` | `<36 项省略>` |
| `elasticity.iso_loss_contour.D_fixed` | 100 |

### `problem_3_results.json`（273 条）

| 数据路径 | 数值 |
|---|---|
| `_meta.seed` | 42 |
| `_meta.python` | `3.11.9` |
| `_meta.numpy` | `2.4.6` |
| `_meta.scipy` | `1.17.1` |
| `_meta.pandas` | `2.3.3` |
| `method` | `SLSQP multi-start + KKT + share-derivative transition` |
| `scaling_params.E` | 1.68984 |
| `scaling_params.A` | 0.353969 |
| `scaling_params.alpha` | 0.339985 |
| `scaling_params.B` | 1.24027 |
| `scaling_params.beta` | 0.279892 |
| `scaling_params.theta` | 0.5 |
| `Q0` | 0.0789294 |
| `eta` | 0.0002 |
| `Lctx_crit` | 3e+04 |
| `optimal_allocation.Lctx_main` | 2048 |
| `optimal_allocation.budgets[0]` | 1e+19 |
| `optimal_allocation.budgets[1]` | 1e+22 |
| `optimal_allocation.budgets[2]` | 1e+24 |
| `optimal_allocation.by_gtype.exp.1e+19.N` | 0.231058 |
| `optimal_allocation.by_gtype.exp.1e+19.D` | 5.78365 |
| `optimal_allocation.by_gtype.exp.1e+19.Q` | 0.54561 |
| `optimal_allocation.by_gtype.exp.1e+19.L` | 3.09838 |
| `optimal_allocation.by_gtype.exp.1e+19.C_tot` | 1e+19 |
| `optimal_allocation.by_gtype.exp.1e+19.C_train` | 8.018e+18 |
| `optimal_allocation.by_gtype.exp.1e+19.C_Q` | 1.434e+18 |
| `optimal_allocation.by_gtype.exp.1e+19.C_attn` | 5.474e+17 |
| `optimal_allocation.by_gtype.exp.1e+19.util` | 1 |
| `optimal_allocation.by_gtype.exp.1e+19.shares.s_train` | 0.801816 |
| `optimal_allocation.by_gtype.exp.1e+19.shares.s_Q` | 0.143447 |
| `optimal_allocation.by_gtype.exp.1e+19.shares.s_attn` | 0.0547373 |
| `optimal_allocation.by_gtype.exp.1e+19.Q_above_Q0` | True |
| `optimal_allocation.by_gtype.exp.1e+22.N` | 5.51552 |
| `optimal_allocation.by_gtype.exp.1e+22.D` | 258.632 |
| `optimal_allocation.by_gtype.exp.1e+22.Q` | 0.96796 |
| `optimal_allocation.by_gtype.exp.1e+22.L` | 2.15107 |
| `optimal_allocation.by_gtype.exp.1e+22.C_tot` | 1e+22 |
| `optimal_allocation.by_gtype.exp.1e+22.C_train` | 8.559e+21 |
| `optimal_allocation.by_gtype.exp.1e+22.C_Q` | 8.568e+20 |
| `optimal_allocation.by_gtype.exp.1e+22.C_attn` | 5.843e+20 |
| `optimal_allocation.by_gtype.exp.1e+22.util` | 1 |
| `optimal_allocation.by_gtype.exp.1e+22.shares.s_train` | 0.855895 |
| `optimal_allocation.by_gtype.exp.1e+22.shares.s_Q` | 0.0856764 |
| `optimal_allocation.by_gtype.exp.1e+22.shares.s_attn` | 0.0584291 |
| `optimal_allocation.by_gtype.exp.1e+22.Q_above_Q0` | True |
| `optimal_allocation.by_gtype.exp.1e+24.N` | 40.7704 |
| `optimal_allocation.by_gtype.exp.1e+24.D` | 3769 |
| `optimal_allocation.by_gtype.exp.1e+24.Q` | 1 |
| `optimal_allocation.by_gtype.exp.1e+24.L` | 1.91393 |
| `optimal_allocation.by_gtype.exp.1e+24.C_tot` | 1e+24 |
| `optimal_allocation.by_gtype.exp.1e+24.C_train` | 9.219e+23 |
| `optimal_allocation.by_gtype.exp.1e+24.C_Q` | 1.514e+22 |
| `optimal_allocation.by_gtype.exp.1e+24.C_attn` | 6.294e+22 |
| `optimal_allocation.by_gtype.exp.1e+24.util` | 1 |
| `optimal_allocation.by_gtype.exp.1e+24.shares.s_train` | 0.92192 |
| `optimal_allocation.by_gtype.exp.1e+24.shares.s_Q` | 0.0151437 |
| `optimal_allocation.by_gtype.exp.1e+24.shares.s_attn` | 0.0629364 |
| `optimal_allocation.by_gtype.exp.1e+24.Q_above_Q0` | True |
| `optimal_allocation.by_gtype.pow.1e+19.N` | 0.2153 |
| `optimal_allocation.by_gtype.pow.1e+19.D` | 6.34152 |
| `optimal_allocation.by_gtype.pow.1e+19.Q` | 0.445591 |
| `optimal_allocation.by_gtype.pow.1e+19.L` | 3.11466 |
| `optimal_allocation.by_gtype.pow.1e+19.C_tot` | 1e+19 |
| `optimal_allocation.by_gtype.pow.1e+19.C_train` | 8.192e+18 |
| `optimal_allocation.by_gtype.pow.1e+19.C_Q` | 1.249e+18 |
| `optimal_allocation.by_gtype.pow.1e+19.C_attn` | 5.592e+17 |
| `optimal_allocation.by_gtype.pow.1e+19.util` | 1 |
| `optimal_allocation.by_gtype.pow.1e+19.shares.s_train` | 0.819199 |
| `optimal_allocation.by_gtype.pow.1e+19.shares.s_Q` | 0.124877 |
| `optimal_allocation.by_gtype.pow.1e+19.shares.s_attn` | 0.055924 |
| `optimal_allocation.by_gtype.pow.1e+19.Q_above_Q0` | True |
| `optimal_allocation.by_gtype.pow.1e+22.N` | 5.79793 |
| `optimal_allocation.by_gtype.pow.1e+22.D` | 237.179 |
| `optimal_allocation.by_gtype.pow.1e+22.Q` | 1 |
| `optimal_allocation.by_gtype.pow.1e+22.L` | 2.15296 |
| `optimal_allocation.by_gtype.pow.1e+22.C_tot` | 1e+22 |
| `optimal_allocation.by_gtype.pow.1e+22.C_train` | 8.251e+21 |
| `optimal_allocation.by_gtype.pow.1e+22.C_Q` | 1.186e+21 |
| `optimal_allocation.by_gtype.pow.1e+22.C_attn` | 5.633e+20 |
| `optimal_allocation.by_gtype.pow.1e+22.util` | 1 |
| `optimal_allocation.by_gtype.pow.1e+22.shares.s_train` | 0.825089 |
| `optimal_allocation.by_gtype.pow.1e+22.shares.s_Q` | 0.118585 |
| `optimal_allocation.by_gtype.pow.1e+22.shares.s_attn` | 0.0563261 |
| `optimal_allocation.by_gtype.pow.1e+22.Q_above_Q0` | True |
| `optimal_allocation.by_gtype.pow.1e+24.N` | 40.9419 |
| `optimal_allocation.by_gtype.pow.1e+24.D` | 3739 |
| `optimal_allocation.by_gtype.pow.1e+24.Q` | 1 |
| `optimal_allocation.by_gtype.pow.1e+24.L` | 1.91406 |
| `optimal_allocation.by_gtype.pow.1e+24.C_tot` | 1e+24 |
| `optimal_allocation.by_gtype.pow.1e+24.C_train` | 9.186e+23 |
| `optimal_allocation.by_gtype.pow.1e+24.C_Q` | 1.87e+22 |
| `optimal_allocation.by_gtype.pow.1e+24.C_attn` | 6.271e+22 |
| `optimal_allocation.by_gtype.pow.1e+24.util` | 1 |
| `optimal_allocation.by_gtype.pow.1e+24.shares.s_train` | 0.918594 |
| `optimal_allocation.by_gtype.pow.1e+24.shares.s_Q` | 0.0186964 |
| `optimal_allocation.by_gtype.pow.1e+24.shares.s_attn` | 0.0627094 |
| `optimal_allocation.by_gtype.pow.1e+24.Q_above_Q0` | True |
| `optimal_allocation.by_gtype.log.1e+19.N` | 0.520637 |
| `optimal_allocation.by_gtype.log.1e+19.D` | 1.43488 |
| `optimal_allocation.by_gtype.log.1e+19.Q` | 1 |
| `optimal_allocation.by_gtype.log.1e+19.L` | 3.25281 |
| `optimal_allocation.by_gtype.log.1e+19.C_tot` | 1e+19 |
| `optimal_allocation.by_gtype.log.1e+19.C_train` | 4.482e+18 |
| `optimal_allocation.by_gtype.log.1e+19.C_Q` | 5.212e+18 |
| `optimal_allocation.by_gtype.log.1e+19.C_attn` | 3.06e+17 |
| `optimal_allocation.by_gtype.log.1e+19.util` | 1 |
| `optimal_allocation.by_gtype.log.1e+19.shares.s_train` | 0.448231 |
| `optimal_allocation.by_gtype.log.1e+19.shares.s_Q` | 0.52117 |
| `optimal_allocation.by_gtype.log.1e+19.shares.s_attn` | 0.0305992 |
| `optimal_allocation.by_gtype.log.1e+19.Q_above_Q0` | True |
| `optimal_allocation.by_gtype.log.1e+22.N` | 5.60039 |
| `optimal_allocation.by_gtype.log.1e+22.D` | 252.983 |
| `optimal_allocation.by_gtype.log.1e+22.Q` | 1 |
| `optimal_allocation.by_gtype.log.1e+22.L` | 2.15047 |
| `optimal_allocation.by_gtype.log.1e+22.C_tot` | 1e+22 |
| `optimal_allocation.by_gtype.log.1e+22.C_train` | 8.501e+21 |
| `optimal_allocation.by_gtype.log.1e+22.C_Q` | 9.189e+20 |
| `optimal_allocation.by_gtype.log.1e+22.C_attn` | 5.803e+20 |
| `optimal_allocation.by_gtype.log.1e+22.util` | 1 |
| `optimal_allocation.by_gtype.log.1e+22.shares.s_train` | 0.850081 |
| `optimal_allocation.by_gtype.log.1e+22.shares.s_Q` | 0.0918871 |
| `optimal_allocation.by_gtype.log.1e+22.shares.s_attn` | 0.0580322 |
| `optimal_allocation.by_gtype.log.1e+22.Q_above_Q0` | True |
| `optimal_allocation.by_gtype.log.1e+24.N` | 40.7026 |
| `optimal_allocation.by_gtype.log.1e+24.D` | 3780 |
| `optimal_allocation.by_gtype.log.1e+24.Q` | 1 |
| `optimal_allocation.by_gtype.log.1e+24.L` | 1.91388 |
| `optimal_allocation.by_gtype.log.1e+24.C_tot` | 1e+24 |
| `optimal_allocation.by_gtype.log.1e+24.C_train` | 9.232e+23 |
| `optimal_allocation.by_gtype.log.1e+24.C_Q` | 1.373e+22 |
| `optimal_allocation.by_gtype.log.1e+24.C_attn` | 6.303e+22 |
| `optimal_allocation.by_gtype.log.1e+24.util` | 1 |
| `optimal_allocation.by_gtype.log.1e+24.shares.s_train` | 0.923242 |
| `optimal_allocation.by_gtype.log.1e+24.shares.s_Q` | 0.0137311 |
| `optimal_allocation.by_gtype.log.1e+24.shares.s_attn` | 0.0630267 |
| `optimal_allocation.by_gtype.log.1e+24.Q_above_Q0` | True |
| `optimal_allocation.baseline_chinchilla.1e+19.N` | 1.24906 |
| `optimal_allocation.baseline_chinchilla.1e+19.D` | 1.24906 |
| `optimal_allocation.baseline_chinchilla.1e+19.Q` | 0.0789294 |
| `optimal_allocation.baseline_chinchilla.1e+19.L` | 3.68072 |
| `optimal_allocation.baseline_chinchilla.1e+19.C_tot` | 1e+19 |
| `optimal_allocation.baseline_chinchilla.1e+19.C_train` | 9.361e+18 |
| `optimal_allocation.baseline_chinchilla.1e+19.C_Q` | 0 |
| `optimal_allocation.baseline_chinchilla.1e+19.C_attn` | 6.39e+17 |
| `optimal_allocation.baseline_chinchilla.1e+19.util` | 1 |
| `optimal_allocation.baseline_chinchilla.1e+19.note` | `Chinchilla等分基线(N=D,Q=Q0无质量投入)，作对照` |
| `optimal_allocation.baseline_chinchilla.1e+22.N` | 39.4989 |
| `optimal_allocation.baseline_chinchilla.1e+22.D` | 39.4989 |
| `optimal_allocation.baseline_chinchilla.1e+22.Q` | 0.0789294 |
| `optimal_allocation.baseline_chinchilla.1e+22.L` | 2.42364 |
| `optimal_allocation.baseline_chinchilla.1e+22.C_tot` | 1e+22 |
| `optimal_allocation.baseline_chinchilla.1e+22.C_train` | 9.361e+21 |
| `optimal_allocation.baseline_chinchilla.1e+22.C_Q` | 0 |
| `optimal_allocation.baseline_chinchilla.1e+22.C_attn` | 6.39e+20 |
| `optimal_allocation.baseline_chinchilla.1e+22.util` | 1 |
| `optimal_allocation.baseline_chinchilla.1e+22.note` | `Chinchilla等分基线(N=D,Q=Q0无质量投入)，作对照` |
| `optimal_allocation.baseline_chinchilla.1e+24.N` | 394.989 |
| `optimal_allocation.baseline_chinchilla.1e+24.D` | 394.989 |
| `optimal_allocation.baseline_chinchilla.1e+24.Q` | 0.0789294 |
| `optimal_allocation.baseline_chinchilla.1e+24.L` | 2.06816 |
| `optimal_allocation.baseline_chinchilla.1e+24.C_tot` | 1e+24 |
| `optimal_allocation.baseline_chinchilla.1e+24.C_train` | 9.361e+23 |
| `optimal_allocation.baseline_chinchilla.1e+24.C_Q` | 0 |
| `optimal_allocation.baseline_chinchilla.1e+24.C_attn` | 6.39e+22 |
| `optimal_allocation.baseline_chinchilla.1e+24.util` | 1 |
| `optimal_allocation.baseline_chinchilla.1e+24.note` | `Chinchilla等分基线(N=D,Q=Q0无质量投入)，作对照` |
| `optimal_allocation.budget_monotonic_L` | True |
| `structural_transition.gtype` | `exp` |
| `structural_transition.logC_grid[0]` | 18 |
| `structural_transition.logC_grid[1]` | 18.2 |
| `structural_transition.logC_grid[2]` | 18.4 |
| `structural_transition.logC_grid[35]` | 25 |
| `structural_transition.logC_grid[...]` | `<32 项省略>` |
| `structural_transition.C_grid[0]` | 1e+18 |
| `structural_transition.C_grid[1]` | 1.585e+18 |
| `structural_transition.C_grid[2]` | 2.512e+18 |
| `structural_transition.C_grid[35]` | 1e+25 |
| `structural_transition.C_grid[...]` | `<32 项省略>` |
| `structural_transition.s_train[0]` | 0.774129 |
| `structural_transition.s_train[1]` | 0.779972 |
| `structural_transition.s_train[2]` | 0.785692 |
| `structural_transition.s_train[35]` | 0.930977 |
| `structural_transition.s_train[...]` | `<32 项省略>` |
| `structural_transition.s_Q[0]` | 0.173024 |
| `structural_transition.s_Q[1]` | 0.166782 |
| `structural_transition.s_Q[2]` | 0.160671 |
| `structural_transition.s_Q[35]` | 0.005469 |
| `structural_transition.s_Q[...]` | `<32 项省略>` |
| `structural_transition.s_attn[0]` | 0.0528472 |
| `structural_transition.s_attn[1]` | 0.0532461 |
| `structural_transition.s_attn[2]` | 0.0536366 |
| `structural_transition.s_attn[35]` | 0.0635547 |
| `structural_transition.s_attn[...]` | `<32 项省略>` |
| `structural_transition.d_sQ_dlogC[0]` | -0.0312104 |
| `structural_transition.d_sQ_dlogC[1]` | -0.0308821 |
| `structural_transition.d_sQ_dlogC[2]` | -0.030132 |
| `structural_transition.d_sQ_dlogC[35]` | -0.006229 |
| `structural_transition.d_sQ_dlogC[...]` | `<32 项省略>` |
| `structural_transition.d_strain_dlogC[0]` | 0.029216 |
| `structural_transition.d_strain_dlogC[1]` | 0.0289086 |
| `structural_transition.d_strain_dlogC[2]` | 0.0282064 |
| `structural_transition.d_strain_dlogC[35]` | 0.005831 |
| `structural_transition.d_strain_dlogC[...]` | `<32 项省略>` |
| `structural_transition.Q_traj[0]` | 0.419047 |
| `structural_transition.Q_traj[1]` | 0.443636 |
| `structural_transition.Q_traj[2]` | 0.468596 |
| `structural_transition.Q_traj[35]` | 1 |
| `structural_transition.Q_traj[...]` | `<32 项省略>` |
| `structural_transition.N_traj[0]` | 0.080176 |
| `structural_transition.N_traj[1]` | 0.0991168 |
| `structural_transition.N_traj[2]` | 0.122499 |
| `structural_transition.N_traj[35]` | 114.01 |
| `structural_transition.N_traj[...]` | `<32 项省略>` |
| `structural_transition.D_traj[0]` | 1.60923 |
| `structural_transition.D_traj[1]` | 2.07865 |
| `structural_transition.D_traj[2]` | 2.68515 |
| `structural_transition.D_traj[35]` | 1.361e+04 |
| `structural_transition.D_traj[...]` | `<32 项省略>` |
| `structural_transition.L_traj[0]` | 3.75079 |
| `structural_transition.L_traj[1]` | 3.59887 |
| `structural_transition.L_traj[2]` | 3.45856 |
| `structural_transition.L_traj[35]` | 1.84697 |
| `structural_transition.L_traj[...]` | `<32 项省略>` |
| `structural_transition.transition_logC` | 22.4 |
| `structural_transition.transition_C` | 2.512e+22 |
| `structural_transition.CQ_first_activation_C` | 1e+18 |
| `structural_transition.definition` | `结构转移=份额对logC导数峰值处(式18) + KKT活跃集切换(Q内点↔边界, C_Q铰链激活)` |
| `lctx_sensitivity.budget_C` | 1e+22 |
| `lctx_sensitivity.gtype` | `exp` |
| `lctx_sensitivity.Lctx_set[0]` | 2048 |
| `lctx_sensitivity.Lctx_set[1]` | 4096 |
| `lctx_sensitivity.Lctx_set[2]` | 8192 |
| `lctx_sensitivity.Lctx_set[3]` | 32768 |
| `lctx_sensitivity.Lctx_set[4]` | 131072 |
| `lctx_sensitivity.Lctx_crit` | 3e+04 |
| `lctx_sensitivity.Lctx_crit_analytic` | 3e+04 |
| `lctx_sensitivity.Lctx_crit_check` | True |
| `lctx_sensitivity.panels.2048.N` | 5.51552 |
| `lctx_sensitivity.panels.2048.D` | 258.632 |
| `lctx_sensitivity.panels.2048.Q` | 0.96796 |
| `lctx_sensitivity.panels.2048.L` | 2.15107 |
| `lctx_sensitivity.panels.2048.shares.s_train` | 0.855895 |
| `lctx_sensitivity.panels.2048.shares.s_Q` | 0.0856764 |
| `lctx_sensitivity.panels.2048.shares.s_attn` | 0.0584291 |
| `lctx_sensitivity.panels.4096.N` | 5.36661 |
| `lctx_sensitivity.panels.4096.D` | 249.956 |
| `lctx_sensitivity.panels.4096.Q` | 0.972814 |
| `lctx_sensitivity.panels.4096.L` | 2.15526 |
| `lctx_sensitivity.panels.4096.shares.s_train` | 0.80485 |
| `lctx_sensitivity.panels.4096.shares.s_Q` | 0.0852608 |
| `lctx_sensitivity.panels.4096.shares.s_attn` | 0.109889 |
| `lctx_sensitivity.panels.8192.N` | 5.10425 |
| `lctx_sensitivity.panels.8192.D` | 234.812 |
| `lctx_sensitivity.panels.8192.Q` | 0.981713 |
| `lctx_sensitivity.panels.8192.L` | 2.16304 |
| `lctx_sensitivity.panels.8192.shares.s_train` | 0.719123 |
| `lctx_sensitivity.panels.8192.shares.s_Q` | 0.0845086 |
| `lctx_sensitivity.panels.8192.shares.s_attn` | 0.196368 |
| `lctx_sensitivity.panels.32768.N` | 4.03879 |
| `lctx_sensitivity.panels.32768.D` | 182.75 |
| `lctx_sensitivity.panels.32768.Q` | 1 |
| `lctx_sensitivity.panels.32768.L` | 2.19875 |
| `lctx_sensitivity.panels.32768.shares.s_train` | 0.442853 |
| `lctx_sensitivity.panels.32768.shares.s_Q` | 0.0734332 |
| `lctx_sensitivity.panels.32768.shares.s_attn` | 0.483714 |
| `lctx_sensitivity.panels.131072.N` | 2.55291 |
| `lctx_sensitivity.panels.131072.D` | 115.93 |
| `lctx_sensitivity.panels.131072.Q` | 1 |
| `lctx_sensitivity.panels.131072.L` | 2.27514 |
| `lctx_sensitivity.panels.131072.shares.s_train` | 0.177576 |
| `lctx_sensitivity.panels.131072.shares.s_Q` | 0.0465834 |
| `lctx_sensitivity.panels.131072.shares.s_attn` | 0.775841 |
| `lctx_sensitivity.note` | `L_ctx_crit=6/eta=30000 tokens；落在8192与32768之间，即>=32768的长...` |

### `problem_4_results.json`（196 条）

| 数据路径 | 数值 |
|---|---|
| `_meta.seed` | 42 |
| `_meta.python` | `3.11.9` |
| `_meta.numpy` | `2.4.6` |
| `_meta.scipy` | `1.17.1` |
| `_meta.pandas` | `2.3.3` |
| `method` | `growth-accounting decomp + stratified sigmoid bridge + ...` |
| `cap_metric` | `mean6` |
| `open_criterion` | `hub_license` |
| `capability_definition` | `六维Benchmark均分(IFEval,BBH,MATH,GPQA,MUSR,MMLU-PRO)` |
| `contribution_decomp.model` | `Cap ~ lnN + year (OLS)` |
| `contribution_decomp.r2` | 0.461658 |
| `contribution_decomp.b_lnN` | 6.26623 |
| `contribution_decomp.c_year` | 12.1419 |
| `contribution_decomp.window.t0` | 2025 |
| `contribution_decomp.window.t1` | 2025 |
| `contribution_decomp.delta_Cap_observed` | 6.74324 |
| `contribution_decomp.delta_lnN_window` | -0.273096 |
| `contribution_decomp.delta_f_scale` | -1.71128 |
| `contribution_decomp.delta_h_nonscale` | 8.54611 |
| `contribution_decomp.scale_pct` | -25.0377 |
| `contribution_decomp.nonscale_pct` | 125.038 |
| `contribution_decomp.sum_check` | 100 |
| `contribution_decomp.interpretation` | `2024-2025 窗口内，同规模下年度能力提升 c_year=12.1 点/年(非规模算法进步)；而平均参数...` |
| `contribution_decomp.open_field_source` | `Epoch_AI_Open_Weights (C4)` |
| `contribution_decomp.n_open_labeled` | 443 |
| `contribution_decomp.yearly_evolution[0].year` | 2024 |
| `contribution_decomp.yearly_evolution[0].scale_pct` | -0.390055 |
| `contribution_decomp.yearly_evolution[0].nonscale_pct` | 100.39 |
| `contribution_decomp.yearly_evolution[1].year` | 2025 |
| `contribution_decomp.yearly_evolution[1].scale_pct` | -38.4328 |
| `contribution_decomp.yearly_evolution[1].nonscale_pct` | 138.433 |
| `contribution_decomp.n` | 4561 |
| `bridge.method` | `stratified monotone sigmoid (式23)` |
| `bridge.strata_by_comparability.High (same model, same validation set).n` | 7 |
| `bridge.strata_by_comparability.High (same model, same validation set).params.Smax` | 0.908066 |
| `bridge.strata_by_comparability.High (same model, same validation set).params.a` | 18.6189 |
| `bridge.strata_by_comparability.High (same model, same validation set).params.L0` | 2.13359 |
| `bridge.strata_by_comparability.High (same model, same validation set).params.c` | 5.44904 |
| `bridge.strata_by_comparability.High (same model, same validation set).r2` | 0.402881 |
| `bridge.strata_by_comparability.High (same model, same validation set).residual_std` | 0.281131 |
| `bridge.strata_by_comparability.High (same model, same validation set).monotone_decreasing` | True |
| `bridge.strata_by_comparability.High (same model, same validation set).L_range[0]` | 2.0933 |
| `bridge.strata_by_comparability.High (same model, same validation set).L_range[1]` | 2.5978 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[0]` | 2.5978 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[1]` | 2.4209 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[2]` | 2.2904 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[6]` | 2.0933 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.loss[...]` | `<3 项省略>` |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[0]` | 5.73039 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[1]` | 5.22707 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[2]` | 5.07027 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[6]` | 6.05984 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.cap[...]` | `<3 项省略>` |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[0]` | 5.4492 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[1]` | 5.45333 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[2]` | 5.49552 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[6]` | 6.0658 |
| `bridge.strata_by_comparability.High (same model, same validation set).scatter.pred[...]` | `<3 项省略>` |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).n` | 68 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).params.Smax` | 15.4138 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).params.a` | 50 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).params.L0` | 2.21636 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).params.c` | 9.91298 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).r2` | 0.356452 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).residual_std` | 9.1149 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).monotone_decreasing` | True |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).L_range[0]` | 1.65 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).L_range[1]` | 2.84 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[0]` | 1.76 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[1]` | 1.75 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[2]` | 1.76 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[67]` | 2.25 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.loss[...]` | `<64 项省略>` |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[0]` | 13.6269 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[1]` | 8.80636 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[2]` | 14.4209 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[67]` | 5.11657 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.cap[...]` | `<64 项省略>` |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[0]` | 25.3268 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[1]` | 25.3268 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[2]` | 25.3268 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[67]` | 12.33 |
| `bridge.strata_by_comparability.Medium (different validation set, approximate).scatter.pred[...]` | `<64 项省略>` |
| `bridge.map_error_note` | `残差带宽反映映射误差，前沿结论须计入桥接不确定性` |
| `frontier.method` | `P90 envelope + linear trend + bootstrap quantile band` |
| `frontier.scenarios.low` | 0 |
| `frontier.scenarios.mid` | 0.5 |
| `frontier.scenarios.high` | 1 |
| `frontier.scenario_note` | `算力增速档=相对历史前沿斜率的比例(0停滞/0.5放缓/1维持)，显式情景假设` |
| `frontier.historical_frontier.t[0]` | 2024 |
| `frontier.historical_frontier.t[1]` | 2025 |
| `frontier.historical_frontier.t[2]` | 2025 |
| `frontier.historical_frontier.t[9]` | 2025 |
| `frontier.historical_frontier.t[...]` | `<6 项省略>` |
| `frontier.historical_frontier.cap[0]` | 25.9748 |
| `frontier.historical_frontier.cap[1]` | 28.2266 |
| `frontier.historical_frontier.cap[2]` | 36.2308 |
| `frontier.historical_frontier.cap[9]` | 41.7462 |
| `frontier.historical_frontier.cap[...]` | `<6 项省略>` |
| `frontier.slope` | 19.6791 |
| `frontier.predictions.low.12m.P10` | 40.7341 |
| `frontier.predictions.low.12m.P50` | 42.8404 |
| `frontier.predictions.low.12m.P90` | 47.7103 |
| `frontier.predictions.low.12m.t_target` | 2026 |
| `frontier.predictions.low.24m.P10` | 40.7341 |
| `frontier.predictions.low.24m.P50` | 42.8404 |
| `frontier.predictions.low.24m.P90` | 44.8379 |
| `frontier.predictions.low.24m.t_target` | 2027 |
| `frontier.predictions.mid.12m.P10` | 51.1856 |
| `frontier.predictions.mid.12m.P50` | 52.6799 |
| `frontier.predictions.mid.12m.P90` | 54.9647 |
| `frontier.predictions.mid.12m.t_target` | 2026 |
| `frontier.predictions.mid.24m.P10` | 60.4132 |
| `frontier.predictions.mid.24m.P50` | 62.2567 |
| `frontier.predictions.mid.24m.P90` | 64.517 |
| `frontier.predictions.mid.24m.t_target` | 2027 |
| `frontier.predictions.high.12m.P10` | 61.0252 |
| `frontier.predictions.high.12m.P50` | 62.5195 |
| `frontier.predictions.high.12m.P90` | 67.3894 |
| `frontier.predictions.high.12m.t_target` | 2026 |
| `frontier.predictions.high.24m.P10` | 80.0923 |
| `frontier.predictions.high.24m.P50` | 81.9358 |
| `frontier.predictions.high.24m.P90` | 87.0685 |
| `frontier.predictions.high.24m.t_target` | 2027 |
| `frontier.compute_cagr_from_C4` | 5.09583 |
| `frontier.compute_cagr_note` | `C4(Epoch AI)历史训练算力中位数 2019-2025 增速 5.10×/年，情景 low/mid/h...` |
| `frontier.frontier_no_regress_24m_ge_12m` | True |
| `frontier.n_open` | 2813 |
| `frontier.extrapolation_note` | `12/24月为情景模拟，含外推不确定性，非数据直接支持` |
| `c8_aggregation.n_subdirs` | 1863 |
| `c8_aggregation.n_parsed` | 1860 |
| `c8_aggregation.n_corrupt_skipped` | 7 |
| `c8_aggregation.n_six_dim_complete` | 1854 |
| `c8_aggregation.task_difficulty_mean.IFEval` | 40.1569 |
| `c8_aggregation.task_difficulty_mean.BBH` | 47.4859 |
| `c8_aggregation.task_difficulty_mean.MATH` | 11.3835 |
| `c8_aggregation.task_difficulty_mean.GPQA` | 29.8035 |
| `c8_aggregation.task_difficulty_mean.MUSR` | 39.9605 |
| `c8_aggregation.task_difficulty_mean.MMLU-PRO` | 31.9917 |
| `c8_aggregation.task_correlation_dims[0]` | `IFEval` |
| `c8_aggregation.task_correlation_dims[1]` | `BBH` |
| `c8_aggregation.task_correlation_dims[2]` | `MATH` |
| `c8_aggregation.task_correlation_dims[5]` | `MMLU-PRO` |
| `c8_aggregation.task_correlation_dims[...]` | `<2 项省略>` |
| `c8_aggregation.task_correlation_matrix[0][0]` | 1 |
| `c8_aggregation.task_correlation_matrix[0][1]` | 0.645455 |
| `c8_aggregation.task_correlation_matrix[0][2]` | 0.490114 |
| `c8_aggregation.task_correlation_matrix[0][5]` | 0.654209 |
| `c8_aggregation.task_correlation_matrix[0][...]` | `<2 项省略>` |
| `c8_aggregation.task_correlation_matrix[1][0]` | 0.645455 |
| `c8_aggregation.task_correlation_matrix[1][1]` | 1 |
| `c8_aggregation.task_correlation_matrix[1][2]` | 0.632933 |
| `c8_aggregation.task_correlation_matrix[1][5]` | 0.968998 |
| `c8_aggregation.task_correlation_matrix[1][...]` | `<2 项省略>` |
| `c8_aggregation.task_correlation_matrix[2][0]` | 0.490114 |
| `c8_aggregation.task_correlation_matrix[2][1]` | 0.632933 |
| `c8_aggregation.task_correlation_matrix[2][2]` | 1 |
| `c8_aggregation.task_correlation_matrix[2][5]` | 0.680869 |
| `c8_aggregation.task_correlation_matrix[2][...]` | `<2 项省略>` |
| `c8_aggregation.task_correlation_matrix[5][0]` | 0.654209 |
| `c8_aggregation.task_correlation_matrix[5][1]` | 0.968998 |
| `c8_aggregation.task_correlation_matrix[5][2]` | 0.680869 |
| `c8_aggregation.task_correlation_matrix[5][5]` | 1 |
| `c8_aggregation.task_correlation_matrix[5][...]` | `<2 项省略>` |
| `c8_aggregation.task_correlation_matrix[...]` | `<2 项省略>` |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.IFEval` | 77.0795 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.BBH` | 72.9734 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.MATH` | 40.3323 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.GPQA` | 40.2685 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.MUSR` | 60.0529 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.2-instruct-78b.MMLU-PRO` | 73.0303 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.IFEval` | 77.8189 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.BBH` | 72.8346 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.MATH` | 39.2749 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.GPQA` | 39.5973 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.MUSR` | 58.7302 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-3.1-instruct-78b.MMLU-PRO` | 71.8501 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.IFEval` | 76.525 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.BBH` | 72.5916 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.MATH` | 40.71 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.GPQA` | 40.2685 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.MUSR` | 57.5397 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.4-rys-78b.MMLU-PRO` | 70.0216 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.IFEval` | 81.8854 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.BBH` | 72.6089 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.MATH` | 58.9124 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.GPQA` | 35.906 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.MUSR` | 41.9312 |
| `c8_aggregation.top5_frontier_radar.MaziyarPanahi_calme-2.2-qwen2.5-72b.MMLU-PRO` | 56.1752 |
| `c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.IFEval` | 72.4584 |
| `c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.BBH` | 72.9214 |
| `c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.MATH` | 48.3384 |
| `c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.GPQA` | 41.6107 |
| `c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.MUSR` | 46.6931 |
| `c8_aggregation.top5_frontier_radar.newsbang_Homer-v1.0-Qwen2.5-72B.MMLU-PRO` | 61.4528 |
| `c8_aggregation.coverage_note` | `覆盖 1860 可解析目录(>=1800要求), 六维完整 1854` |
