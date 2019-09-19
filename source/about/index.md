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

{% centerquote %} **跳过指定文件的渲染** {% endcenterquote %}

- 关于hexo的`_config.yml`配置，官方文档中：`skip_render`：跳过指定文件的渲染，您可使用 glob 表达式来匹配路径。但并没有说明具体该怎么配置，一番折腾后得以解决、如果要跳过source文件夹下的`test.html`，可以这样配置：`skip_render: test.html`、
- 注意，千万不要手贱加上个`/`写成`/test.html`，这里只能填相对于source文件夹的**相对路径**。
- 如果要忽略source下的test文件夹下所有文件，可以这样配置：`skip_render: test/*`
- 如果要忽略source下的test文件夹下`.html`文件，可以这样配置：`skip_render: test/*.html`
- 如果要忽略source下的test文件夹下所有文件和目录，可以这样配置：`skip_render: test/**`
- 如果要忽略多个路径的文件或目录，可以这样配置：

```shell
skip_render: 
  - test.html    
  - test/*
```