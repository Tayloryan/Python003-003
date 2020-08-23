# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline(object):
    def process_item(self, item, spider):
        movies = pd.DataFrame(data = get_url_name(movie_url))
movies.to_csv('./week01/cat_movies.csv', encoding='utf8', index=False, header=False)
        return item
