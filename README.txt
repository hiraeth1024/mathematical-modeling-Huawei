# 导出说明（全部内容）

本压缩包为「导出全部」版，含工作区完整内容（论文/代码/图表/数据/中间产物 _tmp/ 等）。

## 如何运行代码
代码多为相对路径引用（code/xxx.py、figures/、_tmp/），请【在 workspace/ 目录下】运行，
不要 cd 进 code/：
    cd workspace
    pip install -r code/requirements.txt   # 依赖清单在 code/ 下（如无则忽略）
    python code/main.py                     # 入口脚本

包含可导出的 _tmp/ 中间数据；外部复现还需安装依赖并核对输入是否齐全，
重跑 main.py 可能覆盖重建中间结果。

导出的是当前已存在的产物，不代表工作流已全部完成或已通过提交检查。
若包含 EXPORT_WARNINGS.txt，请先阅读其中的运行依赖/文件缺失提示；有提示时不保证代码可在软件外完整复现。
