# 能力清单验收总账（逐项）

- ✅ **P1-C1** [machine] PASS — 产物 output/q1_quality_scores.csv 已产出（1830687 bytes；仅验证交付存在，不代表内容正确）
- ✅ **P1-C2** [semantic] PASS — 结论 PASS —— code/problem1.py:entropy_weights(式3)+compute_Q(式4); main Step1读A1全量51230(read_jsonl_xz断言n=51230), Step3读A2 17523/A3 203752全量算域级Q; figures/problem_1_results.json domain_Q_A1/domain_Q_extended
- ✅ **P1-C3** [semantic] PASS — 结论 PASS —— code/problem1.py:_q1_conflict 式5可计算判据(fineweb_edu与ad_content双高分位0.8), Spearman=0.139, 冲突率4.96%; 消解降权delta=0.5+Kendall tau前后对比
- ✅ **P1-C4** [machine] PASS — 产物 output/q1_mixture_model.json 已产出（1866 bytes；仅验证交付存在，不代表内容正确）
- ✅ **P1-C5** [semantic] PASS — 结论 PASS —— code/problem1.py:_q1_domain_map 读A16 domain_mapping_guide.csv(17行); by_type={direct:3,near_direct:3,inferred:11}; inferred_handling显式保留为解释变量不丢弃
- ✅ **P2-C1** [machine] PASS — 产物 output/q2_classic_scaling.json 已产出（49606 bytes；仅验证交付存在，不代表内容正确）
- ✅ **P2-C2** [semantic] PASS — 结论 PASS —— code/problem2.py:generalized_model Q_eff=Q**theta*D(式9); _p2_generalized用B6-B8(360+450+1704含Q_score)拟合theta; Q1退化 rel_err=0.0<0.001
- ✅ **P2-C3** [semantic] PASS — 结论 PASS —— code/problem2.py:_p2_elasticity 式11-12解析弹性eps_N/eps_D/eps_Q均<0; 式13替代率dN/dQ|_L=-1.31代入拟合参数; delta_N_for_deltaQ_0.1数值给出
- ✅ **P3-C1** [machine] PASS — 结论 PASS —— code/problem3.py:solve_budget SLSQP多起点(n_starts=20)+NonlinearConstraint装预算式; 三型g×三档预算; constraint_audit.py重代入预算式全PASS; output/q3_optimal_allocation.json
- ✅ **P3-C2** [semantic] PASS — 结论 PASS —— code/problem3.py:_q3_transition 连续扫描logC∈[18,25](36点), ds_Q/d(logC)数值差分(式18)峰值定转移点C†≈2.5e22; KKT活跃集监控(Q内点↔边界,C_Q铰链激活)
- ✅ **P3-C3** [machine] PASS — 结论 PASS —— code/problem3.py:_q3_lctx 扫描LCTX_SET={2048,4096,8192,32768,131072}(严格C7实测集); Lctx_crit=6/eta=3e4解析核验; s_attn随L_ctx 0.058→0.776; output/q3_lctx_sensitivity.json
- ✅ **P4-C1** [semantic] PASS — 结论 PASS —— code/problem4.py:_p4_decomp OLS Cap~lnN+year控制规模(lnN=参数)后time项=非规模; 增长核算Δf/Δh占比和=100%; C4开源字段Epoch_AI_Open_Weights(443条)标注
- ✅ **P4-C2** [machine] PASS — 产物 output/q4_bridge_model.json 已产出（7073 bytes；仅验证交付存在，不代表内容正确）
- ✅ **P4-C3** [semantic] PASS — 结论 PASS —— code/problem4.py:_p4_frontier P90前沿包络+Bootstrap分位带(P10/P50/P90); 三情景(low/mid/high算力增速)显式; C4历史算力增速5.1×/年锚定情景; 口径声明(mean6/Hub License/Type/Submission Date)
- ✅ **P4-C4** [machine] PASS — 结论 PASS —— code/problem4.py:_p4_c8 遍历detailed_results/ 1863目录glob JSON逐任务六维; 解析1860目录(六维完整1854), 损坏跳过7计数; output/q4_task_aggregation.csv(1860行)