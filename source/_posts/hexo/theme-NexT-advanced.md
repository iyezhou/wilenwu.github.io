---
ID: 5980ef6822399cf8ecb3c84fd29d6252
title: NexT主题进阶
tags: [Hexo,NexT,Github pages]
copyright: true
date: 2019-09-11 14:14:04
categories: [Hexo]
---
<div align="center"><a title="NexT website repository" href="https://github.com/theme-next/theme-next.org"><img align="center" width="60" height="60" src="https://raw.githubusercontent.com/theme-next/hexo-theme-next/master/source/images/logo.svg?sanitize=true"></a><font  size=5><b>e x T</b></font></div>

NexT 是 [Hexo](http://hexo.io) 框架中最为流行的主题之一。精于心，简于形。
NexT 支持多种常见第三方服务，使用 **第三方服务** 来扩展站点的功能 。
除了 Markdown 支持的语法之外，NexT 借助 Hexo 提供的 **tag 插件**， 为您提供在书写文档时快速插入带特殊样式的内容。

<!-- more -->

# 安装主题

1. 克隆NexT 主题

   {% tabs clone, 2 %}
   <!-- tab 克隆最新版本 -->
   定位到 Hexo 站点目录下，将NexT主题文件克隆或者拷贝到`hexo/theme`目录下即可。
   {% code %}
   cd your-hexo-sit
   git clone https://github.com/iissnan/hexo-theme-next themes/next
   {% endcode %}
   <!-- endtab -->
   
   <!-- tab 克隆稳定版本 -->
   定位到 Hexo 站点目录下，将NexT主题文件克隆或者拷贝到`hexo/theme`目录下即可。本博客就是克隆的这个版本。
   {% code %}
   cd your-hexo-sit
   git clone https://github.com/theme-next/hexo-theme-next  themes/next
   {% endcode %}
   <!-- endtab -->
   {% endtabs %}

2. 启用主题

   与所有 Hexo 主题启用的模式一样。 当 克隆/下载 完成后，打开站点配置文件， 找到 theme 字段，并将其值更改为 next
   
   ```sh \_config.yml
   theme: next
   ```

# 主题核心配置

核心配置可完全参考[NexT官网中文文档](http://theme-next.iissnan.com/getting-started.html) 
包括：选择Scheme、设置语言、设置菜单、设置头像、设置侧栏、添加「标签」页面、添加「分类」页面、设置字体、设置代码高亮主题、侧边栏社交链接、开启打赏功能、友情链接、腾讯公益404页面、数据统计与分析、搜索服务、分享服务等。

主题配置文件 `‪username.github.io\themes\next\_config.yml`
分为若干块，每块都附带官方说明文件网址，可以用谷歌浏览器打开，开启翻译，即可轻松配置。
目前主流的组件基本已被装进 NexT主题，只需修改主题配置文件参数即可，网上的若干优化教程估计已不适用。

NexT 7 自定义样式支持已与主题核心组件分离，如博客背景、文本结束标记等。这样用户可放心升级主题而不会破坏自定义配置。在路径 `source/_data` 下添加自定义文件，并在主题配置文件 `custom_file_path` 取消注释。

另，tag 插件也是NexT的一大亮点，会单独开一篇文章具体介绍，请参考 [NexT tag 插件](http://localhost:4000/2019/09/11/Hexo%20tag%20%E6%8F%92%E4%BB%B6/)

本人博客：由 [Hexo](https://hexo.io/) 强力驱动 v3.9.0 |主题 – [NexT.Gemini](https://theme-next.org/) v7.4.0


# 主题优化

## RSS支持
RSS(Really Simple Syndication)称为简易信息聚合，是一种描述和同步网站内容的格式。RSS搭建了信息迅速传播的一个技术平台，使得每个人都成为潜在的信息提供者。发布一个RSS文件后，这个RSS Feed中包含的信息就能直接被其他站点调用，而且由于这些数据都是标准的XML格式，所以也能在其他的终端和服务中使用，是一种描述和同步网站内容的格式。

NexT 中 RSS 有三个设置选项，满足特定的使用场景。 更改主题配置文件，设定 rss 字段的值。
{% tabs rss, 1 %}
<!-- tab false -->
禁用 RSS，不在页面上显示 RSS 连接。
{% code next\_config.yml %}
rss: false 
{% endcode %}
<!-- endtab -->

<!-- tab blank -->
留空：使用 Hexo 生成的 Feed 链接，需先安装 `hexo-generator-feed` 插件
{% code next\_config.yml %}
rss:  
{% endcode %}

- 安装 `hexo-generator-feed` 插件
   {% code %}
   npm install hexo-generator-feed --save 
   {% endcode %}
   
- 在站点配置文件 `_config.yml` 修改/添加
   {% code \_config.yml %}
   feed:
     type: atom
     path: atom.xml
     limit: 20     # Feed中的最大帖子数(使用0或false显示所有帖子)
   {% endcode %}
   <!-- endtab -->

<!-- tab URL -->
具体的URL：适用于已经烧制过 Feed 的情形。
{% code next\_config.yml %}
rss: /atom.xml
{% endcode %}

- 安装 `hexo-generator-feed` 插件
   {% code %}
   npm install hexo-generator-feed --save 
   {% endcode %}
   
- 在站点配置文件 `_config.yml` 修改/添加
   {% code \_config.yml %}
   feed:
     type: atom
     path: atom.xml
     limit: 20     # Feed中的最大帖子数(使用0或false显示所有帖子)
   {% endcode %}
<!-- endtab -->
{% endtabs %}


## Creative Commons 

NexT支持显示Creative Commons 4.0国际许可证。这些许可证允许创作者声明保留的权利和放弃的权利。

修改主题配置文件
```sh next\_config.yml
creative_commons:
  license: by-nc-sa
  sidebar: true
  post: true
  language: deed.zh

```

## 阅读进度和书签

NexT支持页面滚动阅读进度指示器。

修改主题配置文件 
```sh next\_config.yml
reading_progress:
  enable: true
  color: "#37c6c0"
  height: 2px
```

Bookmark是一个插件，允许用户保存他们的阅读进度。用户只需单击页面左上角的书签图标即可保存滚动位置。当他们下次访问您的博客时，他们可以自动恢复每个页面的最后滚动位置。
在主题配置文件启用
```sh next\_config.yml
bookmark:
  enable: true
  color: "#222"   # 自定义书签颜色
  save: auto  # auto | manual 自动保存进度或点击保存进度
```

## 网站图标(favicon)

默认情况下，Hexo站点在`hexo-site/themes/next/source/images/`目录中使用 NexT favicons 。
可以自己下载图标，放在`hexo-site/source/images/`目录中，修改主题配置文件。

>  图标网站 [easyicon](https://www.easyicon.net/)

```sh
favicon：
  small：/  images/ favicon-16x16-next.png 
  medium： /images/favicon-32x32-next.png 
  apple_touch_icon： /images/apple-touch-icon-next.png 
  safari_pinned_tab： /images/logo.svg 
  android_manifest： /images/manifest.json 
  ms_browserconfig： /images/browserconfig.xml
```

## SEO支持

SEO(Search Engine Optimization)意为搜索引擎优化,利用搜索引擎的规则提高网站在有关搜索引擎内的自然排名。

- 安装站点地图(sitemap)插件
```sh
npm install hexo-generator-sitemap --save
npm install hexo-generator-baidu-sitemap --save
```

- 站点配置文件修改/添加
```sh \_config.yml
# SEO 
sitemap: 
  path: sitemap.xml
baidusitemap:
  path: baidusitemap.xml
```

- 启用百度推送功能，博客会自动将网址推送到百度，这对搜索引擎优化非常有帮助。
主题配置文件修改 `baidu_push: true`

## 字数统计和阅读时长

- 导入插件
   {% code %}
   npm install hexo-symbols-count-time --save
   {% endcode %}

- 站点配置文件
   {% code \_config.yml %}
   symbols_count_time:
     symbols: true              # 是否启用
     time: true                 # 估计阅读时间
     total_symbols: true        # 页脚部分中所有帖子字数
     total_time: true           # 页脚部分中所有帖子的估计阅读时间
     exclude_codeblock: false
   {% endcode %}

- 主题配置文件
   {% code next\_config.yml %} 
   symbols_count_time:
     separated_meta: true       # 以分隔线显示单词计数和估计读取时间
     item_text_post: true       # 显示单词计数和估计阅读时间的文本描述
     item_text_total: false     # 在页脚部分显示单词计数和估计阅读时间的文本描述
     awl: 4                     # 平均字长
     wpm: 275                   # 每分钟的平均单词数
     suffix: mins.
   {% endcode %}

## 文章热度

- 配置 leancloud [官方使用文档](https://theme-next.org/docs/third-party-services/comments#Disqus)

- 修复NexT的leancloud计数器的安全插件
1. 导入插件
   {% code %}
   npm install hexo-leancloud-counter-security --save
   {% endcode %}

2. 站点配置文件添加
   {% code \_config.yml %}
   leancloud_counter_security:
     enable_sync: true
     app_id: <<your app id>>
     app_key: <<your app key>>
     username: <<your username>> # 部署时会询问是否留空
     password: <<your password>> # 建议留空。部署时会询问是否留空
   {% endcode %}

3. 主题配置文件修改 
   {% code next\_config.yml %}
   leancloud_visitors:
     enable: true
     app_id: <<your app id>>
     app_key: <<your app key>>
     # Dependencies: https://github.com/theme-next/hexo-leancloud-counter-security
     security: true
     betterPerformance: false
   {% endcode %}

4. 控制台命令：在Leancloud数据库中注册用户以进行权限控制
   {% code %}
   hexo lc-counter register <<username>> <<password>>
   {% endcode %}





## 相关热门帖子

请参考[官方文档](https://github.com/tea3/hexo-related-popular-posts)

## 背景动画

NexT 支持多种背景动画，导入插件并修改对应主题配置文件即可

加载栏: [pace](https://github.com/theme-next/theme-next-pace)
3D库: [three](https://github.com/theme-next/theme-next-three)
流动线条: [canvas_nest](https://github.com/theme-next/theme-next-canvas-nest)
彩带: [canvas_ribbon](https://github.com/theme-next/theme-next-canvas-ribbon)


# 第三方服务

静态网站在某​​些功能上受到限制，因此我们需要第三方服务来扩展我们的网站。
您可以随时使用NexT支持的第三方服务扩展所需的功能。

## 数学公式

NexT提供了两个用于显示数学公式的渲染引擎。

1. 启用数学公式

   ```sh
   math:
     enable: true
     per_page: true 
   ```

   > per_page: true 默认只渲染 Front-matter 标记 `mathjax: true` 的文档
   > per_page: false 每一页都会导入 `mathjax / katex` 脚本

2. 选择渲染引擎

   目前，NexT提供了两个渲染引擎：MathJax和KaTeX。
   
   {% tabs math, 2 %}
   <!-- tab mathjax -->
   - 需要卸载原始渲染器 `hexo-renderer-marked` 并选择渲染器之一安装：
   {% code %}
   npm un hexo-renderer-marked --save 
   npm i hexo-renderer-kramed --save ＃ or hexo-renderer-pandoc
   {% endcode %}

   - 打卡主题配置文件渲染引擎
   {% code next\_config.yml %}
   mathjax：    
     enable：true
   {% endcode %}
   <!-- endtab -->

   <!-- tab katex -->
   - 需要卸载原始渲染器 `hexo-renderer-marked` 并选择渲染器之一安装：
   {% code %}
   npm un hexo-renderer-marked --save 
    npm i hexo-renderer-markdown-it-plus --save ＃ or hexo-renderer-markdown-it
   {% endcode %}

   - 打卡主题配置文件渲染引擎
   {% code next\_config.yml %}
    katex：    
     enable：true
   {% endcode %}
   <!-- endtab -->
   {% endtabs %}

>  Note: 渲染器插件只能选择其一，否则不能正常显示。



## 评论系统

NexT 支持多款评论系统。
如需取消某个 页面/文章 的评论，在 md 文件的 front-matter 中增加 `comments: false`

- gitalk: 是一个基于Github Issue和Preact的现代评论组件。

   1. 单击此处注册新的[OAuth应用程序](https://github.com/settings/applications/new)。
   其他内容可以随意填写，但请务必填写正确的回调URL（通常是与评论页面对应的域名）。
   然后，您将获得 Client ID和Client secret。
   2. 创建一个您想要在GitHub中存储Gitalk 评论的存储库。
   3. 修改主题配置文件 
   ```sh next\_config.yml
   # Gitalk
   # Demo: https://gitalk.github.io
   gitalk:
     enable: true 
     github_id:             # Github username
     repo:                  # Gitalk 评论的存储库
     client_id:             # Client ID
     client_secret:         # Client Secret
     admin_user:            # 所有者和合作者
     distraction_free_mode: true # Facebook-like distraction free mode
     language: zh-CN
   ```


- Valine (China): 是一种快速，简单和高效的Leancloud，不依赖后端评论系统。[官方使用文档](https://theme-next.org/docs/third-party-services/comments#Disqus)

- 多评论系统支持: NexT允许您同时启用多个评论系统。[官方使用文档](https://theme-next.org/docs/third-party-services/comments#Disqus)


## 聊天服务
请参考[官方文档](https://theme-next.org/docs/third-party-services/chat-services)


# 自定义样式支持

## 文本结束标记

在路径 `source/_data` 下创建/修改 `post-body-end.swig`文件，并添加以下内容
```sh
<div>
    {% if not is_index %}
        <div style="text-align:center;color: #ccc;font-size:14px;">-------------本文结束<i class="fa fa-paw"></i>感谢您的阅读-------------</div>
    {% endif %}
</div>
```

主题配置文件取消注释
```sh next\_config.yml
custom_file_path:
  postBodyEnd: source/_data/post-body-end.swig
```

## 修改背景图及侧边栏颜色，修改主副标题颜色

在路径 `source/_data` 下创建/修改 `styles.styl`文件，并添加以下内容
```sh
// 添加背景 url(https://source.unsplash.com/random/1600x900); 
body {
    background:url(/images/background6.jpg);
    background-repeat: no-repeat;
    background-attachment:fixed;
    background-position:50% 50%;
    background-size:cover;
}

// 标题栏背景
.site-meta {
   background: $blue; 
}  

//主标题颜色
.brand{
    color: $white
}

//副标题颜色
.site-subtitle{
    color: #fff
}


// 修改主体透明度
.main-inner{
    background: #fff;
    opacity: 0.95;
}

// 修改菜单栏透明度
.header-inner {
    opacity: 0.95;
}

// 主页文章添加阴影效果
.post {
   margin-top: 60px;
   margin-bottom: 60px;
   padding: 25px;
   -webkit-box-shadow: 0 0 5px rgba(202, 203, 203, .5);
   -moz-box-shadow: 0 0 5px rgba(202, 203, 204, .5);
}
```

主题配置文件取消注释
```sh next\_config.yml
custom_file_path:
  style: source/_data/styles.styl.swig
```


## 文章加密

在需要加密的文章 Front matter 区域设置 `password: 123456`

在路径 `source/_data` 下创建/修改 `head.swig`文件，并添加以下内容
```sh
<script> 
 (function(){
        if('{{ page.password }}'){
            if (prompt('请输入文章密码') !== '{{ page.password }}'){
                alert('密码错误！');
                history.back();
            }
        }
    })();
</script>
```

主题配置文件取消注释
```sh next\_config.yml
custom_file_path:
  head: source/_data/head.swig
```


参考链接：

[hexo的next主题个性化配置](https://blog.csdn.net/weixin_44815733/article/details/88817220)
[Hexo Next主题进阶详细教程](https://blog.csdn.net/qq_31279347/article/details/82427562)
[hexo个人博客next主题优化](https://www.linjiujiu.xyz/2018/12/11/hexo%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2next%E4%B8%BB%E9%A2%98%E4%BC%98%E5%8C%96/)