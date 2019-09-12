---
title: Hexo博客搭建及配置
tags: [Hexo,NexT,Github pages]
copyright: true
date: 2019-09-10 13:48:53
categories: 
- Hexo
---

[Hexo](https://hexo.io/zh-cn/) 是高效的静态站点生成框架，基于 [Node.js](https://nodejs.org/)。 通过 Hexo 你可以轻松地使用 Markdown 编写文章，除了 Markdown 本身的语法之外，还可以使用 Hexo 提供的 [tag 插件](https://hexo.io/zh-cn/docs/tag-plugins.html) 来快速的插入特定形式的内容。Hexo 还拥有丰富的主题，任君部署。
<!-- more -->


## 前提环境

- [Node.js](http://nodejs.org/) (Should be at least nodejs 6.9)
- [Git](http://git-scm.com/)
- 创建 github pages 库：库名为 `username.github.io` ，`username` 必须和github用户名保持一致 


## Hexo 相关命令 

选择博客目录文件夹，右键打开 `Git Bash Here`

- 安装命令 
```bash
npm install hexo-cli -g             # 安装hexo
hexo init username.github.io        # 初始化项目文件夹
cd username.github.io               # 进入项目根目录
npm install                         # 安装依赖包
```

- 常用操作
```bash
hexo clean           # 清除缓存
hexo generate        # 编译文件 生成静态页面至 \public 目录
hexo serve           # 本地预览  http://localhost:4000 
hexo deploye         # 发布 https://username.github.io

hexo new "PostName"        # 新建文章至 \source\_posts
hexo new page  "pageName"  # 新建页面
```

- 命令简写
```bash
hexo g -s    # 生成加预览
hexo g -d    # 生成加发布
```

## 预览

可在本地4000端口预览 http://localhost:4000
主题的配置文件，修改时会自动更新，无需重启服务器。

- 先安装服务器插件
```sh
npm install hexo-server --save
```

- 修改{% label primary@站点配置文件 %}
```sh
deploy:
  type: git
```

- 预览
```sh
hexo serve 
```

## Git 配置

### 配置 SSH keys

- 生成新的 SSH keys
```sh
ssh-keygen -t rsa -C "github的注册邮箱"
```
    
- 添加 SSH Key 到 GitHub
在本地用户文件夹 `C:\Users\Administrator\` 找到 `.ssh\id_rsa.pub`
用编辑器打开，并复制全部内容 ·`ctrl+A` -> `ctrl+C`
打开 github `setting` -> `SSH keys and GPG keys` -> `New SSH keys` -> 粘贴 -> `Add SSH key`


- 测试设置是否成功
```sh
ssh -T git@github.com
```

- 配置个人信息
```sh
git config --global user.name "username"
git config --global user.email "github注册邮箱"
```

### 部署博客到 github pages

- 安装插件
```sh
npm install hexo-deployer-git --save
```

- 修改{% label primary@站点配置文件 %}
```sh
deploy:
  type: git
  repo: git@github.com:username/username.github.io.git    # 预先创建好的库地址
  branch: master                                          # 分支名称
  message: update                                   # 自定义commit信息
```

- 推送到 github

```sh
hexo deploye
```

完成以上操作后，使用浏览器访访问 https://username.github.io 就可以成功访问我们的博客

当执行 `hexo deploy` 时，Hexo 会将 public 目录中的文件和目录推送至_config.yml 中指定的远端仓库和分支中，并且完全覆盖该分支下的已有内容。
此外，如果您的 Github Pages 需要使用 CNAME 文件**自定义域名**，请将 CNAME 文件置于 `source` 目录下，只有这样 `hexo deploy` 才能将 CNAME 文件一并推送至部署分支

## 站点配置文件

Hexo 框架主要配置2方面的内容：站点配置文件和主题配置文件。

站点配置文件 `‪username.github.io\_config.yml`
主题配置文件  `‪username.github.io\themes\next\_config.yml`

站点配置文件建议参考[中文官方文档]((https://hexo.io/zh-cn/))

站点配置主要分为几块：

 Site  | 网站
:---|:---
title:  title           |网站标题
subtitle: ∞                            | 网站子标题 
description: 个人技术博客              | 网站的描述性
keywords:                              | 网站的关键字 
author: name                       | 网站的作者
language: zh-CN                        | 网站采用语言，与/theme/next/languages/zh-CN.yml下的文件名对应
timezone:                              | 网站的时区

| URL                                  | url配置                                                      |
| :----------------------------------- | :----------------------------------------------------------- |
| url: https://username.github.io      | 网站的url，如果不在域名根目录，应包含子目录，且root要设置为`/子目录/` |
| root: /                              | 网站的根目录                                                 |
| permalink: :year/:month/:day/:title/ | 文章永久链接的形成模版。每一篇文章都有唯一的url。            |
| permalink_defaults:                  | 文章永久链接中，各部分的默认值。                             |

| Directory                | 路径配置             |
| :----------------------- | :------------------- |
| source_dir: source       | 网站中源文件         |
| public_dir: public       | 生成的静态网站的目录 |
| tag_dir: tags            | 标签页所在的文件夹   |
| archive_dir: archives    | 文档页所在的文件夹   |
| category_dir: categories | 类别页所在的文件夹   |
| code_dir: downloads/code | 代码页所在的文件夹   |
| i18n_dir: :lang          | 国际语言所在的文件夹 |
| skip_render: README.md   | 忽略文档清单         |

| Writing                  | 写作设置                                                     |
| :----------------------- | :----------------------------------------------------------- |
| new_post_name: :title.md | 默认新建文档名，`:title`为变量，指文档标题，也可用其他变量   |
| default_layout: post     | 新建文档的默认布局                                           |
| titlecase: false         | 是否要把标题中的首字符大写                                   |
| external_link: true      | 是否要在新开tab中打开外链                                    |
| filename_case: 0         | 文件名是否小写敏感                                           |
| render_drafts: false     | 是否渲染草稿                                                 |
| post_asset_folder: false | 是否启用资源文件夹。如启用，新建文档同时建立同名的资源文件夹 |
| relative_link: false     | 是否把站内资源的链接改为站内相对链接。建议关闭。             |
| future: true             | 文档中指定为未来时间创建                                     |

```sh
highlight:                     
  enable: true                          # 是否开启代码高亮功能 
  line_number: true                     # 代码块中是否在前面加上行号
  auto_detect: false                    # 是否自动检测代码块的语言
  tab_replace:                          # 用什么字符来代替tab(`\t`)字符。 
```

主页设置

```sh
index_generator:          
  path: ''                   # 主页所在路径，默认为''
  per_page: 10               # 主页的索引页包含文章数量，如未定义，则采用根目录下的`per_page`值
  order_by: -date            # 文章（Post类型）排序属性，`-`为降序 
  
archive_generator:           # 归档页
  per_page: 20
  yearly: true
  monthly: true

tag_generator:               # 标签页
  per_page: 10  
```

| Category & Tag                  | 分类和标签                                                   |
| :------------------------------ | :----------------------------------------------------------- |
| default_category: uncategorized | 对文档的默认分类                                             |
| category_map:                   | 对文档中的分类字段进行映射，建立分类文件夹时采用映射后的字符串 |
| tag_map:                        | 对文档中的标签字段进行映射，建立标签文件夹时采用映射后的字符串 |
| per_page: 10                    | 主页/分类/标签/存档等类型索引页包含文章数量                  |
| pagination_dir: page            | 分页所在文件夹                                               |

接下来是扩展(Extensions)，放置插件和主题。

```sh
theme: next    # 更换主题
```



## 写作模板

在新建文章时，Hexo 会根据 `scaffolds` 文件夹内相对应的模板来建立文件

Front-matter 是文件最上方以 `---` 分隔的区域，用于指定个别文件的变量，举例来说：

```bash
---
title: Hello World
date: 2013/7/13 20:46:25
---
```

| 参数         | 描述  | 默认值       |
| :----------- | :------ | :-------- |
| `layout`     | 布局  |        |
| `title`      | 标题    |              |
| `date`       | 建立日期   | 文件建立日期 |
| `updated`    | 更新日期    | 文件更新日期 |
| `comments`   | 开启文章的评论功能   | true         |
| `tags`       | 标签（不适用于分页）   |              |
| `categories` | 分类（不适用于分页）    |              |
| `permalink`  | 覆盖文章网址    |              |
| `keywords`   | 仅用于 meta 标签和 Open Graph 的关键词（不推荐使用） |     |


## 分类和标签

可以在 Front-matter 中设置分类和标签。
```sh
categories:
- Diary
  - Sunday 
tags:
- Games
```


## 文章摘要和截断

在文章中使用 `<!-- more -->`，那么 `<!-- more -->` 之前的文字将会被视为摘要，在主页中展示。



参考链接：
[Github+Hexo搭建专属自己的博客](https://www.linjiujiu.xyz/2018/12/10/Github-Hexo%E6%90%AD%E5%BB%BA%E4%B8%93%E5%B1%9E%E8%87%AA%E5%B7%B1%E7%9A%84%E5%8D%9A%E5%AE%A2/)