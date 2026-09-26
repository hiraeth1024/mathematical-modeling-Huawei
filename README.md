# 华为杯 F 题：算力约束下提升大语言模型能力的资源配置建模

第二十三届中国研究生数学建模竞赛 F 题建模工作区，包含四问求解程序、原始附件、数值结果、图表、LaTeX 论文与复核记录。研究在有限算力下，如何配置模型参数量、训练数据量、数据质量与上下文长度，并分析能力前沿的变化。

## 成果入口

| 内容 | 文件 |
|---|---|
| 当前论文 PDF | [workspace/paper/build/main.pdf](workspace/paper/build/main.pdf) |
| 已填写摘要的 Word 模板 | [华为杯论文模板_已填摘要.docx](workspace/paper/build/华为杯论文模板_已填摘要.docx) |
| 项目状态与运行说明 | [PROJECT_STATUS.md](PROJECT_STATUS.md) |
| 问题一重构评审 | [question1/REVIEW_2026-09-25.md](question1/REVIEW_2026-09-25.md) |
| 问题二、三、四数值复核 | [workspace/review_q234/REVIEW.md](workspace/review_q234/REVIEW.md) |
| 正文扩充与验证记录 | [workspace/review_expansion/REVIEW.md](workspace/review_expansion/REVIEW.md) |
| 后续优化审查 | [PAPER_OPTIMIZATION_REVIEW_2026-09-26.md](PAPER_OPTIMIZATION_REVIEW_2026-09-26.md) |
| 工作进度与下一步建议 | [2026-09-26/工作进度与下一步建议.md](2026-09-26/工作进度与下一步建议.md) |

**文件状态（2026-09-26）**：当前 PDF 实测为 **51 页**，前两页为封面与摘要，随后为目录、正文和附录。它已超过此前设定的“含附录 45～50 页”目标。历史记录中的 35、47、48、49 页对应不同版本；复核记录是否适用于当前文件，应同时比对页数与 SHA-256。Word 模板已填写摘要，但尚未纳入 LaTeX 主文件。

## 四问方法与主要结果

| 问题 | 方法 | 当前结果与解释 |
|---|---|---|
| 一：质量评价与配比 | 22 指标语义解码、固定经验分位归一化、三组平衡赋权、配比回归 | 七域质量中位数 `Q0=0.487876`；A1 冲突率 `0.303%`，C4 域内最高，为 `1.03%` |
| 二：标度律与质量替代 | Huber 稳健拟合、分组留出、有效数据量扩展、弹性与等损失分析 | 含质量模型留出 RMSE `0.674880`，无质量基线 `0.783601`；改善主要来自 B8 |
| 三：预算约束优化 | KKT 分析、预算消元、固定质量求根、质量剖面搜索、SLSQP 交叉检查 | 指数型质量成本下，三档预算候选损失约为 `3.073 / 2.151 / 1.914` |
| 四：能力演化与前沿 | 描述性增长分解、分层单调桥接、Bootstrap 情景、滚动回测 | 一步趋势 MAE `1.773`，末值基线 `1.475`；远期输出为条件情景 |

三档预算为 `10^19 / 10^22 / 10^24 FLOPs`。代码中 `N` 和 `D` 以十亿为单位，质量分数无量纲；换算常量与假设统一放在 `workspace/code/params.py`。

## 目录结构

```text
.
├── AGENTS.md                     # 贡献与协作约定
├── PROJECT_STATUS.md             # 项目状态与历史进展
├── question1/                    # 问题一独立复算、权重敏感性与评审
├── 2026-09-26/                   # 日期进度记录
├── manifest.json                 # 历史工作流导出清单
└── workspace/
    ├── code/                     # main.py、problem1.py～problem4.py、审计程序
    ├── user_data/real_attachments/real_attachments/  # 主程序实际读取的原始附件
    ├── real_attachments/         # 附件副本及清单，部分文件采用 Git LFS
    ├── output/                   # 样本评分、回归结果及独立审计数据
    ├── figures/                  # 各问 JSON、图表 PDF、LaTeX 表与生成器
    ├── paper/
    │   ├── main.tex              # LaTeX 主文件
    │   ├── sections/             # 四问、验证、结论及附录
    │   ├── compile_tex.sh        # XeLaTeX / Tectonic 编译入口
    │   ├── build/                # PDF、Word 模板及编译日志
    │   └── _improvement_rounds/  # 历史论文与源码快照
    ├── review_q234/              # 求解器、导数、预算约束复核
    ├── review_expansion/         # 扩充图表与公式复算
    └── _tmp/                     # 临时数据、渲染图片和检查脚本
```

## 环境与数据准备

所有下文命令均在仓库根目录起步，进入 `workspace/` 后运行。建议使用独立虚拟环境：

```sh
python3 -m venv .venv
source .venv/bin/activate
cd workspace
python -m pip install -r code/requirements.txt
python -m pip install matplotlib
```

依赖清单包含 NumPy、SciPy、pandas、scikit-learn、statsmodels 与 LightGBM；绘图另需 Matplotlib 和可用中文字体。清单为导出时的版本约束，已有复核环境版本记于 `review_q234/REVIEW.md`，两者并非完全一致；复现时请记录实际环境。

开始全量计算前：

- 阅读根目录的 `README.txt` 与 `EXPORT_WARNINGS.txt`。导出记录提示有一个大文件未打包，不能默认所有附件齐全。
- 核对 `code/params.py` 中的 `DATA_ROOT`，其默认指向 `user_data/real_attachments/real_attachments/`，不是同级 `real_attachments/` 副本。
- 若通过 Git 获取数据，先在已配置 Git LFS 的环境执行 `git lfs pull`；LFS 指针不是可读取的数据文件。未纳入导出的文件仍需另行补齐。
- 仅查看已有 PDF、JSON 或评审报告，不需要重跑模型。

## 计算与复核

```sh
# 全量重算四问，并汇总到 figures/all_results.json
python code/main.py

# 仅重算指定问题，其他问题读取 figures/ 中的已有结果
python code/main.py --problems 2 3 4
```

运行会覆盖相关 `output/` 和 `figures/` 产物。问题三依赖问题一的质量基线及问题二参数；修改上游评分或参数后，应同步重算下游并刷新图表。

```sh
# 问题一独立复算与组间权重敏感性
python ../question1/audit_recompute.py
python ../question1/weight_sensitivity.py

# 问题三假设敏感性，以及问题二、三、四数值检查
python code/q3_assumption_sensitivity.py
python code/review_q234.py
python code/sanity_check.py
python code/constraint_audit.py
```

没有独立测试套件或覆盖率门槛。上述程序分别检查独立评分、导数和求解器一致性、非法数值及预算约束。模型修改后须核对论文表述；数值检查通过不等于统计有效性或外部预测能力已得到验证。

## 图表更新

在保存结果与敏感性结果齐全后运行：

```sh
python figures/prep_q1_indicators.py
python figures/prep_q4_decomp.py
python figures/gen_tables.py
python figures/gen_table_q3_sensitivity.py
python figures/gen_code_includes.py
python figures/gen_paper_expansion.py

# 按修改范围运行对应绘图脚本，例如图 10
python figures/gen_fig_q2_generalized_surface.py
```

其他绘图入口为 `figures/gen_fig_q1_*.py` 至 `gen_fig_q4_*.py`；公共样式在 `_figbase.py` 与 `_utils/plot_utils.py`。`gen_paper_expansion.py` 生成扩充图表，并检查分来源 RMSE 汇总、等损失回代、闭式基线和滚动回测，记录写入 `review_expansion/derived_results.json`。

## 论文编译

**编译会覆盖 `paper/build/main.pdf`。当前合并版含 Word 封面和摘要，而 LaTeX 主文件从目录开始；编译脚本不会自动把这两页重新合入。** 如需保留合并版，先备份：

```sh
cp paper/build/main.pdf "paper/build/main-before-build-$(date +%Y%m%d-%H%M%S).pdf"
bash paper/compile_tex.sh
```

脚本优先使用 `xelatex`，否则查找 Tectonic；通过临时 `main_compile.tex` 适配字体，并保留原 `main.tex`。当前字体配置使用 macOS 的 `Songti SC` 和 `Heiti SC`，其他系统需提供对应字体或调整编译配置。

```sh
# 未自动找到 Tectonic 时，指定实际可执行文件路径
TECTONIC_BIN=/path/to/tectonic bash paper/compile_tex.sh

# Tectonic 缓存不完整且允许下载 TeX 资源时
TEX_ALLOW_DOWNLOAD=1 bash paper/compile_tex.sh
```

成功产物为 `paper/build/main.pdf`，日志为 `paper/build/main_compile.log`。修改后检查引用、公式溢出、图例与坐标轴重叠、表格断页及实际页数；封面与摘要合入后还需再次检查总页数和页码。

## 结果使用边界

- `Q0` 是当前评分规则下的七域中位数，不是真实质量概率，也不是通用标准答案。主评分采用组间平衡、组内等权，相同权重不代表熵权计算出错。
- 质量指数 `θ=0.5` 是下游结构性假设；B6–B8 与 A1 的质量标度尚未联合校准，B6/B7 的留出误差也没有随质量项改善。
- 问题三外层质量搜索未证明全局最优，高预算方案还存在跨规模外推限制。
- 问题四的年份贡献是条件关联；Bootstrap 区间未覆盖全部结构变化风险，不能解释为已校准的远期预测。
- 历史 `RESULTS.md`、导出清单与评审记录可能保留旧口径。使用当前 JSON、源码和对应复核记录交叉确认，不直接混用不同版本数字。

贡献约定见 [AGENTS.md](AGENTS.md)。更改模型时保留原始附件，说明受影响的问题、运行命令、数值变化及论文图表更新范围。
