from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import hashlib,json
base=Path(__file__).resolve().parent
ref=next(base.glob('*.docx'))
output=base.parents[1]/'paper/build/华为杯论文模板_已填摘要.docx'
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';ns={'w':W}
def tag(n):return '{'+W+'}'+n
def el(n,**a):
 e=E.Element(tag(n))
 for k,v in a.items():e.set(tag(k),str(v))
 return e
def child(parent,n,**a):
 e=parent.find(tag(n))
 if e is None:e=E.SubElement(parent,tag(n))
 for k,v in a.items():e.set(tag(k),str(v))
 return e
paras=[
'在总算力受限条件下，模型规模、数据数量与质量及上下文长度共同影响大语言模型的训练损失与能力。本文围绕数据质量评价、广义标度律、资源配置和能力前沿构建递进模型，区分附件统计、参数估计与条件情景，分析各类投入的收益及适用边界。',
'针对问题一，对22项指标进行语义解码，采用A1固定经验分位归一化与三组平衡赋权，建立可复算的质量评分。七域质量中位数为0.487876；按高教育价值与广告判定冲突的规则，总冲突率为0.303%，C4域内冲突率最高，为1.03%。权重敏感性分析揭示域排序对评分假设的依赖，配比回归的跨尺度预测仍有局限。',
'针对问题二，采用Huber稳健损失与多起点拟合估计经典标度律，并以质量加权的有效数据量扩展广义模型，推导弹性及等损失替代关系。在相同设置分组留出下，含质量模型的均方根误差为0.675，低于无质量基线的0.784，但改善主要来自B8。鉴于质量标度尚未统一校准，下游将质量指数0.5作为结构性假设并开展敏感性分析。',
'针对问题三，将基础训练、质量提升与注意力开销纳入统一预算，结合KKT条件、预算消元与质量剖面搜索求解，并用独立SLSQP核验。在指数型质量成本下，预算为10¹⁹、10²²、10²⁴ FLOPs时，候选质量分别为0.506、0.967、1.000，损失分别为3.073、2.151、1.914。闭式基线与收益分解进一步区分规模配置收益和质量提升收益；注意力开销与基础训练开销相当的上下文长度为30,000 tokens。',
'针对问题四，采用描述性增长分解、分层单调桥接及月度前沿Bootstrap，计算停滞、放缓和维持趋势三类情景。在五次一步滚动检验中，趋势模型平均绝对误差为1.773，高于末值基线的1.475，因此远期区间仅作条件情景解释。结果表明，资源配置应同时考虑质量收益、处理成本和边界约束；评分与训练收益的联合校准及外部预测验证仍需更多真实数据。'
]
keywords='关键词：数据质量评价；广义标度律；算力约束；资源配置；能力前沿'
with ZipFile(ref) as z:parts={n:z.read(n) for n in z.namelist()}
root=E.fromstring(parts['word/document.xml']);body=root.find('w:body',ns);ps=body.findall('w:p',ns)
assert '题' in ''.join(ps[15].itertext()) and '摘' in ''.join(ps[16].itertext())
def format_run(r,font,size,bold=False):
 rp=child(r,'rPr');rf=child(rp,'rFonts',ascii='Times New Roman',hAnsi='Times New Roman',eastAsia=font,cs='Times New Roman')
 for k in list(rf.attrib):
  if 'Theme' in k:del rf.attrib[k]
 child(rp,'sz',val=size*2);child(rp,'szCs',val=size*2);child(rp,'b',val='1' if bold else '0');child(rp,'bCs',val='1' if bold else '0');child(rp,'color',val='000000')
# Keep the complete second template heading on the abstract page.
child(child(ps[12],'pPr'),'pageBreakBefore')
# Explicit typography requested by the author, retaining the template's title underline.
for r in ps[15].findall('w:r',ns):format_run(r,'黑体',16)
for r in ps[16].findall('w:r',ns):format_run(r,'黑体',14)
for p in [ps[15],ps[16]]:
 child(child(p,'pPr'),'keepNext')
# Fill the existing blank abstract slot and insert ordinary continuation paragraphs.
slot=ps[17];index=list(body).index(slot);body.remove(slot)
for j,text in enumerate(paras+[keywords]):
 p=el('p');pp=E.SubElement(p,tag('pPr'));pp.append(el('pStyle',val='Normal'));pp.append(el('widowControl'));pp.append(el('snapToGrid',val='0'));pp.append(el('spacing',before='0',after='90' if j<len(paras) else '0',line='300',lineRule='exact'));pp.append(el('ind',firstLine='480' if j<len(paras) else '0'));pp.append(el('jc',val='both' if j<len(paras) else 'left'))
 r=E.SubElement(p,tag('r'));format_run(r,'宋体',12);E.SubElement(r,tag('t')).text=text;body.insert(index+j,p)
parts['word/document.xml']=E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(output,'w') as z:
 for n,b in parts.items():z.writestr(n,b)
with ZipFile(ref) as a,ZipFile(output) as b:
 changed=[n for n in a.namelist() if a.read(n)!=b.read(n)]
 assert changed==['word/document.xml'],changed
(base/'artifact.md').write_text(f'''# 摘要模板编辑记录

参考文件：{ref}
SHA-256：{hashlib.sha256(ref.read_bytes()).hexdigest()}
保留：封面标识、学校/队号/队员信息、表格、页眉页脚、样式表及全部媒体关系。
页面：A4，1节，左右1276/1274 twips，上下1702/1048 twips；保留原设置。
编辑位置：word/document.xml，body直接子段落第15/16/17（零起点）分别为题目、摘要标题和空白摘要位。
字体：按用户既有要求，题目16pt黑体、摘要标题14pt黑体居中、摘要与关键词12pt宋体；正文首行缩进24pt、行距15pt。
有意调整：第二套竞赛抬头（第12段）增加段前分页，避免抬头跨封面和摘要页。
正文内容基于当前论文四问结论及验证记录，共5段，附关键词。
仅document.xml改变，其他包部件逐字节一致。原doc与转换参考docx保留。
''')
(base/'abstract_text.txt').write_text('\n\n'.join(paras+[keywords]))
print(output);print('Characters',sum(map(len,paras)), 'changed package parts',changed)
