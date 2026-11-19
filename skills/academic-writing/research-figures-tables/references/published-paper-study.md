# 从真实发表论文中学习科研图表

研究图表时，优先阅读论文已经引用的最相关前作。观察原始 PDF 中的 Figure、Table、Caption 及正文引用，理解图表如何回答研究问题；不把图形风格直接当成目标论文的统一模板。

## Transformer：结构图和局部计算图的分工

Vaswani et al., [Attention Is All You Need](https://proceedings.neurips.cc/paper/7181--attention-is-all-you-need.pdf), NeurIPS 2017。

- **Figure 1** 展示 Encoder/Decoder 两侧总体结构、重复层、残差、层归一化及注意力模块。读者据此判断组件有哪些及其数据关系。
- **Figure 2** 单独解释 Scaled Dot-Product Attention 与 Multi-Head Attention 的计算链，将 Q/K/V、Softmax、不同 Head 的变换等放大，而不在总览图中堆放全部细节。
- **Table 1** 使用紧凑表格比较不同层类型的复杂度、顺序操作和路径长度，便于精确检查符号与表达式。

**适用方法：** 总览图解释整体组成，局部图解释主要算法机制。精确理论公式一般在表格中便于对照。只有读者确实需要时，才增加第二张机制图。

## FlashAttention：把性能问题、算法和结果联系起来

Dao et al., [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://proceedings.neurips.cc/paper_files/paper/2022/file/67d57c32e20fd0a7a302cb81d36e40d5-Paper-Conference.pdf), NeurIPS 2022。

- **Figure 1** 的面板分别解释 GPU 存储层级、Q/K/V 的分块处理以及在一项 GPT-2 attention 基准中的运行时间对照。颜色与箭头分别服务于内存层级、复制和分块循环的科学语义。
- **Figure 2** 将复杂度和访问次数的小表、块大小变化的曲线及相关性能分析放在多个面板中。它将不同阅读任务组织为可以对应的子图，但双轴等具体编码应根据本论文比较合法性重新判断。
- **Table 2** 在固定任务或模型条件下列出多个精确实验值；表格的主要价值是支持查数和辨认比较分组。

**适用方法：** 多面板可以形成“原因—机制—效果”的连续说明，但每个面板都应具有独立职责，整体围绕一个主要问题。不为了仿照三面板结构给其他论文增加不必要的图。

## FlashAttention-2：保持基线对应，突出唯一主要机制变化

Tri Dao, [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://proceedings.iclr.cc/paper_files/paper/2024/file/98ed250b203d1ac6b24bbcf263e3d4a7-Paper-Conference.pdf), ICLR 2024。

- **Figure 1** 使用有限矩阵、分块及颜色边界解释在线 Softmax 和 GPU 存储操作，并通过图注交代示意图有所省略的计算内容。图只表达能够准确说明的部分。
- **Figure 3** 并排展示旧版与新版 attention 前向计算中 warp 的工作划分，保持 Q/K^T/V 位置可对照。旧版划分 K/V，新版划分 Q，图例说明哪些数据被多个 warp 共同访问、哪些被拆分。这种对应关系直接支持机制比较。
- **Figure 4** 按 causal mask 有无、head dimension 64/128 分成四个面板；有不同条件时先分组再比较，不把无法运行的设置作为真实零值。
- **Table 1** 以四组 GPT 训练配置比较不使用 FlashAttention、FlashAttention 和 FlashAttention-2 的吞吐量，数值单位是 TFLOPs/s/GPU。这些结果属于端到端训练，不能与 Figure 4 的 attention kernel 测量混用。

**适用方法：** 解释方法变化时，旧与新方案使用可对应的几何布局和符号，使读者只追踪真正改变的机制。评价受多个实验条件影响时，使用分面或表格分组保留条件，不绘制没有可比意义的平均提升。

## 评价可视化可能造成的误读

Wattenberg et al., [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/), Distill 2016，展示了参数选择与随机性如何改变高维数据的二维投影，并说明聚类图中的距离或面积可能不能按一般直觉解释。

**适用方法：** 使用降维图、聚类热力图、显著性图时必须交代可解释的范围。对一张外观清楚的图，也要检查其视觉关系是否等于科学结论；需要时通过不同参数、独立量化指标或反例补充判断。

## 将这些观察用于新的论文

开始制作之前，选少量与当前问题最接近的已发表图表，记录图号、读者问题、核心编码、图注中保证理解的条件。随后按照自己的方法和数据重新设计。可以迁移的是可读的组织关系、对照原则、图例与图注的职责；不能直接迁移的是其他论文的数值、结构拓扑和版权素材。
