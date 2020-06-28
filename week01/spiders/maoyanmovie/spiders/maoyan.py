# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanmovieItem
from scrapy.selector import Selector



class MaoyanSpider(scrapy.Spider):
     # 定义爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    # def start_requests(self):
    #     for i in range(0, 10):
    #         url = f'https://movie.douban.com/top250?start={i*25}'
    #         yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # def start_requests(self):
    #     url = 'https://maoyan.com/films?showType=3'
    #     yield scrapy.Request(url=url, callback=self.parse)
    # 解析函数
    def parse(self, response):
        # print(response.text)    
        # print('==================')
        # content = Selector(response=response).xpath('//dl[@class="movie-list"]/dd[1]/div/div[@class="movie-item-hover"]/a/div/div[1]/span[1]')
        # print(content)
        # print('==================')
        selector = Selector(response=response)
        i = 0
        for item in selector.xpath('//div[@class="movie-hover-info"]').getall()[0:10]:
            i = i + 1
            print("i:" + str(i))
            # print(item)
            film_name = Selector(text=item).xpath('//span[contains(@class, "name ")]/text()').extract_first()
            film_type = Selector(text=item).xpath('//div/div[2]/text()').getall()[1].replace(' ', '').replace("\n", "")
            plan_date = Selector(text=item).xpath('//div/div[4]/text()').getall()[1].replace(' ', '').replace("\n", "")
            print(film_name)
            print(film_type)
            print(plan_date)        
            item = MaoyanmovieItem()
            item['film_name'] = '电影名称:' + film_name
            item['film_type'] = '电影类型:' + film_type
            item['plan_date'] = '上映日期:' + plan_date
            yield item