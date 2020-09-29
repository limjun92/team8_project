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
            url = f'https://conch.co.kr/product/list.html?cate_no={ctgr}&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul.prdList > li.item')
            if len(ul)==0:
                break
            for li in ul:
                href = 'https://conch.co.kr' + li.select_one('a')['href']
                image = 'https:'+li.select_one('img')['src']
                name = li.select_one('div.text-info > div.name').text.strip()
                price = li.select_one('div > a > div > ul > li:nth-child(2) > span:nth-child(2)').text.strip()
                # print(href, image, name, price)
                detail = [['conchwear',href, name, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./conchwear_{gender}_{type_}.csv')



get_href(['49','86'],'W','T')
get_href(['55'],'W','B')