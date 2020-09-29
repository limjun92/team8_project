import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_href(ctgr, gender, type_):
    df = pd.DataFrame()
    page = 1
    while True:
        url = f'http://www.launday.co.kr/product/list.html?cate_no={ctgr}&page={page}'
        res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
        ul = soup.select('ul.prdList.grid4.zoom > li.xans-record-')
        if len(ul)==0:
            break
        
        for li in ul:
            href = 'http://www.launday.co.kr' + li.select_one('a')['href']
            image = li.select_one('a > img')['src'][2:]
            name = li.select_one('div.description > strong > a > span:nth-child(2)').text
            price = li.select_one('li.xans-record-').text.split(':')[-1].strip()
            detail = [['LAUNDAY',href, name, price, image]]
            df = df.append(detail)
        page+=1
    df.to_csv(f'./launday_{gender}_{type_}.csv')



get_href('23','W','T')
get_href('25','W','B')
# ctgr_list = ['23','25']
# for ctgr in ctgr_list:
#     if ctgr == '23':
#         gender = 'W'
#         type_='T'
#     elif ctgr == '25':
#         gender = 'W'
#         type_='B'

#     file = './launday_{gender}_{type_}.csv'
#     if os.path.isfile(file):
#         os.remove(file)
#     get_href(ctgr, gender, type_)