import requests
import csv
from bs4 import BeautifulSoup
import pandas as p
import os


def get_href(ctgr, gender, type_):
    print(f'-------{ctgr}-------')
    page = 1
    while True:
        params = (
            ('category', ctgr),
            ('p', page),
        )

        res = requests.get('https://kr.puma.com/aramenu/ajax/productview/',  params=params, )

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

        ul = soup.select('ul.products-grid > li.item > div.puma_prod_top > a')
        print(page, len(ul))
        
        for li in ul:
            detail_href = li['href']
            image = 'http:'+li.select_one('img')['src'].replace('210x','420x')
            
            detail = {
                'url' : detail_href,
                'gender' : gender,
                'type' : type_,
                'images' : image,
            }

            with open(f'./puma_{gender}_{type_}_href_images.csv', 'a') as csvfile:
                fieldnames = detail.keys()
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvwriter.writerow(detail)

        if len(ul)<16:
            break
        page+=1

ctgr_list = [392, 161, 238, 44, 42,46,545,45,160, 391, 20, 18,22,21]
    
for ctgr in ctgr_list:
    if ctgr in [392, 161, 238, 44, 42]:
        gender = 'W'
        type_ = 'TOP'
    elif ctgr in [46,545,45]  :
        gender = 'W'
        type_ = 'BOTTOM'   
    elif ctgr in [160, 391, 20, 18]:
        gender = 'M'
        type_ = 'TOP'
    elif ctgr in [22,21]:
        gender = 'M'
        type_ = 'BOTTOM'

    get_href(ctgr, gender, type_)