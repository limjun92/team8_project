import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'cielcoco'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            url = f'http://www.cielcoco.kr/shop/shopbrand.html?type=X&xcode={ctgr}&sort=&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('div.product-wrap > div > div.item-cont > dl.item-list')
            print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'http://www.cielcoco.kr' + li.select('a')[1]['href']
                image = 'http://www.cielcoco.kr' + li.select('img')[-1]['src']
                # print(href, image)
                try:
                    price = li.select_one('li.prd-price > strike').text.strip()
                except:
                    continue
                
                # print(price)
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

# get_href(['009','008'],'W','T')
get_href(['007'],'W','B')