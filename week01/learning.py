import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd
import lxml.etree


def get_url_name(movie_url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    cookie = '__mta=123163444.1597998462049.1598020965450.1598020970538.17; uuid_n_v=v1; uuid=2F3D5EF0E38811EAA24F3FCAC90C2348CBD5BE7640154EDCBF61A5BFE5D1A764; _csrf=7e1f85843fde02d007e00862ca5abbe677956b0cc42dbff543cf3e65dded1c7f; _lxsdk_cuid=17410217264c8-0c260caf8ce58f-15366650-13c680-17410217264c8; _lxsdk=2F3D5EF0E38811EAA24F3FCAC90C2348CBD5BE7640154EDCBF61A5BFE5D1A764; mojo-uuid=854a05f19abed8cbfc3b55653d56b9d4; mojo-session-id={"id":"b99064b78843eedcc655969d12ecc7b3","time":1598020682836}; lt=qnH8PmC9zcQSwTbyP1zODGeFlpUAAAAAVgsAAL2CSTJRLFWlV41ybJE8vVcTQWKGvmicrVxig4dKNEY0okeHVkykE1Y30Sjz3mATWQ; lt.sig=CaSGAycCL9Tcc3m8X_E8tr_u_2U; mojo-trace-id=52; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598021041,1598021181,1598021806,1598021828; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598021828; __mta=123163444.1597998462049.1598020970538.1598021827683.18; _lxsdk_s=17411748031-22e-a9d-ce7%7C%7C94' 

    # myurl = 'https://movie.douban.com/top250'

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
        # print(tags)
        # print(tags.find('span',).text)
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

            # print(atag.text.replace('\\n', '').strip())
            # print(atag.find('span',).text)

            # print(atag.get('href'))
            # print(atag.find('span',).text)
        movie = [movie_name, movie_type, movie_plan_time]
        movies.append(movie)
    return movies


    # xml化处理
    # selector = lxml.etree.HTML(response.text)

    # file_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    # print(f'电影名称：{file_name}')

    # plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
    # print(f'上映日期：{plan_date}')

    # rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    # print(f'评分：{rating}')

    # return [file_name, plan_date, rating]


# 生成包含所有页面的元组
# urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))
# print(urls)

# sleep(10)
# for page in urls:
#     get_url_name(page)
#     sleep(5)

# 电影详情页面
movie_url = 'https://maoyan.com/films?showType=3'
sleep(10)
movies = pd.DataFrame(data = get_url_name(movie_url))
movies.to_csv('./week01/cat_movies.csv', encoding='utf8', index=False, header=False)
