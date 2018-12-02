## 第一个爬虫————酷狗Top 500
将爬取到的信息存到mysql数据库名为test的kugou表中<br>
在爬取酷狗Top500数据的时候不能全部爬取完，它会显示数组越界。。。。。后来经过查看歌曲其中有一首歌曲的格式跟其他的不一样，其他歌曲的歌名跟歌手名是使用     “-”隔开的，而第340条歌曲没有名称只有很多歌手名，因为这首是串烧，所以我所携带规则对于这首歌就不起效了，所以就存在了数组越界。<br>
* 下面是将数据放进mysql数据库的截图
![](https://github.com/ChenLaiHong/crawler/blob/master/simple/images/kugou.png)
## 第二个爬虫————淘宝商品图片
将爬取到的图片存到本地<br>
自行百度下载安装selenium，我这里是使用火狐浏览器。程序运行会自动打开淘宝登录页面，这里要扫描登录一下，其实url我直接贴到浏览器是可以访问的，但是我通过程序来打开就一定要我登录，那就只能登录了。登录完成后就自动爬取了，这里是搜索某一类商品然后爬取，想爬取什么的图片就自行修改查询关键字就可以了。<br>
* 这里是爬取到的图片地址，我已经加上“https:”拼接成地址方便直接下载<br>
![](https://github.com/ChenLaiHong/crawler/blob/master/simple/images/paqujieguo.png)
* 下面是下载好的图片
![](https://github.com/ChenLaiHong/crawler/blob/master/simple/images/tupian.png) 
