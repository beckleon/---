# netease_scrapy
## 1、背景 ##
本项目尝试抓取网易《荒野行动》游戏官网论坛的“综合讨论”区的所有发帖记录（除置顶帖之外），对抓取数据进行初步分析并将结果进行可视化展示。

## 2、使用技术 ##
使用 Scrapy 框架抓取数据并将结果保存到本地 MySQL 数据库内，进行初步的数据清洗之后，将分析结果使用 Superset 展示出来。

## 3、抓取过程及结果 ##
开始抓取时，综合讨论区共有576页，考虑到抓取速度比较快，短时间内新增的帖子不至于多于一页，而早先的主题帖一般也不会被人回复，所以选择从最后一页开始抓取并往前翻页。抓取的数据包括：主题帖id，主题名，链接地址，发帖用户名，发表时间，回复数，查看数。抓取数据如下所示：
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/threads.jpg"/></div>


## 4、数据展示 ##
抓取时间约为1个半小时，截止到2018-03-15日14点50分，除开置顶帖之外，总共抓取到了16962个主题帖以及205101个帖子。
抓取的数据包括：。。。。，抓取内容如下图所示。

其中手机APP发帖数为160088，占总发帖数的78%（app发帖占比图）；除开匿名用户，共有73121名用户在该区发帖
<div align=center><img width="499" height="408" src="https://github.com/beckleon/netease_scrapy/master/pics/overview.jpg"/></div>
