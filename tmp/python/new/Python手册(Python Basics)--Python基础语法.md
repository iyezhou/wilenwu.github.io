
---
title: Python手册(Python Basics)--Python基础语法
tags: [python]
mathjax: false
copyright: true
date: 2018-05-09 00:10:30
categories: [python,Python Basics]
sticky: false
---

**说明**：本手册所列包来自[Awesome-Python](https://awesome-python.com/) ，结合[GitHub](https://github.com/) 和官方文档，参考 [**菜鸟教程**](http://www.runoob.com/python3/python3-tutorial.html)，整理所得。




-------

>  **Python中多行语句**：行末添加反斜杠`\`
> 在`[]{}()`中的多行语句不需要使用反斜杠`\`

<!-- more -->

## 对象（万物皆对象）

`reset`关键字或`reset()`函数，清空所有对象

**访问对象的属性和方法**
`obj.some_method(args)`
`obj.attribute_name`

## 标量数据类型
| 类型 | 说明|示例
| ----- | :----------|:-----
| None  | 空值（常常作为函数的默认参数）  |
| str| 字符串，存有Unicode（UTF-8编码）字符串 |
| bytes | 原生ASCII字节  |
| float | 浮点数  |0.0, 10.3e-3
| int| 整数|10, -0x260,0x69(0x开头的为16进制数字),0o69(八进制), 0b1101(二进制)
| bool  | True/False      |
|complex|复数，3+2i|
> **str,bool,int和float也是函数，可以用来转换类型**

| 字符串  | 说明   |
| ------------ | ---------- |
| 单引号 | word = '字符串'|
| 双引号 | sentence = "这是一个句子"|
| 三引号 | 字符串换行|
| r'\n strings'     | `\\`可以用来转义，前面加r(raw)不发生转义 |
| u'中文字符'    | 中文常加u(unicode)前缀编译 |
| **文档起始中文编码说明** | `# -*- coding: utf-8-*- `   |
| `string[start:end:step]` | 切片（左闭右开区间）   |

![hello](https://img-blog.csdn.net/20180524225312768?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTE4Mjc3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 运算符
| 数学运算符  |**成员运算符**| **身份运算符**
| ---------------- |--------    |-------|
| `**` (乘方)       |in          | is     |
| `%` (求余数)       | not in    | is not   |
| `//` (整除)        |           |        |
| `+`(合并str,tupple,list，数学加号) | ||
| `*`(重复str,tupple,list，数学乘号) | ||
|  `- `(减号)   |||
|  `/`(除号)    |||

| **逻辑运算符** |**比较运算符**(支持连用) | 
| ------------- |------    |
| and         |     `>,<`    |  
| or           |     `>=,<=`    |
| not          |     `!= ，==`     |
```python
>>> 2<3 and 'a'<'b'
True
>>> 2<3<1
False
```
按位运算符|描述（二进制编码运算）|实例<br>`a,b=60,13`
---|---|---
&	|按位与：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	|(a & b) 输出结果 12 ，二进制解释： 0000 1100
\||按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。|(a \| b) 输出结果 61 ，二进制解释： 0011 1101
^|按位异或运算符：当两对应的二进位相异时，结果为1|(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~|按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1|(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<|左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。|a << 2 输出结果 240 ，二进制解释： 1111 0000
\>\>|右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数|a >> 2 输出结果 15 ，二进制解释： 0000 1111

赋值运算符|	描述	|实例
------|------|------
`=`	|简单的赋值运算符	|`c = a + b 将 a + b 的运算结果赋值为 c`<br>`a=b=c=1` 连续赋值
`+=`	|加法赋值运算符	|`c += a 等效于 c = c + a`
`-=`	|减法赋值运算符	|`c -= a 等效于 c = c - a`
`*=`	|乘法赋值运算符	|`c *= a 等效于 c = c * a`
`/=`	|除法赋值运算符	|`c /= a 等效于 c = c / a`
`%=`	|取模赋值运算符	|`c %= a 等效于 c = c % a`
`**=`	|幂赋值运算符	|   `c **= a 等效于 c = c ** a`
`//=`	|取整除赋值运算符	|`c //= a 等效于 c = c // a`

## if 语句

```python
if expression:
  statements 
elif expression: 
  statements
else:
  statements
```
if 语句变体：`value=[false-expr,true-expr][condition]`（利用list索引判断）
三元表达式：`value=true-expr if condition else false-expr`

## 循环语句
```python
#for循环
for value in collection:
  statements

#while循环
while expression:
  statements
else:
  statements
```
**关键字**
`pass`: 占位
`break`: 跳出循环
`coutine`:  跳出本次循环

## python中Switch/Case实现
```python
# if...elif...else实现
# 字典映射
def function_1(...):
    statements
... ...

functions = {'a': function_1,
             'b': function_2,
             'c': self.method_1, ...}

func = functions[value]
func()

# example
switch={
        'a': 1，
        'b': 2,
        'c': 3,
       }
result = switch.get('key','default_value') # 找不到'key'，返回默认值
```


## 自定义函数

```python
def fun_name(var1,var2=default,*args,**kwargs): 
  '说明文档'
  statements  
  return result 
```
- 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

- **参数顺序**：必选参数，默认参数，可变参数， 关键字参数
`*args`是可变参数，以tuple的形式返回
`**kwargs`是关键字参数，以dict的形式返回

```python
>>> def test(a,*args,**kwargs): 
 	   print(a)
 	   print(args)
 	   print(kwargs)
>>> test('a',1,'b',key1=2,key2='c')
'a'
(1,'b')
{'key1':2,'key2':'c'}

>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

 **函数注解**
 - 我们知道 Python 是一种动态语言，变量以及函数的参数是不区分类型。
Python解释器会在运行的时候动态判断变量和参数的类型，这样的好处是编写代码速度很快，很灵活，但是坏处也很明显，不好维护，可能代码写过一段时间重新看就很难理解了，因为那些变量、参数、函数返回值的类型，全都给忘记了。
- 所以Python3里有了这个新特性，可以给参数、函数返回值和变量的类型加上注解，不过这个仅仅是注释而已，对代码的运行来说没有任何影响，变量的真正类型还是会有Python解释器来确定，你所做的只是在提高代码的可读性，让 IDE 了解类型，从而提供更准确的代码提示、补全和语法检查，仅此而已。
- 注解是以字典形式存储在函数的 `__annotations__ `属性中，对函数的其它部分没有任何影响。

```python
>>> def add(x:int, y:int) -> int:
...     return x+y
>>> def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...
>>> f('wonderful')
Annotations: {'eggs': <class 'int'>, 'return': 'Nothing to see here', 'ham': 42}
Arguments: wonderful spam
```

**匿名（lambda）函数**：`lambda vars:expr` 不用写return，返回值就是该表达式的结果 
` lambda x,y:x**y`


**变量的作用域**
Python的作用域一共有4种，分别是：

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
```python
x = int(2.9)  # 内建作用域
 
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
```
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
**global 和 nonlocal关键字**
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了
```python
num=1
def outer():
    num2 = 10
    def inner():
    	global num  # global关键字声明
        nonlocal num2   # nonlocal关键字声明
        print(num+num2)
```

## 闭包
> 参考链接：https://mp.weixin.qq.com/s/I9WIkm4ounSQSK5zpOv5eg

```python
def print_msg():
    # print_msg 是外围函数
    msg = "I'm python"
    def printer():
        # printer 是嵌套函数
        print(msg)
    return printer

another = print_msg()
# 输出 I'm python
another()
```
一般情况下，函数中的局部变量仅在函数的执行期间可用，一旦 print_msg() 执行过后，我们会认为 msg变量将不再可用。然而，在这里我们发现 print_msg 执行完之后，在调用 another 的时候 msg 变量的值正常输出了，这就是闭包的作用，闭包使得局部变量在函数外被访问成为可能。

看完这个例子，我们再来定义闭包，维基百科上的解释是:

> 在计算机科学中，闭包（Closure）是词法闭包（Lexical Closure）的简称，是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。

这里的 another 就是一个闭包，闭包本质上是一个函数，它由两部分组成，printer 函数和变量 msg。闭包使得这些变量的值始终保存在内存中。

**Example:**
用于解偏微分方程组中间函数
> 公式：
> $\vec{r}=(x,y,z)$ 
> $|\vec{r}|=\sqrt{x^2+y^2+z^2}$
> $\hat{r}=\vec{r} \cdot |\vec{r}|^{-1}$    
> $d\vec{v}/dt=-\frac{GM}{r^2} \hat{r}$   
> $d\vec{r}/dt=\vec{v}$
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def gravity(GM=1):
    '''             
    dr/dt=v
    r_norm=sqrt(x^2+y^2+z^2)
    dv/dt=-GM/dot(r,r)*r/r_norm
    ''' 
    def force(t,X_and_V):
        'GM loading...'
        x,y,z,vx,vy,vz=X_and_V
        r=np.array([x,y,z])
        v=np.array([vx,vy,vz])
        dr=v
        r_norm=np.linalg.norm(r)
        dv=-GM/np.dot(r,r)*r/r_norm
        return np.concatenate([dr,dv])
    return force

r0=(20,30,0)
v0=(0.8,0.5,0)
t0,t1=0,100

F=gravity(GM=1000)
motion=solve_ivp(fun=F,t_span=(t0,t1),y0=r0+v0, t_eval=np.linspace(t0,t1,1001))

plt.plot(motion.y[0,:],motion.y[1,:])
plt.show()
```

## 装饰器
装饰器实际上是在不改变原程序的情况下，给某程序增添功能，避免大量雷同代码。
> 菜鸟教程（包括带参数的装饰器和装饰器类等）
> http://www.runoob.com/w3cnote/python-func-decorators.html
> 参考文档：http://lib.csdn.net/article/python/62942

```python
from functools import wraps
def decorator_name(f):
    @wraps(f)  #加载wraps是为了原函数的名字和注释文档不被重写(docstring)
    def decorated(*args, **kwargs):
    	print('I am do something')
        if not True:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated
 
@decorator_name
def func():
    return("Function is running")
```

## 错误和异常处理

```python
try: 
  statements 
except <Error(可选)>:  #try失败时执行，可以指定特定的Error或者Error元祖，例如(TypeError,ValueError)
  statements 
else:       #try成功时执行
  statements 
finally:    #始终执行
  statements 
```

## 模块

```python
 import some_module #导入整个模块 
 from some_module import func1,func2  #从某个模块中导入多个函数 
 from some_module import *  #将某个模块中的全部函数导入
 dir(some_module) #列出模块里的函数 
```
> python自定义包
> https://blog.csdn.net/lxy4239/article/details/79107008
> python模块官方文档
> http://www.pythondoc.com/pythontutorial3/modules.html
> Python3 教程 | 菜鸟教程
> http://www.runoob.com/python3/python3-module.html

## 标准库概览

**os 模块**提供了很多与操作系统交互的函数
```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python35'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0

>>> path=os.path.abspath(__file__) #返回脚本运行绝对路径
>>> dirname,filename=os.path.split(path) #分离出路径和脚本名
```

**命令行参数**
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 `python demo.py one two three` 后可以得到以下输出结果:
```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

**错误输出重定向和程序终止**
sys 还有 stdin， stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息:
```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```
大多脚本的直接终止都使用 sys.exit()

**数据压缩**
以下模块直接支持通用的数据打包和压缩格式：zlib， gzip， bz2， lzma， zipfile 以及 tarfile。
```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```
**性能度量**
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。

例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多。timeit 证明了后者更快一些:
```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```
相对于 timeit 的细粒度，profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

**十进制浮点数算法**
decimal 模块提供了一个 Decimal 数据类型用于浮点数计
Decimal 的结果总是保有结尾的 0，自动从两位精度延伸到4位。Decimal 重现了手工的数学运算，这就确保了二进制浮点数无法精确保有的数据精度。

高精度使 Decimal 可以执行二进制浮点数无法进行的模运算和等值测试:
```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```
decimal 提供了必须的高精度算法:
```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```



