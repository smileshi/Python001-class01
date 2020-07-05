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

    # 解析函数
    def parse(self, response): 
        selector = Selector(response=response)
        for item in selector.xpath('//div[@class="movie-hover-info"]').getall()[0:10]:
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