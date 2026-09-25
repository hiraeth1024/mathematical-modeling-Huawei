# 华为杯 F 题建模求解报告：算力约束下提升大语言模型能力的资源配置建模

> 本报告承接 `PROBLEM_ANALYSIS.md`（赛题分析）与 `CAPABILITY_CHECKLIST.json`（能力合同），为四个子问题给出完整数学模型、求解算法与检验方案。全文 Loss 指验证集交叉熵损失（nats/token，越低越好）。所有题面给定常量以 `DATA_FACTS.json` 的 `given` 段为唯一权威源，原样搬用。

## 〇、总体建模思路与依赖链

四问构成"数据刻画 → 纳入标度律 → 预算优化 → 能力预测"的递进主线，前一问输出是后一问输入：

$$
\underbrace{Q,\ \mathbf p\text{-Loss}}_{\text{问题一}}\ \Rightarrow\ \underbrace{L(N,D,Q,\mathbf p)}_{\text{问题二 广义标度律}}\ \Rightarrow\ \underbrace{\min_{N,D,Q} L\ \text{s.t.}\ C_{\text{tot}}\le C}_{\text{问题三 约束优化}}\ \Rightarrow\ \underbrace{\text{Loss}\to\text{Benchmark},\ \text{前沿预测}}_{\text{问题四}}
$$

- **问题一**：多指标综合评价 + 带单纯形约束回归。输出域级质量 $Q$ 与配比–Loss 定量关系。
- **问题二**：非线性最小二乘拟合经典标度律，扩展为含 $Q,\mathbf p$ 的广义标度律，解析推导弹性与 $Q$–$N$ 替代条件。
- **问题三**：以广义标度律为目标、三部分算力和为预算约束的非线性优化，KKT 解析 + SLSQP 多起点数值求解，定义并识别结构性转移。
- **问题四**：控制规模的贡献分解、分层单调桥接映射、算力放缓情景下的分位带前沿预测。

**本题涉及题型：[优化, 统计/回归/预测, 评价/决策, 非线性拟合]，已对照防错手册（`_utils/error_prevention.md`）第一/三/四章及第九章约束闭环审查。** 本题无物理/几何空间机理，不涉及微分方程守恒律推导，故不套用机理题骨架。

---

## 一、模型假设

每条假设均给出理由、代码参数化开关与替代方案，关键假设在灵敏度分析中扰动。

**假设 1：22 个质量指标经方向统一后"越高越好"，综合质量 $Q$ 由客观赋权线性合成，映射到 $(0,1]$。**
- 理由：题目 S6 明确要求方向统一（负向指标做 $1-x$ 补转换）、列表型压缩为标量；客观赋权（熵权/CRITIC）避免主观拍权重，符合"用全量信号"要求。
- 参数化：`WEIGHT_METHOD ∈ {'entropy','critic','pca'}`（默认 `'entropy'`）；`LISTAGG ∈ {'mean','p50','trimmed'}`。
- 替代假设：若客观赋权对少数指标过度加权，改用主客观组合赋权（`WEIGHT_METHOD='combo'`），或 PCA 首主成分作 $Q$。

**假设 2：配比–Loss 关系在同一训练尺度内可由 $\mathbf p$ 单独预测（$N,D$ 由 RegMix 实验固定），分域建模后按目标域加权。**
- 理由：附件 A4–A15 的 Loss 表本就按 13 域分列，RegMix 原范式即"以 $\mathbf p$ 为特征分域回归 Loss"；快速验算显示同配方不同域 Loss 差 2–3 nats，支持分域。
- 参数化：`MIX_MODEL ∈ {'linear_simplex','ridge','lightgbm'}`（默认对数域 `'linear_simplex'`，`'lightgbm'` 作 RegMix 风格对照）。
- 替代假设：若线性拟合残差有明显弯曲，切换 `'lightgbm'` 捕捉配比交互。

**假设 3：质量 $Q$ 以"质量增强有效数据量"方式进入广义标度律，$Q=1$ 时退化为经典形式。**
- 理由：附件 B6–B8 是唯一含 $Q\_score$ 的数据，且 $Q$↑→Loss↓（实测 corr$(Q,L)=-0.33$）；令有效数据 $D_{\rm eff}=Q^{\theta}D$ 可使 $Q=1$ 时 $D_{\rm eff}=D$ 自然退化，物理可解释（高质量数据等效于更多 token）。
- 参数化：`GEN_FORM ∈ {'eff_data','defect_add'}`（默认 `'eff_data'`：$L=E+AN^{-\alpha}+B(Q^\theta D)^{-\beta}$；备选 `'defect_add'`：$L=E+AN^{-\alpha}+BD^{-\beta}+\kappa(1-Q)^\nu$）。
- 替代假设：若 `eff_data` 在 B6 留出点 RMSE 劣于经典基线，切 `defect_add` 并对比 AIC/BIC。

**假设 4：问题三中配比 $\mathbf p$ 由前两问固定（主方案），仅 $N,D,Q$ 为决策变量；$\mathbf p$ 联立优化作为扩展。**
- 理由：题目明确允许二者，固定 $\mathbf p$ 使 $N/D/Q$ 结构性转移分析更清晰、可解释；附件 B 无逐域配比字段，$\mathbf p$ 只能经 Q1 域级关系间接影响 $B$。
- 参数化：`JOINT_P = False`（默认固定；`True` 时把 17 维 $\mathbf p$ 加入决策变量并加单纯形约束）。
- 替代假设：`JOINT_P=True` 联立优化，用投影梯度处理单纯形约束。

**假设 5：基线质量 $Q_0$ 取问题一抽样集域级 $Q$ 的中位数（题面未定死），在灵敏度分析中扰动 $\pm20\%$。**
- 理由：$Q_0$ 是质量成本铰链 $[g(Q)-g(Q_0)]_+$ 的起算点，题面未给具体值，用数据驱动的中位数最中性。
- 参数化：`Q0 = median(domain_Q)`（默认），灵敏度扫描 `Q0 ∈ {0.8·Q0, Q0, 1.2·Q0}`。
- 替代假设：若中位数导致 $C_Q$ 在所有预算档均为 0，改用抽样集域级 $Q$ 的下四分位数。

**假设 6：问题四综合能力度量取六维 Benchmark 均分（主口径），开源筛选以 Hub License 为准，区分 pretrained/chat，时间轴用提交/发布日期。**
- 理由：Leaderboard 自带 Average 列，均分透明可复现；题目 S21 明确要求声明这些口径。
- 参数化：`CAP_METRIC ∈ {'mean6','weighted','pca'}`（默认 `'mean6'`）；`OPEN_CRITERION ∈ {'hub_license','epoch_openweights'}`。
- 替代假设：加权/PCA 综合作稳健性对照。

---

## 二、符号说明表

| 符号 | 含义 | 单位 | 取值范围 | 首次出现 |
|------|------|------|----------|----------|
| $L$ | 验证集交叉熵损失（因变量） | nats/token | $[1.8,7.3]$（实测） | 问题二 |
| $N$ | 模型参数量 | $10^9$ params | $[0.07,12]$ 真实, 外推至 $10^4$ | 问题二 |
| $D$ | 训练 token 数 | $10^9$ tokens | $[0.134,300]$ | 问题二 |
| $Q$ | 综合数据质量评分 | 无量纲 | $(0,1]$ | 问题一 |
| $Q_0$ | 基线质量（成本起算点） | 无量纲 | 假设 5 给定 | 问题三 |
| $\mathbf p=(p_1,\dots,p_{17})$ | 17 域配比向量 | 比例 | $p_i\ge0,\ \sum p_i=1$ | 问题一 |
| $E$ | 不可约损失 | nats/token | $\approx1.69$（拟合） | 问题二 |
| $A,\alpha$ | 参数项系数与指数 | — | $A\approx0.35,\ \alpha\approx0.34$ | 问题二 |
| $B,\beta$ | 数据项系数与指数 | — | $B\approx1.24,\ \beta\approx0.28$ | 问题二 |
| $\theta$ | 质量–有效数据放大指数 | 无量纲 | 待估 $>0$ | 问题二 |
| $C$ | 总算力预算 | FLOPs | $\{10^{19},10^{22},10^{24}\}$ | 问题三 |
| $C_{\rm train}=6ND$ | 基础训练开销 | FLOPs | 中间量 | 问题三 |
| $C_Q=D[g(Q)-g(Q_0)]_+$ | 质量提升开销 | FLOPs | 中间量 | 问题三 |
| $C_{\rm attn}=\eta ND L_{\rm ctx}$ | 长文本注意力开销 | FLOPs | 中间量 | 问题三 |
| $\eta$ | 注意力开销系数 | — | $2\times10^{-4}$（常量） | 问题三 |
| $L_{\rm ctx}$ | 上下文窗口长度 | tokens | C7 取值集（外生） | 问题三 |
| $L_{\rm ctx}^{\rm crit}=6/\eta$ | 注意力=训练开销临界上下文 | tokens | $3\times10^4$ | 问题三 |
| $g(Q)$ | 每 token 质量成本函数 | FLOPs/token | 指数/幂/对数三型 | 问题三 |
| $\varepsilon_X=\partial\ln L/\partial\ln X$ | 因素 $X$ 弹性 | 无量纲 | 分析量 | 问题二 |
| $s_X(C)$ | 因素 $X$ 算力份额 | 比例 | $[0,1]$ | 问题三 |
| $w_j$ | 质量指标 $j$ 权重 | 无量纲 | $\sum w_j=1$ | 问题一 |
| $B_k$ | 第 $k$ 维 Benchmark 得分 | $0$–$100$ | 观测 | 问题四 |
| $\mathrm{Cap}(t)$ | 综合能力（时间 $t$） | $0$–$100$ | 派生量 | 问题四 |
| $r_C$ | 算力增速（情景假设） | %/年 | 三档情景 | 问题四 |

> 说明：本表仅收录跨章节复用、直接进入核心目标或约束的记号；一次性下标（如指标 $j$、域 $k$、样本 $i$）在首次出现处解释。$N,D$ 附件以 $10^9$ 为单位，代入 $6ND$ 须先乘 $10^9$。

---

## 三、问题一建模：数据质量评价 + 冲突消解 + 配比–Loss 关系

**认领能力项**：P1-C1（22 维预处理与方向统一）、P1-C2（综合质量 $Q$ 样本/语料/域级）、P1-C3（冲突定义与消解）、P1-C4（配比 $\mathbf p$–Loss 回归）、P1-C5（跨体系域映射）。

### 3.1 理论起点与题意映射

问题一是"多指标综合评价 + 带约束回归 + 跨体系关联"的混合任务。数据实测结构：A1 抽样集 $51230$ 条 $\times$ 27 字段（22 质量指标：14 标量 + 8 列表型），A2 arxiv $17523$ 条、A3 github $203752$ 条（各 22 指标，无 content）。配方实验 A4 训练集 $512$ 组配比 $\times$ 13 域 val\_loss，A6–A11 三尺度（1M/60M/1B）检验集，A12–A15（10B/70B）外推表。A16 给出 3 direct + 3 near\_direct + 11 inferred 的域映射。

### 3.2 针对 P1-C1/P1-C2：列表型压缩、方向统一与综合质量 $Q$

**（1）列表型压缩**。8 个列表型指标（fluency\_en、qurater、ad\_en、fineweb\_edu、modernbert\_{cleanliness,reasoning,professionalism,readability}）为逐句/逐段打分向量 $\mathbf v_{ij}=(v_{ij}^{(1)},\dots,v_{ij}^{(m_{ij})})$，用文档级统计量压缩为标量（默认均值，稳健性用截尾均值/中位数）：

$$
x_{ij}=\frac{1}{m_{ij}}\sum_{t=1}^{m_{ij}} v_{ij}^{(t)},\qquad j\in\mathcal J_{\rm list}. \tag{1}
$$

**（2）方向统一 + 归一化**。先对每个指标做 Min–Max 归一化，再对负向指标（ad\_en 广告含量，越低越好）取补转换 $1-x$，使全部 22 指标"越高越好"：

$$
\tilde x_{ij}=\frac{x_{ij}-\min_i x_{ij}}{\max_i x_{ij}-\min_i x_{ij}},\qquad
r_{ij}=\begin{cases}\tilde x_{ij}, & j\in\mathcal J_{+}\ (\text{正向})\[2pt] 1-\tilde x_{ij}, & j\in\mathcal J_{-}\ (\text{负向, ad\_en})\end{cases} \tag{2}
$$

**（3）客观赋权（熵权法）**。对归一化矩阵 $R=(r_{ij})$，指标 $j$ 的信息熵与权重：

$$
p_{ij}=\frac{r_{ij}}{\sum_{i=1}^n r_{ij}},\quad
e_j=-\frac{1}{\ln n}\sum_{i=1}^n p_{ij}\ln p_{ij},\quad
w_j=\frac{1-e_j}{\sum_{k=1}^{22}(1-e_k)}. \tag{3}
$$

**（4）样本级质量与聚合**。样本 $i$ 综合质量、以及样本→语料→域的加权聚合：

$$
Q_i=\sum_{j=1}^{22} w_j\, r_{ij}\ \in(0,1],\qquad
Q^{\rm dom}_d=\frac{1}{|\mathcal S_d|}\sum_{i\in\mathcal S_d} Q_i, \tag{4}
$$

其中 $\mathcal S_d$ 为域 $d$ 的样本集。全量流程同样施于 A2/A3，得 arxiv/github 域级 $Q$，与 A1 抽样集同名域对照（哑铃图 fig\_q1\_domain\_Q\_dumbbell）以验证一致性。

> **求解**：熵权 $w_j$ 由 A1 全量 51230 条计算（不可抽样，见能力合同 P1-C2 falsifiable\_check）；CRITIC/PCA 作交叉验证。$Q$ 的物理合理性由问题二"$Q$↑→Loss↓"回验。

### 3.3 针对 P1-C3：质量冲突的可计算定义与消解

**冲突定义**（可计算判据）：对强正向指标 $j_+$（如 fineweb\_edu）与强负向原始指标 $j_-$（如 ad\_en），若在样本集上二者 Spearman 秩相关 $\rho_{j_+,j_-}$ 显著为负，或单样本同时落入两者高分位（分位错位），则判为冲突样本：

$$
\text{Conflict}(i)=\mathbb 1\!\left[\,r_{i,j_+}\ge\tau_{0.8}^{+}\ \wedge\ \tilde x_{i,j_-}\ge\tau_{0.8}^{-}\,\right],\qquad
\rho_{j_+,j_-}<\rho^\ast\ (\text{显著负}), \tag{5}
$$

其中 $\tau_{0.8}$ 为 0.8 分位阈值。冲突率 $=\frac1n\sum_i\text{Conflict}(i)$。

**消解规则**：对冲突样本采用稳健聚合（截尾均值/中位数替代均值）与降权：$Q_i^{\rm robust}=\sum_j w_j\,\mathrm{med}(r_{ij})$，或对冲突样本乘以降权因子 $\delta\in(0,1)$。对比消解前后 $Q$ 排序变化（Kendall $\tau$），并在 A2/A3 扩展集复现冲突结论以验稳健性。

### 3.4 针对 P1-C4：配比 $\mathbf p$–Loss 定量关系（RegMix 风格，带单纯形约束）

以 17 域配比 $\mathbf p$ 为特征、13 域 val\_loss 为目标，分域建模。主模型为对数域带单纯形约束的线性回归：

$$
\ln \hat L_k(\mathbf p)=a_k+\sum_{i=1}^{17} b_{ki}\,p_i,\qquad
\text{s.t. } p_i\ge0,\ \sum_{i=1}^{17}p_i=1, \tag{6}
$$

对每个目标域 $k$（13 个有 Loss 列的域）拟合系数 $b_{ki}$，其绝对值给出各配比域对该域损失的重要性（棒棒糖图 fig\_q1\_mixture\_importance）。备选 LightGBM 捕捉配比交互（RegMix 原范式）。单纯形约束在预测/寻优时用 softmax 参数化 $p_i=\mathrm{softmax}(z)_i$ 或单纯形投影处理。

**验证链**：A4–A5（512 组）拟合 → A6–A11（256/256/64 行，三尺度）检验 → A12–A15（63 行，10B/70B）外推验稳健。留出 RMSE 与 $R^2$ 分尺度报告。

### 3.5 针对 P1-C5：跨体系域映射（7 质量域 ↔ 17 配比域）

依 A16：3 个 direct（arxiv/github/stackexchange 同名）、3 个 near\_direct（wikipedia\_en↔wikipedia、gutenberg↔book、pile\_cc↔commoncrawl，语义对应直接借用）、11 个 inferred（无同名质量域）。inferred 域处理规则（显式，不无声丢弃）：

- **建模关联**：用可获得质量信号域的 $Q$ 与配比域的 Loss 建立回归，对 inferred 域按体裁相似性（如 dm\_mathematics 借 arxiv/math 信号、pubmed 借 arxiv）赋予推断 $Q$，标注为 inferred 可信度较低。
- **保留解释间接影响**：nih\_exporter、enron\_emails、europarl、philpapers 4 个域无对应 Loss 列，仍保留其配比在式 (6) 中作解释变量（间接影响其它域 Loss），不剔除。

---

## 四、问题二建模：经典标度律 → 广义标度律 + 弹性与替代

**认领能力项**：P2-C1（经典律拟合 $L(N,D)$）、P2-C2（广义律 $L(N,D,Q,\mathbf p)$ 设计与估计）、P2-C3（弹性/边际效用与 $Q$–$N$ 替代条件）。

### 4.1 针对 P2-C1：经典标度律拟合

采用题面给定形式（`DATA_FACTS.given`，禁改）：

$$
L(N,D)=E+A\,N^{-\alpha}+B\,D^{-\beta}, \tag{7}
$$

其中 $E$ 为不可约损失，$A,\alpha,B,\beta$ 待估。以 B1（$1176$ 行真实 Pythia 轨迹，$N\in[0.07,12]$B、$D\in[0.134,300]$B）为主拟合集。为抑制大损失点主导、增强对异常点稳健性，在**对数域**用 Huber 损失做加权非线性最小二乘：

$$
\min_{E,A,\alpha,B,\beta}\ \sum_{m=1}^{M}\ \rho_\kappa\!\Big(\ln L_m-\ln\big(E+A N_m^{-\alpha}+B D_m^{-\beta}\big)\Big),\qquad
\rho_\kappa(u)=\begin{cases}\tfrac12 u^2,&|u|\le\kappa\ \kappa(|u|-\tfrac12\kappa),&|u|>\kappa\end{cases} \tag{8}
$$

**求解**：`scipy.optimize.least_squares(loss='huber')` 或 `curve_fit`，多起点（$\alpha,\beta\in[0.05,0.5]$ 网格初值）避免局部解。**预验证拟合**（本报告已在 B1 上试算）：$E=1.69,\ A=0.35,\ \alpha=0.34,\ B=1.24,\ \beta=0.28,\ R^2\approx1.0$，$\alpha,\beta$ 落在文献常见区间 $[0.05,0.4]$，物理方向正确（$N$↑、$D$↑ 均使 $L$↓）。

**多重验证**（不同可比等级分层报告）：B2（Cerebras 半合成，1029 行）族外验证、B3（8×500 轨迹）插值验证、B4（12 族收敛点，57 行）跨族泛化、B5（44 文献点）文献泛化。B9/B10（100B–10000B 估算 Loss）仅用于外推讨论，标注"非直接观测"。

### 4.2 针对 P2-C2：广义标度律设计（含 $Q,\mathbf p$）

**主方案——质量增强有效数据量**（`GEN_FORM='eff_data'`）。令高质量数据等效于更多 token，即有效数据量 $D_{\rm eff}=Q^{\theta}D$（$\theta>0$）：

$$
\boxed{\,L(N,D,Q,\mathbf p)=E+A\,N^{-\alpha}+B\,\big(Q^{\theta}D\big)^{-\beta}\,} \tag{9}
$$

**$Q=1$ 退化依据**：当 $Q=1$ 时 $Q^\theta=1$，$D_{\rm eff}=D$，式 (9) 严格退化为经典式 (7)——这是把 $Q$ 归一化到 $(0,1]$（$Q=1$ 为满质量）的直接后果，故退化成立有据，非强加约束。

**配比 $\mathbf p$ 的引入**：附件 B 无逐域配比字段（见假设 2/3），$\mathbf p$ 通过问题一的域级贡献间接进入数据项。定义配比调节的有效数据 $D_{\rm eff}=Q^\theta\,\phi(\mathbf p)\,D$，其中 $\phi(\mathbf p)=\sum_i p_i\,\psi_i$、$\psi_i$ 为域 $i$ 由式 (6) 系数导出的相对贡献（归一化使基准配比下 $\phi=1$）。当仅研究 $N,D,Q$ 时 $\phi(\mathbf p)$ 取基准值 1。

**备选方案——质量缺陷附加项**（`GEN_FORM='defect_add'`）：

$$
L=E+A\,N^{-\alpha}+B\,D^{-\beta}+\kappa\,(1-Q)^{\nu},\qquad \kappa>0,\ \nu>0, \tag{10}
$$

$Q=1$ 时附加项为 0 亦退化为经典式。两方案均用 B6–B8（$360/450/1704$ 行，唯一含 $Q\_score\in[0.1,1.0]$，半合成）联合估计新增参数（$\theta$ 或 $\kappa,\nu$），并**标注半合成可信度边界，不表述为直接观测**。

**方案择优判据**：在 B6 留出点上比较 RMSE 与 AIC/BIC，要求广义律不劣于经典律基线（能力合同 P2-C2 falsifiable\_check），且 $Q$ 项方向物理合理（$Q$↑→$L$↓，已由 corr$(Q,L)=-0.33$ 佐证）。若主方案留出 RMSE 劣于基线，切备选方案（见假设 3）。

### 4.3 针对 P2-C3：弹性、边际效用与 $Q$–$N$ 替代条件

**弹性**（解析导出，以主方案式 (9) 为例）。定义 $\varepsilon_X=\partial\ln L/\partial\ln X$：

$$
\frac{\partial L}{\partial N}=-\alpha A N^{-\alpha-1},\quad
\frac{\partial L}{\partial D}=-\beta B Q^{-\theta\beta}D^{-\beta-1},\quad
\frac{\partial L}{\partial Q}=-\theta\beta B\,Q^{-\theta\beta-1}D^{-\beta}. \tag{11}
$$

$$
\varepsilon_N=\frac{-\alpha A N^{-\alpha}}{L},\qquad
\varepsilon_D=\frac{-\beta B (Q^\theta D)^{-\beta}}{L},\qquad
\varepsilon_Q=\theta\,\varepsilon_D. \tag{12}
$$

式 (12) 表明质量弹性 $\varepsilon_Q=\theta\varepsilon_D$——质量放大有效数据，其边际效用是数据弹性的 $\theta$ 倍。各弹性方向均为负（增大任一因素降低损失），量级比较由发散柱状图 fig\_q2\_elasticity\_diverging 展示。

**$Q$–$N$ 替代条件**（等损失线 $dL=0$）。沿等损失面：

$$
\frac{\partial L}{\partial Q}\,dQ+\frac{\partial L}{\partial N}\,dN=0
\ \Rightarrow\
\left.\frac{dN}{dQ}\right|_{L}=-\frac{\partial L/\partial Q}{\partial L/\partial N}
=-\frac{\theta\beta B\,Q^{-\theta\beta-1}D^{-\beta}}{\alpha A\,N^{-\alpha-1}}. \tag{13}
$$

代入拟合参数即得"$\Delta Q=0.1$ 等价于 $\Delta N\approx \left.\tfrac{dN}{dQ}\right|_L\times0.1$"的**数值**替代率（在参考点 $(N_0,D_0,Q_0)$ 处求值），由等高线图 fig\_q2\_substitution\_contour 展示。域间替代/互补由配比二阶交互 $\partial^2 L/\partial p_i\partial p_j$ 的符号判断（负=互补、正=替代）。

> **求解叙事**：经典律用对数域 Huber-NLS（选择理由：损失跨越 $2$–$4.7$ 量级，对数域使残差同方差、Huber 抑制离群轨迹点）；广义律在经典律参数基础上仅新增 $\theta$（或 $\kappa,\nu$）用 B6–B8 拟合，保留 $E,A,\alpha,B,\beta$ 或联合微调；弹性/替代率全部解析求导后代入数值，可复核。

---

## 五、问题三建模：算力约束下的资源配置优化 + 结构性转移

**认领能力项**：P3-C1（$N/D/Q/\mathbf p$ 联合优化，含"四者取舍"总目标 S3/S4/S15）、P3-C2（结构性转移定义与识别）、P3-C3（$L_{\rm ctx}$ 敏感性与临界值解析）。

### 5.1 优化模型（目标 + 约束，分开陈述）

**决策变量**：$N>0$（连续，$10^9$ params）、$D>0$（连续，$10^9$ tokens）、$Q\in(0,1]$（连续）。$\mathbf p$ 默认固定（假设 4），扩展时联立。$L_{\rm ctx}$ 为**外生参数**（题目 S17 明确，非寻优变量）。

**目标函数**（取自问题二广义标度律式 (9)）：

$$
\min_{N,D,Q}\ L(N,D,Q,\mathbf p)=E+A\,N^{-\alpha}+B\,\big(Q^{\theta}D\big)^{-\beta}. \tag{14}
$$

**约束条件**（三部分算力和不超预算，题面给定公式，禁改）：

$$
\begin{aligned}
&\text{(算力预算)}\quad \underbrace{6ND}_{C_{\rm train}}+\underbrace{D\,[g(Q)-g(Q_0)]_+}_{C_Q}+\underbrace{\eta\,ND\,L_{\rm ctx}}_{C_{\rm attn}}\ \le\ C,\[4pt]
&\text{(质量域)}\quad 0<Q\le1,\qquad \text{(正性)}\quad N>0,\ D>0,\[4pt]
&\text{(单纯形, 仅联立时)}\quad p_i\ge0,\ \textstyle\sum_{i=1}^{17}p_i=1,
\end{aligned} \tag{15}
$$

其中 $\eta=2\times10^{-4}$；$g(Q)$ 三型之一（`DATA_FACTS.given`）：指数型 $g=10^{7}e^{6Q}$、幂型 $g=5\times10^{9}Q^{4}$、对数型 $g=2\times10^{9}\ln(1+10Q)$。$[\cdot]_+$ 取正部（$Q>Q_0$ 才计质量成本）。**单位**：$N,D$ 代入前须乘 $10^9$。

### 5.2 KKT 解析刻画

预算约束在最优处通常取等号（增大 $N,D,Q$ 均降损失，会用尽预算）。构造 Lagrange 函数（暂略 $[\cdot]_+$ 的非光滑，先设 $Q>Q_0$ 活跃段）：

$$
\mathcal L=E+A N^{-\alpha}+B(Q^\theta D)^{-\beta}+\mu\big(6ND+D[g(Q)-g(Q_0)]+\eta ND L_{\rm ctx}-C\big). \tag{16}
$$

一阶条件（KKT）：

$$
\begin{aligned}
\partial_N\mathcal L&=-\alpha A N^{-\alpha-1}+\mu D(6+\eta L_{\rm ctx})=0,\
\partial_D\mathcal L&=-\beta B Q^{-\theta\beta}D^{-\beta-1}+\mu\big(6N+[g(Q)-g(Q_0)]+\eta N L_{\rm ctx}\big)=0,\
\partial_Q\mathcal L&=-\theta\beta B Q^{-\theta\beta-1}D^{-\beta}+\mu D\,g'(Q)=0,\
\mu&\ge0,\quad \text{预算等式成立}.
\end{aligned} \tag{17}
$$

由前两式消 $\mu$ 得 $N,D$ 的最优配比关系（类 Chinchilla 的 $N$–$D$ 平衡），第三式给出质量 $Q$ 的内点最优条件 $\theta\beta B Q^{-\theta\beta-1}D^{-\beta}=\mu D g'(Q)$——**当边际质量收益 $<$ 边际质量成本时，$Q$ 停在内点；否则推向边界 $Q=1$**。这一内点↔边界切换是结构性转移的解析来源之一。由此可推 $N^\ast,D^\ast,Q^\ast$ 关于 $C$ 的近似标度关系（低预算 $C_Q,C_{\rm attn}$ 可忽略时退化为 $N^\ast\propto C^{a},D^\ast\propto C^{b}$）。

### 5.3 数值求解

KKT 给出结构，全局解用数值优化：`scipy.optimize.minimize(method='SLSQP')`，对数尺度变量 $(\ln N,\ln D,Q)$ 避免数值尺度悬殊；**多起点**（对每档预算取 $\ge8$ 个随机初值）取最优，缓解非凸。三档预算 $C\in\{10^{19},10^{22},10^{24}\}$ FLOPs（题面 S15，`DATA_FACTS.given`），并在 $\log C\in[18,25]$ 连续扫描以刻画转移。$g(Q)$ 三型分别求解对比（成本函数选择对最优解影响，题目要求）。

### 5.4 针对 P3-C2：结构性转移的数学定义与识别

给出**可判定**定义（三选一或联合，避免只定性说"变了"）：

**（a）算力份额拐点**。定义各部分份额 $s_X(C)=C_X^\ast/C$（$X\in\{{\rm train},Q,{\rm attn}\}$），结构性转移点为份额对 $\log C$ 的导数出现峰值处：

$$
C^\dagger=\arg\max_{C}\ \left|\frac{d\,s_X(C)}{d\,\log C}\right|. \tag{18}
$$

**（b）KKT 活跃约束集切换**。当 $Q^\ast$ 从内点解切到边界 $Q=1$，或 $C_Q$ 铰链从非激活（$Q^\ast\le Q_0$）变为激活（$Q^\ast>Q_0$），活跃集改变即判定转移。

**（c）最优轨迹方向突变**。$(N^\ast,D^\ast,Q^\ast)$ 关于 $\log C$ 的单位切向量 $\hat{\mathbf t}(C)$ 方向发生显著转折（相邻切向夹角超阈值）。

识别方法：连续预算扫描 + 数值差分求 $ds_X/d\log C$ 峰值检测 + 活跃集监控。转移点由折线图 fig\_q3\_transition\_line 标注。**递进性预期**：低预算优先堆基础训练（$s_{\rm train}$ 高、$Q^\ast$ 低甚至 $\le Q_0$、$C_Q=0$），中高预算才值得投质量提升（$s_Q$ 上升、$Q^\ast$ 趋边界）。若某档预算增大而 $Q$ 投入恒为 0 或最优 $L$ 不变，须回查 $g(Q)$ 标定或广义律 $Q$ 项弹性。

### 5.5 针对 P3-C3：$L_{\rm ctx}$ 临界值解析与敏感性

**临界值解析**（题面 S17）：令注意力开销等于训练开销 $\eta ND L_{\rm ctx}=6ND$，与 $N,D$ 无关，解得

$$
L_{\rm ctx}^{\rm crit}=\frac{6}{\eta}=\frac{6}{2\times10^{-4}}=3\times10^{4}\ \text{tokens}. \tag{19}
$$

当 $L_{\rm ctx}\ge L_{\rm ctx}^{\rm crit}$ 时注意力开销已超训练开销，长上下文显著挤压训练预算。**敏感性扫描**取值严格来自 C7 实测集 $\{2048,4096,8192,32768,131072\}$（不臆造 C7 外取值，能力合同 P3-C3）；$3\times10^4$ 恰落在 $8192$ 与 $32768$ 之间，即 $\ge32768$ 的长上下文模型注意力已超训练开销。多面板图 fig\_q3\_lctx\_panels 展示 $N^\ast,D^\ast,Q^\ast,L^\ast$ 随 $L_{\rm ctx}$ 变化并标注临界线。TikZ 可行域图 tikz\_q3\_feasible 展示 $(N,D,Q)$ 空间预算面、等成本线与最优点。

---

## 六、问题四建模：规模/非规模贡献分解 + Loss–Benchmark 桥接 + 前沿预测

**认领能力项**：P4-C1（规模 vs 非规模贡献分离）、P4-C2（Loss–Benchmark 桥接映射）、P4-C3（12/24 月前沿预测 + 不确定性）、P4-C4（C8 逐任务聚合）。

### 6.1 综合能力度量与口径声明（题目 S21 要求显式声明）

综合能力（主口径 `CAP_METRIC='mean6'`）：六维 Benchmark 均分

$$
\mathrm{Cap}=\frac{1}{6}\sum_{k=1}^{6} B_k,\quad k\in\{\text{IFEval, BBH, MATH Lvl5, GPQA, MUSR, MMLU-PRO}\}. \tag{20}
$$

**口径**：开源筛选以 Hub License 为准（开源权重许可证）；区分 pretrained 与 chat/finetuned（Type 字段）；时间轴用提交日期（C1）/发布日期（C4），三者口径差异在报告中说明。加权/PCA 综合作稳健性对照。

### 6.2 针对 P4-C1：规模 vs 非规模技术进步贡献分离

采用"控制规模后的时间趋势即非规模技术进步"的可识别策略。以 C1/C3/C4 数据回归综合能力对规模变量与时间：

$$
\mathrm{Cap}_i=f(\ln N_i,\ln D_i,\ln C_i)+h(t_i)+\varepsilon_i, \tag{21}
$$

其中 $f(\cdot)$（规模项，用 C4 的算力/数据/参数字段控制规模）解释**规模扩张贡献**，$h(t_i)$（时间趋势项，同规模下逐年能力提升）解释**非规模技术进步贡献**。在时间区间 $[t_0,t_1]$ 上，两部分贡献占比：

$$
\text{scale\%}=\frac{\Delta f}{\Delta f+\Delta h},\qquad
\text{nonscale\%}=\frac{\Delta h}{\Delta f+\Delta h},\qquad
\text{scale\%}+\text{nonscale\%}=100\%. \tag{22}
$$

$f$ 用样条/线性、$h$ 用逐年固定效应或平滑趋势；亦可用"能力效率前沿随时间移动"（同算力下最优能力的时间导数）作稳健性对照。堆叠面积图 fig\_q4\_contribution\_decomp 展示占比随时间演化。**递进性预期**：算力放缓情景下非规模贡献占比应上升（规模贡献增速放缓）。

### 6.3 针对 P4-C2：Loss–Benchmark 桥接映射（分层单调）

用 C6（$75$ 条，含 Val\_Loss 与六维 LB\_*）建立 Loss → Benchmark 单调映射，按 Loss\_Comparability 分层（High：Pythia 可与附件 B 对照；其余中可比）。用单调递减 sigmoid/对数回归：

$$
\widehat{\mathrm{Cap}}=\frac{S_{\max}}{1+\exp\!\big(a(L-L_0)\big)}+c,\quad a>0\ (\text{Loss↑→Cap↓}), \tag{23}
$$

分层拟合参数 $(a,L_0,S_{\max},c)$，并讨论映射误差（残差带宽）对前沿结论的影响（映射误差敏感性）。散点+回归图 fig\_q4\_bridge\_scatter 按可比等级着色。

### 6.4 针对 P4-C3：算力放缓情景下的前沿预测 + 不确定性

**前沿定义**：各时间点开源模型综合能力的上包络（如逐月 P90 分位或凸包上沿）。**情景假设**：算力增速 $r_C$ 设三档（低/中/高，如 0%/50%/100% 历史增速，题面未给故做情景，显式声明）。在给定 $r_C$ 下外推算力轨迹，经桥接式 (23) 或直接对前沿时序外推，用**分位回归/Bootstrap** 给出 12/24 月前沿的 P10/P50/P90 分位带：

$$
\mathrm{Frontier}(t+\Delta)\in[\,\hat F_{10}(t+\Delta),\ \hat F_{90}(t+\Delta)\,],\quad \Delta\in\{12,24\}\ \text{月}. \tag{24}
$$

扇形图 fig\_q4\_frontier\_fan 展示分位带。**递进性预期**：24 月前沿 P50 高于 12 月前沿 P50，增速放缓但不停滞（非规模技术进步仍贡献）。外推超出训练数据范围处显式标注"情景模拟、含外推不确定性"。

### 6.5 针对 P4-C4：C8 逐任务聚合

对 C8（$1863$ 目录 / $1958$ JSON，$1854$ 模型六维完整、$4$ 个截断）做逐任务聚合，**不得仅用 C1 汇总表**。聚合规则：按目录取最新可解析记录（按文件时间戳/记录日期），跳过损坏 JSON 并记录跳过数。至少一项分任务分析：各基准任务难度演进（逐任务分数分布随时间）或任务间能力相关性矩阵。雷达图 fig\_q4\_task\_radar 展示前沿模型六维对比。覆盖须 $\ge1800$ 个可解析目录（能力合同 P4-C4）。

---

## 七、模型检验与灵敏度分析设计

### 7.1 模型检验
- **问题一**：$Q$ 的熵权/CRITIC/PCA 三法交叉一致性（Kendall $\tau$）；扩展集 A2/A3 域级 $Q$ 与抽样集对照（哑铃图）；配比回归 A6–A11 分尺度留出 RMSE/$R^2$、A12–A15 外推残差。
- **问题二**：经典律 B1 拟合 $R^2$、残差正态/零均值检验（残差图）；广义律 B6 留出点 RMSE 对比经典基线（要求不劣）；B2/B3/B4/B5 分层泛化误差。
- **问题三**：最优解重代入预算式核验（容差 $10^{-6}$）；多起点解一致性（变异系数）；KKT 一阶条件残差。
- **问题四**：桥接映射分层残差；贡献占比和 $\approx100\%$ 核验；前沿预测回测（用早期数据预测已知点）。

### 7.2 灵敏度分析
- $Q_0$ 扰动 $\pm20\%$ → 观察 $C_Q$ 激活与 $Q^\ast$、结构转移点变化。
- $g(Q)$ 三型对比 → 高 $Q$ 经济性对最优 $Q^\ast$ 的影响（指数型使高 $Q$ 极昂贵、对数型相对可得）。
- $L_{\rm ctx}$ 按 C7 五取值扫描 → $N^\ast,D^\ast,Q^\ast,L^\ast$ 敏感性 + 临界值验证。
- $\theta$（质量放大指数）扰动 → 弹性 $\varepsilon_Q$ 与替代率变化。
- 算力增速 $r_C$ 三档情景 → 前沿预测带宽变化。

### 7.3 鲁棒性检验
- 质量指标：均值/中位数/截尾均值三种列表压缩对 $Q$ 排序的影响。
- 配比模型：线性 vs LightGBM 对重要性排序一致性。
- 前沿预测：Bootstrap 重采样置信带稳定性。

---

## 八、结果预期与执行合同（Step 5.5，comp-code 严格据此执行）

### ⓪ 参数口径表

| 物理量 | 唯一定义值 | 单位 | 语义标签 | 用于哪些子问题 |
|--------|-----------|------|---------|--------------|
| 注意力系数 $\eta$ | $2\times10^{-4}$ | — | eta | Q3 |
| 注意力临界上下文 | $3\times10^{4}$ | tokens | Lctx_crit | Q3 |
| Chinchilla 系数 | $6$ | — | flops_per_param_token | Q3 |
| 指数型 $g$ 参数 | $\gamma=10^7,\lambda=6.0$ | FLOPs/token | gQ_exp | Q3 |
| 幂型 $g$ 参数 | $\gamma=5\times10^9,\lambda=4.0$ | FLOPs/token | gQ_pow | Q3 |
| 对数型 $g$ 参数 | $\gamma=2\times10^9,\lambda=10.0$ | FLOPs/token | gQ_log | Q3 |
| 三档预算 $C$ | $\{10^{19},10^{22},10^{24}\}$ | FLOPs | budget | Q3 |
| $N,D$ 单位换算 | $\times10^9$ 代入 $6ND$ | params/tokens | unit_scale | Q2,Q3 |
| 不可约损失 $E$ | $\approx1.69$（B1 拟合，最终以代码为准） | nats/token | E_irr | Q2,Q3 |
| $Q$ 定义域 | $(0,1]$ | 无量纲 | Q_domain | Q1,Q2,Q3 |

> 同一物理量全篇唯一定义。$Q$ 有两种口径须区分：问题一的 $Q$ 是 22 指标合成的 observed 派生量；B6–B8 的 $Q\_score$ 是实验 setpoint。二者语义标签分别为 `Q_synth`、`Q_setpoint`，建模时不混用。

### ① 结果约束清单（可机器审计，comp-code 写 constraint_audit.py）

- `all(p_i>=0) and abs(sum(p_i)-1)<=1e-3`（配比单纯形，千分位舍入容差）
- `0 < Q <= 1`（质量定义域）
- `6*N*D + D*max(g(Q)-g(Q0),0) + eta*N*D*Lctx <= C + 1e-6*C`（三部分算力不超预算；$N,D$ 已乘 $10^9$）
- `N > 0 and D > 0`（正性）
- `C_Q == D*max(g(Q)-g(Q0), 0)`（质量成本铰链取正部）
- `abs(Lctx_crit - 6/eta) < 1`（临界值解析恒等，应=3e4）
- `Lctx in {2048,4096,8192,32768,131072}`（敏感性扫描取自 C7 实测集）
- `C 增大 => 最优 L 不增`（预算单调性，跨解验证）
- 广义律：`dL/dQ < 0`（Q↑→Loss↓，物理方向）
- 贡献分解：`abs(scale% + nonscale% - 100) < 1e-6`
- 前沿预测：`Frontier(24m,P50) >= Frontier(12m,P50)`（前沿不倒退）

### ② 预期行为
- **时间尺度**：SLSQP 多起点在秒级收敛（3 变量光滑问题）。
- **稳态特征**：预算增大，最优 $L^\ast$ 单调下降并趋近 $E\approx1.69$；$N^\ast,D^\ast$ 单调增。
- **瞬态/转移**：低预算 $Q^\ast\le Q_0$（$C_Q=0$，纯堆 $N,D$）；中高预算 $Q^\ast$ 上升、$s_Q$ 从 0 抬升，出现结构转移点。
- **单调性**：$\varepsilon_N,\varepsilon_D,\varepsilon_Q$ 均为负；$L_{\rm ctx}$ 增大挤压 $N,D$ 预算使 $L^\ast$ 上升。

### ③ 异常处理预案（每种异常唯一修正法）

- **若 SLSQP 报预算约束越界（解不可行）**：→ 原因：初值离可行域远/尺度悬殊。→ 唯一修正：改用对数变量 $(\ln N,\ln D,Q)$ 并从 Chinchilla 平衡点 $6N D\approx0.9C$ 附近取初值重启。→ 禁止：放宽预算约束 $C$ 或删掉约束。
- **若某档预算 $Q^\ast$ 恒=1（贴边界不合理）**：→ 原因：$g(Q)$ 相对 $B$ 项太廉价。→ 唯一修正：核对 $g(Q)$ 是否用了 `DATA_FACTS.given` 原值（$\gamma,\lambda$ 禁改），确认后如实报告（这是 $g$ 型经济性的真实体现）。→ 禁止：擅自改 $\gamma,\lambda$ 让 $Q$ 离开边界。
- **若广义律 $Q$ 系数方向为正（Q↑→Loss↑）**：→ 原因：拟合陷入局部解或 $\theta$ 初值符号错。→ 唯一修正：约束 $\theta>0$ 重拟合并检查 B6 的 corr$(Q,L)<0$。→ 禁止：保留反向结果不说明。
- **若预算增大而 $L^\ast$ 不降（单调性破）**：→ 原因：多起点未找到全局解。→ 唯一修正：增加起点数至 $\ge20$ 并取全局最优。→ 禁止：手工修改结果凑单调。
- **若配比回归外推 A12–A15 残差发散**：→ 原因：外推超训练配比范围。→ 唯一修正：标注为外推区、报告残差带、不裁剪。→ 禁止：删除外推点凑 $R^2$。

### ④ 方法指定（唯一方法，禁止替代）

- **步骤 Q1-a 列表压缩**：方法=文档级均值（稳健性用截尾均值）；禁止替代：随机取单值/首值。
- **步骤 Q1-b 赋权**：方法=熵权法（式 3），CRITIC/PCA 交叉验证；禁止替代：等权/主观拍权重。
- **步骤 Q1-c 配比回归**：方法=对数域带单纯形约束线性回归 + LightGBM 对照；禁止替代：无约束回归后不投影。
- **步骤 Q2-a 经典律拟合**：方法=对数域 Huber-NLS（`least_squares(loss='huber')`）多起点；禁止替代：普通 OLS 直接拟合原始 Loss。
- **步骤 Q2-b 广义律**：方法=$L=E+AN^{-\alpha}+B(Q^\theta D)^{-\beta}$（式 9），B6–B8 拟合 $\theta$；禁止替代：把 $Q$ 当独立线性项加进去而不保证 $Q=1$ 退化。
- **步骤 Q3 优化**：方法=SLSQP 多起点（对数变量），KKT 解析辅助；禁止替代：网格搜索代替、忽略预算约束。
- **步骤 Q3 转移识别**：方法=$ds_X/d\log C$ 峰值 + KKT 活跃集监控；禁止替代：目视判断。
- **步骤 Q4 桥接**：方法=分层单调 sigmoid/对数回归（式 23）；禁止替代：不分层混合拟合、非单调多项式。
- **步骤 Q4 前沿**：方法=分位回归/Bootstrap 分位带；禁止替代：点预测无区间。

### ⑤ 验证检查点（comp-code pass/fail）

- □ Q1：$Q_i\in(0,1]$ 全部满足；扩展集域级 $Q$ 存在并与抽样集对照 → fail 跳异常预案（重算全量）。
- □ Q1：配比回归各尺度留出 $R^2$ 报告；单纯形约束满足 → fail 跳 softmax 参数化。
- □ Q2：经典律 $R^2>0.9$ 且 $\alpha,\beta\in(0,1)$；广义律 B6 留出 RMSE $\le$ 经典基线 → fail 切 defect_add。
- □ Q2：$\varepsilon_Q<0$、替代率数值已代入参数 → fail 检查 $\theta$ 符号。
- □ Q3：每档预算最优解重代入预算式 $\le C$（容差 $10^{-6}$） → fail 跳预案 1。
- □ Q3：$L_{\rm ctx}^{\rm crit}=3\times10^4$ 解析核验；扫描取值 $\subseteq$ C7 集 → fail 修正取值。
- □ Q3：预算单调性 $C$↑→$L^\ast$↓ → fail 增起点。
- □ Q4：贡献占比和 $=100\%$；前沿 24m$\ge$12m → fail 检查回归/外推。
- □ Q4：C8 聚合覆盖 $\ge1800$ 目录，字段来自 detailed_results JSON → fail 重跑摄入。
- □ 最终：所有输出量均在①约束清单范围内。

### ⑥ 结构性验证输入（问题三优化，供 comp-code 层级 5）

**约束活跃性预期**：
- 预算约束：预期**活跃**（取等号），理由：增大任一因素均降损失，最优处必用尽预算。
- $Q\le1$ 边界：中高预算档预期活跃（$Q^\ast\to1$），低预算档不活跃（内点）。
- $Q>0$：不活跃（$Q^\ast$ 远离 0）。

**决策变量合理范围与预期行为**：

| 变量 | 物理含义 | bounds | 预期取值区间 | 若取到边界说明 |
|------|---------|--------|-------------|------------------|
| $N$ | 参数量($10^9$) | $[10^{-3},10^{5}]$ | 随 $C$ 增从 $\sim0.1$ 到 $\sim10^3$ | 取上界=算力主投参数 |
| $D$ | token数($10^9$) | $[10^{-2},10^{6}]$ | 随 $C$ 增单调升 | — |
| $Q$ | 质量 | $(0,1]$ | 低预算$\le Q_0$，高预算$\to1$ | 取上界1=质量投入饱和 |

**灵敏度方向表**：

| 决策变量 | 增大时 $L$ 方向 | 预期灵敏度量级 | 若方向相反说明 |
|----------|-------------------|---------------|------------------|
| $N$ | ↓（主导项之一） | 高 | 目标符号写反 |
| $D$ | ↓ | 高 | 同上 |
| $Q$ | ↓（经 $Q^\theta$ 放大 $D$） | 中（$\theta\varepsilon_D$） | $\theta$ 符号错 |

**稳定性预期**：问题非凸（$Q^\theta D$ 乘积项 + 铰链 $[\cdot]_+$），预期少数局部最优；多起点后结果应稳定，可接受变异系数 $<5\%$。

**资源利用率预期**：预算利用率预期 $\approx100\%$（约束活跃），若某档 $<95\%$ 说明未收敛到边界须增起点。$C_Q$ 份额：低预算 $\approx0\%$、高预算可达 $10\%$–$40\%$（依 $g$ 型），若恒为 0 须查 $Q_0$ 假设。

### ⑦ 方法声称清单（METHOD_CLAIMS，编译阶段实现对账）

| 编号 | 正文将声称的方法 | 代码里必须真实现的特征（可核查） |
|------|---------------------|-------------------------------|
| M1 | 熵权法客观赋权合成 $Q$（全量 A1 51230 条） | 真按式(3)算信息熵 $e_j$ 与权重 $w_j$，读全量 A1（非抽样），列表型先压缩标量 |
| M2 | 带单纯形约束的配比–Loss 回归（RegMix 风格） | 拟合分域系数 + 预测/寻优时满足 $\sum p_i=1,p_i\ge0$（softmax 或投影），非无约束回归 |
| M3 | 对数域 Huber 非线性最小二乘拟合经典标度律 | 真调 `least_squares(loss='huber')` 或等价，在 $\ln L$ 域拟合 $E,A,\alpha,B,\beta$，非普通 OLS |
| M4 | 广义标度律 $L=E+AN^{-\alpha}+B(Q^\theta D)^{-\beta}$，B6–B8 估 $\theta$ | 代码含 $Q^\theta D$ 有效数据结构 + 用含 Q_score 的 B6-B8 拟合 $\theta$，$Q=1$ 退化经典 |
| M5 | KKT + SLSQP 多起点约束优化 | 真调 `minimize(method='SLSQP')` 且预算约束进 constraints，多起点循环，非网格枚举 |
| M6 | 结构性转移份额导数/活跃集判据 | 真算 $s_X(C)$ 并数值差分 $ds_X/d\log C$ 峰值 + 监控 $Q$ 内点/边界切换 |
| M7 | 分层单调 Loss–Benchmark 桥接 | 按 Loss_Comparability 分层拟合单调映射(sigmoid/对数)，非混合非单调 |
| M8 | 分位回归/Bootstrap 前沿分位带 | 真产出 P10/P50/P90 三条带，非点预测加噪声 |
| M9 | C8 逐任务聚合（≥1800 目录） | 真遍历 detailed_results/ JSON 逐任务字段，非只读 C1 汇总列 |

<!-- METHOD_CLAIMS_MACHINE
M1 | must: entropy, ln\(|log\(, weight | forbid: equal_weight, np\.ones.*/.*22
M2 | must: softmax|simplex|projection|sum.*p.*==.*1|LinearConstraint | forbid: 
M3 | must: least_squares|curve_fit|huber, log|ln | forbid: LinearRegression\(\)\.fit
M4 | must: \*\*theta|Q\*\*|power\(Q|Q_eff|Qeff | forbid: 
M5 | must: SLSQP|minimize, constraints|NonlinearConstraint | forbid: itertools\.product.*grid_only
M6 | must: gradient|diff|d.*logC|share|s_X | forbid: 
M7 | must: sigmoid|expit|logistic|log, Comparability | forbid: 
M8 | must: quantile|bootstrap|percentile|P10|P90 | forbid: 
M9 | must: detailed_results, json\.load|glob|listdir | forbid: 
-->

### ⑧ 逻辑合同（LOGIC_CONTRACT_MACHINE，下游 logic_audit.py 机器核）

```json
{"LOGIC_CONTRACT_MACHINE":{
  "bounds":[],
  "no_double_count":[{"aggregate":"C_tot","contains":"C_Q"}],
  "must_features":["N_params_B","D_tokens_B","Q_score","p_17_domains","22_quality_indicators","6d_benchmark"],
  "train_range":{"N":[0.07,12],"D":[0.134,300],"Q_score":[0.1,1.0],"val_loss":[1.8,7.3]},
  "monotonic":[{"more":"C_budget","then":"L_optimal","dir":"better"},{"more":"N","then":"L","dir":"better"},{"more":"D","then":"L","dir":"better"},{"more":"Q","then":"L","dir":"better"},{"more":"Lctx","then":"L_optimal","dir":"worse"}],
  "constraints_with_margin":[{"quantity":"C_tot","limit":1e19,"kind":"le","min_margin":0.0},{"quantity":"C_tot","limit":1e22,"kind":"le","min_margin":0.0},{"quantity":"C_tot","limit":1e24,"kind":"le","min_margin":0.0}],
  "calibration_anchors":[],
  "equivalence_claims":[{"claim":"Q=1时广义律退化为经典标度律","quantity_a":"L_generalized_Q1","quantity_b":"L_classic","rel_tol":0.001,"explanation":""}]
}}
```

> 说明：`bounds` 为空——本题无"反解/取界得上下界"型量（$N,D,Q,L$ 均为正向观测或决策，无删失/封顶反算）。`no_double_count`：总算力 $C_{\rm tot}$ 已含 $C_Q$，代码不得在预算外再另计质量成本。`monotonic`：预算增大最优 Loss 不增、各因素增大 Loss 降、$L_{\rm ctx}$ 增大挤压预算使最优 Loss 升。`equivalence_claims`：$Q=1$ 退化必须数值吻合（rel\_tol=0.001），这是式 (9) 的硬性检验。`train_range` 抄 `DATA_FACTS.json` 实测区间，外推（$N>12,D>300$，如 B9/B10、前沿预测）须标"情景模拟/需现场标定"。

### ⑨ 跨问结论登记（CROSS_PROBLEM_LEDGER）

```json
{"problems":[
  {"id":"Q1","conclusions":[
     {"quantity":"domain_Q_median","value":null,"kind":"bound",
      "imposes":{"on":["Q3"],"note":"Q1 域级 Q 中位数作为 Q3 的基线质量 Q0，须传递一致"}},
     {"quantity":"mixture_domain_importance","value":null,"kind":"bound",
      "imposes":{"on":["Q2"],"note":"配比域重要性用于 Q2 广义律 phi(p) 的域贡献权重"}}]},
  {"id":"Q2","conclusions":[
     {"quantity":"E,A,alpha,B,beta,theta","value":null,"kind":"bound",
      "imposes":{"on":["Q3","Q4"],"note":"广义律参数是 Q3 目标函数与 Q4 桥接/前沿的输入，须同一套参数"}}],
   "observed":{"domain_Q_median":null}},
  {"id":"Q3","conclusions":[
     {"quantity":"L_optimal_per_budget","value":null,"kind":"bound",
      "imposes":{"on":["Q4"],"note":"Q3 最优 Loss 可经 Q4 桥接翻译为 Benchmark 能力，须口径一致"}}],
   "observed":{"E_A_alpha_B_beta_theta":null}},
  {"id":"Q4","observed":{"scaling_params":null,"L_optimal":null}}
]}
```

> 上游结论显式约束下游：Q1 的 $Q_0$ 与配比重要性 → Q2/Q3；Q2 的标度律参数 → Q3/Q4。comp-code 须把实际取到的值填入 `observed`，`value:null` 处待运行填充。

### ⑩ 假设问责表（role=assumed / setpoint 参数）

| 假设参数 | (a) 为何无数据只能假设 | (b) 取值依据 | (c) 灵敏度 | (d) 假设若错结论是否成立 |
|---|---|---|---|---|
| $Q_0$ 基线质量 | 题面未给具体值，仅给 $[\cdot]_+$ 起算点 | Q1 抽样集域级 $Q$ 中位数（数据驱动，中性） | $\pm20\%$ 影响 $C_Q$ 激活门槛与转移点位置，**中等敏感**，须标注结构转移点依赖 $Q_0$ | $Q_0$ 若偏高使低预算档 $C_Q=0$——结论"低预算不投质量"仍定性成立 |
| $\theta$ 质量放大指数 | 仅 B6–B8 半合成数据可估，非大规模真实 | B6–B8 拟合 + $Q$↑→Loss↓ 方向约束 | 影响 $\varepsilon_Q$ 与替代率数值，**高敏感**，替代率结论强依赖 $\theta$，标注为半合成估计 | $\theta$ 若偏差大则替代率数值变，但"质量可替代规模"定性结论成立 |
| $r_C$ 算力增速 | 未来增速题面未给，属情景假设 | 低/中/高三档（0/50/100%历史增速） | 直接决定前沿带宽，**高敏感**，故用分位带而非点预测，显式声明情景 | 前沿预测本就是情景模拟，非数据直接支持，已如实标注 |
| $Q_0$ 之外 $g(Q)$ 型 | 三型均题面给定，非假设 | `DATA_FACTS.given` 原值禁改 | 三型对比即敏感性 | — |

> **软肋标红**：$\theta$ 与 $r_C$ 为高敏感假设——正文须明写"替代率数值与前沿预测强依赖半合成/情景假设，非大规模真实数据直接支持"，禁用"确定"口吻。

### ⑪ 目标/约束原文溯源

| 建模对象 | 数学表达 | 对应题目原句/对齐表行 |
|---|---|---|
| Q3 目标函数 | $\min_{N,D,Q} L(N,D,Q,\mathbf p)$ | "使模型能力最优（Loss 最小）"（S4/S15，对齐表 L 定义行） |
| Q3 预算约束 | $6ND+C_Q+C_{\rm attn}\le C$ | "总成本不超过 $C$"（S15，对齐表"总成本"行） |
| Q3 三部分算力 | $C_{\rm train}=6ND,\ C_Q=D[g(Q)-g(Q_0)]_+,\ C_{\rm attn}=\eta NDL_{\rm ctx}$ | S14（对齐表 $C_Q$、$C_{\rm attn}$ 行，$g(Q)$ 每 token 须乘 $D$、$\eta$ 作用于三者乘积） |
| Q3 临界值 | $L_{\rm ctx}^{\rm crit}=6/\eta=3\times10^4$ | S17（对齐表临界值行） |
| Q3 $L_{\rm ctx}$ 外生 | 参数扫描非决策变量 | S17"外生给定…不作内点寻优变量" |
| Q2 广义律 | $L=E+AN^{-\alpha}+B(Q^\theta D)^{-\beta}$ | S12"含 $N,D,Q,\mathbf p$ 的广义标度律…$Q=1$ 退化" |
| Q2 弹性/替代 | $\varepsilon_X=\partial\ln L/\partial\ln X$，$dN/dQ|_L$ | S13"边际效用与弹性…质量与规模相互替代条件" |
| Q1 综合评价 | 熵权合成 $Q=\sum w_j r_j$ | S6/S7"方向统一…综合评价模型给出 $Q$" |
| Q1 配比关系 | $\ln\hat L_k=a_k+\sum b_{ki}p_i$ s.t. 单纯形 | S9"$\mathbf p$ 与 Loss 定量关系…单纯形约束" |
| Q4 贡献分解 | $\mathrm{Cap}=f(N,D,C)+h(t)$，占比和100% | S19"分离规模与非规模技术进步贡献占比" |
| Q4 桥接 | 分层单调 sigmoid $\widehat{\mathrm{Cap}}(L)$ | S20"Loss–Benchmark 映射…按可比性分层" |
| Q4 前沿 | 分位带 $[\hat F_{10},\hat F_{90}]$ | S21"预测能力前沿…不确定性分析" |

> 优化方向（min Loss）、约束不等号方向（$\le C$）、优化对象（$N,D,Q$ 非 $L_{\rm ctx}$）均与原句一致，无脑补组件。

---

## 九、赛题分析升级结论审视（承接 PROBLEM_ANALYSIS 第八章）

对赛题分析"经典问题升级判定表"逐条审视，全部采用最终模型（无跳过、无无声忽略）：

| 初步映射 | 升级触发句 | 最终模型 | 本报告采用情况 |
|---|---|---|---|
| 单指标打分 | S6/S7 全量+方向统一+列表压缩 | 22 维方向统一 + 熵权综合评价 | ✅ 采用（式 1–4，全量 A1） |
| 普通回归 | S9 单纯形+多尺度+外推 | 带单纯形约束回归 + 多尺度验证 | ✅ 采用（式 6，A6–A15 验证） |
| 经典标度律 | S12 纳入 $Q,\mathbf p$ | 广义标度律（$Q$ 增强有效数据） | ✅ 采用（式 9，$Q=1$ 退化） |
| 无约束优化 | S14/S15 三部分算力$\le C$ | 带非线性预算约束优化 | ✅ 采用（式 14–15，约束进求解器） |
| 静态最优 | S16 预算跨量级结构转移 | 预算扫描 + 份额导数/活跃集识别 | ✅ 采用（式 18，连续扫描） |
| 点预测 | S21 不确定性分析 | 分位带/Bootstrap 区间预测 | ✅ 采用（式 24，P10/P50/P90） |
| 纯相关归因 | S19 分离规模 vs 非规模 | 控制规模的贡献分解 | ✅ 采用（式 21–22，占比和100%） |

**缺参数处理（不以"题面未给"为由跳过升级）**：$Q_0$ 用 Q1 域级 $Q$ 中位数并灵敏度扰动（假设 5）；$r_C$ 设三档情景（假设 6 相关）；$g(Q)$ 三型参数题面已给直接代入。所有升级均保留核心机制，无以简化为名去掉升级。

---

## 十、编程实现要点（comp-code 阶段执行指引）

### 10.1 数据摄入（全量，不抽样）
- A1/A2/A3：`lzma` 解压 jsonl.xz，逐行解析，8 列表型字段先压缩标量。A1 全量 51230 条、A2 17523、A3 203752 条（能力合同红线，不抽样）。
- A4–A15：`pandas` 读 `regmix_tables/*.csv`，按 index 对齐 mixture 与 pile_loss。
- B1–B10：`pandas` 读 `B_scaling_laws/*.csv`，B6–B8 取 Q_score 列。
- C1/C3/C4/C6/C7：`pandas` 读 csv。C8：`glob` 遍历 `detailed_results/*/` 逐任务 JSON，`try/except` 跳过 4 个损坏文件并计数，覆盖 $\ge1800$ 目录。

### 10.2 关键库与算法
- 综合评价：`numpy` 实现熵权/CRITIC，`sklearn.decomposition.PCA` 交叉验证。
- 配比回归：`scipy.optimize`（单纯形约束 softmax 参数化）+ `lightgbm` 对照。
- 标度律拟合：`scipy.optimize.least_squares(loss='huber')`，对数域，多起点。
- 优化：`scipy.optimize.minimize(method='SLSQP')`，对数变量 $(\ln N,\ln D,Q)$，$\ge8$ 起点，`NonlinearConstraint` 装预算式。
- 桥接：`scipy.optimize.curve_fit` 拟合 sigmoid，分层。
- 前沿：`sklearn` 分位回归 或 `numpy` Bootstrap 分位。

### 10.3 输出产物（能力合同 required_output）
- `output/q1_quality_scores.csv`（P1-C1/C2，覆盖 A1 全量 + 扩展集域级 Q）
- `output/q1_mixture_model.json`（P1-C4）
- `output/q2_classic_scaling.json`（P2-C1）+ 广义律参数
- `output/q3_optimal_allocation.json`（P3-C1，三档预算 $N^\ast,D^\ast,Q^\ast,L^\ast$ + 份额）
- `output/q3_lctx_sensitivity.json`（P3-C3，含 $L_{\rm ctx}^{\rm crit}$ 核验）
- `output/q4_bridge_model.json`（P4-C2）
- `output/q4_task_aggregation.csv`（P4-C4，$\ge1800$ 目录）
- `figures/all_results.json`（汇总，供 logic_audit/cross_problem_check）
- 每个最优解写入前调用 `constraint_audit.py`，`audit_fail` 时禁止写稿。

### 10.4 随机性与可复现
- 固定 `seed=42`（Bootstrap、多起点随机初值、LightGBM）；记录运行元信息（库版本、seed）到结果 JSON。

---

## 十一、图表预规划（承接 PROBLEM_ANALYSIS 第九章，paper-figure 读此清单）

<!-- BEGIN FIGURE_MANIFEST -->
### 数据图（matplotlib gen_fig_*.py，paper-figure 产出 .png/.pdf）
- fig_q1_quality_corr — 聚类热力图 (advanced #14) — 22 质量指标(A1全量)相关矩阵+树状图 — 数据源: A1 — 章节: 问题一质量评价
- fig_q1_conflict_scatter — 散点+KDE 边际密度 (basic #4) — fineweb_edu vs ad_en 冲突区 — 数据源: A1 — 章节: 问题一冲突消解
- fig_q1_domain_Q_dumbbell — 哑铃图 (advanced #2) — 抽样集vs扩展集域级Q对照 — 数据源: A1/A2/A3 — 章节: 问题一质量评价
- fig_q1_mixture_importance — 棒棒糖图 (advanced #1) — 17域配比对Loss重要性排序 — 数据源: A4/A5 — 章节: 问题一配比建模
- fig_q2_scaling_fit — 预测vs实际+残差 [2-panel] (competition #4) — 经典标度律拟合优度 — 数据源: B1 — 章节: 问题二经典律拟合
- fig_q2_generalized_surface — 3D曲面图 (competition #6) — 广义律L(N,Q)曲面 — 数据源: B6-B8 — 章节: 问题二广义标度律
- fig_q2_elasticity_diverging — 发散柱状图 (advanced #20) — 各因素弹性ε_N/ε_D/ε_Q — 数据源: Q2拟合 — 章节: 问题二弹性分析
- fig_q2_substitution_contour — 等高线图 (competition #14) — 等损失线Q-N替代关系 — 数据源: Q2拟合 — 章节: 问题二替代条件
- fig_q3_allocation_stacked — 堆叠柱状图 (basic #2) — 三档预算算力份额C_train/C_Q/C_attn — 数据源: Q3优化 — 章节: 问题三最优配置
- fig_q3_transition_line — 折线图+CI (basic #3) — 最优份额随logC变化+结构转移点 — 数据源: Q3优化 — 章节: 问题三结构转移
- fig_q3_lctx_panels — 多面板子图 [4-panel] (basic #12) — 最优N*/D*/Q*/L*随L_ctx变化+临界值 — 数据源: Q3优化/C7 — 章节: 问题三敏感性
- fig_q4_contribution_decomp — 方差分解堆叠面积图 (empirical #20) — 规模vs非规模贡献占比随时间 — 数据源: C1/C4 — 章节: 问题四贡献分解
- fig_q4_bridge_scatter — 散点+回归+边际密度 (competition #26) — Loss→Benchmark桥接分层 — 数据源: C6 — 章节: 问题四桥接
- fig_q4_frontier_fan — 预测扇形图 (advanced #27) — 能力前沿12/24月P10/P50/P90分位带 — 数据源: C1/C3 — 章节: 问题四前沿预测
- fig_q4_task_radar — 雷达图 (competition #5) — C8逐任务六维Benchmark前沿对比 — 数据源: C8 — 章节: 问题四逐任务聚合

### DrawIO 流程/架构图
- fig_roadmap — 技术路线图 — 四问递进求解主线与数据流向 — 章节: 问题重述
- fig_pipeline_q1 — 数据处理Pipeline — Q1质量评价多阶段流程 — 章节: 问题一数据预处理
- fig_index_hierarchy — 指标体系层次图 — 22指标→质量维度→综合评分Q — 章节: 问题一模型构建

### TikZ 图
- tikz_q3_feasible — 算力预算可行域图 — (N,D,Q)空间约束面/等成本线/最优点/转移分区 — 章节: 问题三模型求解

**总数：DATA=15, DRAWIO=3, TIKZ=1, GPTIMG=0, ALL=19**
<!-- END FIGURE_MANIFEST -->

> 图表多样性：无任何类型超过 2 次。建模阶段新增确认：fig_q3_transition_line 须叠加结构转移点标注、fig_q2_generalized_surface 须画 $Q=1$ 退化对照线以佐证等价声称。

