# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem


class CatSpider(scrapy.Spider):
    name = 'cat'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
        
    def parse(self, response):
        # 打印网页的url
        # print(response.url)
        items = []
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
        for movie in movies:
            # print(movie)
            item = SpidersItem()
            movie_name = ""
            movie_type = ""
            movie_plan_time = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].extract().replace("\n", "").strip()
            print(movie_plan_time)
            movie_performer = ""
            # span_list = movie.xpath('./div[@class="movie-hover-title"]/span[1]')
            span_list = movie.xpath('./div[@class="movie-hover-title"]/span[1]')
            # print(span_name_list)

            for span_node in span_list:
                # print(span_node)
                span_node_parent_text = span_node.xpath('../text()')
                span_name = span_node.xpath('.//text()').extract_first().replace("\n", "").strip()
                # print(span_name)
                if(span_name == "类型:"):
                    movie_type = span_node_parent_text[1].extract().replace("\n", "").strip()
                    print(movie_type)
                # elif(span_name == "上映时间:"):
                #     movie_plan_time = span_name_1.xpath('../div[@class="movie-hover-title"]/text()')
                #     print(movie_plan_time)
                elif(span_name == "主演:"):
                    movie_performer = span_node_parent_text[1].extract().replace("\n", "").strip()
                    print(movie_performer)
                else:
                    movie_name = span_name
                    print(movie_name)
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_performer'] = movie_performer
            item['movie_plan_time'] = movie_plan_time
            items.append(item)
        print()
        return items      