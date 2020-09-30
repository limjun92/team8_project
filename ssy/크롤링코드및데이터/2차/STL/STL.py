import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'STL'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        page = 1
        while True:
            if gender == 'M':
                mcode = '002'
            else:
                mcode = '001' #woman
            url = f'http://www.beststl.com/shop/shopbrand.html?type=Y&xcode={ctgr}&mcode={mcode}&scode=001&sort=&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('dl.item-list')
            print(len(ul))
            if len(ul)==0:
                break
            for li in ul:
                href = 'http://www.beststl.com' + li.select_one('a')['href']
                image = li.select_one('img.MS_prod_img_l')['src']
                price = li.select_one('dd > ul > div > li:nth-child(2) > strike').text.strip()
                if price == '0':
                    price = li.select_one('dd > ul > div > li').text.strip()
                # print(href, image, price)
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')




top = ['019']
bottom = ['012']
gender = 'W'
get_href(top,gender,'T')
get_href(bottom,gender,'B')
gender = 'M'
get_href(top,gender,'T')
get_href(bottom,gender,'B')