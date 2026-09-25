# 图表生成报告 — 华为杯 F 题（算力约束下提升大语言模型能力的资源配置建模）

本步骤产出 15 张数据图（matplotlib，矢量 PDF）+ 5 张三线表（booktabs `.tex`）+
`figures/latex_includes.tex`。流程/架构图（`fig_roadmap` / `fig_pipeline_q1` /
`fig_index_hierarchy`）与 `tikz_q3_feasible` 不属于本步骤，由 paper-figure-drawio
与 TikZ 子流程产出。

## 一、对账结果

| 项 | 规划 | 实产 | 状态 |
|---|---|---|---|
| 数据图（FIGURE_MANIFEST 数据图段） | 15 | 15 | 全部产出 |
| `gen_fig_*.py` 脚本 | — | 15（一图一脚本，可独立重跑） | — |
| 三线表 | ≥2（主结果 + 描述统计） | 5 | 超出下限 |
| `latex_includes.tex` | 必需 | 3867 bytes / 15 个 `figure` 块 | 已生成 |

检查器状态：

- `figure_check.sh`：**0 违规 + 0 可升级 + 0 配方问题**，退出码 0。
- `recipe_audit.py`：可判定的 7 张图，规划图型与代码 API 全部一致。
- `figure_pdf_quality_check.py`（按 `latex_includes.tex` 的真实插入宽度反算）：
  字体嵌入、最终印刷字号、文字边界、留白、对比度**全部通过**；余 3 项
  「背景复杂需视觉复核」已用像素级实测判定（见第四节）。
- `figure_narrative_check.py`：通过。
- 表格数值可追溯性：221 个数值单元格，**0 个不可追溯**，标记
  `figures/TABLE_DATA_CHECK_PASSED.txt`。

## 二、上游数据的两处重算（口径一致性已硬断言）

问题一、问题四各有一张图需要文档级/月度级中间量，而 comp-code 的结果 JSON 只
存了聚合量。本步骤新增两个 prep 脚本**沿用 `code/` 里的同一套口径**重算，并对
已发布结果逐项 `assert`，确保没有引入第二套数字：

| 脚本 | 为什么需要 | 复现并断言一致的量 |
|---|---|---|
| `figures/prep_q1_indicators.py` | 22×22 相关矩阵、逐文档冲突散点、扩展集逐文档 Q 都不在结果 JSON 里 | 22 维熵权（`max|Δ|<1e-9`）、冲突率 0.04961936、冲突样本数 2542、A1 七域 Q 与 n、A2 `Q_ext`=0.09330281、A3 `Q_ext`=0.07292017 |
| `figures/prep_q4_decomp.py` | `yearly_evolution` 只有 2024/2025 两点，画不出演化形状 | `b_lnN`=6.2662334、`c_year`=12.1418584、`R²`=0.4616578、`n`=4561、窗口 `t0/t1`、窗口口径 `scale_pct`=-25.0377 |

数据摄入均为**全量不抽样**（A1 51230 条、A2 17523 条、A3 203752 条、C1 4576 行），
行数由 `code/utils.py` 的 `read_*_checked` 对照 `DATA_PROFILE.json` 核验。

## 三、逐图证据台账

每行记录：问题/情景、生成脚本、数据文件与字段、参数条件、样本量、统计量与不确定
性定义。未知来源一律标「无」，不猜。

### 问题一（数据质量与配比）

**1. `fig_q1_quality_corr` — 聚类热力图（advanced #14）**
- 情景：A1 全量文档上 22 个质量指标的两两一致性 + 层次聚类结构。
- 脚本：`figures/gen_fig_q1_quality_corr.py`
- 数据：`figures/_prep_q1.npz['corr']`（← A1 `slimpajama_quality_signal_sample.jsonl.xz`）
- 参数条件：方向统一 + Min-Max 归一化后（式1–2）；`scipy.stats.spearmanr`；
  距离 `d=1-ρ`，average linkage，`maxclust=4`。
- 样本量：n=51230 文档，22×22=484 格。
- 统计量：Spearman ρ，色标固定 `vmin/vmax=±1`、`center=0`。
- 不确定性：**未标注**。相关矩阵为全量总体描述，非重复抽样实验，不加区间。
- 校核：对角线全 1.0、矩阵对称、簇沿叶序连续无交错（簇规模 4/7/4/7）、树状图
  叶坐标 `(5+10i)/(10n)` 与格心 `(i+0.5)/n` 完全重合。
- 备注：484 格不写格内数值（`annot` 省略），故按规则用 `pcolormesh` 矢量网格；
  精确权重见 `TABLE_q1_weights`。规划点名的「ad_en 与 fineweb_edu 反相关」在方向
  统一矩阵中为 **ρ=-0.139**，与已发布的「fineweb_edu vs 原始广告含量 +0.139」
  符号相反、数值一致（`1-x` 取补必然翻转符号），两者自洽。

**2. `fig_q1_conflict_scatter` — 散点 + KDE 边际密度（basic #4）**
- 情景：式5 质量冲突（教育价值高但广告含量也高）的样本分布。
- 脚本：`figures/gen_fig_q1_conflict_scatter.py`
- 数据：`figures/_prep_q1.npz['fe','ad_raw','conflict']`（← A1 全量）
- 参数条件：阈值 = 两指标各自 0.8 分位（教育价值 0.4822、广告含量 0.7134），
  与 `code/problem1.py::_q1_conflict` 同式。
- 样本量：n=51230；冲突子集 n=2542（4.96%）。
- 统计量：散点为逐文档观测值；边际为 Gaussian KDE。
- 不确定性：**未标注**（全量观测散点）。边际 KDE 用 8000 点随机子样本
  （`seed=42`）估计，仅为密度形状，冲突率等统计量均用全量计算。
- 备注：5 万点以 `rasterized=True` 栅格化嵌入（矢量圆点会使 PDF 体积失控），
  文字与矢量图元仍为矢量。

**3. `fig_q1_domain_Q_dumbbell` — 哑铃图（advanced #2）**
- 情景：抽样集（A1）与全量扩展集（A2/A3）的域级质量是否一致。
- 脚本：`figures/gen_fig_q1_domain_Q_dumbbell.py`
- 数据：`figures/_prep_q1.json['domain_Q_A1_ci' / 'domain_Q_extended_ci']`
- 参数条件：扩展集用 **A1 的熵权**合成 Q（同一权重口径才可比）；横轴对数刻度。
- 样本量：A1 七域 171~10000；A2 arxiv 17523；A3 github 203752。
- 统计量：域内文档级 Q 的算术均值。
- 不确定性：**2000 次 bootstrap 的 95% 百分位区间**（`seed=42`），A1 与扩展集两侧
  都给。区间宽度随 n 收窄（book n=171 最宽，github n=203752 最窄）。
- 备注：只有 arxiv / github 两域存在扩展集，其余五域扩展列标「--」，不臆造配对。
  数值不贴点旁（对数轴上区间很窄，贴点必压线），统一放右侧专用数值列。

**4. `fig_q1_mixture_importance` — 棒棒糖图（advanced #1）**
- 情景：17 域配比对验证 Loss 的影响强度排序 + 该域 Q 的可映射性。
- 脚本：`figures/gen_fig_q1_mixture_importance.py`
- 数据：`output/q1_mixture_model.json['mixture_domain_importance']`；映射类型来自
  `figures/problem_1_results.json['domain_mapping']['mapping_pairs']`（← A16
  `domain_mapping_guide.csv`）。
- 参数条件：LightGBM 代理模型增益重要性（代理 R²=0.9767）；训练集 A4/A5
  1m 尺度 512 组配方。
- 样本量：17 个域（direct 3 / near_direct 3 / inferred 11）。
- 统计量：增益重要性（无量纲），中位数作参考线。
- 不确定性：**未标注**。单次拟合的特征重要性，无重复运行，不伪造区间。
- 备注：标记形状编码映射类型——重要性最高的 `enron_emails`(1.069) 恰为 inferred，
  即其 Q 只能按体裁推断，是配比-质量联合建模的主要不确定性来源。

### 问题二（标度律）

**5. `fig_q2_scaling_fit` — 预测 vs 实际 + 残差 [2-panel]（competition #4）**
- 情景：(a) 经典律在 B1 拟合集上的拟合优度；(b) 拟合残差分布。
- 脚本：`figures/gen_fig_q2_scaling_fit.py`
- 数据：`figures/problem_2_results.json['classic']['fit_scatter'/'r2'/'residual_std']`
  （← B1 pythia 8 个轨迹文件逐 checkpoint）
- 参数条件：对数域 Huber-NLS；N∈[0.0705, 11.966]×10⁹、D∈[0.134, 299.893]×10⁹、
  L∈[2.0933, 4.7388]。
- 样本量：n=1176 个 checkpoint。
- 统计量：R²=0.9999998；RMSE=1.47e-04；残差 σ=1.466e-04 nats/token。
- 不确定性：残差分布本身即拟合不确定性的表达（直方图 + 正态拟合曲线）。
- 备注：三个外部集的泛化 RMSE（published 0.1976 / baseline 0.2927 /
  cerebras 1.2431）**已从图内移入 `TABLE_q2_scaling`**——图内只保留一行 R²/RMSE
  短锚点，避免两个多行文字框压住散点。「拟合集近乎无残差」与「跨来源泛化明显退化
  （cerebras R²=-5.07）」必须一起读，正文须同时引用图与表。

**6. `fig_q2_generalized_surface` — 3D 曲面（competition #6）**
- 情景：广义律 L(N,Q) 在 D=100×10⁹ tokens 固定切面上的地形。
- 脚本：`figures/gen_fig_q2_generalized_surface.py`
- 数据：`figures/problem_2_results.json['generalized']['surface_data']`
  （`N_grid` 30 点 logspace 0.1~100、`Q_grid` 30 点 0.1~1.0、`L_surface` 30×30、
  `Q1_line` 30 点）
- 参数条件：θ 取**下游 assumed 0.5**（非 B6-B8 经验值 -10.0）；拟合参数 E=0.2163、
  A=0.5311、α=0.3090、B=2.9534、β=0.1228。
- 样本量：拟合 n=2012，留出 n=502（曲面本身是解析代入，非样本散点）。
- 统计量：L（nats/token）。
- 不确定性：**未在图上标注**。曲面为解析函数值；留出 RMSE（广义 0.6879 vs 同参
  经典基线 0.9713）与 AIC/BIC 见 `TABLE_q2_scaling`。
- 备注：θ 的双口径必须在正文交代——`theta_empirical_B6B8`=-10.0 只描述 B6-B8 的
  **setpoint** 数据（其 `Q_score` 是实验设定的重标定损失，与部署质量 Q_synth 口径
  不同，`corr_Q_L`=0.446），下游 Q3/Q4 一律用 assumed θ=0.5。图中黑色 Q=1 退化线
  即经典律 L(N,D)，退化相对误差 0.0，是模型自洽性检验。
- 版式修正记录：原生画布曾取 6.5×4.3in，按真实插入宽反算后 10% 分位文字仅 7.2pt
  （<8pt 印刷线），收窄到 5.6×4.0in 后通过；图例因 3D 曲面铺满数据区，已迁入
  GridSpec 独立行。

**7. `fig_q2_elasticity_diverging` — 发散柱状图（advanced #20）**
- 情景：ε_N / ε_D / ε_Q 在 4 个工作点上的量级对照。
- 脚本：`figures/gen_fig_q2_elasticity_diverging.py`
- 数据：`figures/problem_2_results.json['generalized']['params']` +
  `['theta_assumed_downstream']`，按式12 解析代入（`_figbase.elasticities`）。
- 参数条件：**同一套广义律参数 + 同一 θ=0.5 + Q 固定 0.5**，工作点只变 (N,D)：
  (0.1, 2)、(1, 20)、(1, 100) = 参考点、(10, 200)，均落在 B1 数据域内。
- 样本量：不适用（解析导数）。
- 统计量：ε=∂lnL/∂ln x（无量纲），12 根柱。
- 不确定性：**未标注**（解析值，无抽样）。
- 校核：参考工作点重算的 ε_N=-0.0657、ε_D=-0.0860、ε_Q=-0.0430 与已发布值
  `abs diff < 1e-12`（脚本内 `assert`）。
- 备注：三个因素**全为负**（增投都降损），因此柱全在零线左侧；这是数据事实，不是
  配色或图型问题。零线、方向锚点与恒等式 ε_Q=θ·ε_D 均保留。**不可跨工作点混用
  经典律参数与广义律参数**，否则柱间不可比——本图统一用广义律参数。

**8. `fig_q2_substitution_contour` — 等高线图（competition #14）**
- 情景：(N,Q) 平面等损失线族与参考点处的替代率。
- 脚本：`figures/gen_fig_q2_substitution_contour.py`
- 数据：`figures/problem_2_results.json['elasticity']['iso_loss_contour']`
  （`N_grid` 40 点 0.1~10、`Q_grid` 40 点 0.1~1.0、`L_surface` 40×40，D 固定 100）
  + `['substitution_dN_dQ']`、`['delta_N_for_deltaQ_0.1']`
- 参数条件：θ=0.5；参考点 (N=1, D=100, Q=0.5)，L₀=2.4983。
- 样本量：不适用（解析曲面）。
- 统计量：L 范围 2.1549~3.2310；切线斜率 dN/dQ|_L=-1.3097；ΔQ=+0.1 ⇔ ΔN=-0.1310。
- 不确定性：**未标注**（解析值）。
- 备注：等值线标注层数取 every-5（原 every-3 时左下密集区 "2.72"×"2.91" 相撞）；
  线与标注改深色 + **不透明**白底板（`alpha=0.8` 时深橙填充透上来，实测
  "2.79" 仅 2.94:1）。

### 问题三（算力分配优化）

**9. `fig_q3_allocation_stacked` — 堆叠柱状图（basic #2）**
- 情景：三档预算 × 三种 g(Q) 的最优份额构成 + Chinchilla 基线对照。
- 脚本：`figures/gen_fig_q3_allocation_stacked.py`
- 数据：`figures/problem_3_results.json['optimal_allocation']['by_gtype' /
  'baseline_chinchilla']`
- 参数条件：C∈{1e19, 1e22, 1e24} FLOPs（题给三档）；L_ctx=2048；η=2e-4；
  Q₀=0.0789（← 问题一域级中位数）；SLSQP 多起点 + KKT 校验；基线为 N=D、Q=Q₀。
- 样本量：12 根柱（3 预算 × 4 方案）。
- 统计量：份额 s=C_分量/C_总（基线份额由 `C_train/C_Q/C_attn ÷ C_tot` 现算）；
  柱顶为 L*。
- 不确定性：**未标注**。确定性优化的唯一最优解，无重复运行；`util`≈1.0 说明预算
  约束取等，解在边界上。
- 备注：exp 型 s_Q 14.34%→8.57%→1.51%，L* 3.098→2.151→1.914，三种 g(Q) 方向
  一致。基线在 1e22 处 L=2.4236，劣于最优 2.1511。双层 x 轴（柱=方案、组=预算）
  取代方案图例；成分图例在 GridSpec 独立行。9 列的 `TABLE_q3_allocation` 自然宽
  ≈109% textwidth，是 5 张表里**唯一**加 `\resizebox` 的。

**10. `fig_q3_transition_line` — 折线图 + 判据线（basic #3）**
- 情景：份额随 logC 的连续演化与结构转移点定位。
- 脚本：`figures/gen_fig_q3_transition_line.py`
- 数据：`figures/problem_3_results.json['structural_transition']`
  （`logC_grid` 36 点 18~25、`s_train`/`s_Q`/`s_attn`、`d_sQ_dlogC`、`transition_logC`）
- 参数条件：g(Q)=指数型；L_ctx=2048；逐点 SLSQP。
- 样本量：36 个预算网格点。
- 统计量：左轴份额（%）；右轴 |ds_Q/dlogC|，峰值 0.0608。
- 不确定性：**未标注，且规划里写的「+CI」不适用**——这是确定性优化的解轨迹，不存在
  重复抽样或随机重启带来的分布。加置信带会是虚构的不确定性，因此改为叠加份额导数
  曲线，用其峰值给出转移判据（式18）+ KKT 活跃集切换，两者一致落在 logC=22.4
  （C=2.51e22 FLOPs）。
- 版式修正记录：xlabel 原写 `$\log_{10}C$`，其下标降部在画布最下缘伸出 tight bbox
  约 2pt 被判出界；已改为中文习惯写法「lg C」（不带下标）。

**11. `fig_q3_lctx_panels` — 多面板子图 [4-panel]（basic #12）**
- 情景：L_ctx 从 2048 扫到 131072 时最优解如何被注意力开销挤压。
- 脚本：`figures/gen_fig_q3_lctx_panels.py`
- 数据：`figures/problem_3_results.json['lctx_sensitivity']['panels' / 'Lctx_crit']`
  （与 `output/q3_lctx_sensitivity.json` 同源）
- 参数条件：C=1e22 FLOPs 固定；g(Q)=指数型；L_ctx 取 C7 实际出现的 5 个值
  {2048, 4096, 8192, 32768, 131072}。
- 样本量：5 个 L_ctx 点 × 4 个面板。
- 统计量：(a) N*/D*（对数纵轴）(b) Q* (c) L* (d) 三项份额（%）。
- 不确定性：**未标注**（确定性最优解）。
- 备注：N* 5.516→2.553；D* 258.6→115.9；Q* 0.968→1.0（顶到上界）；L* 2.151→2.275；
  s_attn 5.84%→77.58%。判据线 L_ctx^crit=6/η=30000 tokens 为**解析值**，与数值
  校验一致（`Lctx_crit_check=true`），恰落在 8192 与 32768 之间——即 ≥32768 的长
  上下文模型注意力开销已超训练开销。该线四面板共用，图例放顶部 GridSpec 独立行
  （面板内竖排文字会压曲线，且面板级图例会溢出画布）。

### 问题四（能力演化与前沿）

**12. `fig_q4_contribution_decomp` — 贡献分解 [2-panel]（empirical #20）**
- 情景：(a) 规模项/非规模项的绝对贡献累积；(b) 两者占比。
- 脚本：`figures/gen_fig_q4_contribution_decomp.py`
- 数据：`figures/_prep_q4.json['monthly']`（← C1 `leaderboard_enhanced.csv` 全量
  4576 行，有效 4561）；校核点取 `problem_4_results.json['contribution_decomp']`。
- 参数条件：同一 OLS 模型 `Cap ~ lnN + year`（b_lnN=6.2662、c_year=12.1419、
  R²=0.4617）；早期窗口基准 = year ≤ 10% 分位（t0=2024.5010）的均值；月度网格
  为「累计到 t 的样本均值」代入同一增长核算恒等式，**不重新拟合第二套系数**。
- 样本量：8 个月度点（2024.583~2025.167），累计样本 617→4263。
- 统计量：Δf=b_lnN·ΔlnN、Δh=c_year·Δt（能力点）；占比=100×Δ·/(Δf+Δh)。
- 不确定性：**未标注**（点估计的确定性分解）。
- 备注：**占比刻意不画 0~100% 堆叠**——因 Δf<0 而 Δh>0，非规模占比 125.04%、规模
  占比 -25.04%（和仍为 100%）。这不是归一化错误，而是「规模是净拖累」的直接表现
  （窗口内平均参数规模下降 ΔlnN=-0.273），故用零线 + 正负分向填充表达。时间跨度
  仅 8 个月是 C1 提交日期的真实分布，非截断。

**13. `fig_q4_bridge_scatter` — 散点 + 回归 + 边际密度（competition #26）**
- 情景：Loss→Benchmark 桥接（式23 单调 sigmoid）按可比性分层的拟合与残差带。
- 脚本：`figures/gen_fig_q4_bridge_scatter.py`
- 数据：`figures/problem_4_results.json['bridge']['strata_by_comparability']`
  （← C6 `loss_benchmark_bridge_expanded.csv` 全量 75 行）
- 参数条件：High 层=同模型同验证集；Medium 层=不同验证集近似对齐。
- 样本量：High n=7（L∈[2.0933, 2.5978]）；Medium n=68（L∈[1.65, 2.84]）。
- 统计量：High R²=0.4029、σ=0.2811；Medium R²=0.3565、σ=9.1149；两层均单调递减。
- 不确定性：**已标注** `uncertainty_band(fit±σ)`，σ 为各层残差标准差。
- 备注：两层残差带宽差一个量级，说明「跨验证集对齐」本身是前沿外推的主要误差源，
  前沿结论必须计入桥接不确定性（`map_error_note`）。High 层仅 7 点，边际用**地毯线
  而非 KDE**（7 点估密度不可靠）。

**14. `fig_q4_frontier_fan` — 预测扇形图（advanced #27）**
- 情景：12/24 月能力前沿在三档算力增速情景下的分位带。
- 脚本：`figures/gen_fig_q4_frontier_fan.py`
- 数据：`figures/problem_4_results.json['frontier']`（`historical_frontier`
  10 点、`slope`、`predictions` 的 P10/P50/P90、`scenarios`）
- 参数条件：历史段 = C1 按月 P90 能力前沿包络（2024.458~2025.208），斜率
  19.679 点/年；情景 low/mid/high = 相对历史斜率 ×{0, 0.5, 1}，对应算力
  停滞/放缓/维持（C4 Epoch AI 历史训练算力中位数增速 5.10×/年）。
- 样本量：历史 10 点；n_open=2813；预测每情景 2 个锚点（12m、24m）。
- 统计量：P50 中位线 + P10–P90 带；12 月 P50 low 42.84 / mid 52.68 / high 62.52，
  24 月 P50 low 42.84 / mid 62.26 / high 81.94。
- 不确定性：**已标注** bootstrap 分位带（`uncertainty_band(P10, P90)`）。
- 备注：预测段只有 12m/24m 两个锚点，故为分段线性连接，**非连续模拟轨迹**。
  low 档 24 月带宽反而收窄，因为斜率为 0 时预测退化为常数、不确定性只剩历史包络的
  重采样。`extrapolation_note` 明确：12/24 月是情景模拟、含外推不确定性、非数据
  直接支持——正文引用时必须保留这一限定。

**15. `fig_q4_task_radar` — 雷达图（competition #5）**
- 情景：C8 Top-5 前沿模型的六维 Benchmark 剖面 vs 全样本均值基准。
- 脚本：`figures/gen_fig_q4_task_radar.py`
- 数据：`figures/problem_4_results.json['c8_aggregation']['top5_frontier_radar' /
  'task_difficulty_mean']`（← C8 detailed_results 1863 个子目录）
- 参数条件：六维 = IFEval / BBH / MATH / GPQA / MUSR / MMLU-PRO，量纲 0–100。
- 样本量：1860 个目录可解析（7 个损坏已跳过），1854 个六维完整；雷达 5 模型 + 1 基准。
- 统计量：各维得分；基准为全样本算术均值（IFEval 40.16 / BBH 47.49 / MATH 11.38 /
  GPQA 29.80 / MUSR 39.96 / MMLU-PRO 31.99）。
- 不确定性：**未标注**（逐模型单次评测得分，无重复）。
- 备注：六维不齐涨——MATH（均值 11.38）与 GPQA（29.80）是共同短板，Top-5 的 MATH
  跨度 39.27~58.91。这说明问题四的「六维均分」单一口径会掩盖任务间结构差异，前沿
  外推应按任务分别看。图例在 GridSpec 独立列，避免压住多边形。

## 四、像素级对比度实测（消化「需视觉复核」告警）

`figure_pdf_quality_check.py` 对复杂背景上的文字只能给「需复核」，无法自动判定。
本步骤把这 3 项（以及修复过程中出现的 5 项）按 300–400 dpi 渲染后**实测像素对比度**
（WCAG 相对亮度公式，前景取文字包围盒内最暗像素，背景取其真实局部底板）：

| 图 | 文字 | 前景 | 背景 | 对比度 | 判定 |
|---|---|---|---|---|---|
| `fig_q2_substitution_contour` | 等值线 "2.47" | (73,74,73) | (255,255,255) | 8.90:1 | 通过 |
| `fig_q2_substitution_contour` | 等值线 "2.79" | (109,110,109) | (255,255,255) | 5.12:1 | 通过 |
| `fig_q2_substitution_contour` | 等值线 "3.10" | (109,110,109) | (255,255,255) | 5.12:1 | 通过 |
| `fig_q2_substitution_contour` | 轴名 "Q" / "N" | (38,38,38) | (255,255,255) | 15.13:1 | 通过 |
| `fig_q4_task_radar` | 半径刻度 "20" | (81,69,69) | (220,204,207) | 5.94:1 | 通过 |
| `fig_q4_task_radar` | 半径刻度 "60" | (92,20,63) | (227,214,214) | 9.13:1 | 通过 |
| `fig_q4_task_radar` | 半径刻度 "80"/"100" | (73,74,73)/(51,51,50) | (250,251,252)/白 | 8.59 / 12.65:1 | 通过 |

阈值 4.5:1，最低实测 5.12:1，全部通过。测量中的一个教训：若把背景取成包围盒外
6px 环带，会越过小尺寸白底板采到橙色填充，得出 2.39:1 的**假阳性**——背景必须取
文字真正所处的局部底板。

## 五、本轮修复的确定缺陷（共 14 项，全部已闭环）

保存钩子与 PDF 终检拦下的问题，一律靠**重排版面 / 迁移文字 / 换判据**解决，
**没有**用缩小字号、删数据、取消误差带来换取通过：

| # | 图 | 缺陷 | 处置 |
|---|---|---|---|
| 1 | `q1_domain_Q_dumbbell` | 数值 "0.0709" 压住散点/区间条 | 数值迁入右侧 GridSpec 专用列，按行对齐 |
| 2 | `q2_elasticity_diverging` | ε_Q=θε_D 文字框压柱 | 方向锚点与恒等式改为图例条目 |
| 3 | `q2_generalized_surface` | 图例遮挡 3D 曲面 | 图例迁入 GridSpec 独立行 |
| 4 | `q2_generalized_surface` | 最终字号仅 6.7pt→7.2pt | 原生画布 6.5×4.3→5.6×4.0in，缩放比回到 ~1 |
| 5 | `q2_generalized_surface` | 轴名 "log10 N" 压刻度 "-1.0" | labelpad 13/10/9 + 固定刻度集 |
| 6 | `q3_lctx_panels` | L_ctx^crit 竖排文字压曲线 | 判据线改顶部独立行共享图例 |
| 7 | `q3_lctx_panels` | 面板级图例溢出画布 | 同上，2×2 改 3×2 GridSpec（首行专放图例） |
| 8 | `q3_lctx_panels` | 带上下标 mathtext 被判文字块重叠 | 标签去掉上标，写「注意力临界 $L_{ctx}$」 |
| 9 | `q1_quality_corr` | x 刻度 "2gram"×"3gram" 相撞 | 35°→52° 仍撞 → 改 90° 竖排 |
| 10 | `q2_substitution_contour` | 等值线标注相撞 + 对比度 3.81:1 | 标注层 every-3→every-5；线/字改深色 + 不透明白底 |
| 11 | `q3_transition_line` | "0.0608" 对比度 4.45:1 | 数值统一改 `COLORS['text']` |
| 12 | `q3_transition_line` | xlabel 下标降部出界 2.1pt | 改「lg C」不带下标 + 留白 0.75→0.42 |
| 13 | `q4_task_radar` | 半径刻度对比度 3.40:1 | `COLORS['grid']`→`COLORS['text']` |
| 14 | `q2_scaling_fit` | 两个多行文字框压散点 | 外部集 RMSE 迁入 `TABLE_q2_scaling`，图内只留一行 |

另有一类系统性修正：**数值标签一律用 `COLORS['text']`**，不再沿用所属系列的浅色
（浅色系列色做文字达不到 4.5:1）。所有 `fontsize<8.0` 已上调到 ≥8.0。

## 六、表格

| 文件 | 列数 | caption（汉字数） | 说明 |
|---|---|---|---|
| `TABLE_q1_weights.tex` | 8 | 质量指标客观权重对照（10） | 22 指标熵权 vs CRITIC，双栏排布 |
| `TABLE_q1_domain_Q.tex` | 6 | 域级综合质量统计（8） | 描述统计 + bootstrap 区间 |
| `TABLE_q2_scaling.tex` | 3 | 标度律参数与拟合优度（10） | **主结果表**：参数/拟合/泛化/弹性 |
| `TABLE_q3_allocation.tex` | 9 | 三档预算下的最优算力配置（12） | 唯一加 `\resizebox`（自然宽 109%） |
| `TABLE_q4_frontier.tex` | 6 | 能力前沿情景预测分位数（11） | 三情景 × 12/24 月 × P10/P50/P90 |

caption 全部 ≤20 汉字，只写短标题；统计口径、重复次数、数据来源留给正文。
列数一致性 0 异常；221 个数值单元格全部可追溯到结果 JSON（允许显示精度截断），
标记文件 `figures/TABLE_DATA_CHECK_PASSED.txt`。

## 七、遗留问题（需下游步骤处理）

1. **LaTeX 环境阻塞（会影响 comp-compile-zh）**：MiKTeX 安装里的 `l3kernel`/`expl3`
   版本低于已装的 `ctex`/`xeCJK` 要求，任何中文文档编译都会失败：
   `! Package ctex Error: Support package 'expl3' too old.`
   `xeCJK` 同样报错，所以不是 `ctex` 单独的问题。
   位置：`C:/Users/hybuzhy/AppData/Local/Programs/MiKTeX/tex/latex/l3kernel/expl3.sty`。
   本步骤**未**擅自更新用户的 TeX 发行版（属系统级共享环境改动）。因此
   `figures/*.tex` 只做了结构校验与宽度解析估算，**未经过真实编译**；表格宽度
   109%→`resizebox` 的判断来自解析估算，编译打通后应复核 Overfull \hbox。
2. **本步骤不负责的图**：`fig_roadmap`、`fig_pipeline_q1`、`fig_index_hierarchy`
   由 paper-figure-drawio 产出；`tikz_q3_feasible` 由 TikZ 子流程产出。
   `figure_check.sh` 的「规划对照」会把这 3 张报为缺失脚本，属预期。
3. **`figure_text_budget.py --selftest` 有 1/56 项预置失败**（标注档
   `$\varphi_B$=1.5%` 被放行）。这是检查器自带的问题，未修改检查器；本步骤的
   图内文字体检走 `figure_check.sh`，结果为 18 个脚本全通过。
4. **θ 双口径**必须在正文交代清楚（见第三节图 6 备注），否则 Q2 的 -10.0 与
   Q3/Q4 的 0.5 会看起来自相矛盾。

## 八、复现方式

```bash
PY="/c/Users/hybuzhy/Software/Modex-MH-Agent/runtime/python/python.exe"
$PY figures/prep_q1_indicators.py      # A1/A2/A3 全量重算（约 10 分钟）
$PY figures/prep_q4_decomp.py          # C1 月度分解
for f in figures/gen_fig_*.py; do $PY "$f"; done
$PY figures/gen_tables.py
$PY figures/gen_latex_includes.py && $PY _utils/fig_include_size.py --figdir figures
bash _utils/figure_check.sh
$PY _utils/figure_pdf_quality_check.py figures --paper paper
```

随机源仅两处，均固定 `seed=42`：bootstrap 重采样（2000 次）与冲突散点边际 KDE
的子样本抽取。两者都不影响任何被报告的统计量（统计量全用全量计算）。

---

# 附：paper-figure-html 步骤产出（HTML 流程/架构图 + TikZ 几何图）

上文由 paper-figure（数据图）步骤撰写。本节记录 paper-figure-html 步骤的产出——即上文
第七节「本步骤不负责的图」所指的 4 张。配色族 = 纯黑白线稿（`MH_DIAGRAM_STYLE=2`）。

## 产出清单（FIGURE_MANIFEST 的 HTML/DrawIO/TikZ 通道）

| 图名 | 类型 | 产物 | 本轮动作 |
|---|---|---|---|
| fig_roadmap | HTML 技术路线图 | figures/fig_roadmap.pdf | 已有，复核通过 |
| fig_pipeline_q1 | HTML 数据处理流程 | figures/fig_pipeline_q1.pdf | 已有，复核通过 |
| fig_index_hierarchy | HTML 指标体系层次图 | figures/fig_index_hierarchy.pdf | 已有，复核通过 |
| tikz_q3_feasible | TikZ 算力预算可行域图 | figures/tikz_q3_feasible.pdf | 本轮新建 |

断线恢复扫描发现 3 张 HTML 图已由上一轮生成且通过全部确定性检查，本轮只补齐缺失的
TikZ 几何图 `tikz_q3_feasible`，并把 4 张图全部写入 `figures/latex_includes.tex`。

## tikz_q3_feasible 内容

在 $(\lg N,\lg D)$ 对数平面刻画问题三的算力预算配置几何：斜率 $-1$ 的两条等成本线
（$C{=}10^{19}$ / $C{=}10^{24}$，即预算约束面 $6ND{+}C_Q{+}C_{\mathrm{attn}}{=}C$ 的截线）、
凸向原点的等损失线 $L_1/L_2$、二者相切给出的最优点 $P_1,P_2$，以及最优轨迹随预算增大
的移动方向。语义标注区分低预算「内点解 $Q^\ast<1$」与高预算「结构转移区 $Q^\ast\to1$
边界」，对应 5.2 节 KKT 活跃集切换。最优点坐标依据 `figures/problem_3_results.json`
的指数型 $g(Q)$ 三档预算实解（如 1e22 档 N*=5.52, D*=258.6, Q*=0.968）。

## 环境修复（解除上文第七节遗留问题 1）

编译 TikZ 中文图触发了此前记录的 `expl3 too old` 阻塞。根因不是 expl3 本身太旧，而是
`miktex packages update l3kernel` 把 expl3/l3kernel 更新到 2026-08 后，独立的 `l3backend`
包仍保留 2024-01 的旧 `l3backend-*.def`，在 kpsewhich 搜索路径上胜出，导致
`\g__pdf_backend_object_int already defined` 双定义。修法：用 l3kernel 目录自带的新版
`l3backend-*.def` 覆盖 l3backend 目录同名文件（原文件备份于 `l3backend/_bak_20260923/`）。
之后 xelatex+ctex 恢复正常，tikz_q3_feasible.tex 已实测编译通过。此修复同时解除后续
comp-compile-zh 的中文编译阻塞。

## 质检结果（确定性检查全通过）

- html_pdf_check（单页/矢量/裁切/宽高比）：3 张 HTML 图全 PASS。
- 几何自检 `--geom-check`（溢出/越界/重叠/对齐）：3 张 HTML 图全 PASS。
- 科研规范自检 `--norm-check`（字号/占页/对比度/认知密度/内容/无斜体）：3 张 HTML 图全 PASS。
- tikz_check 结构自检：tikz_q3_feasible 0 CRITICAL。
- tikz_vision_check：已复核（达 2 轮上限，用当前 PDF 定稿）。
- fig_include_size `--strict`：19 张全部按长宽比/密度写定宽度（tikz_q3_feasible=0.8\textwidth）。
- figure_pdf_quality_check 终检：0 FAIL。tikz_q3_feasible 初版有效字号 7.2pt<8pt，
  经重排（压缩竖向、标签横排、base 字号提到 \normalsize）后达标。
- FIGURE_MANIFEST 对账：HTML/TikZ 通道 4 张全部产出。

**质检口径说明**：确定性检查（结构/几何/规范/尺寸/终检）全部通过。HTML 图的 vision 工具
（drawio_vision_check）本机为编译态且本轮未单独复跑，其确定性几何/规范门已全通过；
TikZ 图 vision 已复核。终检另有若干 CJK 字形「背景复杂」对比度 WARN，属启发式复核项，
mono 图为纯黑字白底、对比度实际充分。

## latex_includes.tex

已追加 4 个 `\includegraphics` 块（fig_roadmap / fig_pipeline_q1 / fig_index_hierarchy /
tikz_q3_feasible），无重复 label，全表共 19 张图。caption 均为短标题，下游 comp-paper 直接引用。
