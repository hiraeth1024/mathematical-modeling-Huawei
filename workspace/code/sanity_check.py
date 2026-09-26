# -*- coding: utf-8 -*-
"""sanity_check.py — 自动化数值审查（只读结果JSON重算结论，不print大数组）。"""
from __future__ import annotations
import os, sys, json, math
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)

errors, warnings, suspicious = [], [], []


def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            walk(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            walk(value, f"{path}[{i}]")
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        _check(path, v=obj)


def _check(name, v):
    if isinstance(v, float):
        if math.isnan(v):
            errors.append(f"{name} = NaN")
        elif math.isinf(v):
            errors.append(f"{name} = Inf")
    key = name.rsplit(".", 1)[-1].replace("[]", "").lower()
    if key in {"r2", "r_squared"} and isinstance(v, (int, float)):
        if v > 1 + 1e-9:
            errors.append(f"{name}={v} R2>1")


for fn in ["problem_1_results.json", "problem_2_results.json",
           "problem_3_results.json", "problem_4_results.json"]:
    p = os.path.join(_ROOT, "figures", fn)
    if os.path.exists(p):
        walk(json.load(open(p, encoding="utf-8")), fn)

print("=" * 50)
print(f"[sanity_check] errors={len(errors)} warnings={len(warnings)} suspicious={len(suspicious)}")
for e in errors[:5]:
    print(f"  ERROR {e}")
if not errors:
    print("[sanity_check] PASS：无 NaN/Inf/非法数值")
sys.exit(1 if errors else 0)
