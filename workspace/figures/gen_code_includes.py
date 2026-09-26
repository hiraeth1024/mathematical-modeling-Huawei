# -*- coding: utf-8 -*-
"""按当前函数范围更新核心代码摘录，避免源码迭代后附录行号失效。"""
import ast
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
appendix = ROOT / 'paper/sections/s10_appendix.tex'
text = appendix.read_text(encoding='utf-8')


def span(file, first, last=None):
    nodes = {n.name: n for n in ast.parse((ROOT / 'code' / file).read_text()).body
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    return nodes[first].lineno, nodes[last or first].end_lineno


specs = [
    ('code:q2-classic', 'problem2.py', *span('problem2.py', 'fit_classic'), '经典标度律的对数域稳健拟合'),
    ('code:q2-generalized', 'problem2.py', *span('problem2.py', 'generalized_model', 'fit_generalized'), '广义标度律及质量指数拟合'),
    ('code:q3-solver', 'problem3.py', *span('problem3.py', 'solve_fixed_quality', 'solve_budget'), '预算消元、质量剖面搜索与边界检验'),
    ('code:q4-frontier', 'problem4.py', *span('problem4.py', '_fit_bridge'), '单调有界的损失到能力桥接'),
]
lines = (ROOT / 'code/problem4.py').read_text().splitlines()
start = next(i + 1 for i, line in enumerate(lines) if line.strip() == 'n_boot = 2000')
end = next(i for i, line in enumerate(lines) if '# 前沿不倒退核验' in line)
specs.append(('code:q4-forecast', 'problem4.py', start, end, '联合重拟合截距与斜率的自助情景预测'))
for label, file, first, last, caption in specs:
    pattern = r'\\lstinputlisting\[[^\n]*label=\{' + re.escape(label) + r'\}[^\n]*'
    replacement = (f'\\lstinputlisting[style=pythonstyle,firstline={first},lastline={last},'
                   f'caption={{{caption}}},label={{{label}}}]{{../code/{file}}}')
    text, n = re.subn(pattern, lambda match: replacement, text)
    assert n == 1, label
appendix.write_text(text, encoding='utf-8')
print('Updated core source ranges:', appendix)
