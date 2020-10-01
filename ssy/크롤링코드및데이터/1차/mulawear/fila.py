import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_href(ctgr_list, gender, type_):
    df = pd.DataFrame()
    df2 = pd.DataFrame()
    for ctgr in ctgr_list:

        page = 1
        href = []
        breaker = False
        print(f'<<<<<<<<<<<<<<<<{ctgr}>>>>>>>>>>>>')
        while True:
            print(f'---------------{page}----------------')
            url = f'https://www.fila.co.kr/product/list.asp?no={ctgr}&gender=&page={page}&sortVal=1&colorVal=0&priceVal=0&sizeVal=0'
            res = requests.get(url)

            soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
            ul = soup.select('ul#productList > li')
            print(len(ul))
            for li in ul:
                if li.get('data-val') == '1':
                    name = li.select_one('div.name').text.strip()
                    detail_href = 'https://www.fila.co.kr' + li.select_one('a')['href']
                    if detail_href in href:
                        breaker = True
                        break
                    href.append(detail_href)
                    image = 'https:' +  li.select_one('a > div > img')['src'].replace('/a/2/','/a/4/')
                    
                    try:
                        price = li.select_one('span.no-sale').text
                    except:
                        price = li.select_one('span.normal').text
                    price = ''.join(price.split('원')[0].split(','))
                    
                    # if ('레깅스' in name) | ('숏레깅스' in name) | ( '쇼츠' in name):
                    #     type_ = 'bottom'
                    #     detail = [['fila',gender,  type_, detail_href, price, image]]
                    #     df2 = df2.append(detail)
                    # else:
                    #     type_ = 'top'
                    #     detail = [['fila',gender,  type_, detail_href, price, image]]
                    #     df = df.append(detail)
                    detail = [['fila',gender,  type_, detail_href, price, image]]
                    df = df.append(detail)

            if breaker == True:
                print('break')
                break

            page+=1

    df.to_csv(f'./fila_{gender}_{type_}.csv')
    # df.to_csv(f'./fila_{gender}_{type_}_탑.csv')
    # df2.to_csv(f'./fila_{gender}_{type_}_레깅스.csv')
    
top = [912, 804, 806, 805, 807, 808]
bottom = [809, 810]
get_href(top, 'man', 'top')
get_href(bottom, 'man', 'bottom')
top = [913, 830, 832, 831, 833, 834]
bottom = [835, 836]
get_href(top, 'woman', 'top')
get_href(bottom, 'woman', 'bottom')


# get_href([837], 'woman', 'top')

#837 손보기!!!!!!!!!!