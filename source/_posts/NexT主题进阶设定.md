---
title: NexT主题进阶设定
tags: [Hexo,NexT,Github pages]
copyright: true
date: 2019-09-11 14:14:04
categories:
- Hexo
---

NexT 是Hexo框架中最为流行的主题之一。精于心，简于形。
NexT 支持多种常见第三方服务，使用 **第三方服务** 来扩展站点的功能 。
除了 Markdown 支持的语法之外，NexT 借助 Hexo 提供的 **标签插件**， 为您提供在书写文档时快速插入带特殊样式的内容。

<!-- more -->

标签设置是NexT的一大亮点，将会单独开一篇文章具体介绍。

个人博客部署主要有3方面的内容：
修改站点配置文件、主题配置文件和导入插件。

配置文件目录如下：
站点配置文件 `‪username.github.io\_config.yml`
主题配置文件 `‪username.github.io\themes\next\_config.yml`

本人博客配置：由 [Hexo](https://hexo.io/) 强力驱动 v3.9.0 |主题 – [NexT.Gemini](https://theme-next.org/) v7.4.0


# 安装主题

## 克隆NexT 主题

{% tabs clone, 2 %}
<!-- tab 克隆最新版本 -->
定位到 Hexo 站点目录下
{% code %}
cd your-hexo-sit
git clone https://github.com/iissnan/hexo-theme-next themes/next
{% endcode %}
<!-- endtab -->

<!-- tab 克隆稳定版本 -->
定位到 Hexo 站点目录下，本博客就是克隆的这个版本
{% code %}
cd your-hexo-sit
git clone https://github.com/theme-next/hexo-theme-next  themes/next
{% endcode %}
<!-- endtab -->
{% endtabs %}

## 启用主题

与所有 Hexo 主题启用的模式一样。 当 克隆/下载 完成后，打开 站点配置文件， 找到 theme 字段，并将其值更改为 next

```
theme: next
```

# NexT 基础配置

NexT 前期基础配置可完全参考[NexT官网文档](http://theme-next.iissnan.com/getting-started.html)
例如，选择 Scheme、设置 菜单、设置 头像等。


# 用户自定义风格

custom_file_path


# Tag 插件

> Tags Settings
> See: https://theme-next.org/docs/tag-plugins/

参考链接：

[Hexo-NexT v7.1.1 Tag插件的使用](https://www.jianshu.com/p/1530f6959f79)
[[HEXO] NexT 主题提高博客颜值](https://walesexcitedmei.github.io/2018/08/30/HEXO-NexT-%E4%B8%BB%E9%A2%98%E6%8F%90%E9%AB%98%E5%8D%9A%E5%AE%A2%E9%A2%9C%E5%80%BC/)
[hexo next主题优化手册](https://inspurer.github.io/2018/11/11/hexo-next%E4%B8%BB%E9%A2%98%E4%BC%98%E5%8C%96/)
[hexo的next主题个性化配置](https://blog.csdn.net/weixin_44815733/article/details/88817220)
[Hexo Next主题进阶详细教程](https://blog.csdn.net/qq_31279347/article/details/82427562)
[Hexo博客NexT主题SEO优化](https://blog.csdn.net/qq_35661627/article/details/81267016)
[Github+Hexo搭建专属自己的博客](https://www.linjiujiu.xyz/2018/12/10/Github-Hexo%E6%90%AD%E5%BB%BA%E4%B8%93%E5%B1%9E%E8%87%AA%E5%B7%B1%E7%9A%84%E5%8D%9A%E5%AE%A2/)