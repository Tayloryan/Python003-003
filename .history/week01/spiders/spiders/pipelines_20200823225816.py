# -*- coding: utf-8 -*-
import pandas as pd

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline(object):
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_plan_time = item['movie_plan_time']
        output = f'{movie_name},{movie_type},{movie_plan_time}\n'
        with open('./cat_scrapy_movies.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
