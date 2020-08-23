# -*- coding: utf-8 -*-
import scrapy


class CatSpider(scrapy.Spider):
    name = 'cat'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        scrapy.Request(url=url, callback=)
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
        

    def parse(self, response):
        pass
