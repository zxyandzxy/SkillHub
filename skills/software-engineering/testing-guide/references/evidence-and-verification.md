# 执行、证据与交付

单元测试证明局部逻辑在其模拟条件下行为正确；集成测试检验组件数据契约；端到端测试更接近完整用户路径；真实人工验收可检查自动化难以捕获的体验与语义要求。这些层级可以按风险选择，不能相互冒充。

检查用例是否实际收集、是否跳过、环境是否一致、失败是否来自本次修改、日志是否指向当前版本。出现基线失败时区别历史问题与新回归，不通过缩小测试范围掩盖失败。

测试替身用于隔离不可控依赖，但关键真实集成仍应覆盖。需要性能、安全和可靠性专项时按其风险选择独立检查，不为普通界面文字改变全面运行所有专项流程。

可参考：[Superpowers Verification Before Completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md)、[Google Mutation Testing](https://research.google/pubs/long-term-effects-of-mutation-testing)。
