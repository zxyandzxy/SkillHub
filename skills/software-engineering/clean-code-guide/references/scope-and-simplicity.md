# 变更范围、简单实现与必要防护

对于一个已确定需求，先查代码入口、调用者和测试；把实现、测试、相关文档的变更限制在满足此需求的必要范围。不要为了“顺手”批量重命名相邻目录或格式化无关文件，避免审查者无法分辨功能修改与无关噪声。

“保持简单”不意味着永远不封装。对第三方请求建立一个职责清晰的适配层即使只有一个调用者，也可能降低耦合；为一次导出需求建立动态插件系统则缺少依据。抽象依据是当前复杂性、接口变化成本与测试边界，不是必须达到某个重复次数。

外部输入、网络、文件和用户数据存在真实失败可能，应处理相应错误并保留上下文。不能凭“这不会发生”删掉必要检查，也不能以广泛捕获后静默返回空值掩盖数据损坏。稳定不变量已在可信边界保障时，无须在每一层重复校验。

参考：[Google Engineering Practices Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html)、[Martin Fowler Refactoring](https://martinfowler.com/books/refactoring.html)、[Karpathy Guidelines](https://github.com/multica-ai/andrej-karpathy-skills)。
