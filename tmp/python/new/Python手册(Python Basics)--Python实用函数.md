
---
title: Python手册(Python Basics)--Python实用函数
tags: [python]
mathjax: false
copyright: true
date: 2018-05-20 15:28:41
categories: [python,Python Basics]
sticky: false
---

**说明**：本手册所列包来自[Awesome-Python](https://awesome-python.com/) ，结合[GitHub](https://github.com/) 和官方文档，参考 [**菜鸟教程**]http://www.runoob.com/python3/python3-tutorial.html)，整理所得。



------

<!-- more -->

## 内建函数

**帮助**||
:---|:---
`?`  |显示对象的信息 
`??` |显示函数的源码 
`np.*load*?` |字符与通配符结合可以匹配所有的名字 
help() |显示对象的帮助信息 
**输入输出**|
input(prompt)| 输入
print(values,sep=' ',end='\n')|输出
**数学函数**|
round(x,n)| 四舍五入 
abs(x)|
len(obj) |序列元素数 
max(obj)|
min(obj)|
pow()|
divmod(a,b)|返回元组(a // b, a % b)
hex(x)|10进制转16进制，以字符表示（0x开头的格式，如0x10）
int(x, base=10)|用于将一个字符串或数字转换为整型，默认十进制
oct(x)|将一个整数转换成8进制字符串|
bin(x)|返回一个整数 int 或者长整数 long int 的二进制表示
complex(real, imag)|返回复数
hash(object)|获取哈希值
**面向对象**|
type(obj)|  输出对象类型 
dir(object)|输出对象属性和方法
isinstance(obj,class_or_tuple)| 判断对象类型('int', 'str',' list'...)
setattr(object, name, value)|设置对象属性
getattr(object, name[, default])|返回一个对象属性值
hasattr(object, name)|判断对象是否包含对应的属性
delattr(object, name)|删除属性
issubclass(class, classinfo)|判断是否子类
vars([object])|函数返回对象object的属性和属性值的字典对象

**高阶函数**|说明
---|:---
map(function,obj)  |对序列中所有元素函数映射 
reduce(function, iterable[, initializer])|对参数序列中元素进行累积<br>python3从内置模块移除`from functools import reduce`
filter(function, iterable)|返回一个迭代器
```python
strings = ['a','as','bat','car','dove','python']
set(map(len, strings))
reduce(lambda x, y: x+y, [1,2,3,4,5])
filter(lambda x: x%2==0, range(1, 101))
```
**字符表达式**|说明
---|---
eval(expression)|执行一个字符串表达式，并返回表达式的值<br>`eval('pow(2,2)')`
exec(object)|执行复杂的表达式，返回None
```python
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
exec(expr)
```

**其他常用函数**|说明
---|---
chr() |把编码转换为对应的字符 
id([object])|获取对象内存地址
iter(object[, sentinel])|生成迭代器
all(iterable)|给定的可迭代对象全部为True，类似于and
any(iterable)|给定的可迭代对象任一为True,类似于or
reversed(seq)  |反转序列，返回迭代器
callable(object)|判断对象是否是可调用，对于函数, 方法, lambda 函式, 类, 以及实现了 `__call__ `方法的类实例, 它都返回 True


## 序列函数

- **`enumerate`函数**，可以返回`(i, value)`元组序列，常用于loop：

```
for i, value in enumerate(collection): 
  #do something with value
```

- **sorted函数**
` sorted(list)` 返回排序好的list副本 
 `sorted(str)`  拆分str，返回排序好的list副本 
 
- **zip函数**
`zip(seq1,seq2)` 可以将多个列表、元组或其它序列成对组合成一个元组对
zip可以处理任意多的序列，元素的个数取决于最短的序列
`zip(*tup)`逆转用法

```python
In [89]: seq1 = ['foo', 'bar', 'baz'] 
In [90]: seq2 = ['one', 'two', 'three']
In [92]: list(zip(seq1, seq2)) 
Out[92]: [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]

In [95]: for i, (a, b) in enumerate(zip(seq1, seq2)):
   ....:     print('{0}: {1}, {2}'.format(i, a, b))
   ....:
0: foo, one
1: bar, two
2: baz, three
```

- **排列组合**

`from itertools import product,permutations,combinations`

> 参考链接：https://blog.csdn.net/specter11235/article/details/71189486

## File(文件) 方法
> 参考链接：http://www.runoob.com/python/file-methods.html

file对象|说明
:---|:---
open(file, mode='r', encoding=None)|新建file对象
**属性**|
file.closed|返回true如果文件已被关闭，否则返回false。
file.mode|返回被打开文件的访问模式。
file.name|返回文件的名称。
file.softspace|如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
**方法**|
file.close()|关闭文件
file.next()|返回文件下一行，迭代时使用
file.read([size])|从文件中读取的字节数
file.readline([size])|读取整行，包括 "\n" 字符
file.readlines([sizeint])|读取所有行并返回列表
file.seek(offset[, whence])|设置文件当前位置
file.tell()|返回文件当前位置
file.write(str)|将字符串写入文件，返回的是写入的字符长度。	
file.writelines(sequence)|向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

```python
with open("/tmp/python.csv") as f:
    data = f.read()
```






