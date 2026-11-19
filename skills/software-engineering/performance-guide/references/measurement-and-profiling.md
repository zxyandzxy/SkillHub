# 性能指标、工作负载与可比测量

## 指标对应任务

Web 可使用 LCP、INP、CLS 以及后端延迟；API 根据真实负载报告 p50/p95/p99、吞吐和资源；移动端可测启动与帧；批处理测总时间、吞吐和峰值内存。只选能回答当前用户目标的指标。不要把 Web Vitals 阈值用于桌面应用。

## 测量条件

保留提交、硬件/虚拟机、系统、依赖、构建模式、数据规模、并发、网络、预热与缓存。分别考虑冷启动和热启动、微基准与真实用户流程。重复测量并记录分布、噪声和异常原因；少量单次结果不足以宣称稳定收益。

## 定位瓶颈

用 profiler、trace、数据库执行计划、火焰图或面向关键路径的指标寻找耗时集中点。N+1 请求、重复 I/O、主线程长任务是调查线索，仍需结合实际工作负载确认它们对目标指标的影响。

## 对照

修改前后测量单位和样本条件应相同。若环境变化或负载不可复现，报告只能支持当前观察，不能推出普遍性能结论。

来源：https://web.dev/articles/vitals ；https://developer.android.com/topic/performance/measuring-performance ；https://docs.cloud.google.com/architecture/framework/performance-optimization 。
