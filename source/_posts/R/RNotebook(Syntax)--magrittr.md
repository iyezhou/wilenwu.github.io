---
ID: 52cf326043a3c64c94c69027b0e8171a
title: R手册(Syntax)--magrittr
tags: [R,magrittr,管道]
mathjax: false
copyright: true
date: 2018-05-02 00:46:17
categories: [R,Syntax]
sticky: false
---
**magrittr**:  管道语法 (pipe)

<!-- more -->

# magrittr:  pipe

**`lhs %>% rhs` forward-pipe**

1. lhs为rhs第一个参数时：`x %>% f(y)等价于 f(x, y)`
2. lhs在任意位置时，用点(.)代替：`z %>% f(x, y, arg = .)等价于 f(x, y, arg = z)`
3. rhs为代码块：`rnorm(100) %>% {c(min(.), mean(.), max(.))} %>% floor`

**`lhs %<>% rhs`复合赋值管道运算符**

`%<>%`用于首先将`lhs`传递给`rhs`表达式，最后将值重新赋给`lhs`。`some_object %<>% foo %>% bar `
相当于`some_object <- some_object %>% foo %>% bar`

**`lhs  ％$％ rhs`**
```r
iris %>%
  subset(Sepal.Length > mean(Sepal.Length)) %$%
  cor(Sepal.Length, Sepal.Width)
```

**`lhs  ％T>％ rhs` T运算符**
返回`lhs`本身，而不是`rhs`函数或表达式，对于`print`或者`plot`类似函数非常有用。
```r
rnorm（200）％>％
  matrix（ncol  =  2）％T>％
  plot  ％>％ ＃plot通常不返回任何内容。
  colSums
```
