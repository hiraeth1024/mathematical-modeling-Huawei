#!/usr/bin/env bash
# Compile main.tex with a XeTeX engine while keeping the source and existing PDF intact.
set -euo pipefail

paper_dir="$(cd "$(dirname "$0")" && pwd)"
cd "$paper_dir"
mkdir -p build/tectonic-cache

# The exported source selects an obsolete macOS CTeX font set. Generate a
# local-font copy for compilation; do not change the paper's source file.
python3 - <<'PY'
from pathlib import Path

source = Path("main.tex").read_text(encoding="utf-8")
original = r"\documentclass[12pt,a4paper]{ctexart}"
assert source.count(original) == 1, "Unexpected document class in main.tex"
replacement = r"""\documentclass[12pt,a4paper,fontset=none]{ctexart}
\setCJKmainfont{Songti SC}
\setCJKsansfont{Heiti SC}
\setCJKmonofont{Songti SC}
\setCJKfamilyfont{zhsong}{Songti SC}
\setCJKfamilyfont{zhhei}{Heiti SC}
\setCJKfamilyfont{zhkai}{Songti SC}
\setCJKfamilyfont{zhfs}{Songti SC}
\providecommand{\songti}{\CJKfamily{zhsong}}
\providecommand{\heiti}{\CJKfamily{zhhei}}"""
Path("main_compile.tex").write_text(source.replace(original, replacement, 1), encoding="utf-8")
PY
trap 'rm -f main_compile.tex' EXIT

export TECTONIC_CACHE_DIR="${TECTONIC_CACHE_DIR:-$paper_dir/build/tectonic-cache}"
if command -v xelatex >/dev/null 2>&1; then
  for _ in 1 2 3; do
    xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main_compile.tex >/dev/null
  done
else
  tectonic_bin="${TECTONIC_BIN:-}"
  if [[ -z "$tectonic_bin" ]]; then
    if command -v tectonic >/dev/null 2>&1; then
      tectonic_bin="$(command -v tectonic)"
    else
      tectonic_bin="/Applications/ChatGPT.app/Contents/Resources/plugins/openai-bundled/plugins/latex/bin/tectonic"
    fi
  fi
  if [[ ! -x "$tectonic_bin" ]]; then
    echo "Neither xelatex nor Tectonic was found. Set TECTONIC_BIN to a XeTeX-capable Tectonic executable." >&2
    exit 1
  fi
  options=()
  if [[ "${TEX_ALLOW_DOWNLOAD:-0}" != "1" ]]; then
    options+=(-C)
  fi
  "$tectonic_bin" "${options[@]}" --keep-logs -o build main_compile.tex
fi
mv build/main_compile.pdf build/main.pdf
echo "Built $paper_dir/build/main.pdf"
