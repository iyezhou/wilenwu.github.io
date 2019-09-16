
---
title: Python手册(Standard Library)--re+正则表达式
tags: [python]
mathjax: false
copyright: true
date: 2018-05-09 23:15:58
categories: [python,Standard Library]
sticky: false
---



----------
<!-- more -->

# re模块

## 函数
| **匹配**| 返回re对象MatchObject |
| :------------- | :------------- |
| re.match(pattern,string,flags)  | 起始位置匹配pattern，返回re.MatchObject  |
| re.search(pattern,string,flags) | 扫描整个字符串并返回第一个成功的匹配  |
| re.findall(pattern,string,flags=0) | 返回匹配到所有子串list |
| re.finditer(pattern, string,  flags=0)| 类似findall，返回迭代器  |
| **检索和替换**||
| re.sub(pattern,replace,string,count=0)| replace为字符或函数<br>count为替换的次数|
| **分割**| 返回字符串列表 |
| re.split(pattern,string,maxsplit=0,flags) | maxsplit最大分割次数|

## re对象
`re.RegexObject` 和 `re.MatchObject`

| re.RegexObject|说明|
| ------------- | ------------- |
| re.compile(pattern,flags=0) | 编译pattern，提高效率，返回re.RegexObject |

| re.MatchObject方法|说明|
| :------------- | :------------- |
| obj.group(num=0) | 返回匹配到的字符串元组|
| obj.groups()  | 返回小组号|
| obj.start()| 返回匹配开始的位置  |
| obj.end()  | 返回匹配结束的位置  |
| obj.span() | 返回匹配到的index元祖(start,end)  |


 ## flags标志
 
| flags |说明|
| ------------- | ------------- |
| re.I | 使匹配对大小写不敏感 |
| re.L | 做本地语言识别（locale-aware）匹配|
| re.M | 多行匹配，影响 ^ 和 $ |
| re.S | 使.(dot)匹配所有字符，包括换行  |
| re.U | Unicode字符集解析  |
| re.X ||


----------


# 正则表达式

| 限定符  | 描述  | 等价|
| :---- | :------ |:------- |
| * | 零次或多次  | {0,} |
| + | 一次或多次  | {1,} |
| ? | 零次或一次  | {0,1}|
| {n}  | 匹配确定的n次||
| {n,} | 至少匹配n次 ||
| {n,m}| 匹配>=n且<=m次||

**限定符都是贪婪匹配，加后缀`?`，可转换为最小匹配（如`*?`）** 

| **非打印字符**|  |
| :---- | :------ |:------- |
| \f| 换页符 ||
| \n| 换行符 ||
| \r| 回车符 ||
| \t| 制表符 ||
| \v| 垂直制表符  ||
| \s| 空白字符| [ \f\n\r\t\v] |
| \S| 非空白字符  | [^ \f\n\r\t\v]|

| **打印字符** | 描述  | 等价|
| :---- | :------ |:------- |
| .(dot)  | 匹配除换行符（\n、\r）之外的任何单个字符||
| \d| 匹配一个数字 | [0-9]|
| \D| 匹配一个非数字| [^0-9]  |
| \w| 匹配字母、数字、下划线  | [A-Za-z0-9_]  |
| \W| 匹配非字母、数字、下划线 | [^A-Za-z0-9_] |
| \num |  ||


| **定位符**  | 描述  | 示例|
| :---- | :------ |:------- |
| `$` | 匹配结尾位置 | `(.csv)$` |
| ^ | 匹配开始位置 | `^(Windows)` |
| \b| 匹配单词边界位置  | `er\b` 可以匹配`never` 中的 `er`，但不能匹配 `verb`中的 `er` |
| \B| 匹配非单词边界位置 | `er\B` 能匹配 `verb` 中的 `er`，但不能匹配 `never`中的 `er` |
| \A| 匹配字符串开始||
| \Z| 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串  ||
| \z| 匹配字符串结束||
| \G| 匹配最后匹配完成的位置。 ||

| **字符集合** | 描述  ||
| :---- | :------ |:------- |
| x\|y | 或，优先级最低||
| [xyz]| 字符集合，匹配任意一个  ||
| [a-z]| 小写字母||
| [0-9]| 数字  ||
| `[^xyz] ` | 匹配不在集合里的任意字符 ||
| `[^a-z]`  | 除了小写字母 ||
| `[A-Z]`| 大写字母||
|`[\u4e00-\u9fa5]`|  匹配中文字符

| **选择**| 描述  | 示例|
| :---- | :------ |:------- |
| (pattern)  | 匹配pattern并获取结果  ||
| (?:pattern)| 匹配 pattern 但不获取匹配结果| `Win(?:7\|10)`相当于`Win7\|Win10`简略版  |
| (?=pattern)| 正向肯定预查（look ahead positive assert)| `Win(?=XP)`能匹配`WinXP`中的`Win`，但不能匹配`Win10`中的`Win` |
| (?!pattern)| 正向否定预查(negative assert)  | `Win(?!XP)`能匹配`Win10`中的`Win`，但不能匹配`WinXP`中的`Win`|
| (?<=pattern)  | 反向(look behind)肯定预查| `(?<=7)Win`能匹配`7Win`中的`Win`，但不能匹配`10Win`中的`Win` |
| (?<!pattern)  | 反向否定预查 | `(?<!7)Win`能匹配`10Win`中的`Win`，但不能匹配`7Win`中的`Win` |

| **Python**  |  ||
| :---- | :------ |:------- |
| (?imx)  | 正则表达式包含三种可选标志：i, m, 或 x  。只影响括号中的区域。 ||
| (?-imx) | 正则表达式关闭 i, m, 或  x 可选标志。只影响括号中的区域。||
| (?imx: re) | 在括号中使用i, m, 或 x  可选标志 ||
| (?-imx: re)| 在括号中不使用i, m, 或 x  可选标志||
| (?#...) | 注释. ||



