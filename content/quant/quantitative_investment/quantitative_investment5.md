Title: 《量化投资：数据挖掘技术与实践(MatLab版)》读书笔记第5章：关联规则方法
Date: 2017-10-02
Category: 量化交易
Tags: 数据分析
Summary: 关联规则的挖掘，是发现数据项集之间的关联关系或相关关系。最常用的算法是 Aprior 算法和 FP-Groth 算法。

关联规则的挖掘，是发现数据项集之间的关联关系或相关关系。


# 关联相关的概念

1. 项和项集

   数据中不可分割的最小单位称为项目( $i$ )，项目的集合称为项集 $I$ 。

   对于项集 $I = \{{i}_{1}, {i}_{2},...,{i}_{k}\}$ ， 称 I 为 k-项集。

2. 事务

   设 $I = {\{i}_{1}, {i}_{2},...,{i}_{k}\}$ 是所有项目构成的项集，
   则一次处理所含项目的集合 $T = \{{t}_{1}, {t}_{2},...,{t}_{n}\}$ ,
   其中每一个 $ {t}_{i} $ 包含的项集都是 I 的子集。

3. 项集的频度(支持度,Support)

   包含某一个项集的事务的个数，称为该项集的频度。

4. 关联规则

   如果 $ X \Rightarrow Y $，其中 X、Y 分别是 I 的子集，并且 $ X \bigcap Y = \varphi $。

   X 称为 规则的前提， Y 称为规则的结果。表示如果出现 X 中的项目，则 Y 中的项目也会出现。

5. 关联规则的支持度(Support)

   交易集合中，同时包含 X、Y 的交易数与所有交易数之比。即：

   $ Support\left(X\Rightarrow Y \right) = Support X \bigcap Y = P(XY) $

6. 关联规则的置信度（Confidence/Strength）

   交易集中，同时包含 X、Y 的交易数与包含 X 的交易数之比。即：

   $ Confidence(X\Rightarrow Y) = \frac{support(X\bigcup Y}{support(X)}=P(Y\mid X) $

7. 最小支持度与最小置信度




5.1 关联规则概要
5.1.2 关联规则的基本概念
5.1.3 关联规则的分类
5.1.4 关联规则挖掘常用算法
5.2 Apriori算法
5.2.1 Apriori算法的基本思想
5.2.2 Apriori算法的步骤
5.2.3 Apriori算法的实例
5.2.4 Apriori算法的程序实现
5.2.5 Apriori算法的优缺点
5.3 FP-Growth算法
5.3.1 FP-Growth算法步骤
5.3.2 FP-Growth算法实例
5.3.3 FP-Growth算法的优缺点
5.4 应用实例：行业关联选股法
5.5 本章小结
