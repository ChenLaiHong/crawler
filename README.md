# crawler
## 第一个爬虫————酷狗Top 500
在爬取酷狗Top500数据的时候不能全部爬取完，它会显示数组越界。。。。。后来经过查看歌曲其中有一首歌曲的格式跟其他的不一样，其他歌曲的歌名跟歌手名是使用“-”隔开的，而第340条歌曲没有名称只有很多歌手名，因为这首是串烧，所以我所携带规则对于这首歌就不起效了，所以就存在了数组越界。