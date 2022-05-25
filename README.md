# CBECgoodsdata-visualization-python
地方跨境电商通关商品数据可视化（python脚本）  
### 基于Python提取不规则地址中的地级行政区  
### 一、问题描述  
在做毕业设计时，遇到一个按市级区域统计物流清单数量的需求，但数据库里的相关数据都是在生产环境下直接入库的。由于物流清单地址字段值是由消费者填写的，地址值的格式不规则、不统一，没办法直接用来做统计。  
### 二、解决方案  
为解决上述问题，常规的想法是使用正则表达式匹配，但数据库里实际的地址字符串没有规律，有些字段省略了“省”、“市”、“县”这些关键字，有些甚至没有写明省址或市址，那么这种方法误差率太高，不适合用于在上述问题中做提取市级行政区的操作。  
在查阅资料后，找到一种基于 Python 脚本的匹配方法。  

​		① 在数据库中导入国内省市区县数据；  

​		② 将地址字符串分词；  

​		③ 将所有关键词，依次同（省）市、县两级数据进行比较；  

​		④ 先匹配全国的市级行政区，若没有匹配出市级行政区，则匹配县级行政区；  

​		⑤ 匹配出区县后，再根据县名，查出对应的地级市  

从国家民政部官网中能够查到国内最新的省市区县数据，将这些数据拷贝到excel 中，并插入数据库；然后导入 jieba 分词库来对地址字符串做分词；最后编写Python 脚本将所有的关键词依次同（省）市、县两级数据进行比较和匹配，提取地级行政区。  
### 三、方法步骤
1、导入全国行政区域字典数据  

​		从国家民政部官网中将国家行政区划数据导入excel，按省、市、区录入  
![image](https://user-images.githubusercontent.com/48922159/170196204-a25a4195-1f58-4f9f-a50a-050cacd83605.png)
​		再将excel表导入数据库  

![image](https://user-images.githubusercontent.com/48922159/170196398-28839423-67cb-4e7b-8bde-b456b1daff3d.png)
![image](https://user-images.githubusercontent.com/48922159/170196456-d5093274-7dde-4ccf-8825-ebcd6df2bf1f.png)

​		基于china_ad_division表整理出市级字典、县级字典  
![image](https://user-images.githubusercontent.com/48922159/170196536-d80ff403-cada-46a1-b40a-8687b17cd3c7.png)
2、相关库准备  

2.1 下载jieba分词库  
![image](https://user-images.githubusercontent.com/48922159/170197605-e748870f-b791-416d-9b98-7b60717fe06a.png)
2.2 配置mysql  
​		安装MySQLdb，我的Python版本是3.10，所以mysqlclient是2.1.0版本  
