---
title: R手册(Visualise)--RColorBrewer and extrafont
tags: [R,RColorBrewer,extrafont,调色板,字体]
mathjax: false
copyright: true
date: 2018-05-03 22:16:10
categories: [R,Visualise]
sticky: false
---

# RColorBrewer：调色板

RColorBrewer是一个R包，使用网站 http://colorbrewer2.org/ 提供的颜色。

颜色分了三个区域，分别对应的是三个类型：
1. seq：序列型，单渐变色，一种主色由浅到深
2. qual：离散型，区分色，几种区分度很高的颜色组合
3. div：极端型，双渐变色，一种颜色到另外一种颜色的渐变，有两种主色

<!-- more -->

```r
display.brewer.all(type="seq/div/qual") # 查看调色板所有颜色
brewer.pal(n, name) # 颜色提取
```

> Base R调色板：
> `base::colours()` 查看所有颜色的名字
> `rainbow(n,alpha=1)`, `heat.colors`, `terrain.colors`, `topo.colors`, `cm.colors`,etc



-------

# extrafont：字体

```r
font_import() # 将系统字体导入R
fonts() # 查看导入R中的字体
```

**使用字体：**

1. 加载包(导入字体): `library(extrafont)` 
2. 加载字体:
   ```R
   windowsFonts( 
     f1=windowsFont(”family1”),
     f2=windowsFont(”family2”))
   ```

3. 使用字体: （假设已经绘制ggplot2图形p）
    ```r
    p+geom_label(family="f1")
    ```



