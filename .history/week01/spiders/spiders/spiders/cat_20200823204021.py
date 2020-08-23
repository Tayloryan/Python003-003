# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class CatSpider(scrapy.Spider):
    name = 'cat'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
        
    def parse(self, response):
        # 打印网页的url
        print(response.url)
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
        for movie in movies:
            # print(movie)
            span_name = movie.xpath('./div[@class="movie-hover-title"]/span[1]//text())
            if(movie_name == "类型:"):

            elif(span_name == "上映时间:"):

            elif():
                
            # link = movie.xpath('./a/@href')
            # print('-----------')
            # print(title)
            # print(link)
            # print('-----------')
            # print(title.extract())
            # print(link.extract())
            # print(title.extract_first())
            # print(link.extract_first())
            # print(title.extract_first().strip())
            # print(link.extract_first().strip())
