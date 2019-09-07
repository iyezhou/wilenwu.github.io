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

```css
ssh -T git@github.com
```

## 配置Git个人信息

```git
git config --global user.name "wilenwu"
git config --global user.email "597379201@qq.com"
```

## 配置 Deployment

```bash
# Deployment
## Docs: https://hexo.io/docs/deployment.html
deploy:
  type: git
  repo: git@github.com:bxm0927/bxm0927.github.io.git
  branch: master
```


# 安装 NexT主题

```
git clone https://github.com/theme-next/hexo-theme-next  themes/next
```