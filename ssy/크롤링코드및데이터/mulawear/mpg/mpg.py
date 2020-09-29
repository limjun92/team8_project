import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_href(ctgr_list, gender, type_):
    df_top = pd.DataFrame()
    df_bottom = pd.DataFrame()
    for ctgr in ctgr_list:
        page = 0
        while True:
            page+=1
            print(f'------------{page}-----------')
            url = 'http://www.mpgsport.co.kr/category/'+ctgr+f'?page={page}'
            print(url)
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul.prdList.grid4 > li.xans-record-')
            print(len(ul))
            if len(ul)==0:
                break
            for li in ul:
                href = 'http://www.mpgsport.co.kr' + li.select_one('div.prdImg > a')['href']
                image = 'https:'+li.select_one('div.prdImg > a >img')['src']
                name = li.select_one('div.description > div.name').text.split(':')[-1].strip()
                try:
                    price = li.select_one('div > div.description > ul > li:nth-child(2) > span').text.split()[-1].strip()
                except:
                    price = li.select_one('div > div.description > ul > li> span').text.strip()
                if ('반바지' in name)|('팬츠' in name)|('쇼츠' in name):
                    type_='B'
                    detail = [['mpg',href, name, price, image]]
                    df_bottom = df_bottom.append(detail)
                else:
                    type_='T'
                    detail = [['mpg',href, name, price, image]]
                    df_top = df_top.append(detail)
            
    df_bottom.to_csv(f'./mpg_{gender}_B.csv')
    df_top.to_csv(f'./mpg_{gender}_T.csv')


# top = ['tops/245/','jacket/247/']
# bottom = ['bottoms/246/']

# get_href(top, 'W', 'T')
# get_href(bottom, 'W', 'B')
get_href(['men/262/'],'M','T')
