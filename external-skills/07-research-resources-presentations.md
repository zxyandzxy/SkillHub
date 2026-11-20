# 07 · 科研资料与 PPT 工具链

覆盖学术文献资料、研究知识库、证据追溯、科研幻灯片和原生 PPTX 制作与检查。

本类收录 **31** 项外部 Skill/工具入口。

> **收录性质：外部资源链接索引。** 本页不含第三方 Skill 的源文件，也不表示相关 Skill 已在本地安装。Stars 为 **GitHub 仓库级**数据，不代表单个 Skill 的独立 Stars 或效果评分；快照日期：**2026-11-20**。  
> 以下质量简评根据公开的说明、目录结构、脚本/示例和维护信息整理，**未运行第三方 Skill 的实际工作效果测试**。访问第三方工具前应自行确认权限与运行环境。


## 科研文献获取与解析（7）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`paper-lookup`** <small>(K-Dense-AI/scientific-agent-skills)</small> | 查询多种学术数据源的论文、预印本、标识符、引用和开放全文。 | [源文件](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/paper-lookup/SKILL.md) | 57,897 | 18 个学术 API；带异常契约测试。 |
| **`markitdown`** <small>(K-Dense-AI/scientific-agent-skills)</small> | 把论文及 Office/PDF 等资料转换成适合检索和 LLM 处理的 Markdown。 | [源文件](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/markitdown/SKILL.md) | 57,897 | 有实际转换程序与兼容性测试。 |
| **`paper-download-arxiv-paper-source`** <small>(yhbcode000/paper-share-skills)</small> | 按 arXiv ID 获取并安全解包原始 LaTeX 论文源码。 | [源文件](https://github.com/yhbcode000/paper-share-skills/blob/main/paper-download-arxiv-paper-source/SKILL.md) | 54 | 源码优先，明确 PDF-only 回退。 |
| **`research-lookup`** <small>(K-Dense-AI/scientific-agent-skills)</small> | 为科研写作构建引用资料包、文献证据列表和来源矩阵。 | [源文件](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/research-lookup/SKILL.md) | 57,897 | 依赖 Parallel API；离线回归测试。 |
| **`pyzotero`** <small>(K-Dense-AI/scientific-agent-skills)</small> | 通过 Zotero API 搜索、管理和导出文献条目及附件。 | [源文件](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/pyzotero/SKILL.md) | 57,897 | 私人文库读写需凭证授权。 |
| **`paperzilla`** <small>(K-Dense-AI/scientific-agent-skills)</small> | 通过 Paperzilla 项目源获取推荐论文和研究摘要。 | [源文件](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/paperzilla/SKILL.md) | 57,897 | 需要账号及指定 CLI。 |
| **`exa-search`** <small>(K-Dense-AI/scientific-agent-skills)</small> | 通过 Exa 搜索技术文献、网页和在线 PDF 并提取正文。 | [源文件](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/exa-search/SKILL.md) | 57,897 | 需要 Exa API Key 与网络访问。 |

## 研究知识库与证据追踪（8）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`open-notebook`** <small>(K-Dense-AI/scientific-agent-skills)</small> | 管理自托管研究资料库，实现资料导入、检索和有来源的问答。 | [源文件](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/open-notebook/SKILL.md) | 57,897 | 自托管后端；API 辅助程序有测试。 |
| **`obsidian-project-kb-core`** <small>(Galaxy-Dawn/claude-scholar)</small> | 管理项目范围内文献、实验、结果、写作与日常记录。 | [源文件](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/obsidian-project-kb-core/SKILL.md) | 6,073 | 具有注册表、链接和索引检查脚本。 |
| **`obsidian-literature-workflow`** <small>(Galaxy-Dawn/claude-scholar)</small> | 分离原始文献笔记、综合结论和写作稿，保持证据链。 | [源文件](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/obsidian-literature-workflow/SKILL.md) | 6,073 | 采用可追踪 Evidence Record 规则。 |
| **`build-evidence-map`** <small>(github/awesome-copilot)</small> | 对存在争议的技术结论建立支持、反对与缺失证据图。 | [源文件](https://github.com/github/awesome-copilot/blob/main/skills/build-evidence-map/SKILL.md) | 41,378 | 具备结构化 Schema 与验证脚本。 |
| **`obsidian-source-ingestion`** <small>(Galaxy-Dawn/claude-scholar)</small> | 将论文、网页、数据和资料归入项目 Obsidian 来源目录。 | [源文件](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/obsidian-source-ingestion/SKILL.md) | 6,073 | 采用来源优先的笔记分类规则。 |
| **`obsidian-kb-artifacts`** <small>(Galaxy-Dawn/claude-scholar)</small> | 维护 Obsidian Markdown、Wiki 链接、Canvas 和索引格式。 | [源文件](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/obsidian-kb-artifacts/SKILL.md) | 6,073 | 专注知识库产物格式。 |
| **`zotero-obsidian-bridge`** <small>(Galaxy-Dawn/claude-scholar)</small> | 把 Zotero 文献库和项目 Obsidian 笔记、综合结果关联。 | [源文件](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/zotero-obsidian-bridge/SKILL.md) | 6,073 | 强调引文与证据来源追溯。 |
| **`daily-paper-generator`** <small>(Galaxy-Dawn/claude-scholar)</small> | 按主题定期筛选 arXiv/bioRxiv 新论文并生成中英双语速览。 | [源文件](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/daily-paper-generator/SKILL.md) | 6,073 | 带查询脚本；须留意筛选遗漏。 |

## 科研幻灯片与 PPTX 制作（8）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`pptx`** <small>(anthropics/skills)</small> | 创建、解析和编辑原生 PPTX/模板，提供逐页内容与视觉检查。 | [源文件](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) | 197,863 | 含 OOXML 校验、缩略图及模板对照。 |
| **`scientific-slides`** <small>(K-Dense-AI/scientific-agent-skills)</small> | 规划科学会议、组会、答辩的幻灯片与讲述流程。 | [源文件](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-slides/SKILL.md) | 57,897 | 支持 PPTX/Beamer；图片式 PDF 不可原生编辑。 |
| **`genoffice`** <small>(genspark-ai/genoffice)</small> | 通过本地 CLI 创建、读取和修改 Office/PPTX 并逐页检查。 | [源文件](https://github.com/genspark-ai/genoffice/blob/main/skills/genoffice/SKILL.md) | 12,674 | 带 PPTX 构建、渲染与端到端测试。 |
| **`pptx-deck-context`** <small>(wshobson/agents)</small> | 制作 PPT 前固定演示目标、论证链、信息来源和设计约束。 | [源文件](https://github.com/wshobson/agents/blob/main/plugins/pptx-deck-creation/skills/pptx-deck-context/SKILL.md) | 42,717 | 强调主张与材料来源映射。 |
| **`pptx-slide-specification`** <small>(wshobson/agents)</small> | 用包含坐标、对象和样式的 JSON 规格描述可编辑幻灯片。 | [源文件](https://github.com/wshobson/agents/blob/main/plugins/pptx-deck-creation/skills/pptx-slide-specification/SKILL.md) | 42,717 | 避免关键内容全图像化。 |
| **`pptx-reference-deck-analysis`** <small>(wshobson/agents)</small> | 只读分析已有 PPTX 的母版、对象、配色及 OOXML 结构。 | [源文件](https://github.com/wshobson/agents/blob/main/plugins/pptx-deck-creation/skills/pptx-reference-deck-analysis/SKILL.md) | 42,717 | 含文件包安全检查脚本。 |
| **`pptx-quality-gates`** <small>(wshobson/agents)</small> | 对 PPTX 的边界、碰撞、来源、可访问性和文件完整性执行检查。 | [源文件](https://github.com/wshobson/agents/blob/main/plugins/pptx-deck-creation/skills/pptx-quality-gates/SKILL.md) | 42,717 | 质量检查契约明确。 |
| **`pptx-visual-assets`** <small>(wshobson/agents)</small> | 管理 PPTX 图形素材，保持重要标签和数字为原生可编辑对象。 | [源文件](https://github.com/wshobson/agents/blob/main/plugins/pptx-deck-creation/skills/pptx-visual-assets/SKILL.md) | 42,717 | 记录素材来源和使用权限。 |

## 论文转幻灯片与演讲稿（8）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`paper-to-slides`** <small>(qqtang-code/paper-to-slides)</small> | 从论文 PDF/LaTeX 生成 Beamer、PDF 和分页面讲稿。 | [源文件](https://github.com/qqtang-code/paper-to-slides/blob/main/plugins/paper-to-slides/skills/paper-to-slides/SKILL.md) | 2 | 有完整样例、构建脚本与成功 CI。 |
| **`paper-to-slides`** <small>(yigengjiang/paper-to-slides)</small> | 将论文转换为可编辑 LaTeX Beamer、PDF 和按时长分配的讲稿。 | [源文件](https://github.com/yigengjiang/paper-to-slides/blob/main/SKILL.md) | 4 | 强调核心原图和可追溯来源。 |
| **`research-report-cn`** <small>(codezzzsleep/research-ppt-skill)</small> | 生成中文学术组会、论文精读与综述的 PowerPoint。 | [源文件](https://github.com/codezzzsleep/research-ppt-skill/blob/main/research-report-cn/SKILL.md) | 7 | 含排版库、实例和数字账本。 |
| **`ppt-speech-writer`** <small>(AI272/speaker)</small> | 依据真实 PPTX 的文本与渲染视觉逐页撰写讲稿并写入备注。 | [源文件](https://github.com/AI272/speaker/blob/main/ppt-speech-writer/SKILL.md) | 482 | 需综合阅读图片、图表和对象。 |
| **`frontend-slides`** <small>(affaan-m/ECC)</small> | 创建 HTML 幻灯片并支持将 PPT 内容转换为浏览器展示。 | [源文件](https://github.com/affaan-m/ECC/blob/main/skills/frontend-slides/SKILL.md) | 307,470 | 主要交付物为 HTML 而非原生 PPTX。 |
| **`academic_ppt`** <small>(realihang/academic-ppt-skill)</small> | 基于 PowerPoint 母版和可编辑元素库制作中文学术汇报。 | [源文件](https://github.com/realihang/academic-ppt-skill/blob/main/SKILL.md) | 2 | 含原生模板与整理脚本；有固定版式约束。 |
| **`ai-paper2slide-skill`** <small>(Leo1998-Lu/ai-paper2slide-skill)</small> | 从论文 LaTeX 生成 PPTX，并附英文逐页讲稿和图源清单。 | [源文件](https://github.com/Leo1998-Lu/ai-paper2slide-skill/blob/main/SKILL.md) | 45 | 严格限制图片来源于原始 TeX 包。 |
| **`paper-to-beamer`** <small>(yhbcode000/paper-share-skills)</small> | 将学术论文转换为指定主题的 Beamer 幻灯片。 | [源文件](https://github.com/yhbcode000/paper-share-skills/blob/main/paper-to-beamer/SKILL.md) | 54 | 默认 SUSTech 主题；依赖 LaTeX 编译。 |

## 使用说明

此处仅提供外部资源的导航。选择工具后，优先阅读链接指向的原始 `SKILL.md`；按需阅读其 `references/`、脚本及官方说明。第三方 API、MCP、桌面软件或运行时依赖应由使用者在实际环境中单独配置。

**来源与版权：**第三方内容仍归其原作者所有，使用时遵循原仓库的许可证和服务条款；本目录不复制、安装或替代第三方工具。
