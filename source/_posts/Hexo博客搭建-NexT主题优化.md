---
title: Hexo博客搭建+NexT主题优化
tags: [Hexo,NexT,Github pages]
copyright: true
date: 2019-09-10 13:48:53
categories: 个人博客
---

Hexo 是高效的静态站点生成框架，她基于 Node.js。 通过 Hexo 你可以轻松地使用 Markdown 编写文章，除了 Markdown 本身的语法之外，还可以使用 Hexo 提供的 [标签插件](https://hexo.io/zh-cn/docs/tag-plugins.html) 来快速的插入特定形式的内容。
<!-- more -->



[Hexo](https://hexo.io/zh-cn/)：快速、简洁且高效的博客框架

```bash
npm install hexo-cli -g
hexo init wilenwu.github.io
cd wilenwu.github.io
npm install
hexo server
```

[NexT](http://theme-next.iissnan.com/)

# SSH keys

```css
npm install hexo -server --save
```

```css
ssh-keygen -t rsa -C "597379201@qq.com"
```



测试设置是否成功

```css
ssh -T git@github.com
```

## 配置Git个人信息

```git
git config --global user.name "wilenwu"
git config --global user.email "597379201@qq.com"
```

## github发布配置

```
npm install hexo-deployer-git --save
```

```bash
# Deployment
## Docs: https://hexo.io/docs/deployment.html
deploy:
  type: git
  repo: git@github.com:wilenwu/wilenwu.github.io.git
  branch: master
```

# GitHub Pages 编译预览

```bash
# 清除缓存
hexo clean

# 编译文件
hexo generate

# 本地预览  http://localhost:4000 
hexo serve

# 发布到github https://wilenwu.github.io
hexo deploye

hexo new "My New Post"        # 新文章`source\_posts`
hexo new page  about/me  # 新页面
```



# 安装 NexT主题

```
git clone https://github.com/theme-next/hexo-theme-next  themes/next
```



| 参数         | 描述                                                 | 默认值       |
| :----------- | :--------------------------------------------------- | :----------- |
| `layout`     | 布局                                                 |              |
| `title`      | 标题                                                 |              |
| `date`       | 建立日期                                             | 文件建立日期 |
| `updated`    | 更新日期                                             | 文件更新日期 |
| `comments`   | 开启文章的评论功能                                   | true         |
| `tags`       | 标签（不适用于分页）                                 |              |
| `categories` | 分类（不适用于分页）                                 |              |
| `permalink`  | 覆盖文章网址                                         |              |
| `keywords`   | 仅用于 meta 标签和 Open Graph 的关键词（不推荐使用） |              |

图标：https://www.easyicon.net/

# 发表文章

```bash


```



# 用户自定义风格

custom_file_path

# Tag 插件

> Tags Settings
> See: https://theme-next.org/docs/tag-plugins/

参考链接：

[Hexo官网文档](https://hexo.io/zh-cn/docs/)
[NexT官网文档](http://theme-next.iissnan.com/getting-started.html)
[Hexo-NexT v7.1.1 Tag插件的使用](https://www.jianshu.com/p/1530f6959f79)
[[HEXO] NexT 主题提高博客颜值](https://walesexcitedmei.github.io/2018/08/30/HEXO-NexT-%E4%B8%BB%E9%A2%98%E6%8F%90%E9%AB%98%E5%8D%9A%E5%AE%A2%E9%A2%9C%E5%80%BC/)
[hexo next主题优化手册](https://inspurer.github.io/2018/11/11/hexo-next%E4%B8%BB%E9%A2%98%E4%BC%98%E5%8C%96/)
[hexo的next主题个性化配置](https://blog.csdn.net/weixin_44815733/article/details/88817220)
[Hexo Next主题进阶详细教程](https://blog.csdn.net/qq_31279347/article/details/82427562)
[Hexo博客NexT主题SEO优化](https://blog.csdn.net/qq_35661627/article/details/81267016)
[Github+Hexo搭建专属自己的博客](https://www.linjiujiu.xyz/2018/12/10/Github-Hexo%E6%90%AD%E5%BB%BA%E4%B8%93%E5%B1%9E%E8%87%AA%E5%B7%B1%E7%9A%84%E5%8D%9A%E5%AE%A2/)

