---
title: 书架
date: 2019-10-08 13:04:44
categories: [bookshelf]
tags: [python,R,数据分析,大数据]
comments: true
copyright: false
sticky: true
---

本博客基于 Hexo 及 GitBook 配合搭建而成。
其中博文依据个人爱好、工作需要等制定了一份详细的学习计划，并根据清单同步更新学习笔记，详情请查阅本「[书架](https://wilenwu.github.io/bookshelf/)」。
<!-- more -->
其中
- 标记 :white_check_mark: 是必修课
- 标记 :white_medium_square: 待定
- 标记 :heart: 是选修课

------

# <font color="orange">大数据</font>

致谢，[ApacheCN 中文开源组织](http://www.apachecn.org/#)：致力于官方文档及AI书籍中文翻译。  

## <font color="green">Linux</font>  

- :white_check_mark:  [Linux基础知识][linux]  
- :white_check_mark:  [Linux Shell 教程][shell]  

[linux]: https://blog.csdn.net/qq_41518277/article/details/80720390
[shell]: https://blog.csdn.net/qq_41518277/article/details/80772546

## <font color="green">Hadoop</font>  

- :white_medium_square:  Hadoop安装配置  
- :white_medium_square:  Hadoop基础知识  
- :white_medium_square:  Rhadoop：R语言完成MapReduce 算法，用来替代Java的MapReduce实现。  

## <font color="green">Hive</font>  

- :white_medium_square:  Hive安装配置  
- :white_check_mark:   [Hive基础知识][hivebasic]  
- :white_check_mark:   [SQL手册][sql]  
- :white_check_mark:   [HiveQL][HiveQL]  
- :white_medium_square:  RHive：Apache Hive促进分布式计算的R扩展  

[sql]: https://wilenwu.github.io/posts/big-data/SQLNotebook.html
[HiveQL]: https://wilenwu.github.io/posts/big-data/BigDataNotebook(Hive)--HiveQL.html
[hivebasic]: https://blog.csdn.net/zhongqi2513/article/details/69388239

## <font color="green">Spark</font>

- :white_check_mark:   [Spark安装配置][spark]  
- :white_check_mark:   [Spark基础知识][spark_base]  
- :heart:  scala：spark 基础语言 
- :heart:  sparkR： Apache Spark R API  
- :heart:  sparklyr：来自RStudio的Apache Spark的R接口，提供dplyr后端  
- :white_check_mark:  [PySpark][PySpark] : Apache Spark Python API  
- :white_medium_square:  [Akka][akka]：Akka并发编程  

[spark]: https://wilenwu.github.io/posts/big-data/BigDataNotebook(Spark)--Spark-installation.html
[spark_base]: https://blog.csdn.net/qq_41518277/article/details/84558396
[akka]: https://blog.csdn.net/lovehuangjiaju/article/details/51039985
[PySpark]: https://blog.csdn.net/qq_41518277/article/details/96487035

## <font color="green">Learning</font> 

机器学习路线 spark & tableau > tensorflow > karas  
[ApacheCN 学习资源汇总 2018.12](https://blog.csdn.net/wizardforcel/article/details/85317667) 
[ApacheCN](http://www.apachecn.org/#)  
[TensorflowCN](https://tensorflow.google.cn/tutorials/?hl=zh-cn)  

------

# <font color="orange">数据分析</font>

- :white_check_mark:   [二分类模型评价指标][evaluation]  
- :white_check_mark:   [数据分析理论概览][theory]  

[evaluation]: https://wilenwu.github.io/posts/data-analysis/classification-evaluation.html
[theory]: https://wilenwu.github.io/posts/data-analysis/Overview-of-Data-Analysis-Theory.html

------

# <font color="orange">Python手册</font> 

> 本手册所列包来自[Awesome-Python](https://awesome-python.com/) ，结合[GitHub](https://github.com/) 和官方文档  
致谢，[ApacheCN 中文开源组织](http://www.apachecn.org/##)：致力于官方文档及AI书籍中文翻译。  

![pandas](images/pandas.png)  

## <font color="green">IDE</font>  

- :white_medium_square:  [常用的Python IDE][ide]  
- :white_check_mark:  [Jupyter Notebook][Jupyter]  

[ide]: https://wilenwu.github.io/posts/python/PythonNotebook(Python-Basics)--common-editor.html
[Jupyter]: https://wilenwu.github.io/posts/python/PythonNotebook(Python-Basics)--Jupyter-Notebook.html

## <font color="green">Python Basics</font>  

- :white_check_mark:  [Python基础][Base]: [Python 3 官方中文文档](base_doc)  
- :heart:  [rpy2][rpy2]： Python 通过rpy2调用 R语言  

[Base]: https://wilenwu.github.io/posts/python/PythonNotebook(Python-Basics)--Python-base.html
[base_doc]: https://docs.python.org/zh-cn/3/
[rpy2]: https://wilenwu.github.io/posts/python/PythonNotebook(Python-Basics)--RPy2.html

## <font color="green">Standard Library</font>  

- :white_check_mark:  [datetime+time+calendar][datetime]  
- :white_check_mark:  [math+random][math]  
- :white_check_mark:  [re+正则表达式][re]  
- :heart:  [tkinter][tk]：Python 的标准 GUI 库  
- :white_medium_square:  [threading][threading] ：多线程  
- :white_medium_square:  [multiprocessing][mul]： 多进程  
- :heart:  [os][os]: 文件和目录处理库([CSDN][csdn_os]参考链接)  
- :white_medium_square:  [asyncio][asyncio]: 内置了对异步IO的支持   

[datetime]: https://wilenwu.github.io/posts/python/PythonNotebook(Standard-Library)--datetime.html
[math]: https://wilenwu.github.io/posts/python/PythonNotebook(Standard-Library)--math+random.html
[re]: https://wilenwu.github.io/posts/python/PythonNotebook(Standard-Library)--re+regular-expression.html
[tk]: http://www.runoob.com/python/python-gui-tkinter.html
[threading]: http://www.runoob.com/python3/python3-multithreading.html
[mul]: http://python.jobbole.com/87760/
[os]: http://www.runoob.com/python/os-file-methods.html
[csdn_os]: https://blog.csdn.net/jinxiaonian11/article/details/78314192
[asyncio]: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090954004980bd351f2cd4cc18c9e6c06d855c498000

## <font color="green">Scientific Computing</font>  

- :white_check_mark:  [NumPy][NumPy]：使用 Python 进行科学计算的基础包。  
- :white_medium_square:  PyDy：PyDy 是 Python Dynamics 的缩写，用来为动力学运动建模工作流程提供帮助， 基于NumPy, SciPy, IPython 和 matplotlib。  
- :heart:  [SciPy][SciPy]：由一些基于 Python ，用于数学，科学和工程的开源软件构成的生态系统。  
- :heart:  [SymPy][SymPy]：SymPy是一个符号计算的Python库  
- :white_medium_square:  astropy：一个天文学 Python 库。  
- :heart:  [noise][noise]：柏林噪声(Python)  

[NumPy]: https://wilenwu.github.io/posts/python/PythonNotebook(Scientific-Computing)--numpy.html
[SciPy]: https://wilenwu.github.io/posts/python/PythonNotebook(Scientific-Computing)--scipy.html
[SymPy]: https://wilenwu.github.io/posts/python/PythonNotebook(Scientific-Computing)--SymPy.html
[noise]: https://wilenwu.github.io/posts/python/PerlinNoise(Python).html

## <font color="green">Data Analysis</font>  

- :white_check_mark:  [pandas][pandas]：提供高性能，易用的数据结构和数据分析工具。  
- :white_check_mark:  [pandas(Time Series)][time series]: 时间序列数据处理工具。  
- :heart:  blaze：NumPy 和 Pandas 的大数据接口。  
- :heart:  orange：通过可视化编程或 Python 脚本进行数据挖掘，数据可视化，分析和机器学习。  

[pandas]: https://wilenwu.github.io/posts/python/PythonNotebook(Data-Analysis)--pandas.html
[Time Series]: https://wilenwu.github.io/posts/python/PythonNotebook(Time-Series)--pandas(TimeSeries).html

## <font color="green">Web Crawling</font> 

*The Website is the API(Application Programming Interface,应用程序编程接口)...*  

- :white_check_mark:  requests: 自动爬取HTML页面，自动网路请求提交。  
- :white_check_mark:  BeautifulSoup ：解析HTML页面（[中文官网][bs4]）。  
- :heart:  Scrapy：专业的网络爬虫框架。  
- :white_medium_square:  Selenium: 是一个用于Web应用程序测试的工具，能够模拟用户行为与浏览器交互。  

[bs4]: https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

## <font color="green">Visualise</font>  

- :white_check_mark:  [matplotlib][matplotlib]: 是一个 Python 的 2D绘图库。  
- :white_check_mark:  [seaborn][seaborn]：基于matplotlib封装的数据可视化库。  
- :white_medium_square:  bqplot： Jupyter Notebook的交互式绘图库  
- :white_medium_square:  bokeh：用 Python 进行交互式 web 绘图。  
- :heart:  [ggplot][ggplot]：ggplot port for python  
- :white_medium_square:  plotly：协同 Python 和 matplotlib 工作的 web 绘图库。  
- :white_medium_square:  pyecharts：基于百度 Echarts 的数据可视化库。  
- :heart:  missingno：缺失数据图示。  

[matplotlib]: https://wilenwu.github.io/posts/python/PythonNotebook(Visualise)--matplotlib.html
[seaborn]: https://wilenwu.github.io/posts/python/PythonNotebook(Visualise)--seaborn.html
[ggplot]: http://yhat.github.io/ggpy/

## <font color="green">Machine Learning</font>  

- :white_check_mark:  [sklearn][scikit-learn]：基于 SciPy 构建的机器学习 Python 模块。  
- :white_check_mark:  [statsmodels][statsmodels]：统计建模和计量经济学。  
- :heart:  [xgboost][xgboost]： 一种可扩展，可移植且分布式的渐变增强库  

[scikit-learn]: https://wilenwu.github.io/posts/python/PythonNotebook(Machine-Learning)--sklearn.html
[statsmodels]: https://blog.csdn.net/qq_41518277/article/details/80275280
[xgboost]: http://xgboost.apachecn.org/##/

## <font color="green">Deep Learning</font>  

- :white_check_mark:  [TensorFlow][TensorFlow]：Google开源的最受欢迎的深度学习框架。  
- :white_medium_square:  [PyTorch][PyTorch]: Facebook 的 AI 研究团队发布了一个 Python 工具包，专门针对 GPU 加速的深度神经网络（DNN）编程。  
- :heart:  [Keras][Keras]: 以 tensorflow/theano/CNTK 为后端的深度学习封装库，快速上手神经网络。[莫烦PYTHON](https://morvanzhou.github.io/tutorials/machine-learning/theano/)  
- :white_medium_square:  [Theano][Theano]:  基于TensorFlow，用于快速数值计算的库。  

[TensorFlow]: https://tensorflow.google.cn/tutorials/?hl=zh-cn
[PyTorch]: https://blog.csdn.net/u010510350/article/details/72526821
[Keras]: https://tensorflow.google.cn/guide/keras?hl=zh-cn
[Theano]: http://deeplearning.net/software/theano/##

## <font color="green">MapReduce</font>  

- :white_check_mark:  PySpark : Apache Spark Python API  

## <font color="green">NLP(Natural Language Processing)</font>  

- :heart:  Jieba ： Chinese text segmentation  
- :white_medium_square:  NLTK：Natural Language Toolkit  

## <font color="green">Documentation</font>  

- :white_medium_square:  MkDocs ： Markdown友好的文档生成器。  
- :white_medium_square:  Python-Markdown2：纯 Python 实现的 Markdown 解析器，比 Python-Markdown 更快，更准确，可扩展  
- :white_medium_square:  PyYAML： implementations for Python.  
- :white_medium_square:  python-docx: for creating and updating Microsoft Word (.docx) files.  
- :heart:  [openpyxl][op]: 全面，包括修改各种Excel格式，不能批量修改数据  
- :white_medium_square:   [xlwings][xw]: 批量实时修改Excel数据，和pandas,matplotlib完美对接，只能修改个别格式  

[op]: https://openpyxl.readthedocs.io/en/stable/usage.html
[xw]: http://docs.xlwings.org/en/stable/quickstart.html

## <font color="green">Learning Python </font> 

- :white_check_mark:  [Python基础中文教程](http://www.pythondoc.com/pythontutorial3/)  

------

# <font color="orange">R手册</font>

> 本手册所列包基本来自[AwesomeR][AwesomeR] ，结合[GitHub][GitHub]和`help(package="pk_name")`官方文档整理所得，有助于使用时下最实用的包对R进行深入的学习。  
致谢，[ApacheCN 中文开源组织](http://www.apachecn.org/## )：致力于官方文档及AI书籍中文翻译。  

![github](images/github.png)  

## <font color="green"> Common </font> 

- :white_check_mark: [R语言入门][basic]: 包括Rstudio介绍，R的数据结构和基础语法等  
- :white_check_mark: [R语言基础包][base]：base, stats等基础包函数  
- :white_check_mark: [R6 and S4][R6]：面向对象  
- :white_check_mark: [tidyverse+tibble][tidyverse]：Hadley包集合，核心包(ggplot2,tibble,tidyr,readr,purrr,dplyr)  
- :white_check_mark: [data.table][data.table]：简短的代码实现快速操作数据  
- :heart:  devtools：使开发R包变得更简单(Hadley) (Update according to [cheat sheets][sheet])  
- :heart:  [rpy2][rpy2]：Python 通过rpy2调用 R语言  

[basic]: https://wilenwu.github.io/posts/R/RNotebook(Common)--R-base.html
[base]: https://wilenwu.github.io/posts/R/RNotebook(Common)--R-basic-packages.html
[tidyverse]: https://wilenwu.github.io/posts/R/RNotebook(Common)--tidyverse+tibble.html
[data.table]: https://wilenwu.github.io/posts/R/RNotebook(Common)--data.table.html
[R6]: https://wilenwu.github.io/posts/R/RNotebook(Common)--Object-Oriented(R6-and-S4).html
[rpy2]: https://wilenwu.github.io/posts/python/PythonNotebook(Python-Basics)--RPy2.html


## <font color="green"> Syntax </font> 

- :white_check_mark: [purrr][purrr]：函数化编程(FP, functional programming) (Hadley)  
- :white_medium_square:  lambda.r：R中的函数式编程和简单模式匹配  
- :white_check_mark: [magrittr][magrittr]：Let’s pipe it  
- :heart:  pipeR：多范式管道编程  

[purrr]: https://wilenwu.github.io/posts/R/RNotebook(Syntax)--purrr.html
[magrittr]: https://wilenwu.github.io/posts/R/RNotebook(Syntax)--magrittr.html

## <font color="green"> Import</font>  

- :white_check_mark: [readr][readr]：快速读取文本型数据(csv,tsv,and fwf).(Hadley)  
- :white_check_mark: [readxl][readxl]：for excel files.(Hadley)  
- :white_check_mark: [openxlsx][openxlsx]：丰富的excel处理工具  
- :heart:  [jsonlite][jsonlite]：JSON处理.(Hadley)  
- :white_medium_square:  haven：for SPSS,SAS and Stata files.(Hadley)  
- :heart:  feather：for sharing with Python and other languages.(Hadley)  

[readr]: https://wilenwu.github.io/posts/R/RNotebook(Import)--read-csv-xlsx-or-json.html#readr:-read-rectangular-text-data
[readxl]: https://wilenwu.github.io/posts/R/RNotebook(Import)--read-csv-xlsx-or-json.html#readxl:-for-excel
[openxlsx]: https://wilenwu.github.io/posts/R/RNotebook(Import)--read-csv-xlsx-or-json.html#openxlsx:-xlsx-reading,-writing-and-editing
[jsonlite]: https://wilenwu.github.io/posts/R/RNotebook(Import)--read-csv-xlsx-or-json.html#jsonlite:-for-json

*DATABASE MANAGEMENT*  

- :heart:  [DBI][DBI]：数据库统一接口(Hadley)  
- :heart:  RHive：通过Apache Hive促进分布式计算的R扩展  

[DBI]: https://wilenwu.github.io/posts/R/RNotebook(Import)--DBI.html

*WEB TECHNOLOGIES*  

- :heart:  RCurl：用于R的通用网络(HTTP/FTP/ ...)接口  
- :white_check_mark: [httr][httr]：for web APIs (RCurl升级版) (Hadley) (Update according to GitHub)  
- :white_check_mark: [rvest][rvest]：web scraping (Hadley)  (Update according to GitHub)  
- :white_check_mark:  xml2：解析XML文件 (Hadley)  (Update according to GitHub)  

[httr]: https://httr.r-lib.org/
[rvest]: https://wilenwu.github.io/posts/R/RNotebook(Import)--rvest.html

## <font color="green"> Tidy+Transform</font>  

*DATA MANIPULATION*  

- :white_check_mark: [tidyr][tidyr]：清理数据,reshape2替代版(Hadley)  
- :white_check_mark: [dplyr and plyr][dplyr]：数据操作(Hadley)  
- :white_medium_square:  rlist：用于list(非规整)数据操作工具箱  
- :white_check_mark: [stringr][stringr]：for strings.(Hadley)  
- :white_medium_square:  utf8：处理和修复R中的多种文本编码问题   
- :white_check_mark: [正则表达式][re]：Regular Expression  
- :white_check_mark: [lubridate+hms][lubridate]：for date and times(Hadley)  
- :white_check_mark: [forcats][forcats]：for factors(Hadley)  
- :white_medium_square:  sjmisc：各种实用功能的集合，支持数据重编码，缺失值处理等，与dplyr包无缝协作。  
- :white_check_mark: [naniar][naniar]：缺失数据概述和可视化  
- :white_check_mark: [simputation][simputation]：缺失数据插补框架  

[tidyr]: https://wilenwu.github.io/posts/R/RNotebook(Tidy+Transform)--tidyr.html
[dplyr]: https://wilenwu.github.io/posts/R/RNotebook(Tidy+Transform)--dplyr-and-plyr.html
[stringr]: https://wilenwu.github.io/posts/R/RNotebook(Tidy+Transform)--stringr.html
[re]: https://wilenwu.github.io/posts/R/RNotebook(Tidy+Transform)--regular-expression.html
[lubridate]: https://wilenwu.github.io/posts/R/RNotebook(Tidy+Transform)--lubridate+hms.html
[forcats]: https://wilenwu.github.io/posts/R/RNotebook(Tidy+Transform)--forcats.html
[naniar]: https://wilenwu.github.io/posts/R/RNotebook(Tidy+Transform)--for-missing-data(naniar-and-simputation).html
[simputation]: https://wilenwu.github.io/posts/R/RNotebook(Tidy+Transform)--for-missing-data(naniar-and-simputation).html

*LARGE DATASETS*  

- :white_medium_square:  ff：在内存外存储数据，处理起来和在内存一样  
- :white_medium_square:  bigmemory：内存外存储，操作，big 系列包提供了其他工具，包括线性模型 (biglm) 和随机森林 (bigrf)。  

## <font color="green"> Visualise</font>  

*GRAPHIC DISPLAYS*  

- :white_check_mark: [RColorBrewer and extrafont][extrafont]：调色板和字体  
- :white_check_mark: [ggmap+baidumap][ggmap]：使用ggplot2在R中绘制静态地图  
- :white_check_mark: ggpubr：ggplot2封装，用于绘制适合出版物要求的图形  
- :heart:  corrplot：相关矩阵或一般矩阵的图形显示  
- :white_medium_square:  misc3d：处理3D图，等值面等  
- :white_check_mark: [ggplot2][ggplot2]：强大的绘图系统，并实现了许多扩展(Hadley)  
- :white_check_mark: [ggplot2 extensions][ggplot2 extensions]: ggplot2扩展，包括各种补充图形，坐标系统，主题等。  

[extrafont]: https://wilenwu.github.io/posts/R/RNotebook(Visualise)--RColorBrewer-and-extrafont.html
[ggplot2]: https://wilenwu.github.io/posts/R/RNotebook(Visualise)--ggplot2.html
[ggmap]: https://wilenwu.github.io/posts/R/RNotebook(Visualise)--ggmap+baidumap.html
[ggplot2 extensions]: http://www.ggplot2-exts.org/ggiraph.html

*HTML WIDGETS*  

- :heart:  [leaflet+leafletCN][leaflet+leafletCN]：最流行的JavaScript库交互式地图之一，动态交互地图。  
- :white_check_mark: [Remap][Remap]：简易动态交互地图(基于Echarts)。  
- :heart:  rCharts：来自R的交互式JS图表。  
- :white_medium_square:  DiagrammeR：在R中创建JS图形和流程图。  
- :white_medium_square:  rbokeh：R与Bokeh的接口。  
- :heart:  plotly：R的交互式图形库，基于ggplot2 和shiny。  

[leaflet+leafletCN]: https://wilenwu.github.io/posts/R/RNotebook(Visualise)--leaflet+leafletCN.html
[Remap]: https://wilenwu.github.io/posts/R/RNotebook(Visualise)--REmap.html

## <font color="green"> Parallel Computing</font> 

- :heart:  [foreach][foreach]：在循环(loop)中并行化运算  

[foreach]: https://wilenwu.github.io/posts/R/RNotebook(Parallel-Computing)--foreach.html

## <font color="green"> MapReduce</font>  

- :heart:  SparkR：Spark的R前端  
- :heart:  sparklyr：来自RStudio的Apache Spark的R接口，提供dplyr后端  

## <font color="green"> Model Tools</font>  

- :white_check_mark: [broom][broom]：用于将统计模型的结果整理成数据框形式(Hadley)  
- :white_check_mark: [modelr][modelr]：管道建模辅助包(Hadley)  
- :heart:  caret：分类和回归问题的数据训练综合工具包（包括交叉验证，网格搜索等）  

[broom]: https://wilenwu.github.io/posts/R/RNotebook(Model-Tools)--broom.html
[modelr]: https://wilenwu.github.io/posts/R/RNotebook(Model-Tools)--modelr.html


## <font color="green"> Machine Learning</font>  

- :white_check_mark: [mlr][mlr]：机器学习（分类，回归，生存分析，聚类等）的可扩展框架，提供了用于分析的整套工具，包括重抽样，缺失值插补，模型评估(cv,etc)，超参数调优(grid-search,etc)，特征选择，可视化(ROC,learnning-curve,etc)等  
- :white_medium_square:  mlapi：提供模型的统一接口，以便机器学习流程化(借鉴python scikit-learn，尚未开发完整)  
- :white_check_mark: xgboost：以其速度和性能而著称的eXtreme Gradient Boosting Tree模型  
- :white_check_mark: arules：关联规则挖掘和频繁项集  
- :white_medium_square:  survival：生存分析模型  
- :white_medium_square:  nnet：神经网络  

[mlr]: https://wilenwu.github.io/posts/R/RNotebook(Machine-Learning)--mlr.html

## <font color="green"> Deep Learning</font>  

- :heart:  tensorflow：Google开源的最受欢迎的深度学习框架  
- :heart:  h2o：深度学习框架 (Update according to [cheat sheets][sheet])  
- :heart:  keras：以 tensorflow/theano/CNTK 为后端的深度学习封装库   

## <font color="green"> NLP (Natural Language Processing)</font>  

- :white_check_mark: [jiebaR][jiebaR]：中文分词包  
- :white_medium_square:  Rwordseg：中文分词包，安装复杂  
- :white_check_mark: [wordcloud2][wordcloud2]：词云  
- :white_medium_square:  tm： 一个全面的文本挖掘框架  
- :heart:  quanteda：文本挖掘 (Update according to [cheat sheets][sheet])  
- :heart:  tidytex：简单文本挖掘，结合dplyr，ggplot2和其他简洁工具  
- :white_check_mark: [text2vec][text2vec]：一个快速文本挖掘框架（jiebaR推荐包） (Update according to GitHub)  

[jiebaR]: https://wilenwu.github.io/posts/R/RNotebook(NLP)--jiebaR.html
[wordcloud2]: https://wilenwu.github.io/posts/R/RNotebook(NLP)--wordcloud2.html
[text2vec]: https://wilenwu.github.io/posts/R/RNotebook(NLP)--text2vec.html

## <font color="green"> Time Series</font>  

- :white_check_mark: [zoo][zoo]：定义了规则和不规则时间序列S3类  (Update according to GitHub)  
- :heart:  [xts][xts]：对时间序列数据(zoo)的一种扩展实现，统一时间序列的操作接口  (Update according to GitHub)  
- :white_check_mark: [prophet][prophet]：线性或非线性模型高质量时间序列预测，它最适合日常数据  
- :white_check_mark: [forecast][forecast]：时间序列建模和预测  
- :white_check_mark: [forecastHybrid][forecastHybrid]：结合forcast包时间序列模型混合预测  
- :white_medium_square:  CausalImpact：使用贝叶斯结构时间序列模型进行因果推理  

[zoo]: https://wilenwu.github.io/posts/R/RNotebook(Time-Series)--zoo.html
[xts]: http://joshuaulrich.github.io/xts/
[prophet]: https://wilenwu.github.io/posts/R/RNotebook(Time-Series)--forecast-and-prophet.html
[forecast]: https://wilenwu.github.io/posts/R/RNotebook(Time-Series)--forecast-and-prophet.html
[forecastHybrid]: https://wilenwu.github.io/posts/R/RNotebook(Time-Series)--forecast-and-prophet.html

## <font color="green"> Finance</font>  

- :white_medium_square:  quantmod：定量金融建模与交易框架（股票）  
- :white_medium_square:  PerformanceAnalytics：用于性能和风险分析的计量经济学工具  

## <font color="green"> Communicate</font>  

- :white_check_mark: [R Markdown][rmarkdown]：用于创建可重复性报告和动态文档  
- :white_medium_square:  rticles：提供了一套RMarkdown模板  
- :white_medium_square:  flexdashboard：基于rmarkdown，可以轻松的创建仪表盘  
- :white_medium_square:  slidify：从Rmarkdown生成可重现的html5幻灯片  
- :white_medium_square:  knitr：用于在PDF和HTML文档中嵌入R代码块  
- :white_check_mark: [shiny][shiny]：使用R语言开发交互式web应用程序的工具  

[rmarkdown]: https://wilenwu.github.io/posts/R/RNotebook(Communicate)--R-Markdown.html
[shiny]: https://wilenwu.github.io/posts/R/RNotebook(Communicate)--shiny.html

## <font color="green"> Learning R</font>  

- :white_check_mark: [Advanced R][Advanced R]   
- :white_check_mark: [R packages][R packages]   
- :white_check_mark: [R for Data Science][DataScienceR]   
- :white_check_mark: [AwesomeR][AwesomeR]：R包大全  
- :white_check_mark: [RStudio Cheat Sheets][sheets]   
- :white_check_mark: [TaskViews][task]：CRAN Task Views  
- :white_check_mark: [Search][Search]：Google search engine  

[Advanced R]: http://adv-r.had.co.nz/
[R packages]: http://r-pkgs.had.co.nz/
[DataScienceR]: http://r4ds.had.co.nz/
[AwesomeR]: https://github.com/asxinyu/AwesomeResources
[sheets]: https://www.rstudio.com/resources/cheatsheets/
[task]: https://cran.r-project.org/web/views/
[Search]: https://cran.r-project.org/search.html
[GitHub]: https://github.com/

------

# <font color="orange">数学</font>

- :white_check_mark:   [初等数学]( https://blog.csdn.net/qq_41518277/article/details/89397900)  
- :white_check_mark:   高等数学 (数学分析)：  
[微积分][c1]  
[多元函数微积分][c2]  
[无穷级数][c3]  
[常微分方程][ode]  
[空间解析几何][sag]  
- :white_check_mark:   [线性代数](https://blog.csdn.net/qq_41518277/article/details/89703485)  
- :white_check_mark:   概率论与数理统计：  
 [概率论][ps1]  
 [数理统计][ps2]  
- :white_check_mark:   数学物理方法：  
[复变函数][cf1]  
[积分变换][cf2]  
[偏微分方程(数学物理方程)][pde]  
- :white_check_mark:   [群论基础](https://mp.csdn.net/mdeditor/90261550#)  
- :white_check_mark:   [近世代数(抽象代数)](https://blog.csdn.net/qq_41518277/article/details/92605711) ：群、环、域  
- :white_check_mark:   微分几何  
- :white_medium_square:  [高等几何](https://blog.csdn.net/qq_41518277/article/details/92614884)  
- :heart:  拓扑学   

- :white_medium_square:  数论  
- :white_medium_square:  泛函分析  
- :heart:  混沌理论   
- :heart:  计算物理学   
- :white_medium_square:  张量分析(多重线性代数)   

[c1]: https://blog.csdn.net/qq_41518277/article/details/89397964
[c2]: https://blog.csdn.net/qq_41518277/article/details/89761069
[c3]: https://blog.csdn.net/qq_41518277/article/details/90029881
[ode]: https://blog.csdn.net/qq_41518277/article/details/89703473
[pde]: https://blog.csdn.net/qq_41518277/article/details/90295633
[sag]: https://blog.csdn.net/qq_41518277/article/details/89739640
[ps1]: https://blog.csdn.net/qq_41518277/article/details/90261253
[ps2]: https://blog.csdn.net/qq_41518277/article/details/90733362
[cf1]: https://blog.csdn.net/qq_41518277/article/details/89742631
[cf2]: https://blog.csdn.net/qq_41518277/article/details/97121991

------

# <font color="orange">物理</font>  

## <font color="green">foundational physics</font>  

- :white_check_mark:   普通物理（力学，热学，光学，电磁学，原子物理学）  
- :white_check_mark:   理论力学  
- :white_check_mark:   电动力学  
- :white_check_mark:   热力学与统计物理  
- :white_check_mark:   量子力学  
- :white_medium_square:  弹性力学   
- :white_medium_square:  分析力学   
- :heart:  流体力学   

## <font color="green">advanced physics</font>  

- :white_check_mark:   狭义相对论  
- :white_check_mark:   广义相对论  
- :white_check_mark:   高等量子理论  
- :white_check_mark:   场论基础 (经典场论，相对论场论，量子场论)   
- :white_check_mark:   规范场论  
- :white_check_mark:   量子场论  
- :white_medium_square:  线性物理  
- :heart:  弦理论和M理论   

- :white_medium_square:  固体物理  
- :heart:  粒子物理   
- :white_medium_square:  原子和分子物理  
- :white_medium_square:  凝聚态物理  
- :white_medium_square:  普通天文学  
- :heart:  天体物理    
- :white_medium_square:  近代光学

------

# <font color="orange">个人博客</font>

- :white_check_mark:   [Hexo博客搭建及配置][hexo]    
- :white_check_mark:   [Hexo标签插件的使用][tags]    
- :white_check_mark:   [NexT主题进阶][NexT]    

[hexo]: https://wilenwu.github.io/posts/hexo/Hexo-setup&configuration.html
[tags]: https://wilenwu.github.io/posts/hexo/Hexo-tag-plugins.html
[NexT]: https://wilenwu.github.io/posts/hexo/theme-NexT-advanced.html

------

# <font color="orange">Markdown</font>
- :white_check_mark:   [GitHub Flavored Markdown 规范][md]  
- :white_check_mark:   [KaTeX 数学符号列表][katex]  
- :white_medium_square:  [Markdown For Typora][mft]  

[md]: https://wilenwu.github.io/posts/markdown/GitHub-Flavored-Markdown-Spec.html
[katex]: https://wilenwu.github.io/posts/markdown/KaTeX-for-Mathematical-Symbols.md.html
[mft]: https://wilenwu.github.io/posts/markdown/Markdown-For-Typora.html

------

# <font color="orange">正则表达式</font>

