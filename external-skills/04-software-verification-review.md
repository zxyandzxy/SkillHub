# 04 · 软件验证与审查

覆盖代码审查、需求到代码符合性检查、测试、回归、排障和补丁验证。

本类收录 **27** 项外部 Skill/工具入口。

> **收录性质：外部资源链接索引。** 本页不含第三方 Skill 的源文件，也不表示相关 Skill 已在本地安装。Stars 为 **GitHub 仓库级**数据，不代表单个 Skill 的独立 Stars 或效果评分；快照日期：**2026-11-20**。  
> 以下质量简评根据公开的说明、目录结构、脚本/示例和维护信息整理，**未运行第三方 Skill 的实际工作效果测试**。访问第三方工具前应自行确认权限与运行环境。


## 代码审查与合规（12）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`differential-review`** <small>(trailofbits/skills)</small> | 对 Git diff、PR 与提交开展风险导向的增量代码审查。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/differential-review/skills/differential-review/SKILL.md) | 8,312 | 包含代码影响范围与历史分析。 |
| **`spec-to-code-compliance`** <small>(trailofbits/skills)</small> | 比较规格、设计文档和实际实现，标出缺失与冲突。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md) | 8,312 | 适合设计到代码的一致性验证。 |
| **`variant-analysis`** <small>(trailofbits/skills)</small> | 从已知缺陷寻找整个代码库中的同源变体。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/variant-analysis/skills/variant-analysis/SKILL.md) | 8,312 | 可与静态扫描工具配合。 |
| **`semgrep`** <small>(trailofbits/skills)</small> | 使用 Semgrep 规则执行跨代码库的静态分析和缺陷模式定位。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/semgrep/SKILL.md) | 8,312 | 依赖 Semgrep 工具及规则。 |
| **`codeql`** <small>(trailofbits/skills)</small> | 使用 CodeQL 建立语义查询、跟踪数据流并发现缺陷。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/codeql/SKILL.md) | 8,312 | 依赖 CodeQL 环境和查询规则。 |
| **`c-review`** <small>(trailofbits/skills)</small> | 对 C/C++ 用户态应用开展内存安全、整数溢出和竞态问题审查。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/c-review/skills/c-review/SKILL.md) | 8,312 | 语言专项；含审计工作流。 |
| **`audit-context-building`** <small>(trailofbits/skills)</small> | 先梳理陌生代码库的关键假设、调用关系和安全边界，再开展审查。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/audit-context-building/skills/audit-context-building/SKILL.md) | 8,312 | 强调审查前的上下文建模。 |
| **`review-walkthrough`** <small>(trailofbits/skills)</small> | 将分支变更转换为可交互的 HTML 代码评审导览。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/review-walkthrough/skills/review-walkthrough/SKILL.md) | 8,312 | 侧重审阅可读性与变更证据。 |
| **`code-review`** <small>(mattpocock/skills)</small> | 对变更代码执行结构化审阅并识别潜在缺陷、设计风险。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md) | 328,468 | 面向日常工程代码评审。 |
| **`receiving-code-review`** <small>(obra/superpowers)</small> | 核验评审反馈的正确性，决定接受、澄清或拒绝修改。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md) | 322,432 | 避免无证据照单全收。 |
| **`requesting-code-review`** <small>(obra/superpowers)</small> | 在关键开发节点主动发起针对性的代码审查。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md) | 322,432 | 适合多阶段开发质量门禁。 |
| **`security-review`** <small>(github/awesome-copilot)</small> | 检查注入、权限、机密泄露及不安全依赖等一般代码安全风险。 | [源文件](https://github.com/github/awesome-copilot/blob/main/skills/security-review/SKILL.md) | 41,378 | 覆盖多语言，需按风险验证发现。 |

## 测试与覆盖（9）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`mutation-testing`** <small>(trailofbits/skills)</small> | 利用变异测试检查现有测试套件是否能发现实际行为错误。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/mutation-testing/skills/mutation-testing/SKILL.md) | 8,312 | 针对 mewt/muton 变异测试工作流。 |
| **`property-based-testing`** <small>(trailofbits/skills)</small> | 用性质与生成输入验证程序在广泛输入空间的行为。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/SKILL.md) | 8,312 | 突出边界条件和不变量。 |
| **`test-driven-development`** <small>(obra/superpowers)</small> | 以失败测试驱动代码实现和持续重构。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md) | 322,432 | 具有明确的红绿重构工作流。 |
| **`tdd`** <small>(mattpocock/skills)</small> | 按测试先行方法实现需求并在迭代中确认行为。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) | 328,468 | 独立 TDD 技术路线。 |
| **`test-gap-audit`** <small>(github/awesome-copilot)</small> | 评估测试覆盖的行为风险、缺失路径和薄弱断言。 | [源文件](https://github.com/github/awesome-copilot/blob/main/skills/test-gap-audit/SKILL.md) | 41,378 | 强调覆盖充分性而非仅统计行数。 |
| **`test-collaboration`** <small>(affaan-m/ECC)</small> | 维护需求、风险、Bug 与测试用例之间的可追踪关系。 | [源文件](https://github.com/affaan-m/ECC/blob/main/skills/test-collaboration/SKILL.md) | 307,470 | 适合多模块测试治理。 |
| **`ai-regression-testing`** <small>(affaan-m/ECC)</small> | 针对 AI 辅助编码常见盲点设计可执行回归测试。 | [源文件](https://github.com/affaan-m/ECC/blob/main/skills/ai-regression-testing/SKILL.md) | 307,470 | 关注生产路径与模拟路径差异。 |
| **`browser-qa`** <small>(affaan-m/ECC)</small> | 通过浏览器自动化验证 UI 交互、响应布局、控制台和可访问性。 | [源文件](https://github.com/affaan-m/ECC/blob/main/skills/browser-qa/SKILL.md) | 307,470 | 需要浏览器自动化执行环境。 |
| **`verification-before-completion`** <small>(obra/superpowers)</small> | 要求在宣布完成前运行适当检查并提供实际结果证据。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 322,432 | 强调完成声明须有验证依据。 |

## 排障、补丁与回归（6）

| Skill | 功能简介 | 原始地址 | Stars（仓库） | 质量与使用提示 |
| --- | --- | --- | ---: | --- |
| **`post-patch-validation`** <small>(trailofbits/skills)</small> | 对补丁执行原始漏洞、相关变体、行为保持与回归核验。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/post-patch-validation/skills/post-patch-validation/SKILL.md) | 8,312 | 强调基线与修复版本证据。 |
| **`patching-bugs`** <small>(trailofbits/skills)</small> | 围绕已知 Bug 构建可审阅补丁、复现与验证记录。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/patching-bugs/skills/patching-bugs/SKILL.md) | 8,312 | 面向缺陷修复闭环。 |
| **`regression-hunt`** <small>(trailofbits/skills)</small> | 系统追踪 PR、提交引入的回归并保留可复核证据。 | [源文件](https://github.com/trailofbits/skills/blob/main/plugins/regression-hunt/skills/regression-hunt/SKILL.md) | 8,312 | 适合多提交变更的回归调查。 |
| **`systematic-debugging`** <small>(obra/superpowers)</small> | 基于证据进行问题复现、根因分析和逐步验证。 | [源文件](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md) | 322,432 | 避免未经验证就修改代码。 |
| **`diagnosing-bugs`** <small>(mattpocock/skills)</small> | 以可复现现象和代码证据定位软件缺陷。 | [源文件](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md) | 328,468 | 强调诊断步骤而非猜测修复。 |
| **`bug-reproduction-brief`** <small>(github/awesome-copilot)</small> | 把模糊故障报告变成可重复执行的最小复现说明。 | [源文件](https://github.com/github/awesome-copilot/blob/main/skills/bug-reproduction-brief/SKILL.md) | 41,378 | 适合作为开发与测试交接材料。 |

## 使用说明

此处仅提供外部资源的导航。选择工具后，优先阅读链接指向的原始 `SKILL.md`；按需阅读其 `references/`、脚本及官方说明。第三方 API、MCP、桌面软件或运行时依赖应由使用者在实际环境中单独配置。

**来源与版权：**第三方内容仍归其原作者所有，使用时遵循原仓库的许可证和服务条款；本目录不复制、安装或替代第三方工具。
