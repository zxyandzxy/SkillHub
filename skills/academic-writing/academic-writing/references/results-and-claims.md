# 结果叙述、证据强度与全文一致性

在撰写 Results、Discussion、结论或涉及实验数值的 Introduction / Abstract 时读取。若实验数据或评价协议本身不可信，先由研究者确认，不能通过改写叙述将其变成可靠证据。

## 一、写结果前先核对的事实

明确：当前结果是否为正式实验，采用什么任务/数据版本，指标定义和方向是什么，样本分母是什么，对照是否匹配，重复运行是否为独立观察，失败和缺失如何处理，以及图表数据是否来自同一配置。只有源材料支持的数值才可进入论文。

## 二、对每个 RQ 的写作次序

1. **直接回答**：在明确范围和比较对象下，结果方向与主要结论是什么。
2. **观察与幅度**：报告最能体现差异的原始量、绝对差、比例/百分点及必要分布。不要只报告“提升显著”。
3. **不确定性**：只在数据与实验设计允许时描述置信区间、重复波动或统计检验；没有逐任务配对数据不能擅自进行配对显著性断言。
4. **研究含义**：解释观察如何回答预设 RQ、实际成本/收益和可解释的作用机制。
5. **反例与范围**：如存在真实反例、重要竞争解释或适用边界，在与结论有关的位置准确交代；完整有效性威胁分析归入适当章节。

如果结果与作者预计不同，忠实报告观察并说明哪些解释仍需验证，不修改分析口径或选择性排除样本。

## 三、公开案例：Agentless 的补丁筛选消融

以下数字属于已发表论文报告，**不是 SkillHub 自己运行的实验**。来源：Xia 等，*Agentless: Demystifying LLM-based Software Engineering Agents*，FSE 2025，论文 Table 4；检索入口：https://arxiv.org/abs/2407.01489 。请在真实投稿中重新核对所使用论文版本。

| Patch selection 配置 | 成功数 | 率 | 论文报告的额外平均成本 |
| --- | ---: | ---: | ---: |
| Majority voting | 77/300 | 25.67% | $0.00 |
| + Regression tests | 81/300 | 27.00% | $0.01 |
| + Reproduction tests | 96/300 | 32.00% | $0.25 |

示范性英文叙述（本 SkillHub 自行撰写，不是论文原句）：

> On the 300-issue SWE-bench Lite benchmark, majority voting yields 77 resolved issues (25.67%). Adding regression-test screening increases this count to 81 (27.00%), and further incorporating reproduction-test screening raises it to 96 (32.00%). The final configuration resolves 15 more issues than the regression-screened configuration, a gain of 5.00 percentage points, with an additional average patch-selection cost reported as $0.25 per issue. These results show that the test-based selection stages improve the outcome under the evaluated candidate-patch and benchmark settings.

这段表达包含四种不同性质的信息：任务与分母、每个配置的观察数值、实际绝对差异、被实验设置支持的结论。它不因三组总成功数就宣称“统计显著”，也不从总量直接推断每个补丁失败的具体机制。若要证明机制，需要逐任务的补丁筛选记录、可靠的对照或消融支持。

简短修订判断示例：

- “Results improve by 5%”含糊；若数据是从 27.00% 到 32.00%，应写 **5.00 percentage points**；若要给相对提升，明确使用 `(32−27)/27`。
- “Reproduction tests prove the mechanism”过强；只有配置性能总表时，可以写“the result supports the utility of reproduction-test screening under the evaluated setting”。
- 论文表格已有各配置全部数字时，正文只强调主要差异与研究含义，不逐格复述。

## 四、主张强度与行文位置

- **数据事实**：某指标在指定条件下取某值；使用原始数据或可信正式发表来源核对。
- **允许的比较**：在相同或已解释的对照条件下报告高低与幅度。
- **机制线索**：有消融或针对性证据时表述为某机制可能解释结果；不把相关性当因果。
- **更广泛结论**：需要跨数据、方法、成本或模型的额外实证证据；当前结果不够时只在其真实范围内陈述。

正面且充分支持的发现应当正面表达。重要条件可以在 Results / Setup 直接出现，而系统性的局限解释放在 Discussion 或 Threats to Validity；不要为了语气积极而删掉会改变读者判断的条件。

## 五、全文一致性核查

核对标题/摘要/贡献/RQ/方法承诺/结果/Discussion/结论的主张是否一致。进一步检查：

- 样本数、分母、数据版本、Baseline 名称、指标方向、单位、百分比与百分点；
- 公式定义、统计单位、重复次数、缺失/失败规则与实验实际记录；
- 图表编号、描述、图注和正文引用是否指向同一证据；
- 相关工作主张是否真实由所引文献支持，不能因当前稿件措辞顺畅就视为已核实；
- 结果变动后是否同步更新受影响的摘要、贡献和结论。

发现冲突时回到权威来源或明确提交作者决定，不能在两个不一致值间自行折中，也不能为达成预定结论改动原始数据。

本参考负责**写作中的相关证据核对**；逐条追溯所有引用、原始实验和跨产物数字的完整审计，应交由 `research-integrity-audit` 专项执行。
