build my blog


# [hexo](https://hexo.io/zh-cn/)：快速、简洁且高效的博客框架

```css
npm install hexo-cli -g
hexo init blog
cd blog
npm install
hexo server
```



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

## 配置 Deployment

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

```sh
# 清除旧 public 文件
hexo clean

# 编译文件
hexo generate

# 本地预览  http://localhost:4000 
hexo serve

# 部署到博客 https://wilenwu.github.io
hexo deploye
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



# 发表文章


```sh
hexo new `title`         # 新文章`source\_posts`
hexo new page  about/me  # 新页面
```



# 用户自定义风格

custom_file_path

