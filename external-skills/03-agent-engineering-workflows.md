# 03 · Agent 软件工程工作流

覆盖需求澄清、方案设计、工作计划、Agent 协作、上下文管理、代码实现与交付。

本类收录 **21** 项外部 Skill/工具入口。

> **收录性质：外部资源链接索引。** 本页不含第三方 Skill 的源文件，也不表示相关 Skill 已在本地安装。Stars 为 **GitHub 仓库级**数据，不代表单个 Skill 的独立 Stars 或效果评分；快照日期：**2026-11-20**。  
> 以下质量简评根据公开的说明、目录结构、脚本/示例和维护信息整理，**未运行第三方 Skill 的实际工作效果测试**。访问第三方工具前应自行确认权限与运行环境。


## 需求与方案设计（9）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`brainstorming`** <small>(obra/superpowers)</small> | 在实现前澄清需求、约束、设计选择和完成定义。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | 322,432 | Superpowers 核心设计工作流。 |
| **`to-tickets`** <small>(mattpocock/skills)</small> | 把大需求拆成可跟踪、可实施的工程任务票据。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md) | 328,468 | 适合 issue 驱动的工程协作。 |
| **`codebase-design`** <small>(mattpocock/skills)</small> | 分析现有代码结构并制定变更设计，减少与架构的冲突。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md) | 328,468 | 强调基于现有代码做设计。 |
| **`intent-driven-development`** <small>(affaan-m/ECC)</small> | 从开发意图与业务目标建立实现步骤和验收约束。 | [源文件](https://github.com/affaan-m/ECC/blob/main/skills/intent-driven-development/SKILL.md) | 307,470 | 保留意图到实施的追溯链。 |
| **`contract-first`** <small>(affaan-m/ECC)</small> | 先定义接口或模块契约，再开展并行实现与验证。 | [源文件](https://github.com/affaan-m/ECC/blob/main/skills/contract-first/SKILL.md) | 307,470 | 适用于跨模块协作和集成。 |
| **`plan-canvas`** <small>(affaan-m/ECC)</small> | 把复杂工程规划整理为结构化、可跟踪的任务与决策视图。 | [源文件](https://github.com/affaan-m/ECC/blob/main/skills/plan-canvas/SKILL.md) | 307,470 | 服务中大型任务规划。 |
| **`domain-modeling`** <small>(mattpocock/skills)</small> | 梳理领域实体、业务规则和边界后设计代码模型。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md) | 328,468 | 适合复杂业务域的软件设计。 |
| **`wayfinder`** <small>(mattpocock/skills)</small> | 将跨多轮会话的大型工程目标拆解为可逐步解决的决策票据。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md) | 328,468 | 依赖 Issue 跟踪系统。 |
| **`to-spec`** <small>(mattpocock/skills)</small> | 把需求与初步设计整理成实现可用的工程规格说明。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md) | 328,468 | 重视规格明确性。 |

## 实现与工作流（8）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`writing-plans`** <small>(obra/superpowers)</small> | 制定细粒度实现步骤、验证任务与交付检查。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) | 322,432 | 具备明确工程计划模板。 |
| **`executing-plans`** <small>(obra/superpowers)</small> | 按既定开发计划逐项实施、核验结果与汇报偏差。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md) | 322,432 | 强调执行与计划一致性。 |
| **`subagent-driven-development`** <small>(obra/superpowers)</small> | 分派隔离的子任务给多个 Agent，并在任务边界执行复核。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md) | 322,432 | 适合受控的多 Agent 协作。 |
| **`dispatching-parallel-agents`** <small>(obra/superpowers)</small> | 识别互不依赖的任务并组织并行 Agent 执行。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md) | 322,432 | 应配合隔离和结果合并流程。 |
| **`using-git-worktrees`** <small>(obra/superpowers)</small> | 使用 Git worktree 隔离多分支或并行开发工作区。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md) | 322,432 | 直接服务 Git 协作。 |
| **`finishing-a-development-branch`** <small>(obra/superpowers)</small> | 开发完成后检查测试、提交、合并或分支清理方案。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md) | 322,432 | 面向工程交付收尾。 |
| **`implement-spec`** <small>(mattpocock/skills)</small> | 根据既定软件规格实施变更，并核对规格要求。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement-spec/SKILL.md) | 328,468 | 适合需求已明确的实施任务。 |
| **`parallel-feature-development`** <small>(wshobson/agents)</small> | 组织多个 Agent 并行开发相对独立的功能模块。 | [源文件](https://github.com/wshobson/agents/blob/main/plugins/agent-teams/skills/parallel-feature-development/SKILL.md) | 42,717 | 依赖任务拆分和工作区隔离。 |

## Agent 文档、上下文与规范（4）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`writing-for-agents`** <small>(mattpocock/skills)</small> | 把人类文档改写为 Agent 可执行、边界明确的操作说明。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md) | 328,468 | 适用于 AGENTS.md 与工程指令。 |
| **`harness-engineering`** <small>(github/awesome-copilot)</small> | 将编码 Agent 的重复错误沉淀为仓库规则、检查与持续反馈机制。 | [源文件](https://github.com/github/awesome-copilot/blob/main/skills/harness-engineering/SKILL.md) | 41,378 | 强调工程规则和回归检查。 |
| **`context-compression`** <small>(muratcankoylan/Agent-Skills-for-Context-Engineering)</small> | 压缩长会话上下文并保留决策、文件变更、风险和交接信息。 | [源文件](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-compression/SKILL.md) | 18,383 | 特别适合长任务交接。 |
| **`context-driven-development`** <small>(wshobson/agents)</small> | 围绕持久化上下文和阶段目标组织长周期工程开发。 | [源文件](https://github.com/wshobson/agents/blob/main/plugins/conductor/skills/context-driven-development/SKILL.md) | 42,717 | 适合多阶段 Agent 工程工作流。 |

## 使用说明

此处仅提供外部资源的导航。选择工具后，优先阅读链接指向的原始 `SKILL.md`；按需阅读其 `references/`、脚本及官方说明。第三方 API、MCP、桌面软件或运行时依赖应由使用者在实际环境中单独配置。

**来源与版权：**第三方内容仍归其原作者所有，使用时遵循原仓库的许可证和服务条款；本目录不复制、安装或替代第三方工具。
