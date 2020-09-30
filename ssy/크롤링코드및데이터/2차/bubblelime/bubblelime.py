import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'bubblelime'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        page = 0
        while True:
            page+=1
            print(f'--------------{page}page-----------------')
            params = (
                ('xcode','008'),
                ('mcode',ctgr),
                # ('type',url_type),
                ('page',page)

            )
            url = 'http://www.bubblelime.co.kr/shop/shopbrand.html?'
            # url = f'http://www.bubblelime.co.kr/shop/shopbrand.html?type=X&xcode={ctgr}&sort=&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'},params=params)
            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('div.box_prd')
            print(ctgr)
            print(len(ul))
            if len(ul)==0:
                break
            for li in ul:
                href = 'http://www.bubblelime.co.kr' + li.select_one('div.thumb > a')['href']
                image = 'http://www.bubblelime.co.kr' + li.select_one('div.thumb > a > img')['src']
                price = li.select_one('ul > li.price > span > s').text.strip()
                # print(href, image, price)
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)

    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

mcode = ['001', '005', '004', '002', '003']
# url_type = ['M', 'M', 'M', 'M', 'M']

top = ['011']
gender = 'W'
get_href(mcode, gender,'B')
# get_href(top, gender,'T')
