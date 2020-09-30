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

def get_href(ctgr, gender, type_):
    page = 1
    href = []
    breaker = False

    while True:
        print(page)
        url = f'https://www.fila.co.kr/product/list.asp?no={ctgr}&gender=&page={page}&sortVal=1&colorVal=0&priceVal=0&sizeVal=0'
        res = requests.get(url)

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
        ul = soup.select('ul#productList > li')
        
        for li in ul:
            if li.get('data-val') == '1':
                detail_href = 'https://www.fila.co.kr' + li.select_one('a')['href']
                if detail_href in href:
                    breaker = True
                    break
                href.append(detail_href)
                image = 'https:' +  li.select_one('a > div > img')['src']
                print(image)
                detail = {
                    'url' : detail_href,
                    'gender' : gender,
                    'type_' : type_,
                    'images' : image,
                    
                }

                with open(f'./fila_{gender}_{type_}_href_images.csv', 'a') as csvfile:
                    fieldnames = detail.keys()
                    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    csvwriter.writerow(detail)

        if breaker == True:
            break

        page+=1

ctgr_list = [912, 804, 806, 805, 807, 808, 809, 810]
top = [912, 804, 806, 805, 807, 808]
bottom = [809, 810]
for ctgr in ctgr_list:
    if ctgr in top:
        gender = 'M'
        type_ = 'TOP'
    else:
        gender = 'M'
        type_ = 'BOTTOM'

    get_href(ctgr, gender, type_)


