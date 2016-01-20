#CSUInfoAPI
This is a simple API to query CSU academic infomation based on the  micro python framework [Flask](http://flask.pocoo.org/).  
这是一个基于Flask轻量级网络框架的Restful-API应用，主要是为客户端提供校内学术信息查询接口。数据都来自各大学院官网，由[CSUAcademicSpider](https://github.com/OceanJ/CSUAcademicSpider)爬虫获取和存储。    


##已开发接口  

###获取所有地点信息  
 - URL : [/all_locations]()  
 - Method :`GET`  
 - Response :  `JSON`  
`location_id`   地点ID  
`title`         地点全称  
`latitude`      纬度    
`longitude`     经度  

Sample：
```[
{
"latitude": 28.176791,
"location_id": 1,
"longitude": 112.936979,
"title": "本部民主楼"
},
{
"latitude": 28.177171,
"location_id": 2,
"longitude": 112.937651,
"title": "本部计算机楼"
},
...
]
```
###获取所有学术信息
 - URL : [/all_info]()
 - Method : `GET`
 - Response : `JSON`  
`aca_id`      信息ID  
`a.title`     标题  
`a.url`       来源URL     
`a.time`      举办时间（准确）  
`a.location`  举办地点  
`l.longitude` 举办地点经度  
`l.latitude`  举办地点纬度  
`a.academy`   举办学院  
`a.type`      学术类型（科学/技术/工程/医学）  
`a.html_content`  **具体正文**(非HTML源码)
`a.date_sort`   序列化日期（用于排序和检索）  
Sample：
```
[
{
"title": " 营养与食品卫生学系研究士开题报告通知（2016.01.15）",
"url": "http://sph.csu.edu.cn/info/1031/2301.htm",
"academy": "公共卫生学院",
"html_content": "\r\n 营养与食品卫生学系研究士开题报告通知&......",
"longitude": 112.991397,
"location": "公共卫生学院 营养与食品卫生学系PBL教室",
"date_sort": "20160115",
"time": "2016年1月15日（周五）上午9:00",
"latitude": 28.221955,
"type": "医学类",
"aca_id": 96
},
....
]
```
###通过关键字检索学术信息
 - URL ：[/search_match_string/<string:match_string>]()
 - Params :match_string
 - Method : `GET`
 - Response : `JSON`  
 返回所有标题、学院名、地点或内容中有关键字的学术信息  
 数据格式同上，不再重复  

 Sample:
 `curl localhost:5000/search_match_string/美国`

```
[
{
"title": " 美国阿拉巴马大学心理学系科研副主任David C. Schwebel学术讲座",
"url": "http://sph.csu.edu.cn/info/1031/2282.htm",
"academy": "公共卫生学院",
"html_content":  美国阿拉巴马大学心理学系科研副主任David C. Schwebel学术讲座&……",
"longitude": 112.991397,
"location": "公共卫生学院6楼616教室",
"date_sort": "20160113",
"time": "2016年1月13日上午9:30-11:30",
"latitude": 28.221955,
"type": "医学类",
"aca_id": 94
},
...
]
```



###通过类型检索学术信息
  - URL ：[/search_type/<string:type>]()
  - Params :type
  - Method : `GET`
  - Response : `JSON`  
  返回指定类型的学术信息      
  数据格式同上，不再重复

  Sample:
  `curl localhost:5000/search_type/社科类 `
```
[
{
"title": "公共管理前沿与方法论坛2015第14期（总第63期）",
"url": "http://csuspa.csu.edu.cn/html/201512/14/20151214162622.htm",
"academy": "公管院",
"html_content": "....",
"longitude": 112.935851,
"location": "升华北10楼和谐阁",
"date_sort": "20151216",
"time": "2015年12月16日（周三）14：30-17：00",
"latitude": 28.176783,
"type": "社科类",
"aca_id": 42
},
...
]
```


###通过地点ID检索学术信息
   - URL ：[/search_location_id/<int:location_id>]()
   - Params :match_string
   - Method : `GET`
   - Response : `JSON`  
  返回所有地点ID为指定ID的学术信息       
  数据格式同上，不再重复

Sample:`curl localhost:5000/search_location_id/9 `
```
[
{
"title": "III族氮化物半导体材料和深紫外半导体激光",
"url": "http://wl.csu.edu.cn/Seconpage.aspx?strid=7b0484b2-1494-4459-b9ab-16d1b2288868&id=1e2a7463-dca8-4ade-8e19-11adb4fe1763",
"academy": "物理院",
"html_content": "...",
"longitude": 112.944061,
"location": "南校区双超所211会议室  ",
"date_sort": "20160114",
"time": "2016年1月14日下午2:30-3:30",
"latitude": 28.168653,
"type": "科学技术类",
"aca_id": 26
},
...
]
```



###通过日期区间检索学术信息
  - URL ：[/search_date]()
  - Params :  
    `begin` 开始日期   
    `end`   结束日期（格式都为 YYYYMMDD 20160101）  
  - Method : `GET`
  - Response : `JSON`  
  返回所有举办日期在指定日期区间的学术信息     
  数据格式同上，不再重复

  Sample: `curl localhost:5000/search_date?begin=20160101&&end=20170101 `
```
[
{
"title": " 营养与食品卫生学系研究士开题报告通知（2016.01.15）",
"url": "http://sph.csu.edu.cn/info/1031/2301.htm",
"academy": "公共卫生学院",
"html_content": " 营养与食品卫生学系研究士开题报告通知（2016.01.15...",
"longitude": 112.991397,
"location": "公共卫生学院 营养与食品卫生学系PBL教室",
"date_sort": "20160115",
"time": "2016年1月15日（周五）上午9:00",
"latitude": 28.221955,
"type": "医学类",
"aca_id": 96
},
...
]
```
