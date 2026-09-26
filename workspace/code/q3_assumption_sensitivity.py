# -*- coding: utf-8 -*-
"""Recompute Q3 allocations under explicit Q0 and theta assumptions."""
from __future__ import annotations

import utils as u
from params import BUDGETS, SEED
from problem3 import _load_q0, _load_q2_params, solve_budget


def main():
    u.set_all_seeds(SEED)
    q0 = _load_q0()
    base_params = list(_load_q2_params())
    theta0 = base_params[-1]
    scenarios = {
        "baseline": (q0, theta0),
        "Q0_minus20pct": (0.8 * q0, theta0),
        "Q0_plus20pct": (1.2 * q0, theta0),
        "theta_0.2": (q0, 0.2),
        "theta_0.8": (q0, 0.8),
    }
    output = {
        "method": "Q3 exponential cost; Lctx=2048; budget-eliminated profile per budget",
        "budgets_flops": BUDGETS,
        "scenarios": {},
    }
    for name, (q0_s, theta_s) in scenarios.items():
        params = base_params.copy()
        params[-1] = theta_s
        by_budget = {}
        for budget in BUDGETS:
            sol = solve_budget(budget, q0_s, params, 2048, "exp", n_starts=20)
            if sol is None:
                raise RuntimeError(f"No feasible candidate for {name}, C={budget}")
            if sol["C_tot"] > budget * (1 + 1e-6):
                raise AssertionError(f"Budget violation for {name}, C={budget}")
            by_budget[f"{budget:.0e}"] = {
                "N": sol["N"], "D": sol["D"], "Q": sol["Q"],
                "L": sol["L"], "util": sol["util"],
            }
        output["scenarios"][name] = {"Q0": q0_s, "theta": theta_s,
                                      "by_budget": by_budget}
        print(name, [(b, round(v["Q"], 3), round(v["L"], 3))
                     for b, v in by_budget.items()])
    u.save_json(output, "figures/q3_assumption_sensitivity.json")
    return output


if __name__ == "__main__":
    main()
