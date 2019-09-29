---
ID: d6f62644a1e9e76424deca9f72f3d51f
title: R手册(Model Tools)--broom and modelr
tags: [R,broom,modelr]
mathjax: false
copyright: true
date: 2018-05-04 00:43:40
categories: [R,Model Tools]
sticky: false
---
broom: 数据清洗工具
modelr: 辅助管道建模工具

<!-- more -->

# broom：Convert statistical analysis objects into tidy format

这个软件包提供了三种完成三种不同类型整理的S3方法：[GitHub链接](https://github.com/tidyverse/broom)

- **tidy:** 构建一个总结模型或检验整洁的统计信息data.frame。这包括回归中coefficients and p-values，聚类中的每个集群信息per-cluster或multtest函数的每个测试信息per-test等
- **augment:** 将列添加到建模的原始数据中。这包括预测，残差和集群分配等(predictions, residuals, and cluster assignments)
- **glance:** 构建一个简洁的模型的单行摘要。这通常包含构建整个模型的计算值such as R^2, adjusted R^2, and residual **standard error**

考虑一个说明性的例子，对内置mtcars数据集进行线性拟合。

```r
lmfit <- lm(mpg ~ wt, mtcars)

library(broom)
tidy(lmfit)
##          term  estimate std.error statistic      p.value
## 1 (Intercept) 37.285126  1.877627 19.857575 8.241799e-19
## 2          wt -5.344472  0.559101 -9.559044 1.293959e-10

head(augment(lmfit))
##           .rownames  mpg    wt  .fitted   .se.fit     .resid       .hat
## 1         Mazda RX4 21.0 2.620 23.28261 0.6335798 -2.2826106 0.04326896
## 2     Mazda RX4 Wag 21.0 2.875 21.91977 0.5714319 -0.9197704 0.03519677
## 3        Datsun 710 22.8 2.320 24.88595 0.7359177 -2.0859521 0.05837573
## 4    Hornet 4 Drive 21.4 3.215 20.10265 0.5384424  1.2973499 0.03125017
## 5 Hornet Sportabout 18.7 3.440 18.90014 0.5526562 -0.2001440 0.03292182
## 6           Valiant 18.1 3.460 18.79325 0.5552829 -0.6932545 0.03323551
##     .sigma      .cooksd  .std.resid
## 1 3.067494 1.327407e-02 -0.76616765
## 2 3.093068 1.723963e-03 -0.30743051
## 3 3.072127 1.543937e-02 -0.70575249
## 4 3.088268 3.020558e-03  0.43275114
## 5 3.097722 7.599578e-05 -0.06681879
## 6 3.095184 9.210650e-04 -0.23148309

glance(lmfit)
##   r.squared adj.r.squared    sigma statistic      p.value df    logLik
## 1 0.7528328     0.7445939 3.045882  91.37533 1.293959e-10  2 -80.01471
##        AIC      BIC deviance df.residual
## 1 166.0294 170.4266 278.3219          30
```


# modelr ：辅助管道建模

modelr软件包提供的功能可以帮助您在建模时创建精美的流水线。

## 分区和采样

`resample(data, idx)` 抽取idx向量指定的观测值
`resample_partition(data, p)` 按p向量给定的值分区

```r
rs <- resample(mtcars, 1:10)
as.data.frame(rs)

ex <- resample_partition(mtcars, c(test = 0.3, train = 0.7))
lapply(ex, dim)

bootstrap(mtcars, 100)%>%
 map( ~ lm(mpg ~ wt, data = .))%>%
 map_df( broom::tidy)
```

## 交叉验证抽样

`bootstrap(data, n, id = ".id")` 生成n个bootstrap副本
`crossv_kfold(data, k = 5, id = ".id")`将数据拆分为k独占分区，并将每个分区用于测试训练拆分
`crossv_mc(data, n, test = 0.2, id = ".id")`生成n组数据，交叉验证模型，test为测试集比例

```r
# bootstrap
boot <- bootstrap(mtcars, 100)
# k-fold cross-validation
cv1 <- crossv_kfold(mtcars, 5)
# Monte Carlo cross-validation
cv2 <- crossv_mc(mtcars, 100)

crossv_mc(mtcars, 100)%>%
  map(cv2$train, ~ lm(mpg ~ wt, data = .))%>%   #模型
  map2_dbl(cv2$test, rmse)%>%
  hist()
```


## 模型质量指标

`rmse(model, data)` 均方根误差
`mae(model, data)` 平均绝对误差
`rsquare(model, data)` R^2预测的方差除以响应的方差
`qae(model, data, probs)`误差的分位数


## 与模型交互

一组函数使您可以无缝地将预测和残差添加为现有数据框的附加列：
`add_predictions(data, model)`向数据框添加预测
`add_residuals(data, model)`向数据框添加残差

```r
df <- tibble::data_frame(
  x = sort(runif(100)),
  y = 5 * x + 0.5 * x ^ 2 + 3 + rnorm(length(x))
)

mod <- lm(y ~ x, data = df)
df %>% add_predictions(mod)
df %>% add_residuals(mod)
```

为了可视化目的，通常使用数据中均匀间隔的网格点
`data_grid(data, ..., .model = NULL)`展开数据框，包含所有值的组合，对可视化模型有用
`seq_range(x, n, by, trim = NULL, expand = NULL, pretty = FALSE)`在矢量范围内生成一个序列

```r
# 对连续性变量， seq_range函数很有用
mtcars_mod <- lm(mpg ~ wt + cyl + vs, data = mtcars)
data_grid(mtcars, wt = seq_range(wt, 10), cyl, vs) %>%   
  add_predictions(mtcars_mod)%>%
  head()
#> # A tibble: 60 x 4
#>       wt   cyl    vs  pred
#>    <dbl> <dbl> <dbl> <dbl>
#>  1  1.51     4     0  28.4
#>  2  1.51     4     1  28.9
#>  3  1.51     6     0  25.6
#>  4  1.51     6     1  26.2
#>  5  1.51     8     0  22.9
```

