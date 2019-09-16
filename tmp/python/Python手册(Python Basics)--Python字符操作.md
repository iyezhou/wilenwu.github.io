**说明**：本手册所列包来自[Awesome-Python](https://awesome-python.com/) ，结合[GitHub](https://github.com/) 和官方文档，参考 **SeanCheney** 大神在简书上翻译的[《利用Python进行数据分析·第2版》](https://www.jianshu.com/p/04d180d90a3f)，整理所得。



@[toc](目录)

-------

## 字符串方法

`str='strings'`

| **计数**   |      |
| ---------------- | ----------------- |
| str.count(substr,beg=0,end=len(string)) | 返回substr出现的次数|
| **去空格**     ||
| str.lstrip(chars)  | 删除str左边的字符（或空格）     |
| str.rstrip(chars)  | 删除str右边的字符（或空格）     |
| str.strip(chars)   | 删除str两边的字符（或空格）     |
| **字符串补齐**   ||
| str.center(width,fillchar)| 返回str居中，宽度为width的字符串(fillchar为填充字符)      |
| str.ljust(width,fillchar) | str左对齐|
| str.rjust(width,fillchar) | str右对齐|
| str.zfill (width)  | str右对齐，前面填充0 |
| **大小写转换**   ||
| str.capitalize()   | str的第一个字符大写  |
| str.title() | 每个单词首字母大写    |
| str.lower() | 小写    |
| str.upper() | 大写    |
| str.swapcase()     | 大小写互换 |
| **字符串条件判断** ||
| str.isalnum()      | 所有字符都是字母或数字  |
| str.isalpha()      | 所有字符都是字母     |
| str.isdigit()      | 所有字符都是数字     |
| str.isnumeric()    | 只包含数字字符      |
| str.isspace()      | 只包含空白 |
| str.istitle()      | 字符串是标题化      |
| str.islower()      | 都是小写  |
| str.isupper()      | 都是大写  |
| str.startswith(substr)    | 以substr开头    |
| str.endswith(substr)      | 以substr结尾    |
| **字符串搜索定位与替换**     |    |
| str.find(substr)    | 返回substr的索引位置，如果找不到，返回-1     |
| str.rfind(str)     ||
| str.index(substr)  | 返回substr的索引位置，如果找不到，返回异常   |
| str.rindex(str)    ||
| str.replace(old,new,max)  | 字符串替换，不超过 max 次（默认为1）。     |
| **字符串分割变换** ||
| str.join(seq)      | 以str分隔符，合并seq中所有的元素 |
| str.split(sep="",num)     | 分割str，num=str.count(sep)默认 |
| str.splitlines(keepends)  | 按照行('\r','\r\n',\n')分隔，参数 keepends为False则不包含换行符 |
| **字符串编码与解码**||
| str.encode(encoding='UTF-8')     | 以 encoding 指定的编码格式编码字符串 |

```python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog

greek=[
    ['A',r'\Alpha'],['α',r'\alpha'],
    ['B',r'\Beta'],['β',r'\beta'],
    ['Γ',r'\Gamma'],['γ',r'\gamma'],
    ['Δ',r'\Delta'],['δ',r'\delta'],
    ['E',r'\Epsilon'],['ϵ',r'\epsilon'],
    ['Z',r'\Zeta'],['ζ',r'\zeta'],
    ['H',r'\Eta'],['η',r'\eta'],
    ['Θ',r'\Theta'],['θ',r'\theta'],['Θ',r'\varTheta'],['ϑ',r'\vartheta'],
    ['I',r'\Iota'],['ι',r'\iota'],
    ['K',r'\Kappa'],['κ',r'\kappa'],
    ['Λ',r'\Lambda'],['λ',r'\lambda'],
    ['M',r'\Mu'],['μ',r'\mu'],
    ['N',r'\Nu'],['ν',r'\nu'],
    ['Ξ',r'\Xi'],['ξ',r'\xi'],
    ['O',r'\Omicron'],['ο',r'\omicron'],
    ['Π',r'\Pi'],['π',r'\pi'],['Π',r'\varPi'],['ϖ',r'\varpi'],
    ['R',r'\Rho'],['ρ',r'\rho'],
    ['Σ',r'\Sigma'],['σ',r'\sigma'],['Σ',r'\varSigma'],['ς',r'\varsigma'],
    ['T',r'\Tau'],['τ',r'\tau'],
    ['Υ',r'\Upsilon'],['υ',r'\upsilon'],
    ['Φ',r'\Phi'],['ϕ',r'\phi'],['Φ',r'\varPhi'],['φ',r'\varphi'],
    ['X',r'\Chi'],['χ',r'\chi'],
    ['Ψ',r'\Psi'],['ψ',r'\psi'],
    ['Ω',r'\Omega'],['ω',r'\omega']
  ]

others=[
         ['∇',r'\nabla'],
         ['∂',r'\partial'],
         ['∪',r'\cup'],['∩',r'\cap'],
         ['∀',r'\forall'],
         ['∁',r'\complement'],
         ['∃',r'\exists'], ['∃',r'\exist'],
         ['⊂',r'\subset'],['⊂',r'\sub'],
         ['⊃',r'\supset'],['⊃',r'\sup'], 
         ['⊆',r'\subseteq'], ['⊇',r'\supseteq'],
         ['×',r'\times'],
         ['±',r'\pm'], ['∓',r'\mp'],
         ['⩽',r'\leqslant'], ['⩾',r'\geqslant'],
         ['∞',r'\infty'],
         ['∼',r'\sim']
         ]
         
root=tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename()
f1 = open('概率论与数理统计(Probability & Statistics I).md','r+',encoding='utf-8')
f2 = open('output.md','w+',encoding='utf-8')

def symbols_replace(katex,old):
    new=old
    for i in katex:
        new=new.replace(i[1],i[0])   
    return new

for old in f1.readlines():
    new=symbols_replace(greek,old)
    new=symbols_replace(others,new)
    f2.write(new)
f1.close()
f2.close()
```


## 格式化字符串

格式化字符串语法`str.format()`
格式字符串由 `{}`包围的`replacement_field` 和任何不包含在大括号中的普通文本组成。
由 `str.format()` 方法传递参数。

`replacement_field`简单组成： `{field_name:format_spec}`

- **field_name** : 
1. 是一个数字，表示位置参数（element_index），如果`field_name`依次为`0,1,2，...`，则它们可以全部省略，并且数字`0,1,2，...`将按照该顺序自动插入。
2. 或者关键字（attribute_name）,`str.format()`可通过关键字传递参数。

- **format_spec**：`[width][.precision][type]`
1. `width`：（数字）表示宽度
2.  `.precision`：（dot+数字）小数位数
3.  `type`：表示类型
> **type列表：**
> `s`：表示字符格式
> `d`：十进制整数
> `f`：固定精度
> `e`：科学记数法
> `n`：数字
> `%`：百分比显示

```python
# for example:

print('Life is short, {} need {}'.format('You','Python'))  # 忽略数字
print('Life is short, {0} need {1}'.format('You','Python'))  # 带数字编号
print('Life is short, {1} need {0}'.format('Python','You'))  # 打乱顺序
#上面代码统一输出为: 'Life is short, You need Python'
print('Life is short, {name} need {language}'.format(name='You',language='R Language'))  # 关键字

import math
print('r={r:.1e}'.format(r=10**5))
print('π={pi:.2f}'.format(pi=math.pi))
print('e/PI={percent:.2%}'.format(percent=math.e/math.pi))
```

## 字符串常量
| 标准库   | `import string`     |
| ------------ | ---------- |
| string.digits      | 数字0~9 |
| string.letters     | 所有字母（大小写）    |
| string.lowercase   | 所有小写字母|
| string.printable   | 可打印字符的字符串    |
| string.punctuation | 所有标点  |
| string.uppercase   | 所有大写字母|
