import requests
from bs4 import BeautifulSoup
import pandas as pd

shop_name = 'philosophia'
def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    hrefs = []
    for ctgr in ctgr_list:
        print(f'<<<<<<<<<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>>>>>>>>>>>>')
        page = 1
        while True:
            print(f'------------------{page}---------------')
            
            url = f'https://www.p-sophia.com/category/{ctgr}/?page={page}'
            print(url)
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'},)

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('li.item')
            print(len(ul))
            if len(ul)==0:
                break

            for li in ul:
                href = 'https://www.p-sophia.com' + li.select_one('div#line > a')['href']
                if href in hrefs:
                    continue
                hrefs.append(href)
                image = 'https:' + li.select_one('div#line > a > figure > img')['src']
                # print(href, '\n',image)
                try:
                    price = li.select_one('div > div.description > ul > li:nth-child(2) > span > span:nth-child(1)').text.strip()
                except:
                    res = requests.get(href,headers={'User-Agent': 'Mozilla/5.0'},)
                    soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
                    price = soup.select_one('#span_product_price_text').text.strip()

                # print(price)
                detail = [[shop_name,href, price, image]]
                df = df.append(detail)
            page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

get_href(['상의/265'],'W','T')
get_href(['하의/266'],'W','B')
