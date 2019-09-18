---
title: 关于
date: 2019-09-07 21:46:41
type: "post"
comments: false
---

​    折腾了3周，本站终于初步成型，还有若干地方需要修修补补。
<p align="right">2019-09-10</p>


{% note warning %} 以下是踩过的坑 {% endnote %}

{% centerquote %}**本地图片**{% endcenterquote %}
用绝对链接引用位于 `hexo/source/images/example.jpg` 的图片
绝对路径的根目录都是 `source/`，而不是站点根目录 `/`

```md
![example](/images/example.jpg)
{% asset_img /images/example.jpg example %}
```