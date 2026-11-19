# 模块职责、架构约束与关键决策

沿入口、关键调用、数据读写和公共 API 确认实际设计。观察到循环依赖、绕开公共接口直接改内部状态、多个模块共享写权限、同一规则多份实现时，先判断是否真实增加修改成本和错误风险，再决定调整。

模块边界由职责、变化原因和数据所有权决定，不依赖固定文件数或目录层级。一次新需求若只需复用现有导出模块，不应自动建立新的插件框架；跨服务状态一致性要求很高时，必须说明提交/补偿与故障恢复语义。

对影响多个模块、数据存储、外部接口或技术选型的难撤销决定可记录轻量 ADR：背景、主要备选、选择、可验证理由及负面后果。历史决定被替代时保留背景并指向当前结论，普通函数内部选择不需单独文档。

参考：[SEI Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)、[Google Cloud Architecture Decision Records](https://docs.cloud.google.com/architecture/architecture-decision-records)、[ArchUnit](https://www.archunit.org/userguide/html/000_Index.html)。这些材料提供结构化取舍与可机械核查依赖方向的实践；具体工具和流程由项目生态决定。
