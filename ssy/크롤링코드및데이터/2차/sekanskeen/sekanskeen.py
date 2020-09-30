

import requests
from bs4 import BeautifulSoup
import pandas as pd

shop_name = 'sekanskeen'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            url = f'https://2ndskin.co.kr/category/'+ctgr
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul.prdList.grid3.inline > li')
            print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'https://2ndskin.co.kr' + li.select_one('div.thumbnail > a')['href']
                image = 'https:'+li.select_one('div.thumbnail > a > img')['src']
                # print(href+'\n'+image)
                
                price = li.select_one('p.price.custom').text.strip()
                if price == '0':
                    price = li.select_one('p.price.product_price > strike').text.strip()
                print(price)

                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            # page+=1
            break
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')



get_href(['%EC%8A%A4%ED%8F%AC%EC%B8%A0%EB%B8%8C%EB%9D%BC/133/','%ED%83%91%EC%A0%90%ED%8D%BC/123/'],'W','T')
get_href(['%EB%A0%88%EA%B9%85%EC%8A%A4/127/'],'W','B')

