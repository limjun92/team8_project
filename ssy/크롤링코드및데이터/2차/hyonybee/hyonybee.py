import requests
from bs4 import BeautifulSoup
import pandas as pd

shop_name = 'hyonybee'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            url = f'http://www.hyonybee.com/product/list.html?cate_no={ctgr}&page={page}'
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul.prdList > li')
            print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'http://www.hyonybee.com' + li.select_one('div.thumbnail > a')['href']
                image = 'https:' + li.select_one('div.thumbnail > a > img')['src']
                # print(href, '\n',image)
                # try:
                price = li.select_one('div > div.infomation > ul > li:nth-child(1) > span:nth-child(2)').text.strip()
                # except:
                #     price = li.select_one('div.description > ul > li > span:nth-child(2)').text.strip()
                #anchorBoxId_131 > 
                # print(price)
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

get_href(['45', '44'],'W','T')
get_href(['46'],'W','B')
