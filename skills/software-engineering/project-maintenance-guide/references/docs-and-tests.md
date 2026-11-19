# 文档权威性与测试资产价值

## 文档

从实际读者问题区分教程（如何学习）、操作指南（如何完成任务）、参考（准确 API/约束）和解释（为什么这样设计），参考 [Diátaxis](https://diataxis.fr/)。同一条配置事实应有唯一权威来源，其他页面通过引用连接。接口与使用方式变更时同步更新实际入口；被替代的历史重要 ADR 标记 superseded 并链接现行决定。

## 测试

先判断测试验证哪个业务行为和哪一层接口，以及它提供了多少独立信心。单纯变慢或偶发失败不足以删除；需检查环境、时间和共享状态原因。高度重复的测试可以整理为更合适的层次，但不得削弱关键验收。暂停有价值的 flaky 测试时应记录原因、影响及恢复条件。

## 脚本和生成物

临时诊断脚本通常应在问题解决后清理；重复执行有价值的工具应建立稳定入口。生成产物是否进入 Git/ignore 由构建、发布和科研复现目的决定，不能机械按扩展名删除。

参考：[Google Documentation Best Practices](https://google.github.io/styleguide/docguide/best_practices.html)、[Software Engineering at Google Documentation](https://abseil.io/resources/swe-book/html/ch10.html)、[Martin Fowler Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)。
