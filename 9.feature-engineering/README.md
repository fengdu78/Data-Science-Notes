## 一、面向机器学习的特征工程

- [一、引言](1.引言.ipynb)
- [二、简单数字的奇特技巧](2.简单数字的奇特技巧.ipynb)
- [三、文本数据：展开、过滤和分块](3.文本数据.ipynb)
- [四、特征缩放的效果：从词袋到 TF-IDF](4.特征缩放的效果：从词袋到_TF-IDF.ipynb)
- [五、类别特征：机器鸡时代的鸡蛋计数](5.类别特征.ipynb)
- [六、降维：使用 PCA 压缩数据集](6.降维：用_PCA_压缩数据集.ipynb)
- [七、非线性特征提取和模型堆叠](7.非线性特征提取和模型堆叠.ipynb)
- [八、自动化特征提取器：图像特征提取和深度学习](8.自动化特征提取器：图像特征提取和深度学习.ipynb)
- [九、回到特征：将它们放到一起(备注：代码还在测试)](9.回到特征：将它们放到一起.ipynb)
- [附录、线性模型和线性代数基础](附录.线性模型和线性代数基础.ipynb)

**内容简介**

第 1 章从数字数据的基本特征工程开始：过滤，合并，缩放，日志转换和能量转换以及交互功能。

第 2 章和第 3 章深入探讨了自然文本的特征工程：bag-of-words，n-gram 和短语检测。

第 4 章将 tf-idf 作为特征缩放的例子，并讨论它的工作原理。

第 5 章讨论分类变量的高效编码技术，包括特征哈希和 bin-counting。

第 6 章中进行主成分分析，我们深入机器学习的领域。

第 7 章将 k-means 看作一种特征化技术，它说明了模型堆叠的有效理论。

第 8 章都是关于图像的，在特征提取方面比文本数据更具挑战性。在得出深度学习是最新图像特征提取技术的解释之前，我们着眼于两种手动特征提取技术 SIFT 和 HOG。

第 9 章中完成了一个端到端示例中的几种不同技术，为学术论文数据集创建了一个推荐器。

------

[原版（英文）图书地址](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/)

**翻译**：[apachecn](https://github.com/apachecn)，[翻译版本地址](https://github.com/apachecn/feature-engineering-for-ml-zh)

**代码修改和整理**：[黄海广](https://github.com/fengdu78)，原文修改成jupyter notebook格式，并增加和修改了部分代码，测试全部通过，所有数据集已经放在[百度云](data/README.md)下载。

## 二、特征工程的神器-基于Python的特征自动化选择代码

[FeatureSelectorUsage](FeatureSelectorUsage/)

该选择器基于python编写，有五种方法来标识要删除的特征：

- 缺失值
- 唯一值
- 共线特征
- 零重要性特征
- 低重要性特征

如果需要引用这个Repo:

格式： `fengdu78, Data-Science-Notes, (2019), GitHub repository, https://github.com/fengdu78/Data-Science-Notes`