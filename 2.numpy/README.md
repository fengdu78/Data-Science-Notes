## Numpy简介

Numpy是一个用python实现的科学计算的扩展程序库，包括：

- 1、一个强大的N维数组对象Array；
- 2、比较成熟的（广播）函数库；
- 3、用于整合C/C++和Fortran代码的工具包；
- 4、实用的线性代数、傅里叶变换和随机数生成函数。numpy和稀疏矩阵运算包scipy配合使用更加方便。

NumPy（Numeric Python）提供了许多高级的数值编程工具，如：矩阵数据类型、矢量处理，以及精密的运算库。专为进行严格的数字处理而产生。多为很多大型金融公司使用，以及核心的科学计算组织如：Lawrence Livermore，NASA用其处理一些本来使用C++，Fortran或Matlab等所做的任务。

## 一、适合初学者快速入门的Numpy实战全集

本文由光城同学整理

### 本文目录
​      1.Numpy基本操作

 - 1.1 列表转为矩阵
 - 1.2 维度
 - 1.3 行数和列数()
 - 1.4 元素个数

   2.Numpy创建array
 - 2.1 一维array创建
 - 2.2 多维array创建
 - 2.3 创建全零数组
 - 2.4 创建全1数据
 - 2.5 创建全空数组
 - 2.6 创建连续数组
 - 2.7 reshape操作
 - 2.8 创建连续型数据
 - 2.9 linspace的reshape操作

   3.Numpy基本运算
 - 3.1 一维矩阵运算
 - 3.2 多维矩阵运算
 - 3.3 基本计算

   4.Numpy索引与切片

   5.Numpy array合并
 - 5.1 数组合并
 - 5.2 数组转置为矩阵
 - 5.3 多个矩阵合并
 - 5.4 合并例子2

   6.Numpy array分割
 - 6.1 构造3行4列矩阵
 - 6.2 等量分割
 - 6.3 不等量分割
 - 6.4 其他的分割方式

   7.Numpy copy与 =
 - 7.1 =赋值方式会带有关联性
 - 7.2 copy()赋值方式没有关联性

   8.广播机制

   9.常用函数
   
# 二.Numpy简易入门

- 1.Numpy简易入门
      1.1 认识NumPy数组对象

  ​    1.2 创建NumPy数组

  ​    1.3 ndarry对象的数据类型

  ​        1.3.1 查看数据类型

  ​        1.3.2 转换数据类型

  ​    1.4 数组运算

  ​        1.4.1向量化运算

  ​        1.4.2 数组广播

  ​        1.4.3 数组与标量间的运算

  ​    1.5 ndarray的索引和切片

  ​        1.5.1 整数索引和切片的基本使用

  ​        1.5.2 花式（数组）索引的基本使用

  ​        1.5.3 布尔型

  ​    1.6 数组的转置和轴对称

  ​    1.7 NumPy通用函数

  ​    1.8 利用NumPy数组进行数据处理

  ​        1.8.1 将条件逻辑转为数组运算

  ​        1.8.2 数组统计运算

  ​        1.8.3 数组排序

  ​        1.8.4 检索数组元素

  ​        1.8.5 唯一化及其他集合逻辑

  ​    1.9 线性代数模块

  ​    1.10随机数模块



## 三、Numpy练习题100题-提高你的数据分析技能

本文总结了Numpy的常用操作，并做成练习题，练习题附答案建议读者把练习题完成。作者认为，做完练习题，Numpy的基本操作没有问题了，以后碰到问题也可以查这些习题。

网上可以搜到大量的Numpy教程和官方文档，但没有简单的方法来练习。教程是很好的资源，但要付诸实践。 只有实践，才能更好的加深学习。

本站从github搜索到了一些Numpy的练习题100题，含答案，并进行整理：

原代码作者：**Nicolas P. Rougier**（https://github.com/rougier/numpy-100）

**本练习代码可以在github下载：**

[numpy-100](numpy-100)

**使用方法**
文件夹有三个不同的ipynb文件:

- **100_Numpy_exercises_no_solution.ipynb** 

没有答案代码的文件，这个是你做的练习

- **100_Numpy_exercises_with_hint.ipynb**

没有答案代码的文件，但有提示，这个你也可以用来练习

- **100_Numpy_exercises.ipynb**

有答案代码和注释的文件

你可以在**100_Numpy_exercises_no_solution.ipynb** 里输入代码，看看运行结果是否和**100_Numpy_exercises.ipynb** 里面的内容一致。

## 四、Numpy练习题

整理了一个Numpy的练习题，总结了Numpy的常用操作，可以测试下自己对Numpy的掌握程度，有答案哦。

### 试题目录

  * Array creation routines（数组创建）
  * Array manipulation routines（数组操作）
  * String operations（字符串操作）
  * Numpy-specific help functions（Numpy特定帮助函数）
  * Input and output（输入和输出）
  * Linear algebra（线性代数）
  * Discrete Fourier Transform（离散傅里叶变换）
  * Logic functions（逻辑函数）
  * Mathematical functions（数学函数）
  * Random sampling (numpy.random)（随机抽样）
  * Set routines（集合操作）
  * Sorting, searching, and counting（排序、搜索和计数）
  * Statistics（统计）

### 试题内容

试题分为13个练习，每个练习分为两个ipynb文件，文件名带`_Solutions` 的是带答案的文件，建议初学者先练习下不带答案的文件,做不出来再看看答案。

**本练习代码可以在github下载：**

[numpy_exercises](numpy_exercises)

### 作者及来源

- 作者： Kyubyong
- 来源：https://github.com/Kyubyong/numpy_exercises 