import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

import lxml.etree


def get_url_name(movie_url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

    # myurl = 'https://movie.douban.com/top250'

    # 电影详情页面
    # movie_url = 'https://movie.douban.com/subject/1292052/'

    # 声明为字典使用字典的语法赋值
    header = {}
    header['user-agent'] = user_agent

    # 获取网络请求结果
    response = requests.get(movie_url, headers=header)

    # print(response.text)
    # print(response.status_code)

    # BeautifulSoup 解析网络请求
    # bs_info = bs(response.text, 'html.parser')
    # for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    #     for atag in tags.find_all('a'):
    #         print(atag.get('href'))
    #         print(atag.find('span',).text)

    # xml化处理
    selector = lxml.etree.HTML(response.text)

    file_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    print(f'电影名称：{file_name}')

    plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
    print(f'上映日期：{file_name}')

    rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    print(f'评分：{rating}')

    return mylist[file_name, plan_date, rating]


# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))
print(urls)

sleep(10)
mylist = []
for page in urls:
    mylist.append(get_url_name(page))
    sleep(5)
movie1 = pd.DataFrame(data = mylist)
movie1.to_csv('./movie1.csv')