import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'wannabezfit'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<{ctgr}>>>>>>>>>>>')
        page = 1
        # while True:
        print(f'------------------{page}---------------')
        url = f'https://wannabezfit.co.kr/product/list.html?cate_no={ctgr}'
        res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
        ul = soup.select('ul.prdList > li.item.xans-record-')
        print(len(ul))
        if len(ul)==0:
            break

        for li in ul:
            href = 'https://wannabezfit.co.kr' + li.select_one('a')['href']
            image = 'https:'+li.select_one('img')['src']
            # print(href,'\n',image)
            price = li.select_one('div > div.description > div > ul > li:nth-child(2) > span:nth-child(2)').text.strip()
            # print(price) 
            detail = [[shop_name,href, price, image]]
            df = df.append(detail)
            # page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')


get_href(['25'],'W','T')
get_href(['27'],'W','B')