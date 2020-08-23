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
        movie_list = []
        movie = ''
        for i in item
            movie = [i['movie_name'], i['movie_type'], i['movie_plan_time']]
            movie_list.append(movie)
        movies = pd.DataFrame(movie_list)
        movies.to_csv('./cat_scrapy_movies.csv', encoding='utf8', index=False, header=False)
        return item
