# 故障类别、状态与资源边界

## 故障不是一种状态

业务拒绝、临时故障、持续不可用、部分执行和违反不变量需要不同策略。定义操作成功、失败、未完成和未知是否已执行的状态。尤其对持久化写入，客户端未收到确认不证明操作没有生效。

## 资源与异常

文件、锁、连接、事务应按平台机制关闭或回滚。仅在能恢复、提供上下文或转换接口契约的边界捕获异常；不让所有错误都变成含糊成功。诊断信息保留原始原因但不得输出秘密。

## 原子性与补偿

多步操作说明原子边界、写入顺序、临时状态、事务/原子替换或补偿。不能安全恢复时保留未知或失败状态，并提供人工检查入口。降级需要维持语义，例如只读模式而非假装数据可写。

参考：https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions ；https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles 。
