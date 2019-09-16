**说明**：本手册所列包来自[Awesome-Python](https://awesome-python.com/) ，结合[GitHub](https://github.com/) 和官方文档，参考 **SeanCheney** 大神在简书上翻译的[《利用Python进行数据分析·第2版》](https://www.jianshu.com/p/04d180d90a3f)，整理所得。


@[toc]

------

## tuple (元祖)
元组是一个固定长度，不可改变的Python序列对象

- **创建tuple**
`tup = (4, 5,6), (7, 8)`
`tup = tuple(obj)` 
`tup=()`

- **拆分元祖**
```python
tup = 4,5,(6,7)
a,b,(c,d) = tup

# 特殊拆分
values = 1,2,3,4,5
a,b,*_ = values #*_代表剩余部分，'_'名字不重要,作为惯用写法用'_'
```
- **元祖数学运算**
```python
tup1=(1,2,3)
tup2=('a','b')
tup1+tup2
Out: (1,2,3,'a','b')
tup2*3
Out: ('a','b','a','b','a','b')
```

- **索引和切片**
`tup[index]`
`tup[start:stop:step]`

- **方法**  
`tup.count(value)`  统计元组中某元素的个数
`tup.index(value)` 元素第一次出现的索引位置

## list (列表)

- **创建list**
`a = [2, 3,7, None]` 
`a=list(obj)`
`a=[]`

```python
In: list('abcd')  
Out: ['a','b','c','d'] 
```
- **元祖数学运算**
同元组

- **索引和切片**
`a[index]`
`a[start:stop:step]`
`a[::-1] ` 倒叙切片


- **方法**  

方法|说明
------|--------
`a.count(value)` |统计列表中某元素的个数
`a.index(value)` |元素第一次出现的索引位置
a.append(obj)  |向列表尾部追加一个新元素，只占一个索引位
a.extend(iterator)  |向列表尾部追加多个元素，将迭代器中的每个元素都追加进来
a.insert(index,obj)  |指定位置插入元素
a.pop(index) |删除并返回指定位置元素 
a.clear()  |清空列表
a.remove(obj)  |寻找第一个值并除去 
a.copy() |列表浅复制
a.reverse()  |反转列表
a.sort(reverse=False) | 将list中的元素升序排列 
```python
a=[1,2]
a.append([3,4]) # [1,2,[3,4]]
a.append(['a','b']) # [1,2,[3,4],'a','b']
```

## dict (字典)
字典的值可以是任意Python对象，而键通常是不可变的标量类型（整数、浮点型、字符串）或元组（元组中的对象必须是不可变的），这被称为“可哈希性”。

**创建dict**（哈希映射或关联数组）
`d={'key1':value1,'key2':value2, ...} ` 由key-value对创建
`d=dict(obj)`
`d=dict.fromkeys(seq, value=None)` 由key value序列创建
`d=dict(zip(key_list,value_list))` **zip函数创建**（key-value)元组迭代器
`d=dict(d1,**d2)` 合并字典d1和d2
`d={}`


`d['key']` 访问dict元素
`d['new_key']='new_value' ` 添加新key-value对
`'key' in dict` 是否包含键值'key' 

`del d['key']`  删除元素
`del d` 删除字典

方法 | 说明
---|:---
d.copy()|浅复制
d.pop(key,default=None)|删除并返回对应value<br>`ret = dict.pop('a')`	
d.popitem()|随机返回并删除字典中的一对键和值(一般删除末尾对)
d.clear()  |删除所有元素
d.update(dict2) | 将dict2中元素融入dict 
d.keys() |返回keys迭代器
d.values() |返回values迭代器
d.items()  |返回dict中所有的(key,val)元祖数组
d.get(key,default=None) |如果key存在，返回value，否则返回default
d.setdefault(key, default=None)|如果key存在，返回value，则插入 key 及设置的默认值 default，并返回 default

## set (集合)
集合是无序的不可重复的元素的集合。
` {1,2,3} == {3,2,1}  #返回TRUE`

**创建set**
` a = {1, 2, 3, 4, 5} `
` a = set(obj) `
` a = set()` 空集合，`{}`只能用来创建空字典

方法 | 说明|替代语法
---|---|---
 a.add(value)  |将value添加到a|
 a.remove(value) |寻找第一个值并除去，不存在会报错|
 a.discard(value)|删除集合中指定的元素，不会报错|
 d.copy()|浅复制|
 a.pop(index)  |删除并返回指定位置元素|
 a.clear() |清空a |
 a.update(b)|将b中元素融入a|`a\=b` 
 a.union(b)|a和b的不重复元素| `a\b` 
 a.intersection(b| 交集|`a&b`
 a.difference(b) |差集（存在于a，不存在于b）|`a-b`
 a.issubset(b) |if a∈b return True|
 a.issuperset(b) |if b∈a return True|
 a.isdisjoint(b) | if $a∩b=\emptyset$(交集)  return True |


## 列表、集合和字典推导式 
```python
list_comp=[expr for val in collection if condition]  
set_comp = {expr for value in collection if condition}  
dict_comp = {key-expr :value-expr for value in collection if condition} 

# list推导式等价for循环
 list_comp = []
 for val in collection:  
   if condition: 
     list_comp.append(expr) 
```


## iterator(迭代器) and generator(生成器)

- 迭代器
` iterator = iter(obj)` 
`range(start=0,end,step=1)`  返回一个迭代器，它产生一个均匀分布的整数序列 `[start,end) by step`
序列对象（tuple, dict, ...）都可以作为迭代器使用
`next(iterator)`  （迭代函数）下一个
- 生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator），生成器是一个返回迭代器的函数，只能用于迭代操作
- [Python itertools模块详解](https://www.cnblogs.com/fengshuihuan/p/7105545.html)


```python
# 排列，组合，笛卡儿积：
from itertools import combinations,permutations,product,combinations_with_replacement

# 自建迭代器
def squares(n=10):  
  print('Generating squares from1 to {0}'.format(n ** 2))  
  for i in range(1, n + 1): 
    yield i ** 2  #将return替换为yield即可返回迭代器
gen = squares() 
for x in gen: 
  print(x, end=' ') 
```

