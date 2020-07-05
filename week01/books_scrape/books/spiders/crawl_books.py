# -*- coding: utf-8 -*-
import scrapy


class CrawlBooksSpider(scrapy.Spider):
    name = 'crawl_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass
