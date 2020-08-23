import requests
from bs4 import BeautifulSoup as bs
import lxml.etree


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

# 电影详情页面
movie_url = 'https://movie.douban.com/subject/1292052/'

# 声明


response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a',):
        print(atag.get('href'))
        print(atag.find('span',).text)

# print(response.text)
# print(response.status_code)
