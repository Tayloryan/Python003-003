import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd
import lxml.etree


def get_url_name(movie_url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    cookie = '' 


    # 声明为字典使用字典的语法赋值
    header = {}
    header['user-agent'] = user_agent
    header["cookie"] = cookie

    # 获取网络请求结果
    response = requests.get(movie_url, headers=header)

    # print(response.text)
    # print(response.status_code)

    # BeautifulSoup 解析网络请求
    bs_info = bs(response.text, 'html.parser')
    movies = []
    for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[:10]:
        movie_name = ""
        movie_type = ""
        movie_plan_time = ""
        for atag in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
            if(atag.find('span', attrs={'class': 'name'})):
                movie_name = atag.find('span', attrs={'class': 'name'}).text
                print(movie_name)
            if(atag.find('span', attrs={'class': 'hover-tag'})):
                span_name = atag.find('span', attrs={'class': 'hover-tag'}).text
                if(span_name == "类型:"):
                    movie_type = atag.text.replace("类型:", "").replace("\n", "").strip()
                    print(movie_type)
                elif(span_name == "上映时间:"):    
                    movie_plan_time = atag.text.replace("上映时间:", "").replace("\n", "").strip()
                    print(movie_plan_time)

        movie = [movie_name, movie_type, movie_plan_time]
        movies.append(movie)
    return movies


# 电影详情页面
movie_url = 'https://maoyan.com/films?showType=3'
sleep(10)
movies = pd.DataFrame(data = get_url_name(movie_url))
movies.to_csv('./week01/cat_movies.csv', encoding='utf8', index=False, header=False)
