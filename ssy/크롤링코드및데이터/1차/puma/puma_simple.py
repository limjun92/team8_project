import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os


def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'-------{ctgr}-------')
        page = 1
        while True:
            params = (
                ('category', ctgr),
                ('p', page),
            )

            res = requests.get('https://kr.puma.com/aramenu/ajax/productview/',  params=params, )

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

            ul = soup.select('ul.products-grid > li.item ')
            print(page, len(ul))
            
            for li in ul:
                detail_href = li.select_one('a')['href']
                image = 'http:'+li.select_one('a > img')['src'].replace('210x','420x')
                # print(detail_href, image)
                try:
                    price = li.select_one('div.puma_prod_info > span').text.strip()
                except :
                    price = li.select_one('div.price > span').text
                price = ''.join(price.split('원')[0].split(','))
                # print(price)
                detail = [['puma', gender,  type_, detail_href, price, image]]
                df = df.append(detail)

            if len(ul)<16:
                break
            page+=1

    df.to_csv(f'./puma_{gender}_{type_}.csv')




get_href([392, 161, 238, 44, 42], 'woman', 'top')
get_href([46,545,45], 'woman', 'bottom')
get_href([160, 391, 20, 18], 'man', 'top')
get_href([22,21], 'man', 'bottom')