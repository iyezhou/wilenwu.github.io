---
ID: a6be1f1f2719bfe477cd1420bd44b1c6
title: Hexo标签插件的使用
tags: [Hexo,NexT,Github pages]
copyright: true
date: 2019-09-11 14:10:48
categories: [Hexo]
---
「tag 插件」(Tag Plugin) 是 Hexo 提供的一种快速生成特定内容的方式。 例如，在标准 Markdown 语法中，我们无法指定图片的大小。这种情景，我们即可使用标签来解决。 Hexo 内置来许多标签来帮助写作者可以更快的书写， [完整的标签列表](https://hexo.io/docs/tag-plugins.html) 可以参考 Hexo 官网。 另外，Hexo 也开放来接口给主题，使主题有可能提供给写作者更简便的写作方法。 

<!-- more -->

# Hexo 标签插件使用

## 引用块

在文章中插入引言，可包含作者、来源和标题，均可选。

标签方式：使用 `blockquote` 或者 简写 `quote`。

```sh
{% blockquote author, source link source_link_title %}
content
{% endblockquote %}
```

{% blockquote author, source link source_link_title %}
content
{% endblockquote %}


## 代码块

在文章中插入代码，包含指定语言、附加说明和网址，均可选。
标签方式：使用 `codeblock` 或者 简写 `code`。

```sh
{% codeblock [title] [lang:language] [url] [link text] %}
code snippet
{% endcodeblock %}
```

{% codeblock title lang:language url link text %}
code snippet
{% endcodeblock %}

反引号代码块

\`\`\`[language] [title] [url] [link text] 
code snippet 
\`\`\`

## iframe

在文章中插入 iframe。

```
{% iframe url [width] [height] %}
```

## Image

在文章中插入指定大小的图片。

```
{% img [class names] /path/to/image [width] [height] "title text 'alt text'" %}
```

## Link

在文章中插入链接，并自动给外部链接添加 `target="_blank"` 属性。

```
{% link text url [external] [title] %}
```

## Include Code

插入 `source/downloads/code` 文件夹内的代码文件。`source/downloads/code` 不是固定的，取决于你在配置文件中 `code_dir` 的配置。

```sh
{% include_code [title] [lang:language] path/to/file %}
```

# NexT 标签插件使用

## 文本居中引用

此标签将生成一个带上下分割线的引用，同时引用内文本将自动居中。 文本居中时，多行文本若长度不等，视觉上会显得不对称，因此建议在引用单行文本的场景下使用。 例如作为文章开篇引用 或者 结束语之前的总结引用

使用方式

- HTML方式：直接在 Markdown 文件中编写 HTML 来调用，给 `img` 添加属性 `class="blockquote-center"` 即可。
- 标签方式：使用 `centerquote` 或者 简写 `cq`。

```
# HTML方式
<blockquote class="blockquote-center">blah blah blah</blockquote>

# 标签方式
{% centerquote %}blah blah blah{% endcenterquote %}
```

{% cq %} 佚名 {% endcq %}

## 突破容器宽度限制的图片

当使用此标签引用图片时，图片将自动扩大 26%，并突破文章容器的宽度。 此标签使用于需要突出显示的图片, 图片的扩大与容器的偏差从视觉上提升图片的吸引力。 此标签有两种调用方式（详细参看底下示例）：

使用方式

- HTML方式：直接在 Markdown 文件中编写 HTML 来调用，为 `img` 添加属性 `class="full-image"`即可。
- 标签方式：使用 `fullimage` 或者 简写 `fi`， 并传递图片地址、 `alt` 和 `title` 属性即可。 属性之间以逗号分隔。

```
# HTML方式:
<img src="/image-url" class="full-image" />

# 标签 方式
{% fullimage /image-url, alt, title %}
```

## Note 标签

使用方式

```
{% note [class] [no-icon] %} 
content (support inline tags too.io).
{% endnote %}
```

> [class]: default | primary | success | info | warning | danger
> [no-icon] : 禁用图标


效果如下
{% note default %} default {% endnote %}
{% note default no-icon %} default no-icon {% endnote %}
{% note primary %} primary  {% endnote %}
{% note success %} success {% endnote %}
{% note info %} info  {% endnote %}
{% note warning %} warning {% endnote %}
{% note danger %} danger{% endnote %}

## Tabs 选项卡

使用方式

```
{% tabs Unique name, [index] %}
<!-- tab [caption] [@icon] -->
**This is Tab 1.**
<!-- endtab -->

<!-- tab Solution 2 -->
**This is Tab 2.**
<!-- endtab -->

<!-- tab Solution 3 @paw -->
**This is Tab 3.**
<!-- endtab -->
{% endtabs %}
```
> Unique name：选项卡唯一名字
> [index]：活动卡索引号
> [caption]：标签标题
> [@icon]：FontAwesome图标名称

{% tabs Unique name, 1 %}
<!-- tab caption @github -->
**This is Tab 1.**
<!-- endtab -->

<!-- tab Solution 2 -->
**This is Tab 2.**
<!-- endtab -->

<!-- tab Solution 3 @paw -->
**This is Tab 3.**
<!-- endtab -->
{% endtabs %}


## Label 标签

使用方法

```
{% label [class]@Text %}
```
> [class] : default | primary | success | info | warning | danger.

效果如下

Will you choose {% label default@default %}, {% label primary@primary %}, {% label success@success %}, {% label info@info %}, {% label warning@warning %} or {% label danger@danger %} ?

## Video 标签

```
{% video https://example.com/sample.mp4 %}
```

## Button 标签

使用 `button` 或者 简写 `btn`

```
{% button url, text, icon [class], [title] %}
```

> url：绝对或相对路径
> text, icon：按钮文字或FontAwesome图标
> [class]：FontAwesome类：fa-fw | fa-lg | fa-2x | fa-3x | fa-4x | fa-5x
> [title]：鼠标悬停时的工具提示

{% btn #,home, home %}  


## 流程图

```markdown
{% mermaid type%}
{% endmermaid %}
```
> type: 请访问 https://github.com/knsv/mermaid 以获取更多信息

```sh
{% mermaid sequenceDiagram %}
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long that the text does not fit on a row.
Bob-->>Alice: Checking with John...
Alice->>John: Yes... John, how are you?
{% endmermaid %}
```

{% mermaid sequenceDiagram %}
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long that the text does not fit on a row.
Bob-->>Alice: Checking with John...
Alice->>John: Yes... John, how are you?
{% endmermaid %}

## 图片集

```
{% grouppicture [group]-[layout] %}{% endgrouppicture %}
{% gp [group]-[layout] %}{% endgp %}
```

> [group]  : 要在组中添加的图片总数
> [layout] : 显示组下的默认图片

```
{% grouppicture 6-3 %}
  ![](/images/github.png)
  ![](/images/github.png)
  ![](/images/github.png)
  ![](/images/github.png)
  ![](/images/github.png)
  ![](/images/github.png)
{% endgrouppicture %}
```
{% grouppicture 6-3 %}
  ![](/images/github.png)
  ![](/images/github.png)
  ![](/images/github.png)
  ![](/images/github.png)
  ![](/images/github.png)
  ![](/images/github.png)
{% endgrouppicture %}