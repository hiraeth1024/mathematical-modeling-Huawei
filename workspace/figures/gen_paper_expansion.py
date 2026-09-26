# -*- coding: utf-8 -*-
"""Reproducible supplementary figures/tables from saved results and stated formulas."""
from pathlib import Path
import hashlib
import json
import sys
import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'code'))
from _figbase import load, save_fig, set_paper_placement, PALETTE, COLORS, cn, declutter_axes, panel
from problem3 import solve_fixed_quality, solve_budget, loss_gen
from params import UNIT_SCALE, ETA

p1,p2,p3,p4 = [load(f'problem_{i}_results.json') for i in range(1,5)]
sens = load('q3_assumption_sensitivity.json')
ws = json.loads((ROOT/'output/q1_weight_sensitivity.json').read_text())
params = tuple(p3['scaling_params'][k] for k in ['E','A','alpha','B','beta','theta'])
E,A,alpha,B,beta,theta=params
q0=p3['Q0']; k=UNIT_SCALE**2*(6+ETA*2048)
report = {'source_hashes':{},'derived':{},'checks':{}}
for f in ['problem_1_results.json','problem_2_results.json','problem_3_results.json','problem_4_results.json','q3_assumption_sensitivity.json']:
    report['source_hashes']['figures/'+f]=hashlib.sha256((HERE/f).read_bytes()).hexdigest()
report['source_hashes']['output/q1_weight_sensitivity.json']=hashlib.sha256((ROOT/'output/q1_weight_sensitivity.json').read_bytes()).hexdigest()

def axes(n=1, height=3.6):
    fig, axs=plt.subplots(n,1,figsize=(6.4,height),layout='constrained')
    set_paper_placement(fig)
    return fig,axs

def save(fig,name):
    save_fig(fig, 'figures/'+name+'.pdf'); plt.close(fig)

def table(name,caption,label,spec,header,rows):
    lines=[r'\begin{table}[!htbp]',r'\centering',r'\songti\zihao{-4}',r'\setlength{\tabcolsep}{4pt}',r'\caption{'+caption+'}',r'\label{'+label+'}',r'\begin{tabular}{'+spec+'}',r'\toprule',header+r' \\',r'\midrule']
    lines += [r' & '.join(row)+r' \\' for row in rows]
    lines += [r'\bottomrule',r'\end{tabular}',r'\end{table}']
    (HERE/name).write_text('\n'.join(lines)+'\n',encoding='utf-8')

# Q1: every point is a declared weight setting, never a random confidence sample.
sc=ws['scenarios']; q=np.array([x['Q0'] for x in sc]); tau=np.array([x['domain_kendall'] for x in sc])
fig,ax=axes()
pts=ax.scatter(q,tau,c=[x['group_weights']['model'] for x in sc],cmap='YlOrRd',s=65,edgecolors='white',linewidths=.6)
ax.axvline(q0,color=COLORS['down'],linestyle='--',linewidth=1.3,label=cn('主方案 $Q_0$=%.5f'%q0))
ax.set(xlabel=cn('七域质量中位数 $Q_0$'),ylabel=cn('域序 Kendall 相关'))
ax.set_ylim(.35,1.06);declutter_axes(ax,grid='y');ax.legend(frameon=False,fontsize=9)
cb=fig.colorbar(pts,ax=ax,pad=.03);cb.set_label(cn('模型评分组权重'))
save(fig,'fig_q1_weight_robustness')
rows=[]
for domain,d in sorted(p1['conflict']['by_domain'].items(),key=lambda kv:-kv[1]['rate']):
    rows.append([domain,str(d['n']),str(d['n_conflict']),f"{100*d['rate']:.4f}\\%"])
table('TABLE_q1_conflict_domains.tex','A1 各域冲突计数与域内发生率','tab:q1-conflict-domains','lrrr','来源域 & 样本数 & 冲突数 & 域内冲突率',rows)

# Q2: aggregated RMSE is a sample-count-weighted mean of squared errors.
by=p2['generalized']['holdout_by_source']; names=list(by)
fig,ax=axes();x=np.arange(len(names));width=.32
for off,key,lab,col in [(-width/2,'rmse_generalized','含质量模型',PALETTE[0]),(width/2,'rmse_no_quality','无质量独立拟合',PALETTE[1])]:
    vals=[by[n][key] for n in names];bars=ax.bar(x+off,vals,width,color=col,label=cn(lab))
    ax.bar_label(bars,fmt='%.3f',padding=3,fontsize=8)
ax.set_xticks(x);ax.set_xticklabels([f"{n} (n={by[n]['n']})" for n in names]);ax.set_ylabel(cn('分来源留出 RMSE（nats/token）'));ax.set_ylim(0,1.5);declutter_axes(ax,grid='y');ax.legend(frameon=False,fontsize=9)
save(fig,'fig_q2_source_validation')
rows=[]
for name,d in by.items(): rows.append([name,str(d['n']),f"{d['rmse_generalized']:.4f}",f"{d['rmse_no_quality']:.4f}",f"{(d['rmse_no_quality']-d['rmse_generalized']):+.4f}"])
table('TABLE_q2_source_validation.tex','同一分组留出集上的来源分层误差','tab:q2-source-validation','lrrrr','来源 & 留出数 & 含质量 RMSE & 无质量 RMSE & 后者减前者',rows)
for key,total in [('rmse_generalized','rmse_holdout_generalized'),('rmse_no_quality','rmse_holdout_classic_baseline')]:
    actual=np.sqrt(sum(d['n']*d[key]**2 for d in by.values())/sum(d['n'] for d in by.values()))
    assert np.isclose(actual,p2['generalized'][total],atol=1e-12)
report['checks']['grouped_rmse_aggregation']=True

# Exact iso-loss substitution at the paper reference point.
ref=p2['elasticity']['reference_point']; nref=ref['N0'];dref=ref['D0'];lref=ref['L0']
dq=np.linspace(0,.25,101); qq=q0+dq
nn=(A/(lref-E-B*(qq**theta*dref)**(-beta)))**(1/alpha)
linear=nref+p2['elasticity']['substitution_dN_dQ']*dq
assert np.max(np.abs([loss_gen(n,dref,q,params)-lref for n,q in zip(nn,qq)]))<1e-12
fig,ax=axes();ax.plot(dq,nref-nn,color=PALETTE[0],lw=2,label=cn('精确等损失节省量'));ax.plot(dq,nref-linear,color=PALETTE[1],ls='--',lw=1.7,label=cn('参考点线性近似'))
ax.set(xlabel=cn('质量增量 $\\Delta Q$'),ylabel=cn('参数节省量（十亿参数）'));declutter_axes(ax,grid='y');ax.legend(frameon=False,fontsize=9)
save(fig,'fig_q2_finite_substitution')
report['checks']['exact_iso_loss_identity']=True

# Closed form fixed-Q baseline, compared to existing numerical solutions.
rows=[];closed_errors=[]
for c in p3['optimal_allocation']['budgets']:
    key=f'{c:.0e}';ns=(alpha*A/(beta*B)*q0**(theta*beta)*(c/k)**beta)**(1/(alpha+beta));ds=c/(k*ns)
    base=p3['optimal_allocation']['baseline_fixed_quality'][key]
    closed_errors.append(abs(ns-base['N'])/base['N'])
    rows.append([r'$10^{%d}$'%round(np.log10(c)),f'{ns:.4f}',f'{ds:.3f}',f'{ds/ns:.2f}',f"{base['L']:.5f}"])
assert max(closed_errors)<1e-10
report['checks']['fixed_quality_closed_form_max_relative_error']=max(closed_errors)
table('TABLE_q3_closed_form.tex','固定基线质量下的解析配置与数据参数比','tab:q3-closed','rrrrr','$C$ (FLOPs) & $N_0^*$ (B) & $D_0^*$ (B) & $D_0^*/N_0^*$ & $L_0^*$',rows)

st=p3['structural_transition']; budgets=np.array(st['C_grid']);opt=np.array(st['L_traj']);fixed=[];equal=[]
for c in budgets:
    fixed.append(solve_fixed_quality(float(c),q0,q0,params,2048,'exp')['L'])
    nd=np.sqrt(c/k);equal.append(loss_gen(nd,nd,q0,params))
fixed=np.array(fixed);equal=np.array(equal);quality=np.maximum(fixed-opt,0);allocation=equal-fixed
assert np.all(allocation>=-1e-10)
fig,(ax1,ax2)=axes(2,5.6)
ax1.plot(np.log10(budgets),allocation,color=PALETTE[1],lw=1.8,label=cn('固定质量下的规模配比改善'))
ax1.plot(np.log10(budgets),quality,color=PALETTE[0],lw=1.8,label=cn('放开质量决策的净改善'))
ax1.set_ylabel(cn('损失下降量（nats/token）'));ax1.legend(frameon=False,fontsize=8.5);panel(ax1,'(a)');declutter_axes(ax1,grid='y')
ax2.plot(np.log10(budgets),100*quality/(fixed-E),color=PALETTE[0],lw=1.8)
ax2.set(xlabel=cn('预算 $\\log_{10} C$（FLOPs）'),ylabel=cn('占可约损失的改善（%）'));panel(ax2,'(b)');declutter_axes(ax2,grid='y')
save(fig,'fig_q3_gain_decomposition')
report['derived']['quality_gain_budget_scan']={'C':budgets.tolist(),'quality_gain':quality.tolist(),'allocation_gain':allocation.tolist()}

# Profiles: loss increase relative to the joint optimum, not statistical uncertainty.
fig,axs=plt.subplots(1,3,figsize=(8.0,3.0),layout='constrained');set_paper_placement(fig)
profiles={}
for ax,c in zip(axs,p3['optimal_allocation']['budgets']):
    qs=np.linspace(q0,1,129);sol=[solve_fixed_quality(c,float(q),q0,params,2048,'exp') for q in qs];ls=np.array([s['L'] for s in sol]);best=p3['optimal_allocation']['by_gtype']['exp'][f'{c:.0e}']
    ax.plot(qs,100*(ls-best['L'])/(best['L']-E),color=PALETTE[0],lw=1.7)
    ax.axvline(best['Q'],color=COLORS['down'],ls='--',lw=1)
    ax.set_xlabel(cn('固定质量 $Q$'));ax.set_title(r'$C=10^{%d}$'%round(np.log10(c)),fontsize=10);declutter_axes(ax,grid='y')
    profiles[f'{c:.0e}']={'Q':qs.tolist(),'L':ls.tolist()}
axs[0].set_ylabel(cn('相对可约损失增加（%）'));save(fig,'fig_q3_quality_profiles');report['derived']['quality_profiles']=profiles

# Reconstruct the documented expanding-window backtest, never fit on future observations.
hf=p4['frontier']['historical_frontier'];t=np.array(hf['t']);cap=np.array(hf['cap']);pred=[]
for i in range(5,len(t)):
    design=np.column_stack([np.ones(i),t[:i]-t[i-1]])
    coef=np.linalg.lstsq(design,cap[:i],rcond=None)[0]
    pred.append(float(coef[0]+coef[1]*(t[i]-t[i-1])))
pred=np.array(pred);observed=cap[5:];last=cap[4:-1]
errors=pred-observed;last_errors=last-observed
back=p4['frontier']['one_step_backtest']
assert np.isclose(np.abs(errors).mean(),back['trend_mae'],atol=1e-9)
assert np.isclose(np.abs(last_errors).mean(),back['last_value_mae'],atol=1e-9)
rows=[[f'{ti:.3f}',f'{y:.3f}',f'{a:.3f}',f'{b:.3f}',f'{e:+.3f}'] for ti,y,a,b,e in zip(t[5:],observed,pred,last,errors)]
table('TABLE_q4_backtest.tex','扩展窗口的一步预测与实测前沿','tab:q4-backtest','rrrrr','测试时间 & 实测 & 趋势预测 & 末值预测 & 趋势误差',rows)
fig,(ax1,ax2)=axes(2,5.4)
ax1.plot(t,cap,'o-',color=COLORS['text'],ms=4,lw=1.5,label=cn('实测月度前沿'))
ax1.plot(t[5:],pred,'s--',color=PALETTE[0],ms=5,label=cn('一步趋势预测'))
ax1.plot(t[5:],last,'^:',color=PALETTE[1],ms=5,label=cn('末值延续'))
ax1.set_ylabel(cn('六维基准均分'));ax1.legend(frameon=False,fontsize=8);declutter_axes(ax1,grid='y');panel(ax1,'(a)')
x=np.arange(5);w=.32
ax2.bar(x-w/2,errors,w,color=PALETTE[0],label=cn('趋势误差'));ax2.bar(x+w/2,last_errors,w,color=PALETTE[1],label=cn('末值误差'));ax2.axhline(0,color=COLORS['text'],lw=.8)
ax2.set_xticks(x);ax2.set_xticklabels([f'{v:.2f}' for v in t[5:]],fontsize=8);ax2.set(xlabel=cn('测试月份（小数年）'),ylabel=cn('预测减实测（点）'));ax2.legend(frameon=False,fontsize=8);declutter_axes(ax2,grid='y');panel(ax2,'(b)')
save(fig,'fig_q4_rolling_validation')
report['derived']['backtest']={'t':t[5:].tolist(),'observed':observed.tolist(),'trend':pred.tolist(),'last_value':last.tolist(),'trend_errors':errors.tolist()};report['checks']['backtest_matches_saved_metrics']=True

fig,ax=axes(height=4.0)
labels={'chat_finetuned':'对话/微调','merged':'合并','pretrained':'预训练'}
rows=[]
for i,(kind,label) in enumerate(labels.items()):
    d=p4['frontier']['by_model_type'][kind]
    ax.plot(d['t'],d['cap'],marker=['o','s','^'][i],ms=4,lw=1.4,color=PALETTE[i],label=cn(f'{label} (n={d["n"]})'))
    rows.append([label,str(d['n']),str(min(d['monthly_n'])),str(max(d['monthly_n'])),f"{d['slope']:+.2f}"])
ax.plot(t,cap,'--',color=COLORS['text'],lw=1.5,label=cn('全样本前沿'))
ax.set(xlabel=cn('提交时间（年，小数）'),ylabel=cn('月度第90百分位'));ax.legend(frameon=False,fontsize=8.5,ncol=2);declutter_axes(ax,grid='y')
save(fig,'fig_q4_type_frontiers')
table('TABLE_q4_type_frontiers.tex','按模型类型分层的前沿样本与线性斜率','tab:q4-type-frontiers','lrrrr','类型 & 总记录 & 月最少 & 月最多 & 斜率（点/年）',rows)

# Scenario comparison at the middle budget: both baseline and response are shown.
rows=[]
for name,d in sens['scenarios'].items():
    s=d['by_budget']['1e+22'];label={'baseline':'基准','Q0_minus20pct':r'$Q_0$ 降20\%','Q0_plus20pct':r'$Q_0$ 升20\%','theta_0.2':r'$\theta=0.2$','theta_0.8':r'$\theta=0.8$'}[name]
    rows.append([label,f"{s['N']:.3f}",f"{s['D']:.2f}",f"{s['Q']:.4f}",f"{s['Q']-d['Q0']:.4f}"])
table('TABLE_q3_sensitivity_full.tex','中档预算下的配置敏感性：绝对质量与增量质量','tab:q3-sensitive-full','lrrrr','情景 & $N^*$ (B) & $D^*$ (B) & $Q^*$ & $Q^*-Q_0$',rows)

report['status']='PASS';(ROOT/'review_expansion/derived_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Supplementary artifacts generated; formula and backtest checks PASS')
