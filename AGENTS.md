# Repository Guidelines

## Project Structure & Module Organization

This repository is an exported modeling workspace for Huawei Cup Problem F. Work from `workspace/`: `code/main.py` runs the four stages in `problem1.py` through `problem4.py`; `code/params.py` holds shared constants, and `code/utils.py` handles data paths and output. Raw attachments are under `user_data/real_attachments/real_attachments/`. Generated results live in `output/` and `figures/`; figure generators are named `figures/gen_fig_*.py`. The paper source is `paper/main.tex` with chapters in `paper/sections/`. Treat `_tmp/` as scratch space and the root `manifest.json` as an export record.

## Build, Test, and Development Commands

Run commands from `workspace/` because scripts use workspace-relative paths:

```sh
cd workspace
python3 -m pip install -r code/requirements.txt
python3 code/main.py
python3 code/main.py --problems 2 3 4
python3 code/review_q234.py
python3 code/sanity_check.py
python3 code/constraint_audit.py
./paper/compile_tex.sh
```

`main.py` recomputes the four models and overwrites generated results. Use `--problems` to recompute selected stages while loading the others from saved results. `review_q234.py` compares numerical solvers and checks derivatives, boundaries, and validation outputs. The two audit scripts check saved numerical values and resource constraints. The paper script uses a XeTeX engine, resolves references, and writes `paper/build/main.pdf` while preserving `paper/main.tex`. Check `README.txt` and `EXPORT_WARNINGS.txt` before attempting a full reproduction.

## Coding Style & Naming Conventions

Use four-space indentation, UTF-8, descriptive `snake_case` names, and type hints where they clarify interfaces. Keep shared assumptions and units in `code/params.py`; preserve the convention that `N` and `D` are measured in billions and compute costs are in FLOPs. Follow existing `problem*.py`, `gen_fig_*.py`, and `TABLE_*.tex` naming patterns. No formatter or linter configuration is included, so keep edits consistent with surrounding code.

## Testing Guidelines

There is no standalone test suite or coverage target. After model changes, rerun the affected stage, then both audit scripts. Check generated JSON and CSV against the claims in `paper/sections/`; an audit pass alone does not establish statistical validity. Avoid editing raw attachments or generated outputs by hand.

## Commits & Pull Requests

This export has no `.git` history, so no existing commit convention can be inferred. Use short, imperative commit subjects such as `Fix frontier uncertainty calculation`. Pull requests should state the modeling change, affected data and artifacts, commands run, and any changes to reported figures or paper conclusions. Include updated PDF or figure previews when presentation changes. Verify the PDF page count against the `manifest.json` limit before submission.
