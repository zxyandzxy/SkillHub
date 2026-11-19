# 设计方案到增量实施

按可验证的功能行为而不是“编辑一个文件”拆分任务。一项增量最好能贯通必要的接口、数据处理与用户可观察结果；纯基础工作也应明确它解锁哪个能力和如何验证。系统始终保持可构建、可恢复、可集成的基线。

长期项目可在现有文档中维护四类信息职责：最终目标及约束、里程碑、依赖关系、当前执行批次。不强制四份文件。新事实出现时只调整受影响的决定及下游任务，不反复重写全部路线。

多 Agent 并行需要独立输入与输出、明确文件边界、接口契约和集成责任；两个任务同时修改同一核心数据模型时常应保持串行。交接时用 Git 工作区、真实测试和运行状态核对进度，不能仅依赖旧摘要。

参考：[DORA Working in Small Batches](https://dora.dev/capabilities/working-in-small-batches/)、[OpenAI Run Long Horizon Tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)。
