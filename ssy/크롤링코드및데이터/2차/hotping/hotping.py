import requests
from bs4 import BeautifulSoup
import pandas as pd

shop_name = 'hotping'

def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    hrefs = []
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            
            url = f'https://www.hotping.co.kr/product/list.html?cate_no={ctgr}'
            print(url)
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'},)

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('li.item')
            print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'https://www.hotping.co.kr' + li.select_one('div.thumbnail > a')['href']
                if href in hrefs:
                    continue
                hrefs.append(href)
                image = 'https:' + li.select_one('div.thumbnail > a > img')['src']
                # print(href, '\n',image)
                price = li.select_one('div > ul > li:nth-child(1) > span:nth-child(2)').text.strip()
                print(price)
                
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            # page+=1
            break
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

get_href(['622'],'W','T')
get_href(['623'],'W','B')
