import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os


def get_href(ctgr, gender, type_):
    df = pd.DataFrame()
    page = 1
    print(f'<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>')
    while True:
        print(f'---------------{page}----------------')
        url = f'http://www.mulawear.com/shop/shopbrand.html?type=Y&xcode={ctgr}&sort=&page={page}'
        res = requests.get(url)

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
        ul = soup.select('div.useBannerPrdCont > dl.item-list')
        print(len(ul))
        if len(ul)==0:
            break
        
        for li in ul:
            detail_href = 'http://www.mulawear.com' + li.select_one('a')['href']
            image = li.select_one('a > img')['src']
            try:
                price = li.select_one('li.prd-price > strike').text.strip()
            except:
                price = li.select_one('li.prd-price > span.price').text.strip()

            price = ''.join(price.split('원')[0].split(','))
            # print(price)
            detail = [['mulawear',gender,  type_, detail_href, price, image]]
            df = df.append(detail)
        page+=1
    df.to_csv(f'./mulawear_{gender}_{type_}.csv')


# xcode_list = ['012','009','010','007']
get_href('012','woman','top')
get_href('009','woman','bottom')
get_href('010','man','top')
get_href('007','man','bottom')

