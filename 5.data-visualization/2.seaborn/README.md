# 数据可视化的利器-Seaborn简易入门

Matplotlib试着让简单的事情更加简单，困难的事情变得可能，而Seaborn就是让困难的东西更加简单。 

Seaborn是针对统计绘图的，一般来说，seaborn能满足数据分析90%的绘图需求。

Seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，在大多数情况下使用seaborn就能做出很具有吸引力的图，应该把Seaborn视为matplotlib的补充，而不是替代物。

用matplotlib最大的困难是其默认的各种参数，而Seaborn则完全避免了这一问题。

### seaborn一共有5个大类21种图，分别是：

- Relational plots 关系类图表

  1. relplot() 关系类图表的接口，其实是下面两种图的集成，通过指定kind参数可以画出下面的两种图
  2. scatterplot() 散点图
  3. lineplot() 折线图

- Categorical plots 分类图表

  1. catplot() 分类图表的接口，其实是下面八种图表的集成，通过指定kind参数可以画出下面的八种图
  2. stripplot() 分类散点图
  3. swarmplot() 能够显示分布密度的分类散点图
  4. boxplot() 箱图
  5. violinplot() 小提琴图
  6. boxenplot() 增强箱图
  7. pointplot() 点图
  8. barplot() 条形图
  9. countplot() 计数图

- Distribution plot 分布图

  1. jointplot() 双变量关系图
  2. pairplot() 变量关系组图
  3. distplot() 直方图，质量估计图
  4. kdeplot() 核函数密度估计图
  5. rugplot() 将数组中的数据点绘制为轴上的数据

- Regression plots 回归图

  1. lmplot() 回归模型图
  2. regplot() 线性回归图
  3. residplot() 线性回归残差图

- Matrix plots 矩阵图

  1. heatmap() 热力图
  2. clustermap() 聚集图



![公众号](../images/gongzhong.jpg)

机器学习qq群：554839127（我们有6个群，加过一个就不需要加了）
