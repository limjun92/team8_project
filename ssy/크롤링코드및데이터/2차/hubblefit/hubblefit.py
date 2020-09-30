import requests
from bs4 import BeautifulSoup
import pandas as pd

shop_name = 'hubblefit'
def get_href(gender, type_):
    df = pd.DataFrame()
    page = 1
    while True:
        print(f'------------------{page}---------------')
        url = f'https://www.hubblefit.com/topall/?&page={page}&sort=recent'
        res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
        ul = soup.select('div.shop-item._shop_item')
        print(len(ul))
        

        for li in ul:
            href = 'https://www.hubblefit.com' + li.select_one('div.item-wrap > a')['href']
            image = li.select_one('img._hover_img.hover_img')['src']
            # print(href+'\n'+image)
            # try:
            price = li.select_one('div.item-pay-detail > p').text.strip()
            #container_w202002131986da86d0b6c > div:nth-child(1) > div.item-detail > div.item-pay > div.item-pay-detail > p
            # except:
            #     price = li.select_one('div.description > ul > li > span:nth-child(2)').text.strip()
            #anchorBoxId_131 > 
            # print(price)
            detail = [[shop_name,href, price, image]]
            df = df.append(detail)
        if len(ul)<25:
            break
        page+=1
    df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')

get_href('M','T')
