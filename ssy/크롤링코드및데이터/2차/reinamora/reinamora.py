import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        page = 1
        while True:
            url = f'http://reinamora.co.kr/product/list.html?cate_no={ctgr}&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul.prdList.grid4 > li.xans-record-')
            if len(ul)==0:
                break
            for li in ul:
                href = 'http://reinamora.co.kr' + li.select_one('a')['href']
                image = li.select_one('img')['src']
                price = li.select_one('div > div.description > ul > li:nth-child(4) > span').text.strip()
                # print(href, image, price)
                detail = [['reinamora',href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./reinamora_{gender}_{type_}.csv')




top = ['25']
bottom = ['27']

get_href(top,'W','T')
get_href(bottom,'W','B')