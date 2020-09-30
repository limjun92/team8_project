import requests
import csv
from bs4 import BeautifulSoup
import pandas as p
import os

def get_href(ctgr, gender, type_):
    page = 1
    href = []
    breaker = False

    while True:
        print('page:',page)

        params = (
            ('psv', '20'),
            ('cno', ctgr),
            ('page', page),
        )

        res = requests.get('https://www.kappakorea.net/product/list.asp', params=params)

        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

        ul = soup.select('div.info > a')
        ul2 = soup.select('div.photo > img')

        if len(ul) == 0 :
            break

        for i in range(len(ul)):
            
            detail_href = 'https://www.kappakorea.net' + ul[i]['href']
            # if detail_href in href:
            #     breaker = True
            #     break
            # else:
                # href.append(detail_href)
            # print(href)
                
            image = 'https://www.kappakorea.net' + ul2[i]['src']
            
            detail = {
                'url' : detail_href,
                'gender' : gender,
                'type_' : type_,
                'images' : image,
                
            }

            with open(f'./kappa_{gender}_{type_}_href_images.csv', 'a') as csvfile:
                fieldnames = detail.keys()
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvwriter.writerow(detail)

        # if breaker == True:
        #     break

        page+=1


top = [104, 141, 106, 102, 110]
bottom = [107, 103]
ctgr_list = top + bottom
for ctgr in ctgr_list:
    if ctgr in top:
        gender = 'M'
        type_ = 'TOP'
    else:
        gender = 'M'
        type_ = 'BOTTOM'

    get_href(ctgr, gender, type_)


