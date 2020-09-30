import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

shop_name = 'oui-grow'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:

        url = f'https://www.oui-grow.com/{ctgr}'
        res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
        ul = soup.select('div.shop-item._shop_item')
        print(len(ul))

        idx_list = []
        for li in ul:
            href = 'https://www.oui-grow.com' + li.select_one('a')['href']
            idx = href.split('idx=')[-1]
            if idx in idx_list:
                continue
            idx_list.append(idx)
            image = li.select_one('img._org_img')['data-original']
            price = li.select_one('div.item-pay-detail > p').text.strip()

            detail = [[shop_name,href, price, image]]
            df = df.append(detail)
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')




top = ['173','174']
bottom = ['171']

gender = 'W'
get_href(top,gender,'T')
get_href(bottom,gender,'B')
