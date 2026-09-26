# -*- coding: utf-8 -*-
"""独立复核 Q2/Q3/Q4 数值接口、边界、求解精度与优化前后变化。"""
from __future__ import annotations
import json
import time
from pathlib import Path
import numpy as np
from problem2 import classic_model, generalized_model
from problem3 import (solve_budget, solve_budget_slsqp, loss_gen, compute_total,
                      solve_fixed_quality, _load_q2_params, _load_q0)
from problem4 import _fit_bridge, _open_mask
from params import BUDGETS, LCTX_SET
import pandas as pd
import utils as u


def main():
    root = u._ROOT
    r2, r3, r4 = [json.loads((root / f'figures/problem_{i}_results.json').read_text()) for i in (2, 3, 4)]
    cp = list(r2['classic']['params'].values())
    params = _load_q2_params()
    q0 = _load_q0()
    assert r2['generalized']['split']['group_overlap'] == 0
    assert np.allclose(generalized_model(params, 1., 100., 1.), classic_model(cp, 1., 100.))
    assert r2['elasticity']['reference_point']['Q0'] == q0
    ref = r2['elasticity']['reference_point']
    point = np.array([ref['N0'], ref['D0'], ref['Q0']])
    eps_errors = []
    for i, key in enumerate(('eps_N', 'eps_D', 'eps_Q')):
        plus, minus = point.copy(), point.copy()
        plus[i] *= np.exp(1e-5); minus[i] *= np.exp(-1e-5)
        numeric = (np.log(loss_gen(*plus, params)) - np.log(loss_gen(*minus, params))) / 2e-5
        eps_errors.append(abs(numeric - r2['elasticity'][key]))
    assert max(eps_errors) < 1e-8
    el = r2['elasticity']
    assert abs(loss_gen(point[0] + el['exact_iso_loss_delta_N'], point[1], q0 + el['finite_delta_Q'], params) - ref['L0']) < 1e-10
    gain = el['equivalent_parameter_increase_B']
    assert abs(loss_gen(point[0] + gain, point[1], q0, params) - loss_gen(point[0], point[1], q0 + el['finite_delta_Q'], params)) < 1e-10

    rows, profile_seconds, slsqp_seconds = [], 0., 0.
    for kind in ('exp', 'pow', 'log'):
        for budget in BUDGETS:
            start = time.perf_counter()
            sol = solve_budget(budget, q0, params, 2048, kind)
            profile_seconds += time.perf_counter() - start
            dense = solve_budget(budget, q0, params, 2048, kind, q_grid_size=513)
            start = time.perf_counter()
            other = solve_budget_slsqp(budget, q0, params, 2048, kind, n_starts=20)
            slsqp_seconds += time.perf_counter() - start
            assert other is not None, (kind, budget, 'SLSQP no converged candidate')
            budget_error = abs(compute_total(sol['N'], sol['D'], sol['Q'], q0, 2048, kind)[0] / budget - 1)
            assert budget_error < 1e-12
            assert abs(sol['L'] - dense['L']) < 1e-8
            assert sol['L'] <= other['L'] + 1e-7
            assert sol['stationarity_residual'] < 1e-6
            baseline = solve_fixed_quality(budget, q0, q0, params, 2048, kind)
            assert sol['L'] <= baseline['L'] + 1e-10
            rows.append({'cost': kind, 'budget': budget, 'profile_L': sol['L'],
                         'slsqp_L': other['L'], 'dense_grid_delta_L': sol['L'] - dense['L'],
                         'stationarity_residual': sol['stationarity_residual'],
                         'quality_state': sol['quality_state'],
                         'fixed_quality_L': baseline['L'], 'quality_only_gain': baseline['L'] - sol['L']})
    # 原数值边界附近与 theta 情景：核验缩放和铰链处理。
    for theta in (.2, .8):
        p = list(params); p[-1] = theta
        for budget, ctx in ((1e18, 2048), (1e25, 131072)):
            sol = solve_budget(budget, q0, p, ctx, 'exp')
            assert sol['stationarity_residual'] < 1e-6
    sol = solve_budget(1e22, 1., params, 2048, 'exp')
    assert sol['Q'] == 1. and sol['C_Q'] == 0.

    test = pd.DataFrame({'Hub License': ['apache-2.0', 'other', '', 'mit'],
                         'Epoch_AI_Open_Weights': ['Yes', None, None, 'No']})
    assert _open_mask(test).tolist() == [True, False, False, False]
    par, pred = _fit_bridge(np.linspace(1, 4, 20), np.linspace(80, 20, 20))
    assert 0 <= par['c'] <= par['c'] + par['Smax'] <= 100
    assert np.all(np.diff(pred) <= 0)
    for stratum in r4['bridge']['strata_by_comparability'].values():
        assert stratum['bounded_0_100'] and np.isfinite(stratum['loocv_rmse'])
    for scenario in r4['frontier']['predictions'].values():
        for quantiles in scenario.values():
            assert 0 <= quantiles['P10'] <= quantiles['P50'] <= quantiles['P90'] <= 100
    assert r4['frontier']['open_selection']['type_counts'].get('pretrained', 0) > 0
    assert r4['c8_aggregation']['n_excluded_from_ranking'] == 6
    assert all(all(v is not None for v in scores.values()) for scores in r4['c8_aggregation']['top5_frontier_radar'].values())
    report = {'status': 'PASS', 'elasticity_finite_difference_max_error': max(eps_errors),
              'profile_vs_slsqp': rows,
              'timing_9_budgets_seconds': {'profile': profile_seconds, 'slsqp_20_starts': slsqp_seconds},
              'speed_ratio': slsqp_seconds / profile_seconds,
              'limits': '外层网格与独立SLSQP一致性不等于数学全局最优证明；远期区间未得到长期回测验证'}
    u.save_json(report, 'review_q234/verification.json')
    print('PASS: finite differences, finite increments, 9 budget comparisons, quality boundaries, bridge and forecast checks')
    print('speed ratio', report['speed_ratio'])
    return report


if __name__ == '__main__':
    main()
