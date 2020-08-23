# -*- coding: utf-8 -*-
import pandas as pd

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline(object):
    def process_item(self, item, spider):
        print("代码来过这里")
        print(item)
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_plan_time = item['movie_plan_time']
        output = f'|{movie_name}|\t|{movie_type}|\t|{movie_plan_time}'
        with open('./cat_scrapy_movies.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
