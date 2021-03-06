import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'tmpl'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<{ctgr}>>>>>>>>>>>')
        page = 1
        # while True:
        print(f'------------------{page}---------------')
        url = f'https://tmpl.co.kr/product/list.html?cate_no={ctgr}'
        res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
        ul = soup.select('ul.prdList > li.xans-record-')
        print(len(ul))
        if len(ul)==0:
            break

        for li in ul:
            href = 'https://tmpl.co.kr' + li.select_one('a')['href']
            image = 'https:'+li.select_one('img')['src']
            # print(href, image)
            price = li.select_one('div.description > ul').text.split(':')[-1].strip()
            # print(price) 
            detail = [[shop_name,href, price, image]]
            df = df.append(detail)
            # page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')


get_href(['49'],'W','T')
get_href(['50'],'W','B')