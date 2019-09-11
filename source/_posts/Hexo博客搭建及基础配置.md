---
title: Hexo博客搭建及基础配置
tags: [Hexo,NexT,Github pages]
copyright: true
date: 2019-09-10 13:48:53
categories: 
- Hexo
---

[Hexo](https://hexo.io/zh-cn/) 是高效的静态站点生成框架，基于 [Node.js](https://nodejs.org/)。 通过 Hexo 你可以轻松地使用 Markdown 编写文章，除了 Markdown 本身的语法之外，还可以使用 Hexo 提供的 [标签插件](https://hexo.io/zh-cn/docs/tag-plugins.html) 来快速的插入特定形式的内容。Hexo 还拥有丰富的主题，任君部署。
<!-- more -->

个人博客部署主要有3方面的内容：
修改站点配置文件、主题配置文件和导入插件。

配置文件目录如下：

站点配置文件 `‪username.github.io\_config.yml`
主题配置文件  `‪username.github.io\themes\next\_config.yml`

前期Hexo 相关的安装及基础配置建议参考[官方文档]((https://hexo.io/zh-cn/))，有详细的中文介绍。

## 前提环境

- [Node.js](http://nodejs.org/) (Should be at least nodejs 6.9)
- [Git](http://git-scm.com/)
- 新建 github pages 库：库名为 `username.github.io` ，`username` 必须和github用户名保持一致 


## Hexo 相关命令 

选择博客目录文件夹，右键打开 `Git Bash Here`

- 安装命令 
```bash
npm install hexo-cli -g             # 导入Hexo
hexo init username.github.io        # 初始化博客文件
cd username.github.io               # 进入博客根目录
npm install                         # 导入
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

## Git

- 配置 SSH keys
    - 先在根目录下生成 SSH keys，复制
    ```sh
    ssh-keygen -t rsa -C "github注册邮箱"
    ```
    
    - 将生成的 SSH keys 加入 github
    setting -> SSH keys and GPG keys -> New SSH keys -> 粘贴即可

    
    - 测试设置是否成功
    ```sh
    ssh -T git@github.com
    ```

- 配置Git个人信息
```sh
git config --global user.name "username"
git config --global user.email "github注册邮箱"
```

- 安装插件
```sh
npm install hexo-deployer-git --save
```

- 修改{% label primary@站点配置文件 %}
```sh
deploy:
  type: git
  repo: git@github.com:username/username.github.io.git    # 库地址
  branch: master                                          # 分支名称
  message: update                                   # 自定义commit信息
```


- 发布

```sh
hexo deploye
```

当执行 `hexo deploy` 时，Hexo 会将 public 目录中的文件和目录推送至_config.yml 中指定的远端仓库和分支中，并且完全覆盖该分支下的已有内容。
可查看 github pages 网站  https://username.github.io

此外，如果您的 Github Pages 需要使用 CNAME 文件**自定义域名**，请将 CNAME 文件置于 `source` 目录下，只有这样 `hexo deploy` 才能将 CNAME 文件一并推送至部署分支



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

