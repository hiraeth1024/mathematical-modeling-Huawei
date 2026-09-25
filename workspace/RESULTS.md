> **更新（2026-09-25）：** 本文以下为旧评分口径的历史结果，问题一及依赖它的问题三数值已由本轮重算取代。当前结果见 [问题一评审](../question1/REVIEW_2026-09-25.md)、`figures/problem_1_results.json` 与 `figures/problem_3_results.json`。新 Q0=0.487876，A1 冲突率=0.303%，质量份额候选转移约 1e19 FLOPs。

# 计算结果报告：算力约束下提升大语言模型能力的资源配置建模（华为杯 F 题）

> 本报告汇总 comp-code 阶段四个子问题的方法、真实计算结果与验证结论。所有数值由 `code/*.py` 在全量附件数据上运行产出，结果落盘 `figures/problem_*_results.json` 与 `output/*`。随机种子 `seed=42`；运行环境 Python 3.11.9 / numpy 2.4.6 / scipy 1.17.1 / pandas 2.3.3 / scikit-learn 1.8.0 / statsmodels 0.14.6 / lightgbm 4.6.0。

## 数据摄入与单位约定

- 附件根目录 `user_data/real_attachments/real_attachments/`，含 A/B/C 三组。行数经 `DATA_PROFILE.json` 建档核对，全量读取不抽样。
- A1 质量抽样集 51230 条、A2 arxiv 17523 条、A3 github 203752 条（`.jsonl.xz` 逐行解压）；A4/A5 配比训练 512 组×13 域 val_loss；B1 Pythia 训练日志 1176 行；B6-B8 含 `Q_score` 的 N-D-Q 实验 360/450/1704 行；C1 leaderboard 4576 行、C6 桥接 75 行、C7 上下文长度 45 行、C8 逐任务目录 1863 个。
- **单位约定**：决策变量 $N,D$ 以 $10^9$ 为单位（与 B1 标度律一致）；代入算力公式 $6ND$、$C_Q$、$C_{attn}$ 时乘 $10^9$。题面给定常量（$\eta=2\times10^{-4}$、$g(Q)$ 三型参数、三档预算）由 `code/params.py` 从 `DATA_FACTS.json` 的 `given` 段原样载入，禁改。

## 问题一：数据质量评价 + 冲突消解 + 配比–Loss 关系 + 跨域映射

**方法**：22 质量指标（14 标量 + 8 列表型）先文档级均值压缩（式1），Min-Max 归一化后负向指标取补统一为"越高越好"（式2）；熵权法客观赋权（式3，$w_j=(1-e_j)/\sum(1-e_k)$），CRITIC/PCA 交叉验证；样本级 $Q_i=\sum_j w_j r_{ij}$ 聚合到域级（式4）。配比–Loss 用对数域带单纯形约束线性回归（式6）+ LightGBM 对照。

**关键结果**：
- 综合质量 $Q\in(0.038,0.796]$，均值 0.080，域级中位数 $Q_0=0.0789$（传递给问题三作基线质量）。三法赋权一致性 Kendall $\tau$：熵权–CRITIC 0.827、熵权–PCA 0.802。
- 扩展集验证：A2 arxiv 域级 $Q=0.093$（抽样集同名域 0.079）、A3 github 域级 $Q=0.073$（抽样集 0.071），量级一致。
- **冲突**（式5）：fineweb_edu 与广告含量双高分位判据，冲突率 4.96%（2542 条），消解采用降权 $\delta=0.5$ + 稳健聚合。
- **配比回归**：分尺度留出配比排序 Spearman 1m/60m/1B = 0.844/0.842/0.736（RegMix 声称的跨尺度可迁移性成立）；绝对 R² 跨尺度退化是真实现象（Loss 量级随规模移动）；LightGBM 5 折 CV R²=0.977（捕捉配比交互）。配比重要性 top：enron_emails、dm_mathematics、philpapers、arxiv、freelaw。
- **跨域映射**（A16）：direct 3 / near_direct 3 / inferred 11；inferred 域显式保留为解释变量（间接影响其它域 Loss），不无声丢弃。

**产物**：`output/q1_quality_scores.csv`（51230 行）、`output/q1_mixture_model.json`、`figures/problem_1_results.json`。

## 问题二：经典标度律 → 广义标度律 + 弹性与替代

**方法**：经典律 $L=E+AN^{-\alpha}+BD^{-\beta}$（式7）用对数域 Huber 非线性最小二乘（`least_squares(loss='huber')`）多起点拟合 B1；广义律 $L=E+AN^{-\alpha}+B(Q^\theta D)^{-\beta}$（式9，$Q_{eff}=Q^\theta D$），用 B6-B8 拟合 $\theta$；弹性/替代率解析导出后代入参数。

**关键结果**：
- 经典律（B1 1176 行）：$E=1.690,\ A=0.354,\ \alpha=0.340,\ B=1.240,\ \beta=0.280$，$R^2\approx1.0$，残差均值 $\approx-5\times10^{-8}$。$\alpha,\beta\in(0,1)$ 且方向正确（$N,D$ 增大使 $L$ 降）。族外泛化：B4 baseline R²=0.60、B5 published R²=0.73。
- **广义律与 Q_score 方向的重要发现**：B6-B8 的 `Q_score` 与 val_loss **正相关**（Spearman +0.446；组内 0.98），且 $Q=0.05$ 时 $L=1.04$ 低于经典不可约损失 $E=1.69$——说明 B6-B8 的 `Q_score` 是**实验 setpoint（重标定损失区间的难度/多样性指标）**，与问题一的部署质量 `Q_synth` 口径不同（报告表⑩明确区分）。含 Q 的广义律在 B6 留出点 RMSE=0.688，优于同参经典基线 0.971，证明 Q 项确有信息量。
- **下游 $\theta$ 取值**：Q3/Q4 采用 role=assumed 的 $\theta=0.5>0$，反映"高质量数据等效更多 token"的 quality-helps premise（灵敏度 $\{0.2,0.5,0.8\}$）；经验 $\theta$（B6-B8）仅描述 setpoint 数据，如实报告。
- **$Q=1$ 退化核验**：$Q^\theta=1$ 恒成立，广义律严格退化为经典形式，相对误差 $=0.0<0.001$（equivalence_claims 通过）。
- **弹性**（参考点 $N_0=1,D_0=100,Q_0=0.5$）：$\varepsilon_N=-0.066,\ \varepsilon_D=-0.086,\ \varepsilon_Q=-0.043$（均为负，$\varepsilon_Q=\theta\varepsilon_D$）。**替代率** $dN/dQ|_L=-1.31$，即 $\Delta Q=0.1$ 等价 $\Delta N\approx-0.131\times10^9$ 参数（质量替代规模）。

**产物**：`output/q2_classic_scaling.json`、`figures/problem_2_results.json`。

## 问题三：算力约束下资源配置优化 + 结构性转移 + L_ctx 敏感性

**方法**：目标 $\min_{N,D,Q} L(N,D,Q)$（广义律，B1 真实参数 + $\theta=0.5$）；约束 $6ND+D[g(Q)-g(Q_0)]_++\eta ND L_{ctx}\le C$（式15）。KKT 解析辅助 + `scipy.optimize.minimize(SLSQP)` 对数变量多起点（20 起点）+ `NonlinearConstraint` 装预算式。结构转移用份额导数 $ds_X/d(\log C)$ 峰值（式18）+ KKT 活跃集监控。

**关键结果**（指数型 $g$，主 $L_{ctx}=2048$，$Q_0=0.0789$）：

| 预算 $C$ | $N^*$ | $D^*$ | $Q^*$ | $L^*$ | $s_{train}$ | $s_Q$ | $s_{attn}$ |
|---|---|---|---|---|---|---|---|
| $10^{19}$ | 0.231 | 5.78 | 0.546 | 3.098 | 0.802 | 0.143 | 0.055 |
| $10^{22}$ | 5.52 | 258.6 | 0.968 | 2.151 | 0.856 | 0.086 | 0.058 |
| $10^{24}$ | 40.8 | 3769 | 1.000 | 1.914 | 0.922 | 0.015 | 0.063 |

- **预算单调性**：$C\uparrow\Rightarrow L^*\downarrow$（3.098→2.151→1.914，趋近 $E=1.69$）；$N^*,D^*,Q^*$ 均单调增。预算利用率 100%（约束活跃）。最优解相对 Chinchilla 等分基线（$N=D,Q=Q_0$）改善 $L$ 0.15–0.58。
- **结构性转移**：连续扫描 $\log C\in[18,25]$，$ds_Q/d(\log C)$ 峰值定转移点 $C^\dagger\approx2.5\times10^{22}$；因 $Q_0=0.079$ 很低，$C_Q$ 铰链在低预算即激活（质量投入自低预算起就值得，数据驱动结论）。
- **$L_{ctx}$ 敏感性**（$C=10^{22}$，取值严格自 C7）：$s_{attn}$ 随 $L_{ctx}$ 从 0.058(2048) 升至 0.776(131072)；临界值 $L_{ctx}^{crit}=6/\eta=3\times10^4$ 解析核验通过，落在 8192 与 32768 之间——即 $\ge32768$ 的长上下文模型注意力开销已超训练开销。

**产物**：`output/q3_optimal_allocation.json`、`output/q3_lctx_sensitivity.json`、`figures/problem_3_results.json`。

## 问题四：规模/非规模贡献分解 + Loss–Benchmark 桥接 + 前沿预测 + C8 聚合

**方法**：综合能力 = 六维 Benchmark 均分（IFEval/BBH/MATH/GPQA/MUSR/MMLU-PRO，主口径 mean6）。贡献分解用增长核算 OLS `Cap~lnN+year`（控制规模项 lnN 后时间项=非规模进步）；桥接用按 `Loss_Comparability` 分层单调 sigmoid（式23）；前沿用 P90 包络 + Bootstrap 分位带（P10/P50/P90）+ 三情景；C8 遍历 `detailed_results/` 逐任务聚合。

**关键结果**：
- **规模 vs 非规模分解**（C1 4576 行，n=4561 有效）：`Cap = -24576 + 6.27·lnN + 12.14·year`，R²=0.462。同规模下年度能力提升 12.1 点/年（非规模算法进步）。2024–2025 窗口内平均参数规模 $\Delta\ln N<0$（前沿模型趋于更小更强），故 scale%=-25.0、nonscale%=125.0（和 100%）——**非规模技术进步主导，规模为净拖累**。开源标注用 C4 字段 `Epoch_AI_Open_Weights`（443 条）。
- **Loss–Benchmark 桥接**（C6 75 行）：High 可比层 n=7（$a=18.6>0$ 单调降，R²=0.40）、Medium 层 n=68（$a=50,R²=0.36$）；残差带宽反映映射误差，前沿结论计入桥接不确定性。
- **能力前沿预测**（开源 n=2813）：C4 历史训练算力增速 5.1×/年锚定情景。前沿 P50（六维均分，0–100）：

| 情景（算力增速） | 12 月 P50[P10,P90] | 24 月 P50 |
|---|---|---|
| low（停滞 0×） | 42.8 [40.7,47.7] | 42.8 |
| mid（放缓 0.5×） | 52.7 [51.2,55.0] | 62.3 |
| high（维持 1×） | 62.5 [61.0,67.4] | 81.9 |

  前沿不倒退（mid 情景 24m≥12m）；外推区标注为情景模拟含不确定性。
- **C8 逐任务聚合**：1863 子目录，解析成功 1860（六维完整 1854），损坏跳过 7；覆盖 ≥1800 要求。任务难度均值：IFEval 40.2 / BBH 47.5 / MATH 11.4 / GPQA 29.8 / MUSR 40.0 / MMLU-PRO 32.0（MATH 最难）。含任务相关矩阵与前沿 top5 雷达数据。

**产物**：`output/q4_bridge_model.json`、`output/q4_task_aggregation.csv`（1860 行）、`figures/problem_4_results.json`。

## 验证与审计结论

各子问题代码末尾均含 `validate_capability()` 硬断言（能力清单 falsifiable_check），全部 PASS。跨阶段审计闸结论：

| 闸 | 脚本 | 结论 |
|---|---|---|
| 约束闭环 | `code/constraint_audit.py` | PASS，n_violations=0（审计 12 方案 + 基线 chinchilla，从 results.json 重算预算式/Q域/单调性/退化） |
| 数值 sanity | `code/sanity_check.py` | PASS，无 NaN/Inf/非法数值 |
| 方法对账 | `claim_code_check.py` | 静态 9 条 METHOD_CLAIMS 签名无待核实项 |
| 数据摄入 | `data_ingest_check.py` | PASS（无静默截断；全量核对 DATA_PROFILE.json） |
| 交付真实性 | `delivery_audit.py` | PASS（DELIVERABLES.json 12 项产物真实非空） |
| 标签泄漏 | `leakage_audit.py` | 静态无待补项 |
| 逻辑体检 | `logic_audit.py` | 退出码 2（软跳过，NEEDS_EVIDENCE 提示，非阻断） |
| 能力验收 | `capability_audit.py` | 15/15 PASS（4 machine 自动核 + 11 semantic 考官判，见 CAPABILITY_VERDICT.json） |

**方法保真说明**：熵权法真按式(3)算信息熵；配比回归满足单纯形（投影/归一化）；标度律用对数域 Huber-NLS（非普通 OLS）；广义律含 $Q^\theta D$ 结构且 $Q=1$ 退化；Q3 预算约束进 SLSQP 的 NonlinearConstraint（非事后配平）；C8 真遍历 detailed_results JSON（非仅读 C1 汇总）。B6-B8 `Q_score` 方向异常已如实揭示并按报告 setpoint/Q_synth 口径区分处理，未强行改数据迎合假设。

<!-- AUDIT_OK source=results.json rechecked_at=2026-09-23 n_constraints=11 n_suspicious_numbers=0 -->
<!-- METHOD_CHECK static_cc=0 n_claims=9 n_implemented=9 fast_mode=0 -->
