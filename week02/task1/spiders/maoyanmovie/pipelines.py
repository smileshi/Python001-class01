# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class MaoyanmoviePipeline:
    def process_item(self, item, spider):       
        film_name = item['film_name']
        film_type = item['film_type']
        plan_date = item['plan_date']
        # output = f'|{film_name}|\t|{film_type}|\t|{plan_date}|\n\n'
        # with open('e:/maoyan.txt', 'a+', encoding='gbk') as article:
        #     article.write(output)
        conn = pymysql.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "Welcome12",
            db = "test",
            charset = 'utf8mb4'
        )
    
        cursor = conn.cursor()
        sql = "insert movie_info(movie_name, movie_type, movie_plan_date) VALUES('" f'{film_name}' "','" f'{film_type}' "','" f'{plan_date}' "')"
        print(sql)
        try:        
            cursor.execute(sql)        
            conn.commit()
        except:        
            conn.rollback()

        cursor.close()
        conn.close()
        return item
