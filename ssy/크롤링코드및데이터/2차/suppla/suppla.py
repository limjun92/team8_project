import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'suppla'
def get_href(gender, type_):
    df = pd.DataFrame()
    # for ctgr in ctgr_list:
    #     print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
    page = 1
    # while True:
    print(f'------------------{page}---------------')
    url = f'https://www.kantukan.co.kr/shop/mall/prdt/prdt_list.php?pcate=033020011&type=8&page=1&opt=sort_num&limit_e=300&col_sort=four&list_type=2'
    res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
    ul = soup.select('div.prdt_Nlist')
    print(ul)
    print(len(ul))
    # if len(ul)==0:
    #     break

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
        # page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

# get_href(['009','008'],'W','T')
get_href('W','B')