# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanmoviePipeline:
    def process_item(self, item, spider):        
        film_name = item['film_name']
        film_type = item['film_type']
        plan_date = item['plan_date']
        output = f'{film_name},{film_type},{plan_date},\n\n'
        with open('e:/maoyan.csv', 'a+', encoding='gbk') as article:
            article.write(output)       
        return item
