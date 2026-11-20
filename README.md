# SkillHub

SkillHub 收录面向 AI Agent 的可复用专业 Skills。每个 Skill 提供可执行的任务指导，并配有说明专业方法、证据和设计依据的研究文档。

## 浏览 Skills

从 [CATALOG.md](CATALOG.md) 按任务类型选择 Skill。目录分为四类：

| 类别 | 主要任务 |
| --- | --- |
| [technical-content](skills/technical-content/) | 技术写作、演示、阅读型报告与交互解释 |
| [academic-writing](skills/academic-writing/) | 论文写作、科研图表、审稿意见处理、独立评审与事实核查 |
| [research](skills/research/) | 文献研究、Idea、研究与实验设计、数据集、科研工程和结果分析 |
| [software-engineering](skills/software-engineering/) | 需求、设计、编码、测试、排障、评审和专项工程质量 |

标准路径为：

```text
skills/<category>/<name>/SKILL.md
research/<category>/<name>/RESEARCH.md
```

`SKILL.md` 说明何时使用、如何执行及任务边界；`references/` 中的专业细节按需读取。对应的 `RESEARCH.md` 说明该领域的实际问题、相关证据和方法选择，并在末章解释这些认识如何形成 Skill 的规则。研究文档面向读者，平时执行任务无需全部加载。

## 外部 Skills 与工具推荐

`external-skills/` 提供按任务分类的第三方 Skill / 工具 **链接索引**，共收录 **141 项**。这些资源不属于本仓库已安装的 Skills，也未复制其源码。Stars 是 GitHub 仓库级参考指标，不是 Skill 效果评分。

| 分类 | 外部资源索引 | 数量 |
| --- | --- | ---: |
| 科研方法 | [查看资源](external-skills/01-research-methods.md) | 12 |
| 论文写作与审查 | [查看资源](external-skills/02-paper-writing-review.md) | 13 |
| Agent 软件工程工作流 | [查看资源](external-skills/03-agent-engineering-workflows.md) | 21 |
| 软件验证与审查 | [查看资源](external-skills/04-software-verification-review.md) | 27 |
| 技术演示制作 | [查看资源](external-skills/05-technical-demos.md) | 14 |
| 科研图形工具链 | [查看资源](external-skills/06-research-figures.md) | 23 |
| 科研资料与 PPT 工具链 | [查看资源](external-skills/07-research-resources-presentations.md) | 31 |

外部资源主要服务于本仓库已有的四个方向：技术内容表达、学术成果、科研工作流、软件工程。具体能力、依赖与质量提示详见各分类文档；使用前请阅读第三方原始说明并按其许可证和服务条款执行。

## 让 Agent 使用 SkillHub

**方式一：安装到支持 Skills 的 Agent 环境。** 从本仓库复制整个 `skills/<category>/<name>/` 目录到该 Agent 所支持的 Skill 安装位置，保留 `SKILL.md`、`references/` 及其他配套文件。不同 Agent 的路径、注册与自动触发机制可能不同，以目标环境为准。

**方式二：按需从仓库读取。** 将本仓库的实际 GitHub 地址提供给 Agent，并在它实际支持的常驻或项目指令文件中引入 [config/AGENTS.md](config/AGENTS.md) 所列协作原则与发现流程。Agent 优先检查已有 Skills；需要新的专项方法时先读取 [CATALOG.md](CATALOG.md)，再按任务选择对应 `SKILL.md`，必要时加载它引用的参考文件。

`AGENTS.md` 并非所有 Agent 都原生支持。仅给出一个 GitHub 链接，也不保证 Agent 自动访问网络、安装文件或执行远程程序。对于不支持联网或文件访问的环境，先按其官方方式安装适用的 Skill。

本仓库使用相对链接，未预设尚未指定的 GitHub 仓库地址；对外部署常驻指令时应提供实际仓库 URL。

## 维护

新增或调整 Skill 时，保持 `skills/` 与 `research/` 的同名分类与对应关系，并根据需要更新 `references/`。用标准库脚本重新生成索引：

```bash
python tools/generate_catalog.py
python tools/generate_catalog.py --check
```

`--check` 同时验证基本目录结构及索引是否与 Skill 元数据一致。专业方法或具体行为的正确性仍需按使用任务核查。

## 许可

原创内容按 [MIT License](LICENSE) 发布。包含改编来源的 Skill 如有 `THIRD_PARTY_LICENSES.md`，请同时遵守该文件所保留的版权与许可要求。研究文档中的外部论文、网站及社区资源链接属于参考资料，不代表取得其原文、图片或软件的再分发授权。
