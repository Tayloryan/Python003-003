import requests
from bs4 import BeautifulSoup as bs
import lxml.etree


def get_url_name(myurl):
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
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a'):
            print(atag.get('href'))
            print(atag.find('span',).text)

    # xml化处理
    # selector = lxml.etree.HTML(response.text)

    # file_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    # print(f'电影名称：{file_name}')


# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))

print(urls)

from time import sleep

sleep(10)

for page in urls
