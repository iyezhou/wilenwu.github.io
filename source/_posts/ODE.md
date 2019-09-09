---
title: ODE
tags: [ode]
categories: [math]
---

> 参考文献：
> 丁同仁《常微分方程教程》
> MOOC同济大学《高等数学》
> MOOC国防科技大学《高等数学》

<!-- more -->

# 微分方程(Differential Equation)

**微分方程**：包含未知函数及其导数的方程叫做==微分方程==((Differential Equation))。未知函数导数的最高阶数称为该==微分方程的阶==(order)。
1. **常微分方程(ODE)**：若未知函数是一元函数的微分方程称为常微分方程(Ordinary Differential Equation, ODE)  。
一般的 ==n 阶常微分方程==的形式(也称隐式表达式)为$$F(x,y,y',y'',\dots,y^{(n)})=0 \tag{1}$$ 如果微分方程是关于未知函数及各阶导数的线性表达式 $$y^{(n)}+a_1(x)y^{(n-1)}+\cdots+a_{n-1}(x)y'+a_n(x)y=f(x)\tag{2}$$  则称为 ==n 阶线性(linearity)常微分方程==。
2. **偏微分方程(PDE)**：若未知函数是多元函数，方程中含有自变量的偏微分，称之为偏微分方程(Partial Differential Equations, PDE)。


**微分方程的解**：如果将一个函数$y=φ(x)$其各阶导数代入微分方程 (1) 得到恒等式$F(x,φ(x),φ'(x),φ''(x),\dots,φ^{(n)}(x))\equiv0$，则称$y=φ(x)$为上述方程的一个==解==(solution)。
1. **通解**：n 阶微分方程 (1) 的解 $y=φ(x,C_1,C_2,\cdots,C_n)$ 含有 n 个相互独立的任意常数 $C_1,C_2,\cdots,C_n$ ，则称为该微分方程的==通解==(general solution)。
其中任意常数相互独立是指每一个常数对解的影响是其他常数所不能代替的，即雅克比行列式(Jacobian)满足 $$\cfrac{D(φ,φ',\cdots,φ^{(n-1)})}{D(C_1,C_2,\cdots,C_n)}=
\begin{vmatrix}
\frac{∂ φ}{∂ C_1} &\frac{∂ φ}{∂ C_2} & \cdots &\frac{∂ φ}{∂ C_n} \\ 
\frac{∂ φ'}{∂ C_1} &\frac{∂ φ'}{∂ C_2} &\cdots &\frac{∂ φ'}{∂ C_n} \\ 
\vdots &\vdots &\ddots &\vdots \\ 
\frac{∂ φ^{(n)}}{∂ C_1} &\frac{∂ φ^{(n)}}{∂ C_2} &\cdots &\frac{∂ φ^{(n)}}{∂ C_n} \\ 
\end{vmatrix}\neq 0$$
2. **特解**：我们称不包含任意常数的解为==特解==(particular solution)。
3. **初值问题**：通常为了解决实际问题，确定常数的值，需要引入初值条件(initial conditions)。初值条件联合微分方程组成==初值问题==(Initial Value Problem, IVP)或柯西问题。
一阶常微分方程的初值问题通常记作 $\begin{cases}y'=f(x,y) \\ 
y(x_0)=y_0\end{cases}$
4. **隐式解与隐式通解**：如果关系式 $\Phi(x,y)=0$ 所确定的隐函数 $y=φ(x)$ 为微分方程 (1) 的解，则称 $\Phi(x,y)=0$ 是方程的一个==隐式解==(implicit solution)。对于 n个相互独立常数的解  $\Phi(x,y,C_1,C_2,\cdots,C_n)=0$ 的解为隐式通解。
5. **积分曲线**：微分方程的解对应的曲线称为==积分曲线==(integral curve)。
初值问题 $\begin{cases}y'=f(x,y) \\ 
y(x_0)=y_0\end{cases}$ 的解对应过点$(x_0,y_0)$的一条积分曲线，该曲线在点$(x_0,y_0)$ 处的切线的斜率为 $f(x_0,y_0)$，切线方程为 $y=y_0+f(x_0,y_0)(x-x_0)$
若不给定初始条件，微分方程的通解在几何上对应着一族积分曲线，称为==积分曲线族==(family of integral curves)。

6. **线素场**：考虑微分方程 $y'=f(x,y)$，若 $f(x,y)$ 的定义域为平面区域G，在G 内每一点 $P(x,y)$ 作斜率为 $f(x,y)$ 的单位线段，则称该线段为点 $P(x,y)$的==线素==。G 内所有的线素构成由微分方程确定的==线素场==(line element field)或==方向场==(direction field)。
在构造微分方程 $y'=f(x,y)$ 的线素场时，通常利用斜率关系式 $f(x,y)=k$ 确定曲线 $L_k$，称它为线素场的==等斜线==(isocline)。显然，等斜线$L_k$上各点的斜率都等于 $k$，简化了线素场逐点构造的方法。
7. **奇异点**：设一阶微分方程为 $P(x,y)dx+Q(x,y)dy=0$，函数$P(x,y),Q(x,y)$在区域G是连续的，若 $P(x_0,y_0)=Q(x_0,y_0)=0,,(x_0,y_0)\in G$，线素场在点$(x_0,y_0)$处便失去意义，我们称这样的点为==奇异点==(singular point)。

- **示例**：作微分方程 $y'=y/x$ 和 $y'=-x/y$的线素场。
(1) $y'=y/x$ 的等斜线为 $L_k:y=kx$，说明线素斜率为 k 的所有点都集中在直线 $y=kx$ 上，也可求得方程的积分曲线簇为射线 $\tanθ=y/x,θ$为任意常数，原点 O为奇异点。
(2) $y'=-x/y$的等斜线为 $L_k:y=-\frac{1}{k}x$，说明线素斜率为 k 的所有点都集中在直线 $y=-\frac{1}{k}x$ 上，且线素斜率和等斜线垂直相交，也可求得方程的积分曲线簇为同心圆 $x^2+y^2=C^2$，原点 O为奇异点。
![积分曲线](https://img-blog.csdnimg.cn/20190822161742447.png =160x)![积分曲线](https://img-blog.csdnimg.cn/20190822161807118.png =160x)

# 一阶常微分方程(First-Order Ordinary Differential Equations)

## 可分离变量方程(Equations of separated variables)

对于形如$$\frac{\mathrm{d}y}{\mathrm{d}x}=g(x)h(y)\tag{1}$$的微分方程，称为==可分离一阶方程==(separable first-order equations)，方程可化为$\cfrac{1}{h(y)}\mathrm{d}y=g(x)\mathrm{d}x$，对方程两边积分$\displaystyle\int \cfrac{1}{h(y)}\mathrm{d}y=\int g(x)\mathrm{d}x$
设$H(y),G(x)$分别为$\cfrac{1}{h(y)},g(x)$的原函数，可知隐式通解为 $H(y)=G(x)+C$
这种通过分离变量求方程通解的方法叫做==分离变量法==(Separation of variables)



#