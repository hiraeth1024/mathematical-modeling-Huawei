# -*- coding: utf-8 -*-
"""main.py — 主调度：串联四个子问题，汇总 figures/all_results.json。

从空缓存可完整运行；本轮各子问题已独立执行并验证。
用法：python _utils/run_compute.py code/main.py
"""
from __future__ import annotations
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import utils as u
import params
import argparse
import importlib
import json


def main(problems=(1, 2, 3, 4)):
    u.set_all_seeds(params.SEED)
    print("#" * 60)
    print("# 华为杯 F 题：算力约束下提升大语言模型能力的资源配置建模")
    print("# comp-code 主程序：四问递进求解")
    print("#" * 60)

    outputs = {}
    for i in range(1, 5):
        if i in problems:
            outputs[i] = importlib.import_module(f"problem{i}").main()
        else:
            path = u._ROOT / "figures" / f"problem_{i}_results.json"
            outputs[i] = json.loads(path.read_text(encoding="utf-8"))
    r1, r2, r3, r4 = (outputs[i] for i in range(1, 5))

    # 汇总（供 paper-figure / logic_audit / cross_problem_check）
    all_results = {
        "_meta": u.run_meta(),
        "problem_1": r1,
        "problem_2": r2,
        "problem_3": r3,
        "problem_4": r4,
        # CROSS_PROBLEM_LEDGER observed 值填充
        "cross_problem_ledger_observed": {
            "Q1_domain_Q_median": r1["domain_Q_median"],
            "Q2_scaling_params": r2["classic"]["params"],
            "Q2_theta_assumed": r2["generalized"]["theta_assumed_downstream"],
            "Q3_L_optimal_per_budget": {
                f"{C:.0e}": r3["optimal_allocation"]["by_gtype"]["exp"][f"{C:.0e}"].get("L")
                for C in params.BUDGETS},
            "Q3_Q0_from_Q1": r3["Q0"],
        },
    }
    u.save_json(all_results, "figures/all_results.json")
    print("\n" + "=" * 60)
    print("[main] 四问全部完成，汇总 → figures/all_results.json")
    return all_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--problems", nargs="+", type=int, choices=(1, 2, 3, 4), default=[1, 2, 3, 4])
    main(parser.parse_args().problems)
