# 测试 oracle 与场景设计

可靠 oracle 来自独立规则。假设商店规定“满 100 元免运费”：可以构造 99、100、101 元三个边界输入，预期运费根据已确认规则推导；不能调用刚写好的 `shipping_fee()` 计算 expected。这个示例用于说明测试方法，并非真实测试记录。

常见失败：测试只检查 CSV 非空，不验证列顺序和业务内容；mock 了所有外部服务，无法检查真实序列化协议；异常路径不检查数据回滚与资源释放。覆盖率可帮助发现没执行的代码，却不能证明断言测到了正确行为。

白盒方法关注代码分支、状态及异常；黑盒方法从用户场景或公开 API 验证结果，两者互补。高风险任务可以由不同上下文的评审者核查测试预期是否漏掉重要边界，但更换 Agent 并不自动保证独立性。

参考：[Google Test Behaviors, Not Methods](https://testing.googleblog.com/2014/04/testing-on-toilet-test-behaviors-not.html)、[ISTQB Foundation Level](https://www.istqb.org/certifications/certified-tester-foundation-level)。
