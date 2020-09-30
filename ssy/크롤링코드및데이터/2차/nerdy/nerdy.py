import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'nerdy'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            url = f'https://www.whoisnerdy.com/product/list.html?cate_no={ctgr}&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            # xans-element- xans-product xans-product-listnormal ec-base-product
            ul = soup.select('div.xans-product-listnormal > ul> li.xans-record-')
            # print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'https://www.whoisnerdy.com' + li.select_one('div.thumbnail > a')['href']
                image = 'https:' + li.select_one('div.thumbnail > a > img')['src']
                # print(href, image)

                price = li.select_one('div > div.description').text.split(':')
                if len(price) == 3:
                    price = price[-1].strip()
                else:
                    price = price[-2].split()[0].strip()
                
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

get_href(['30','61'],'W','T')
get_href(['31'],'W','B')