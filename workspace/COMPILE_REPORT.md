# 最终 PDF 编译报告



## 合规检查汇总（comp-compile-zh 最终门）

- 编译引擎：XeLaTeX + ctexart，三遍串行编译，退出码均为 0，`main.log` 零错误、零 undefined 引用。
- 页数：36 页（官方提交参考 ≤50，仅提示）。
- 数据真实性：摘要与正文关键数字对照真实 JSON 逐项核对通过（Q 域中位数 0.079、冲突率 4.96%、广义标度律留出 RMSE 0.971→0.688、配比排序 Spearman 0.74–0.84、经典标度律 R²≈1、不可约损失 E=1.69、注意力临界 6/η=3×10⁴）。已写入 `% DATA_CHECK_PASSED`。
- 图表嵌入：全部 18 张 figures/*.pdf 均进入正文并有引用与解读；新增补全问题一流程图与指标层次图。
- 图 PDF 终检：修复 9 张插入尺寸过小图（字号 <8pt），加宽后 `--referenced-only` 检查通过。
- 摘要物理单页：修复关键词行使版面检测定位成功，摘要收于单页。
- 能力声称核对：15/15 PASS；事实审计 0 拒绝；引用格式无阻断项；匿名合规。
- PDF 快照：36 页，SHA-256 8159adf9b271…，报告与最终 PDF 一致。

<!-- MODEX_PDF_SNAPSHOT_BEGIN -->
## 最终 PDF 文件快照

> 以下仅证明文件版本、页数与哈希一致，不代表其他质量检查已通过。此前检查结论保留，是否仍适用需核对其输入版本。

- 文件：`C:/Users/hybuzhy/AppData/Roaming/ModexData/library-Aav9aY/workspaces/3721546c023d/paper/main.pdf`
- 实际总页数：**36 页**
- 文件大小：1921223 字节
- SHA-256：`8159adf9b2717a17246b5bb9ef6ff28a1e24759ff54baa100f7d70dcee182eb2`
- 快照时间（UTC）：2026-09-23T16:22:48+00:00

<!-- MODEX_PDF_SNAPSHOT_V1 {"bytes":1921223,"captured_at":"2026-09-23T16:22:48+00:00","pages":36,"pdf":"C:/Users/hybuzhy/AppData/Roaming/ModexData/library-Aav9aY/workspaces/3721546c023d/paper/main.pdf","sha256":"8159adf9b2717a17246b5bb9ef6ff28a1e24759ff54baa100f7d70dcee182eb2"} -->
<!-- MODEX_PDF_SNAPSHOT_END -->
