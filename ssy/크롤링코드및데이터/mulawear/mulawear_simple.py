import requests
import csv
from bs4 import BeautifulSoup
import pandas as p
import os

detail_href = []
xcode = ['012','009','010','007','019']
# 여성 상의 012
# 남성 상의 010
# 여성 하의 009
# 남성 하의 007
# 기타 019

def get_href():
    xcode_list = ['012','009','010','007','019']
    for xcode in xcode_list:
        print(xcode)
        page = 1
        while True:
            print(page)
            url = f'http://www.mulawear.com/shop/shopbrand.html?type=Y&xcode={xcode}&sort=&page={page}'
            res = requests.get(url)

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('div.useBannerPrdCont > dl.item-list')
            if len(ul)==0:
                break
            
            for li in ul:
                detail_href = 'http://www.mulawear.com' + li.select_one('a')['href']
                image = li.select_one('a > img')['src']
                
                detail = {
                    'url' : detail_href,
                    'images' : image
                }

                with open('./mulawear_href_images.csv', 'a') as csvfile:
                    fieldnames = detail.keys()
                    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    csvwriter.writerow(detail)
            page+=1

file = './mulawear_href_images.csv'
if os.path.isfile(file):
    os.remove(file)
get_href()