# SkillHub Skills 索引

根据当前任务选择最相关的 Skill，先读取 `SKILL.md`，再按需读取参考资料；不用一次加载全部 Skills。与每项 Skill 同名的 `RESEARCH.md` 解释方法形成的依据。

## 技术内容表达（`technical-content`）

| Skill | 适用任务与触发说明 | 指令 | 研究依据 |
| --- | --- | --- | --- |
| `interactive-explainers` | 设计、实现或检查通过滑块、按钮、可视状态、计算和动画解释技术机制的交互式教学内容。只有可控状态变化本身帮助理解算法、系统或科学概念时使用；只有导航、折叠、静态图表的长报告使用 reading-first-reports。 | [SKILL.md](skills/technical-content/interactive-explainers/SKILL.md) | [RESEARCH.md](research/technical-content/interactive-explainers/RESEARCH.md) |
| `reading-first-reports` | 创建、修改或检查可独立阅读的长篇 HTML 技术报告、研究总结与交互较少的在线文档，处理目录、深链接、引用、响应布局和打印 PDF。读者主要沿连续正文理解内容时使用；逐页演示选择 technical-presentations，状态驱动教学选择 interactive-explainers。 | [SKILL.md](skills/technical-content/reading-first-reports/SKILL.md) | [RESEARCH.md](research/technical-content/reading-first-reports/RESEARCH.md) |
| `technical-presentations` | 研究论文讲解、科研进展和其他技术演示的逐页内容组织与实际页面制作。用于解释论文背景与机制、编写可独立阅读的 PPT 文稿、修改现有演示，以及按需制作和检查 PPTX、HTML 或 PDF；不强制先生成幻灯片文件。 | [SKILL.md](skills/technical-content/technical-presentations/SKILL.md) | [RESEARCH.md](research/technical-content/technical-presentations/RESEARCH.md) |
| `technical-writing` | 撰写、重组或精修技术文章、教程、概念解释、领域综述及论文面向工程读者的改写；涉及读者先备知识、贯穿实例、来源保持和技术说明时使用。面向学术投稿的正文改写使用 academic-writing。 | [SKILL.md](skills/technical-content/technical-writing/SKILL.md) | [RESEARCH.md](research/technical-content/technical-writing/RESEARCH.md) |

## 学术成果（`academic-writing`）

| Skill | 适用任务与触发说明 | 指令 | 研究依据 |
| --- | --- | --- | --- |
| `academic-writing` | 为计算机科学与软件工程研究论文撰写、重组、修改或精修摘要、引言、相关工作、方法、实验、结果、讨论及结论。适用于投稿论文的论证组织、段落写作、学术英文、LaTeX 局部编辑和全文主张一致性检查；不负责独立审稿、审稿回复、生成研究数据或重做实验设计。 | [SKILL.md](skills/academic-writing/academic-writing/SKILL.md) | [RESEARCH.md](research/academic-writing/academic-writing/RESEARCH.md) |
| `independent-paper-review` | 对计算机科学论文进行独立学术评审、投稿前审查、修订版本评审或模拟审稿，判断问题价值、原创性、技术有效性、实验设计、证据强度与表达质量。用户明确要求评审、审稿人视角或论文准备度判断时使用；普通正文修改用 academic-writing，数值引用专项核查用 research-integrity-audit。 | [SKILL.md](skills/academic-writing/independent-paper-review/SKILL.md) | [RESEARCH.md](research/academic-writing/independent-paper-review/RESEARCH.md) |
| `paper-revision-response` | 分析期刊或会议审稿意见、确定论文修改策略、检查补充证据、生成作者可审阅的 LaTeX 原文/改后对照与双语译文，并撰写逐条审稿回复。仅在实际收到审稿意见或准备大修、Rebuttal、Response Letter 时使用。 | [SKILL.md](skills/academic-writing/paper-revision-response/SKILL.md) | [RESEARCH.md](research/academic-writing/paper-revision-response/RESEARCH.md) |
| `research-figures-tables` | 规划、制作或修改计算机科学和 AI 研究论文的动机/案例图、方法架构与数据流图、实验曲线、统计图、消融表及 LaTeX 表格。适用于整篇论文的图表规划、公开论文图表研究、可编辑源制作、图表与正文核对、真实排版下的视觉检查。按研究主张与原始证据选择表达方式；不设计新实验、不修改统计协议，也不凭生成式图像创造精确数据或方法拓扑。 | [SKILL.md](skills/academic-writing/research-figures-tables/SKILL.md) | [RESEARCH.md](research/academic-writing/research-figures-tables/RESEARCH.md) |
| `research-integrity-audit` | 核对学术稿件的引用、主张、实验数字、样本量、指标、统计单位、图表、配置和原始结果，发现可定位的证据不一致。请求核查论文事实、实验数值或投稿前诚信检查时使用；广泛文献综述与整体学术审稿由其他 Skill 承担。 | [SKILL.md](skills/academic-writing/research-integrity-audit/SKILL.md) | [RESEARCH.md](research/academic-writing/research-integrity-audit/RESEARCH.md) |

## 科研工作流（`research`）

| Skill | 适用任务与触发说明 | 指令 | 研究依据 |
| --- | --- | --- | --- |
| `dataset-benchmark-engineering` | 构建或实质性扩展科研数据集、Benchmark、标注、评估任务或知识资产，覆盖来源版本、质量核验、测试有效性、数据泄漏、许可、信息可见性和发布边界；简单复用现成数据集不触发完整构建流程。 | [SKILL.md](skills/research/dataset-benchmark-engineering/SKILL.md) | [RESEARCH.md](research/research/dataset-benchmark-engineering/RESEARCH.md) |
| `experimental-analysis` | 分析真实科研实验结果与消融，核查任务单位、分母、配对、失败/缺失和统计口径，回答 RQ、解释效应与不确定性、检查机制证据及反例，形成有边界的论文结论；不修改正式实验协议。 | [SKILL.md](skills/research/experimental-analysis/SKILL.md) | [RESEARCH.md](research/research/experimental-analysis/RESEARCH.md) |
| `literature-research` | 围绕计算机科学或软件工程问题检索、核验、筛选和深读学术文献；需要寻找最近工作、检查论文发表状态、追踪引文、比较方法机制或建立有出处的综述时使用。不会独自宣告研究 Idea 全球首创。 | [SKILL.md](skills/research/literature-research/SKILL.md) | [RESEARCH.md](research/research/literature-research/RESEARCH.md) |
| `research-design` | 把选定的科研 Idea 转化成可执行的研究问题、主张—证据对应、Baseline、公平比较、数据与指标、统计单位、消融和正式实验协议；用于实验设计或复核，不负责实际运行或在见到正式结果后更改研究口径。 | [SKILL.md](skills/research/research-design/SKILL.md) | [RESEARCH.md](research/research/research-design/RESEARCH.md) |
| `research-engineering` | 实现科研方法与 Baseline、复现代码、执行 Pilot 或经授权的正式实验、诊断实验故障并保存可追溯原始结果；重视协议保真、稳定实验身份、失败记录和中断恢复，不自行更改研究方案或解释论文主张。 | [SKILL.md](skills/research/research-engineering/SKILL.md) | [RESEARCH.md](research/research/research-engineering/RESEARCH.md) |
| `research-ideation` | 依据真实问题、已核验文献与现有方法不足，形成或反向挑战计算机科学研究 Idea；适用于研究空白分析、创新机制、Idea 筛选、最近竞争工作比较、可证伪预测与低成本可行性判断。完整实验协议交给 research-design。 | [SKILL.md](skills/research/research-ideation/SKILL.md) | [RESEARCH.md](research/research/research-ideation/RESEARCH.md) |

## 软件工程（`software-engineering`）

| Skill | 适用任务与触发说明 | 指令 | 研究依据 |
| --- | --- | --- | --- |
| `clean-code-guide` | 编写、修改或重构代码时采用小而完整的改动、适当抽象、清晰职责和实际证据；适用于编码实现、局部重构和变更后自查。仅处理任务相关内容，不自动开展全仓资产治理或专项安全审计。 | [SKILL.md](skills/software-engineering/clean-code-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/clean-code-guide/RESEARCH.md) |
| `code-review-guide` | 对代码、Pull Request、提交或工作区差异进行只读评审，检查是否符合真实需求、引入哪些工程风险，以及测试与交付证据是否充分；也用于核查收到的评审意见。评审本身不授权自动修改、提交或合并。 | [SKILL.md](skills/software-engineering/code-review-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/code-review-guide/RESEARCH.md) |
| `debugging-guide` | 程序报错、测试失败、偶发故障、功能回归或异常性能现象需要定位原因和修复时使用，遵循复现、观测、可证伪假设、最小修复与回归验证。预防性的超时幂等和恢复设计使用 reliability-guide；已证实瓶颈的专项优化使用 performance-guide。 | [SKILL.md](skills/software-engineering/debugging-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/debugging-guide/RESEARCH.md) |
| `design-guide` | 设计软件新模块、重要接口和数据边界，审查真实架构、比较重大方案、安排可验证实施增量；用于系统设计、架构演进和跨阶段开发计划。简单局部修复无需启动完整设计流程。 | [SKILL.md](skills/software-engineering/design-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/design-guide/RESEARCH.md) |
| `performance-guide` | 当用户要求定义性能目标、分析延迟和吞吐量、建立基线、使用 profiler 定位瓶颈或证明优化收益时使用。要求可比较的工作负载与真实测量，不把普通代码清理升级为性能项目；未定位的异常卡顿先由 debugging-guide 排障。 | [SKILL.md](skills/software-engineering/performance-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/performance-guide/RESEARCH.md) |
| `project-handoff-guide` | 开发任务跨会话、长时间中断、换 Agent、阶段交接或需要恢复 Git 工作现场时使用，提取关键决定、真实进度、验证状态与下一步，并对照实际仓库核查。只负责状态交接，不负责周期性的全仓文件清理。 | [SKILL.md](skills/software-engineering/project-handoff-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/project-handoff-guide/RESEARCH.md) |
| `project-maintenance-guide` | 梳理与治理长期软件仓库中重复、失效或过时的文档、测试、脚本、配置、生成物和研究产物，决定保留、更新、合并、隔离、归档或安全删除；适用于有明确范围的项目资产维护，不替代普通代码局部清理。 | [SKILL.md](skills/software-engineering/project-maintenance-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/project-maintenance-guide/RESEARCH.md) |
| `reliability-guide` | 设计或检查软件遇到网络、存储、并发和外部服务故障时的错误语义、资源清理、超时、有限重试、幂等、补偿、降级与恢复。预防性可靠性工作时使用；已发生而原因未知的缺陷先用 debugging-guide 定位。 | [SKILL.md](skills/software-engineering/reliability-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/reliability-guide/RESEARCH.md) |
| `requirements-guide` | 产品目标、真实用户场景、业务规则、范围或验收条件存在影响实现的重要歧义时使用，调查事实、按决定依赖澄清关键问题，并形成可确认和可验证的需求。明确的小修复无需重新访谈；系统架构与编码由其他 Skill 负责。 | [SKILL.md](skills/software-engineering/requirements-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/requirements-guide/RESEARCH.md) |
| `security-privacy-guide` | 功能触及认证授权、用户数据、文件和数据库、外部接口、敏感日志、秘密、依赖风险或个人隐私时使用。根据资产与信任边界选择必要控制并进行风险相称的负面验证；普通低风险文案修改不需要全面安全审计。 | [SKILL.md](skills/software-engineering/security-privacy-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/security-privacy-guide/RESEARCH.md) |
| `testing-guide` | 依据已确认需求设计、实现和执行软件测试，验证功能、缺陷修复和重构的实际行为；关注独立测试预期、黑盒与白盒互补、集成边界、测试有效性及真实交付证据。无需为每次微小改动强制建立完整测试计划。 | [SKILL.md](skills/software-engineering/testing-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/testing-guide/RESEARCH.md) |
| `ui-ux-guide` | 设计、修改或审查真实用户界面、交互流程、视觉层级、界面文案、组件状态、响应布局和无障碍体验时使用。以用户实际任务和目标平台为依据，并通过运行页面检查；不负责整体系统架构或将启发式评价冒充用户研究。 | [SKILL.md](skills/software-engineering/ui-ux-guide/SKILL.md) | [RESEARCH.md](research/software-engineering/ui-ux-guide/RESEARCH.md) |

共 **27** 项 Skill。

如需安装，请将完整 Skill 目录（包括 `references/` 等配套文件）放入目标 Agent 支持的 Skills 位置。如何通过常驻规则按需发现本索引，参见 [config/AGENTS.md](config/AGENTS.md)。
