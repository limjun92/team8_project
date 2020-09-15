from bs4 import BeautifulSoup
import requests
import time
import re
import csv
import pandas as pd
import json


# 상품별 id얻기
def get_href(shop_name, category): 
    prod_id_list = []
    page = 1
    while True:
        url = f'https://smartstore.naver.com/{shop_name}/category/{category}?page={page}&st=RECENT&dt=IMAGE&size=40&free=false&cp=1'
        # print(url)
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content.decode('utf-8', 'replace'), 'html.parser')
        
        ul = soup.select('div.module_list_product_default.extend_five.extend_thumbnail_square > ul.list > li.item')
        # print(page, len(ul))
        for li in ul:
            prod_id = li.select_one('a')['href'].split('/')[-1]
            prod_id_list.append(prod_id)

        if len(ul) < 40: # 원래 총 40개씩 보여주는데 그 이하로 보여주면 마지막 페이지.
            return prod_id_list

        page += 1


# 상품 디테일 리스트 생성
def get_detail(shop_name, prod_id_list, gender, category): 
    for prod_id in prod_id_list:
        # print(prod_id)
        headers = {
            'authority': 'smartstore.naver.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',

        }
        url = f'https://smartstore.naver.com/{shop_name}/products/{prod_id}'
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.content.decode('utf-8', 'replace'), 'html.parser')
        
        
        p = re.compile("\"originalProductNo\" : \".+")
        matched = p.search(response.text).group()
        original_num = matched.split(':')[1].split("\"")[1]
        
        name = soup.select_one('#wrap > div > div.prd_detail_basic > div.info > form > fieldset > div._copyable > dl > dt > strong').getText()
        price = soup.select_one('#wrap > div > div.prd_detail_basic > div.info > form > fieldset > div._copyable > dl > dd > div.area_cost > strong > span.thm').getText()
              
        
        thumbnail = soup.select_one('#wrap > div > div.prd_detail_basic > div._image.view > div.bimg > div.img_va > img')["src"]
        image_list = [thumbnail]
        ul = soup.select('#wrap > div > div.prd_detail_basic > div._image.view > div._thumbnail_area.thmb_lst.more > span > img')
        
        for li in ul[1:]:
            image_list.append(li["src"].replace('f40','m510'))

        detail = {
            'link' : url,
            'prod_id' : prod_id,
            'original_num' : original_num,
            'name' : name,
            'price':price,
            'gender' : gender,
            'category' : category,
            'img_list' : image_list
        }


        # 오류가 나서 다시 시작할 땐 해당 파일 지우고 시작하기!!!!!
        with open(f'./{shop_name}_{gender}_{category}_detail.csv', 'a') as csvfile: #'쇼핑몰 이름_성별_카테고리_detail.csv'라는 이름으로 파일 생성
            fieldnames = detail.keys()
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writerow(detail)

# 상품별 리뷰 리스트 생성
def get_review(shop_name, prod_id, original_num, gender, category):

    page = 0

    while True:
        page += 1 # 페이지 1부터 시작해서 더 이상 페이지에 내용이 없을 때까지 루프
        headers = {
            'authority': 'smartstore.naver.com',
            'charset': 'utf-8',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://smartstore.naver.com/{shop_name}/products/{prod_id}',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        params = (
            ('page', page),
            ('size', '20'),
            ('sortType', 'REVIEW_RANKING'),
            ('contentType', 'ALL'),
            ('topicCode', ''),
        )

        response = requests.get(f'https://smartstore.naver.com/{shop_name}/products/{original_num}/reviews/page.json', headers=headers, params=params)


        soup = BeautifulSoup(response.content.decode('utf-8', 'replace'), 'html.parser')
        # print(soup) # 페이지 자체가 잘 불러와지는지 확인
        soup_dict=json.loads(str(soup))['htReturnValue']['pagedResult']['content']
        # print(soup_dict) # 리뷰가 포함된 부분 잘 불러와지는지 확인
        if soup_dict == []: # 리뷰가 더 이상 없는 경우 종료.
            break
            
        for rev in soup_dict:
            try:
                image = rev['resources'][0]['resourceUrl']
            except IndexError:
                image = None
                
            rev_id = rev['id']
            
            review = {
                'prod_id' : prod_id,
                'original_num':original_num,
                'id' : rev['id'],
                'score' : rev['reviewScore'],
                'writer' : rev['writerId'],
                'date' : rev['createdDate'],
                'contents' : rev['contents'],
                'images' : image,
            }
            
            # 오류가 나서 다시 시작할 땐 해당 파일 지우고 시작하기!!!!!
            with open(f'./{shop_name}_{gender}_{category}_review.csv', 'a',encoding='UTF-8',) as csvfile:
                fieldnames = review.keys()
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvwriter.writerow(review)


shop_name = 'greenwich'
category = '21843c727a2c462b9edc402b7322e22b'
gender = 'W'

prod_id_list = get_href(shop_name, category)
print('# 상품 id 리스트 생성 완료')

get_detail(shop_name, prod_id_list, gender, category)
print('# 상품 detail 리스트 생성 완료')

df = pd.read_csv(f'./{shop_name}_{gender}_{category}_detail.csv', encoding='cp949',names=['link','prod_id','original_num','name','price','gender','category','img_list'])
detail_df = df.iloc[:,1:3]
print('# review에 필요한 id 추출')

for index, line in detail_df.iterrows():
    prod_id, original_num = line.values
    # print(prod_id)
    get_review(shop_name, str(prod_id), str(original_num), gender, category)
print('# 상품 review 리스트 생성 완료')