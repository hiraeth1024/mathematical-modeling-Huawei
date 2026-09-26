# 华为杯 F 题项目状态文档

> 生成日期：2026-09-26 · 最后更新：2026-09-26 · 分支：`main`（含未提交的正文扩充与排版变更）

---

## 一、项目概述

本项目是 **2026 华为杯全国研究生数学建模竞赛 F 题「算力约束下提升大语言模型能力的资源配置建模」** 的完整建模工作区，以自动化竞赛工作流（`comp_huawei` 模板，工作流 id `3721546c023d`，状态 `completed`）从赛题分析、建模、编程、图表、论文编写到改进循环全程生成。

**核心问题**：在总算力预算 `C` 有限时，如何在参数量 `N`、训练数据量 `D`、数据质量 `Q`、领域配比 `p` 与上下文长度 `L_ctx` 之间取舍，以最小化验证集交叉熵损失并预测真实基准能力前沿。

**四问递进结构**：

| 问题 | 任务 | 核心方法 | 关键结果 |
|---|---|---|---|
| 一 | 数据质量评价 + 冲突消解 + 配比–Loss 关系 | 22 指标语义解码 → A1 经验分位 → 三组平衡赋权；分域 Loss 配比回归 | `Q0=0.487876`，冲突率 0.303% |
| 二 | 经典标度律 → 广义标度律 + 弹性与替代 | Huber 多起点非线性最小二乘；`Q^θ·D` 有效数据量 | 广义律含质量 RMSE=0.675 优于基线 |
| 三 | 算力约束下资源配置优化 + 结构性转移 | KKT 解析 + 预算消元 + SLSQP 交叉验证 | 三档预算下 `N/D/Q` 最优配置 |
| 四 | 贡献分解 + Loss–Benchmark 桥接 + 前沿预测 | 增长核算 OLS + 分层单调 sigmoid + Bootstrap 分位带 | 年份项占回归增量约 125%（描述性分解，非因果贡献） |

**最新动态（2026-09-25~26）**：
- 问题一质量评分全线重构：修正分类 logits 语义误读、改用 A1 经验分位参照、三组平衡赋权，A1/A2/A3 全量重算。
- 问题二/三/四代码评审与数值迭代收尾：数值校验与约束审计通过。
- 论文完成专项排版优化：逐页定位 `[H]` 强制浮动、章节浮动屏障与 `\clearpage` 导致的空白，改为受控浮动并优化目录、参考文献和附录衔接；最终由 **42 页压缩为 35 页**，未删减模型内容、数据或图表。
- 在上述 35 页紧凑版基础上，按用户确认的“整份 PDF 含附录 45～50 页”口径扩充到 **47 页**：新增约 7,700 个汉字、7 张图、7 张表（6 张计算表及 1 张证据表），保持原有字体、页边距和图内样式。
- 当前 PDF 已编译并完成全篇页面检查；新增公式和数值由 `figures/gen_paper_expansion.py` 复算，检查记录见 `workspace/review_expansion/`。
- 当前有独立的 `question1/` 审查工作目录，记录问题一重构的规划、发现与进度。

---

## 二、项目结构树

```
mathematical-modeling-Huawei/
├── AGENTS.md                        # 仓库级指南：结构约定、构建命令、提交规范
├── README.md                        # 空壳 README（仅标题）
├── README.txt                       # 导出说明：在 workspace/ 下运行与复现提示
├── EXPORT_WARNINGS.txt              # 导出警告：1 个 >200MB 文件未打包
├── manifest.json                    # 工作流导出清单（含步骤时间戳、产物清单；6.3MB 较大）
├── question1/                       # 【独立审查工作区】问题一重构的规划/发现/进度
│   ├── task_plan.md                 #   四问审查计划 + 问题一重算阶段清单
│   ├── findings.md                  #   问题发现、构念效度分析、重算口径决策
│   ├── progress.md                  #   会话进度记录（2026-09-25 两次会话）
│   ├── REVIEW_2026-09-25.md         #   问题一重构结果评审（新口径与结果）
│   ├── weight_sensitivity.py        #   组内 CRITIC / 组间权重扫描敏感性脚本
│   └── audit_recompute.py           #   独立复算脚本（不 import 业务代码，直接从原始数据算）
│
└── workspace/                       # 主工作区（所有代码、图、论文、数据）
    ├── PROBLEM_ANALYSIS.md          # 赛题分析输出
    ├── MODELING_REPORT.md           # 建模报告输出
    ├── RESULTS.md                   # 计算报告（四问方法/结果/验证，含更新注记）
    ├── AUDIT_REPORT.md              # 数值/约束/数据摄入审计摘要
    ├── CAPABILITY_AUDIT.md / *_CHECKLIST.json / *_VERDICT.json   # 能力审计
    ├── COMPILE_REPORT.md            # 论文编译报告
    ├── FIGURE_REPORT.md             # 图表数据核对报告
    ├── DATA_FACTS.json              # 数据事实（题面给定常量，params 原样载入）
    ├── DATA_PROFILE.json            # 数据行数建档核对
    ├── DELIVERABLES.json            # 交付产物清单
    ├── SEMANTIC_REVIEW_TODO.md      # 语义评审待办
    ├── PAPER_* / TABLE_DATA_*_CHECKLIST.md + *_REPORT.md        # 论文/表数据核对
    ├── PAPER_MODELING_QUALITY_REPORT.md / PAPER_IMPROVEMENT_STATE.json
    ├── _problem_file.txt / _image_descriptions.json / _script_output.txt
    │
    ├── code/                        # 【程序实现】四阶段入口 + 审计脚本
    │   ├── main.py                  #   入口：固定 seed=42，顺序跑 problem1~4 → all_results.json
    │   ├── params.py                #   统一参数源（6ND、η、三型 g(Q)、三档预算、L_ctx 集合）
    │   ├── utils.py                 #   路径、全量行数核验、随机种子、单纯形工具、原子保存
    │   ├── problem1.py              #   问题一：质量评分 + 冲突消解 + 配比回归（Q1 管道核心）
    │   ├── q1_pipeline.py           #   问题一语义解码/分位归一化/三组赋权管道
    │   ├── quality_scoring.py       #   质量评分公共函数（Q2/Q3 亦复用）
    │   ├── problem2.py              #   问题二：经典/广义标度律拟合 + 弹性替代
    │   ├── problem3.py              #   问题三：预算消元主算法 + SLSQP + 结构转移
    │   ├── problem4.py              #   问题四：分解 + 桥接 + 前沿预测 + C8 聚合
    │   ├── q3_assumption_sensitivity.py   # 问题三 θ/Q0/L_ctx 敏感性
    │   ├── review_q234.py           #   三问数值复核（差分/求解器对照/图更新）
    │   ├── sanity_check.py          #   完整遍历嵌套数组核验
    │   ├── constraint_audit.py      #   主方案/基线/轨迹/上下文预算核验
    │   └── requirements.txt
    │
    ├── figures/                     # 【图表产物 + 生成脚本】（本轮新增 7 张矢量 PDF）
    │   ├── gen_fig_q1_*.py          #   Q1: conflict_scatter / domain_Q_dumbbell / mixture_importance / quality_corr
    │   ├── gen_fig_q2_*.py          #   Q2: scaling_fit / substitution_contour / elasticity_diverging / generalized_surface
    │   ├── gen_fig_q3_*.py          #   Q3: allocation_stacked / transition_line / lctx_panels
    │   ├── gen_fig_q4_*.py          #   Q4: contribution_decomp / frontier_fan / task_radar / bridge_scatter
    │   ├── gen_tables.py / gen_table_q3_sensitivity.py / gen_code_includes.py / gen_latex_includes.py
    │   ├── prep_q1_indicators.py / prep_q4_decomp.py        # 图表数据准备
    │   ├── gen_paper_expansion.py   #   正文扩充图表及独立恒等式/回测检查
    │   ├── _figbase.py              #   绘图基类/公共样式
    │   ├── fig_roadmap.*            #   四问递进技术路线（HTML 引擎 + PDF）
    │   ├── fig_index_hierarchy.*    #   层级索引图
    │   ├── fig_pipeline_q1.*        #   问题一管道图
    │   ├── TABLE_q1_*.tex / TABLE_q2_*.tex / TABLE_q3_*.tex(×2) / TABLE_q4_*.tex   # 插入论文的 LaTeX 表
    │   ├── tikz_q3_feasible.tex/.pdf
    │   ├── problem_1_results.json ~ problem_4_results.json  # 各问结果汇总
    │   ├── all_results.json         #   四问统一结果（Q3 经 domain_Q_median 消费 Q1）
    │   ├── q3_assumption_sensitivity.json / _prep_q*.json/.npz
    │   ├── latex_includes.tex / TABLE_DATA_CHECK_PASSED.txt
    │   └── (2 张原始题面截图 PixPin_*.png)
    │
    ├── output/                      # 【数值产出】
    │   ├── q1_quality_scores.csv    #   A1 51230 行逐样本 Q
    │   ├── q1_mixture_model.json    #   配比回归
    │   ├── q1_independent_audit.json / q1_weight_sensitivity.json
    │   ├── q2_classic_scaling.json
    │   ├── q3_optimal_allocation.json / q3_lctx_sensitivity.json
    │   ├── q4_bridge_model.json / q4_task_aggregation.csv    # 1860 行逐任务
    │   └── (9 files)
    │
    ├── paper/                       # 【论文 LaTeX】（XeTeX/ctexart，正文 + 双附录）
    │   ├── main.tex                 #   主文件：格式规范 / 符号表 / 引用各 sections
    │   ├── compile_tex.sh           #   编译脚本 → build/main.pdf
    │   ├── sections/                #   0_refs(参考文献) · 3_q1 · 4_q2 · 5_q3 · 6_q4 · 7_verify · 8_conclusion · 9_appendix · 10_appendix
    │   ├── _improvement_rounds/     #   round0_original.pdf / round1.pdf / round2.pdf（改进迭代快照）
    │   ├── PAPER_IMPROVEMENT_LOG.md
    │   └── build/                   #   main.pdf（48 页，含附录，图 10 已调整并检查）+ 编译日志 + tectonic-cache
    │
    ├── review_expansion/            # 正文扩充报告、复算数据、最终 PDF 检查
    │
    ├── review_q234/                 # 【问题二三迭代复核工作区】
    │   ├── REVIEW.md                #   三问迭代报告（方法修正 + 数值 + 结论边界）
    │   ├── before_problem_*.json    #   迭代前原始结果备份
    │   ├── verification.json / verification.log / sanity.log / constraints.log
    │   ├── q2_run.log / q3_run.log / q4_run.log / q3_sensitivity.log / recompute.log ...
    │   └── gen_fig_*.log / final_pdf_check.json / format_font_check.json / compile.log
    │
    ├── user_data/                   # 【上传的赛题材料】（原样保留）
    │   ├── 数据说明.pdf / 数据说明_extracted.txt
    │   ├── 算力约束下提升大语言模型能力的资源配置建模.docx / _extracted.md
    │   └── real_attachments/real_attachments/       # 原始附件（A/B/C 三组，3800+ 文件）
    │       ├── A_data_value/          # A: Pythia-Meta-rater / slim-190M · arxiv · github
    │       │   ├── regmix_tables/ · slimpajama_quality_extended/ · domain_mapping_guide.csv
    │       ├── B_scaling_laws/        # B: Pythia 训练轨迹 + 跨族文献验证点
    │       └── C_efficiency_evolution/ # C: 模型榜单 + 逐任务评测 + 损失–基准桥接 + 架构元数据
    │
    ├── real_attachments/            # 符号链接/镜像（开发环境使用的可访问副本，含 source_manifest.json、
    │   │                            #   attachment_size_summary.csv、数据说明_extracted.txt）
    │   └── A_data_value / B_scaling_laws / C_efficiency_evolution
    │
    ├── _utils/plot_utils.py         # 绘图公共工具
    ├── .deps/lightgbm/              # 本地捆绑的 lightgbm 依赖
    ├── _tmp/                        # 【草稿空间】中间产物、日志、缓存、审查用截图（不入交付）
    └── 算力约束下提升大语言模型能力的资源配置建模.docx   # 题面副本（根）
```

---

## 三、当前完成状态

### ✅ 已完成（截至 2026-09-26）

| 环节 | 状态 | 说明 |
|---|---|---|
| 赛题分析 / 建模 / 编程 | ✅ completed | 工作流全部 8 步 completed，manifest.json 有完整记录 |
| 问题一重构 | ✅ 已完成 | 语义解码 + A1 分位 + 三组平衡赋权，全量重算 A1/A2/A3 |
| 问题一独立复核 | ✅ 通过 | 独立脚本逐行最大差 2.2e-16；域排序对权重做敏感性对照 |
| 问题二/三迭代 | ✅ 收尾（09-26） | 公平验证、预算消元、统一参数；三问数值校验通过 |
| 问题四迭代 | ✅ 收尾 | 分解/桥接/前沿一致性修正完成 |
| 论文正文扩充与排版 | ✅ 48 页（含附录） | `paper/build/main.pdf`；已逐页复核，无 Overfull/未定义引用/图表裁切或重叠 |
| 数据审计 / 约束审计 / 能力审计 | ✅ 通过 | 详见 `workspace/AUDIT_REPORT.md`、`CAPABILITY_VERDICT.json` |

### 📌 关键运行命令（须在 `workspace/` 下执行）

```sh
cd workspace
pip install -r code/requirements.txt
python code/main.py                     # 全量重算（覆盖既有结果）
python code/main.py --problems 2 3 4    # 只重算指定问，其余加载保存结果
python code/q3_assumption_sensitivity.py
python code/review_q234.py              # 三问数值复核 + 参数对照
python code/sanity_check.py & python code/constraint_audit.py
python figures/gen_paper_expansion.py  # 扩充图表、解析基线及滚动回测检查
bash paper/compile_tex.sh               # XeTeX 编译 → build/main.pdf
```

### ⚠️ 注意事项 / 结论边界

- **复现提示**：`EXPORT_WARNINGS.txt` 声明有 1 个超 200MB 文件未打包；`real_attachments/` 下的超大文件是 Git LFS 指针，真实数据在 `user_data/real_attachments/real_attachments/`，外部复现需核对输入是否齐全。
- **含义声明**：`RESULTS.md` 标注为历史口径，问题一及依赖它的问题三数值已被重构结果取代；当前结果以 `question1/REVIEW_*.md` 与 `figures/problem_1/3_results.json` 为准。
- **模型限制**：
  - 问题一权重与方向是建模假设（无外部质量–损失标签 → 无法公平校准组间权重）。
  - 广义律的 `θ=0.5` 是假设（quality-helps premise），B6–B8 的 `Q_score` 与 A1 质量标度尚未校准，不能仅凭相关性断言其等同于部署质量或难度；配比系数未进入广义律/优化。
  - 三问优化没有全局最优证明（Q 外层网格 + 局部细化）；结构转移点对评分标度/成本函数/网格敏感。
  - 问题四前沿预测是情景分位数，非校准远期预测；非规模贡献是条件关联而非因果识别。
- **版面**：沿用紧凑版的受控浮动与小四字号；目录自然续为 2 页，图 10 调整后整份 PDF 为 48 页（含附录）。最终页数、哈希和日志状态以 `workspace/review_expansion/final_pdf_check.json` 为准。
- **新增验证结论**：含质量模型的整体留出 RMSE 改善主要来自 B8；在 B6、B7 上反而劣于无质量基线，不能概括为各来源一致改善。


## 四、本轮正文扩充与后续建议

- 新增章节文件：`s2_data_evidence.tex`、`s3_q1_extended.tex`、`s4_q2_extended.tex`、`s5_q3_derivation.tex`、`s5_q3_extended.tex`、`s6_q4_extended.tex`、`s7_verify_extended.tex`。
- 内容涵盖证据分层、评分性质、权重敏感性、质量标度可识别性、有限增量替代、固定质量唯一驻点及闭式基线、质量净收益、分类型前沿、滚动回测和不确定性传播。
- 复算通过：分来源 RMSE 聚合、等损失曲线回代、解析基线与数值解对照、滚动回测与保存指标一致。原始附件、四问主结果与已审计核心算法保持原样；本轮属于分析和表达扩充。
- 扩充前备份：`workspace/paper/_improvement_rounds/expansion_before_20260926.pdf` 及同名源文件 ZIP。详细报告见 `workspace/review_expansion/REVIEW.md`，日期记录见 `2026-09-26/工作进度与下一步建议.md`。
- 下一步优先核对提交模板是否另需独立标题/摘要页；当前主文件从目录开始。随后检查匿名化、附件齐全性和提交清单。后续研究应优先补质量分数与真实训练收益的联合数据、更多时间窗口及外部预测检验。

### 图 10 标签调整（2026-09-26）

将经典律退化线与弹性参考点图例移至图底部独立区域，为三维坐标轴标题留出空间；保留原数值与配色。重新编译得到 48 页，已检查第 17 页图 10 无图例与坐标轴文字重叠；编译无 Overfull 或未定义引用。
