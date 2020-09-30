

import requests
from bs4 import BeautifulSoup
import pandas as pd

shop_name = 'blackmonster'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            url = f'https://www.black-monster.co.kr/product/list.html?cate_no={ctgr}&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul.prdList.columnsmall > li')
            print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'https://www.black-monster.co.kr' + li.select_one('div.thumb_warp > a')['href']
                image = 'https:'+li.select_one('div.thumb_warp > a > img')['src']
                # print(href+'\n'+image)
                
                price = li.select_one('ul.xans-element-.xans-product.xans-product-listitem').text.split('판매가 :')[-1].split(':')[0].strip()
                # if price == '0':
                #     price = li.select_one('p.price.product_price > strike').text.strip()
                # print(price)

                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
            # break
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')



get_href(['176','177','178'],'W','T')
get_href(['198'],'W','B')

get_href(['169','171','172'],'M','T')
get_href(['184'],'M','B')

