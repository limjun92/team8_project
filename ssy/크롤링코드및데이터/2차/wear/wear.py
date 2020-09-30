import requests
from bs4 import BeautifulSoup
import pandas as pd

shop_name = 'wear'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            url = f'https://www.w3ar.com/product/list.html?cate_no={ctgr}&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul.prdList.grid3 > li')
            print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'https://www.w3ar.com' + li.select_one('div.thumbnail > a')['href']
                image = 'https:' + li.select_one('div.thumbnail > a > img')['src']
                # print(href, image)
                try:
                    price = li.select_one('div.description > ul > li:nth-child(2) > span').text.strip()
                except:
                    price = li.select_one('div.description > ul > li > span:nth-child(2)').text.strip()
                
                # print(price)
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

get_href(['46'],'W','T')
get_href(['47'],'W','B')
