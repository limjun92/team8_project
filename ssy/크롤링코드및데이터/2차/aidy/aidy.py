import requests
from bs4 import BeautifulSoup
import pandas as pd


shop_name = 'aidy'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            url = f'http://aidy.co.kr/product/list.html?cate_no={ctgr}&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('#contents > div > div.prdList-wrap.align-left > div > div:nth-child(4) > ul > li')
            # print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'http://aidy.co.kr' + li.select_one('a')['href']
                image = 'http:'+li.select('img')[0]['data-original']
                # print(href, image)

                price = li.select_one('div > span > ul > li > span:nth-child(2)').text.strip().split('₩')[-1]
                # print(price)
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

get_href(['26'],'W','T')
get_href(['28'],'W','B')