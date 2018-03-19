# netease_scrapy
## 1、背景 ##
本项目尝试抓取网易《荒野行动》游戏官网论坛的“综合讨论”区的所有发帖记录（除置顶帖之外），对抓取数据进行初步分析并将结果进行可视化展示。

## 2、使用技术 ##
使用 Scrapy 框架抓取数据并将结果保存到本地 MySQL 数据库内，进行初步的数据清洗之后，将分析结果使用 Superset 展示出来。

## 3、抓取过程及结果 ##
开始抓取时，综合讨论区共有576页，考虑到抓取速度比较快，短时间内新增的帖子不至于多于一页，而早先的主题帖一般也不会被人回复，所以选择从最后一页开始抓取并往前翻页。抓取的数据包括：主题帖id，主题名，链接地址，发帖用户名，发表时间，回复数，查看数。抓取的数据保存至threads表，内容如下所示：
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/threads.jpg"/></div>

在抓取到主题帖的链接地址时，进入主题帖并抓取所有的回复贴数据，包括：回复贴id，对应的主题帖id，回复贴发表用户名，用户id，帖子的楼层，发表时间，是否为app发帖（1是0否）。抓取的数据保存至posts表，内容如下所示：
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/posts.jpg"/></div>


## 4、数据展示 ##

### 总览 ###

抓取时间约为1个半小时，截止到2018年03月15日14点50分，除开置顶帖之外，总共抓取到了16962个主题帖以及205101个帖子。最早的帖子发表于2017年08月29日，至2018年03月15日总共199天，平均每天85个主题帖，1031个帖子。其中手机APP发帖数为160088，占总发帖数的78%，说明手机APP是手机游戏的主要交流手段；除开匿名用户，共有73121名玩家在该区发帖。
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/overview.jpg"/></div>

### 发帖内容分析 ###

查看数最多的 和 回复数最多的 前十大帖子如下图所示：
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/reviewtop10.jpg"/></div>
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/replytop10.jpg"/></div>
说明活动贴及攻略贴是吸引玩家查看和回复的主要帖子。

主题帖使用的名字前十，以及主题名的词云展示如下图：
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/titlenametop10.jpg"/></div>
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/wordcloud.jpg"/></div>

### 用户分析 ###

发帖量前十的玩家如下图所示，发帖最多的玩家在本版发表了1851个帖子，平均每天9个。
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/usertop10.jpg"/></div>
在所有发表过帖子的用户里，只发过一篇帖子的玩家有44320个，占到总人数的60%左右。发表帖子10篇及以内的玩家数目为71370个，占到所有发帖玩家数目的97.6%，说明玩家在论坛并不活跃。
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/post_usernum.jpg"/></div>
从玩家发帖时间来看，玩家在18点至24点之间发帖总数为68860个，占到总数的33.6%左右，其次是下午时段12点至18点。说明玩家在下午及晚上更为活跃。
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/post_timezone.jpg"/></div>

### 趋势分析 ###

下图是玩家每天发帖数目的记录。从游戏论坛开放开始，前期处于不温不火的状态。从11月开始，游戏出现热度，至12月14日达到最高峰，一天发帖量达到4730个。随后每天的发帖量保持在1000至2000左右，但是可以从趋势图看出，游戏热度是在逐渐减退的。
<div align=center><img src="https://raw.githubusercontent.com/beckleon/netease_scrapy/master/pics/post_trend.jpg"/></div>

## 5、总结 ##
从抓取的内容总体来看，玩家在官方论坛上不太活跃。可能由多种因素造成，这里不做推测。
