import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'front2line'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            url = f'https://www.front2line.com/product/list.html?cate_no={ctgr}&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul.prdList > li.item_list')
            if len(ul)==0:
                break

            for li in ul:
                href = 'https://www.front2line.com' + li.select_one('div.prdImg > a')['href']
                image = 'https:'+li.select_one('img.thumb_Img')['src']
                # print(href, image)
                price = li.select_one('div > div.description > div > ul > li.price_all > span.price > span.strike').text.strip()
                # print(price)
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')




get_href(['43','158','171'],'W','T')
get_href(['44'],'W','B')