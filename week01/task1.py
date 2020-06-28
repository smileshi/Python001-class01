# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)
with open('e:/maoyan.txt', 'a+', encoding='gbk') as article:
            article.write(response.text)

bs_info = bs(response.text, 'html.parser')

i = 0
film_name = ''
film_type = ''
plan_date = ''
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    i = i + 1
    nametag = tags.find('span', attrs={'class': 'name'})
    film_name = nametag.get_text()
    print(f'电影名称: {film_name}')

    for divTag in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
        typeTag = divTag.find('span', attrs={'class': 'hover-tag'})
        
        if typeTag != None:
            content = typeTag.get_text()
            if content == '类型:':
                film_type = divTag.get_text().replace(' ', '').replace("\n", "")
                print(f'{film_type}')
            if content == '上映时间:':
                plan_date =  divTag.get_text().replace(' ', '').replace("\n", "")
                print(f'{plan_date}')
    mylist = [f'电影名称: {film_name}', film_type, plan_date]
    movie1 = pd.DataFrame(data = mylist)
    movie1.to_csv('e:/movie3.csv', encoding='gbk', mode = 'a', index=False, header=False)
    if i == 11:
        break