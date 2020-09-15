import requests
import csv
from bs4 import BeautifulSoup
import pandas as p
import os


def get_href():
    ctgr_list = ['41','17','25','50']
    # 41:여성의류, 17:남성의류, 25:남성etc, 50:여성etc
    for ctgr in ctgr_list:
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
                    'images' : image
                }

                with open('./puma_href_images.csv', 'a') as csvfile:
                    fieldnames = detail.keys()
                    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    csvwriter.writerow(detail)
            if len(ul)<16:
                break
            page+=1

file = './puma_href_images.csv'
if os.path.isfile(file):
    os.remove(file)
get_href()