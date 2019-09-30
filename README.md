[Hexo](https://hexo.io/zh-cn/) 是高效的静态站点生成框架，基于 [Node.js](https://nodejs.org/)。 通过 Hexo 你可以轻松地使用 Markdown 编写文章，除了 Markdown 本身的语法之外，还可以使用 Hexo 提供的 [tag 插件](https://hexo.io/zh-cn/docs/tag-plugins.html) 来快速的插入特定形式的内容。Hexo 还拥有丰富的主题，任君部署。


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

- 修改站点配置文件
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
