
说明：本手册所列包基本来自[AwesomeR][AwesomeR] ，结合[GitHub][GitHub]和`help(package="pk_name")`官方文档整理所得，有助于使用时下最实用的包对R进行深入的学习。

其中，标记 <kbd>⭐</kbd>的是本人的必学包，❤为待选包。

致谢，[ApacheCN 中文开源组织](http://www.apachecn.org/#)：致力于官方文档及AI书籍中文翻译。

![github](https://img-blog.csdn.net/201806031909378?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTE4Mjc3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

---------------------------------------
# Common

  - [x] [R语言入门][basic]: 包括Rstudio介绍，R的数据结构和基础语法等
  - [x] [R语言基础包][base]：base, stats等基础包函数
  - [x] [R6 and S4][R6]：面向对象
  - [x] [tidyverse+tibble][tidyverse]：Hadley包集合，核心包(ggplot2,tibble,tidyr,readr,purrr,dplyr)
  - [x] [data.table][data.table]：简短的代码实现快速操作数据
  - [ ] devtools：❤使开发R包变得更简单(Hadley) (Update according to [cheat sheets][sheet])
  - [ ] [rpy2][rpy2]：❤Python 通过rpy2调用 R语言

[basic]: https://blog.csdn.net/qq_41518277/article/details/80464319
[base]: https://blog.csdn.net/qq_41518277/article/details/80150625
[tidyverse]: https://blog.csdn.net/qq_41518277/article/details/80152636
[data.table]: https://blog.csdn.net/qq_41518277/article/details/80158005
[R6]: https://blog.csdn.net/qq_41518277/article/details/80158036
[rpy2]: https://blog.csdn.net/qq_41518277/article/details/85226955


# Syntax

  - [x] [purrr][purrr]：函数化编程(FP, functional programming) (Hadley)
  - [ ] lambda.r：R中的函数式编程和简单模式匹配
  - [x] [magrittr][magrittr]：Let’s pipe it
  - [ ] pipeR：❤多范式管道编程

[purrr]: https://blog.csdn.net/qq_41518277/article/details/80161309
[magrittr]: https://blog.csdn.net/qq_41518277/article/details/80161309

# Import

  - [x] [readr][readr]：快速读取文本型数据(csv,tsv,and fwf).(Hadley)
  - [x] [readxl][readxl]：for excel files.(Hadley)
  - [x] [openxlsx][openxlsx]：丰富的excel处理工具
  - [ ] [jsonlite][jsonlite]：❤JSON处理.(Hadley)
  - [ ] haven：for SPSS,SAS and Stata files.(Hadley)
  - [ ] feather：❤for sharing with Python and other languages.(Hadley)

[readr]: https://blog.csdn.net/qq_41518277/article/details/80158061
[readxl]: https://blog.csdn.net/qq_41518277/article/details/80158061
[openxlsx]: https://blog.csdn.net/qq_41518277/article/details/80158061
[jsonlite]: https://blog.csdn.net/qq_41518277/article/details/80158061

*DATABASE MANAGEMENT*

  - [ ] [DBI][DBI]：❤数据库统一接口(Hadley)
  - [ ] RHive：❤通过Apache Hive促进分布式计算的R扩展

[DBI]: https://blog.csdn.net/qq_41518277/article/details/80158078

*WEB TECHNOLOGIES*

  - [ ] RCurl：❤用于R的通用网络(HTTP/FTP/ ...)接口
  - [x] [httr][httr]：for web APIs (RCurl升级版) (Hadley) (Update according to GitHub)
  - [x] [rvest][rvest]：web scraping (Hadley)  (Update according to GitHub)
  - [x]  xml2：解析XML文件 (Hadley)  (Update according to GitHub)

[httr]: https://blog.csdn.net/qq_41518277/article/details/80158123
[rvest]: https://blog.csdn.net/qq_41518277/article/details/80158123

# Tidy+Transform

*DATA MANIPULATION*

  - [x] [tidyr][tidyr]：清理数据,reshape2替代版(Hadley)
  - [x] [dplyr and plyr][dplyr]：数据操作(Hadley)
  - [ ] rlist：用于list(非规整)数据操作工具箱
  - [x] [stringr][stringr]：for strings.(Hadley)
  - [ ] utf8：处理和修复R中的多种文本编码问题 
  - [x] [正则表达式][re]：Regular Expression
  - [x] [lubridate][lubridate]：for date and times(Hadley)
  - [x] [hms][hms]：for times(Hadley)
  - [x] [forcats][forcats]：for factors(Hadley)
  - [ ] sjmisc：各种实用功能的集合，支持数据重编码，缺失值处理等，与dplyr包无缝协作。
  - [x] [naniar][naniar]：缺失数据概述和可视化
  - [x] [simputation][simputation]：缺失数据插补框架

[tidyr]: https://blog.csdn.net/qq_41518277/article/details/80484244
[dplyr]: https://blog.csdn.net/qq_41518277/article/details/80159020
[stringr]: https://blog.csdn.net/qq_41518277/article/details/80160592
[re]: https://blog.csdn.net/qq_41518277/article/details/80158351
[lubridate]: https://blog.csdn.net/qq_41518277/article/details/80160857
[hms]: https://blog.csdn.net/qq_41518277/article/details/80160857
[forcats]: https://blog.csdn.net/qq_41518277/article/details/80484269
[naniar]: https://blog.csdn.net/qq_41518277/article/details/80161089
[simputation]: https://blog.csdn.net/qq_41518277/article/details/80161089

*LARGE DATASETS*

  - [ ] ff：在内存外存储数据，处理起来和在内存一样
  - [ ] bigmemory：内存外存储，操作，big 系列包提供了其他工具，包括线性模型 (biglm) 和随机森林 (bigrf)。

# Visualise

*GRAPHIC DISPLAYS*

  - [x] [RColorBrewer and extrafont][extrafont]：调色板和字体
  - [x] [ggmap+baidumap][ggmap]：使用ggplot2在R中绘制静态地图
  - [x] ggpubr：ggplot2封装，用于绘制适合出版物要求的图形
  - [ ] corrplot：❤相关矩阵或一般矩阵的图形显示
  - [ ] misc3d：处理3D图，等值面等
  - [x] [ggplot2][ggplot2]：强大的绘图系统，并实现了许多扩展(Hadley)
  - [x] [ggplot2 extensions][ggplot2 extensions]: ggplot2扩展，包括各种补充图形，坐标系统，主题等。

[extrafont]: https://blog.csdn.net/qq_41518277/article/details/80188194
[ggplot2]: https://blog.csdn.net/qq_41518277/article/details/80182022
[ggmap]: https://blog.csdn.net/qq_41518277/article/details/80188948
[ggplot2 extensions]: http://www.ggplot2-exts.org/ggiraph.html

*HTML WIDGETS*

  - [ ] [leaflet+leafletCN][leaflet+leafletCN]：❤最流行的JavaScript库交互式地图之一，动态交互地图。
  - [x] [Remap][Remap]：简易动态交互地图(基于Echarts)。
  - [ ] rCharts：❤来自R的交互式JS图表。
  - [ ] DiagrammeR：在R中创建JS图形和流程图。
  - [ ] rbokeh：R与Bokeh的接口。
  - [ ] plotly：❤R的交互式图形库，基于ggplot2 和shiny。

[leaflet+leafletCN]: https://blog.csdn.net/qq_41518277/article/details/80189247
[Remap]: https://blog.csdn.net/qq_41518277/article/details/80537172

# Parallel Computing

  - [ ] [foreach][foreach]：❤在循环(loop)中并行化运算

[foreach]: https://blog.csdn.net/qq_41518277/article/details/80189348

# MapReduce

  - [ ] SparkR：❤Spark的R前端
  - [ ] sparklyr：❤来自RStudio的Apache Spark的R接口，提供dplyr后端 (Update according to [cheat sheets][sheet])

# Model Tools

  - [x] [broom][broom]：用于将统计模型的结果整理成数据框形式(Hadley)
  - [x] [modelr][modelr]：管道建模辅助包(Hadley)
  - [ ] caret：❤分类和回归问题的数据训练综合工具包（包括交叉验证，网格搜索等）

[broom]: https://blog.csdn.net/qq_41518277/article/details/80189381
[modelr]: https://blog.csdn.net/qq_41518277/article/details/80189381


# Machine Learning

  - [x] [mlr][mlr]：机器学习（分类，回归，生存分析，聚类等）的可扩展框架，提供了用于分析的整套工具，包括重抽样，缺失值插补，模型评估(cv,etc)，超参数调优(grid-search,etc)，特征选择，可视化(ROC,learnning-curve,etc)等
  - [ ] mlapi：提供模型的统一接口，以便机器学习流程化(借鉴python scikit-learn，尚未开发完整)
  - [x] xgboost：以其速度和性能而著称的eXtreme Gradient Boosting Tree模型
  - [x] arules：关联规则挖掘和频繁项集
  - [ ] survival：生存分析模型
  - [ ] nnet：神经网络

[mlr]: https://blog.csdn.net/qq_41518277/article/details/80189427


# Deep Learning

  - [ ] tensorflow：❤Google开源的最受欢迎的深度学习框架
  - [ ] h2o：❤深度学习框架 (Update according to [cheat sheets][sheet])
  - [ ] keras：❤以 tensorflow/theano/CNTK 为后端的深度学习封装库  (Update according to [cheat sheets][sheet])

# NLP (Natural Language Processing)

  - [x] [jiebaR][jiebaR]：中文分词包
  - [ ] Rwordseg：中文分词包，安装复杂
  - [x] [wordcloud2][wordcloud2]：词云
  - [ ] tm： 一个全面的文本挖掘框架
  - [ ] quanteda：❤文本挖掘 (Update according to [cheat sheets][sheet])
  - [ ] tidytex：❤简单文本挖掘，结合dplyr，ggplot2和其他简洁工具
  - [x] [text2vec][text2vec]：一个快速文本挖掘框架（jiebaR推荐包） (Update according to GitHub)

[jiebaR]: https://blog.csdn.net/qq_41518277/article/details/80198407
[wordcloud2]: https://blog.csdn.net/qq_41518277/article/details/80486990
[text2vec]: https://blog.csdn.net/qq_41518277/article/details/80487013

# Time Series

  - [x] [zoo][zoo]：定义了规则和不规则时间序列S3类  (Update according to GitHub)
  - [ ] xts：❤对时间序列数据(zoo)的一种扩展实现，统一时间序列的操作接口  (Update according to GitHub)
  - [x] [prophet][prophet]：线性或非线性模型高质量时间序列预测，它最适合日常数据
  - [x] [forecast][forecast]：时间序列建模和预测
  - [x] [forecastHybrid][forecastHybrid]：结合forcast包时间序列模型混合预测
  - [ ] CausalImpact：使用贝叶斯结构时间序列模型进行因果推理

[zoo]: https://blog.csdn.net/qq_41518277/article/details/80484661
[prophet]: https://blog.csdn.net/qq_41518277/article/details/80197687
[forecast]: https://blog.csdn.net/qq_41518277/article/details/80197687
[forecastHybrid]: https://blog.csdn.net/qq_41518277/article/details/80197687

# Finance

  - [ ] quantmod：定量金融建模与交易框架（股票）
  - [ ] PerformanceAnalytics：用于性能和风险分析的计量经济学工具

# Communicate

  - [x] [R Markdown][rmarkdown]：用于创建可重复性报告和动态文档
  - [ ] rticles：提供了一套RMarkdown模板
  - [ ] flexdashboard：基于rmarkdown，可以轻松的创建仪表盘
  - [ ] slidify：从Rmarkdown生成可重现的html5幻灯片
  - [ ] knitr：用于在PDF和HTML文档中嵌入R代码块
  - [x] [shiny][shiny]：使用R语言开发交互式web应用程序的工具

[rmarkdown]: https://blog.csdn.net/qq_41518277/article/details/80149789
[mk]: https://blog.csdn.net/qq_41518277/article/details/80149002
[shiny]: https://blog.csdn.net/qq_41518277/article/details/80428273

# Others

  - [x] [Advanced R][Advanced R] 
  - [x] [R packages][R packages] 
  - [x] [R for Data Science][DataScienceR] 
  - [x] [AwesomeR][AwesomeR]：R包大全
  - [x] [RStudio Cheat Sheets][sheets] 
  - [x] [TaskViews][task]：CRAN Task Views
  - [x] [Search][Search]：Google search engine
  - [x] [GitHub][GitHub]：Built for developers


[Advanced R]: http://adv-r.had.co.nz/
[R packages]: http://r-pkgs.had.co.nz/
[DataScienceR]: http://r4ds.had.co.nz/
[AwesomeR]: https://github.com/asxinyu/AwesomeResources
[sheets]: https://www.rstudio.com/resources/cheatsheets/
[task]: https://cran.r-project.org/web/views/
[Search]: https://cran.r-project.org/search.html
[GitHub]: https://github.com/
[sheet]: https://blog.csdn.net/qq_41518277/article/details/80215702

----------



![g2](https://img-blog.csdn.net/20180603191006988?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTE4Mjc3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)