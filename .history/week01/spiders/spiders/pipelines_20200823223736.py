# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline(object):
    def process_item(self, item, spider):
        print("代码来过这里")
        print(i)
        movies = pd.DataFrame(item)
        movies.to_csv('./week01/spiders/cat_scrapy_movies.csv', encoding='utf8', index=False, header=False)
        return item
