from selenium import webdriver
import time
import csv
import pandas as pd
# 환경 변수로 등록한 경우
# driver = webdriver.PhantomJS()
# 절대 경로로 실행시킬 경우

driver = webdriver.Chrome("./chromedriver.exe")
# driver.get('https://shop.adidas.co.kr/PF020201.action?S_CTGR_CD=01001002002001&NFN_ST=Y')
# driver.get('https://shop.adidas.co.kr/PF020201.action?S_CTGR_CD=01002002002008&NFN_ST=Y')
# ctgrs = driver.find_elements_by_css_selector('#container_r > div > div.plp-contents.clfix > div.plp-navigation > div > div.filter_box.product_category.not_toggle.last > div.content > div > ul > li:nth-child(2) > div > ul > li:nth-child(2) > dl > dd > dl:nth-child(2) > dd > dl:nth-child(1) > dd > ul > li')
# top=[]
# bottom=[]
# for ctgr in ctgrs:
#     ctgr_id = ctgr.get_attribute('id').split('_')[-1]
#     ctgr_name = ctgr.text
#     if ctgr_name in ['수영복','언더웨어']:
#         pass    
#     elif ctgr_name in ['자켓','긴팔티셔츠','반팔티셔츠','민소매티셔츠','축구 저지','트랙탑','후디 / 스웨트셔츠']:
#         top.append(ctgr_id)
#     else:
#         bottom.append(ctgr_id)
# for ctgr in ctgrs:
#     ctgr_id = ctgr.get_attribute('id').split('_')[-1]
#     ctgr_name = ctgr.text
#     if ctgr_name in ['수영복']:
#         pass    
#     elif ctgr_name in ['스포츠브라','자켓','긴팔티셔츠','반팔티셔츠','민소매티셔츠','트랙탑','후디 / 스웨트셔츠']:
#         top.append(ctgr_id)
#     else:
#         bottom.append(ctgr_id)
shop_name = 'adidas'
# top = ['01002002002008', '01002002002005', '01002002002004', '01002002002003', '01002002002001', '01002002002018', '01002002002017']     
# bottom = ['01002002002009', '01002002002014', '01002002002016']
# gender = 'W'
top = ['01001002002001', '01001002002003', '01001002002004', '01001002002005', '01001002002013', '01001002002014', '01001002002016']
bottom = ['01001002002012', '01001002002015']
gender = 'M'
df = pd.DataFrame()
for ctgr in top:
    page = 0
    type_='T'
    while True:
        page += 1
        driver.get(f"https://shop.adidas.co.kr/PF020201.action?=&ALL=NONE&S_CTGR_CD={ctgr}&CONR_CD=10&S_ORDER_BY=1&S_PAGECNT=100&PAGE_CUR={page}&S_SIZE=&S_TECH=&S_COLOR=&S_COLOR2=&CATG_CHK=&CATG_CLK=&STEP_YN=N&S_QUICK_DLIVY_YN=&S_PRICE=&S_STATE1=&S_STATE2=&S_STATE3=&NFN_ST=Y")
        time.sleep(3) # 접속하는 동안 대기
        # print(driver.page_source) # 해당 페이지 전체 HTML 반환
        print(f'-------------------------------------{ctgr}:page{page}------------------------------------')

        inner=driver.find_elements_by_css_selector("div.inner") # bs4 기능 일부 지원
        if len(inner)==0:break

        for prod in inner:
            img = prod.find_element_by_css_selector("div.img > a > img").get_attribute('src').replace('230','720') 

            prod = prod.find_element_by_css_selector("div.info_wrapper > a ")
            prod_id=prod.get_attribute('href').split("'")[1]
            href = f'https://shop.adidas.co.kr/PF020401.action?PROD_CD={prod_id}'
            try:
                info_price=prod.find_element_by_css_selector("div.info_price > div.line").text # bs4 기능 일부 지원
            except:
                info_price=prod.find_element_by_css_selector("div.info_price").text

            detail = [[shop_name, href, info_price, img]]
            df = df.append(detail)
df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')
    


df = pd.DataFrame()
for ctgr in bottom:
    page = 0
    type_='B'
    while True:
        page += 1
        driver.get(f"https://shop.adidas.co.kr/PF020201.action?=&ALL=NONE&S_CTGR_CD={ctgr}&CONR_CD=10&S_ORDER_BY=1&S_PAGECNT=100&PAGE_CUR={page}&S_SIZE=&S_TECH=&S_COLOR=&S_COLOR2=&CATG_CHK=&CATG_CLK=&STEP_YN=N&S_QUICK_DLIVY_YN=&S_PRICE=&S_STATE1=&S_STATE2=&S_STATE3=&NFN_ST=Y")
        time.sleep(3) # 접속하는 동안 대기
        # print(driver.page_source) # 해당 페이지 전체 HTML 반환
        print(f'-------------------------------------{ctgr}:page{page}------------------------------------')

        inner=driver.find_elements_by_css_selector("div.inner") # bs4 기능 일부 지원
        if len(inner)==0:break

        for prod in inner:
            img = prod.find_element_by_css_selector("div.img > a > img").get_attribute('src').replace('230','720') 

            prod = prod.find_element_by_css_selector("div.info_wrapper > a ")
            prod_id=prod.get_attribute('href').split("'")[1]
            href = f'https://shop.adidas.co.kr/PF020401.action?PROD_CD={prod_id}'
            try:
                info_price=prod.find_element_by_css_selector("div.info_price > div.line").text # bs4 기능 일부 지원
            except:
                info_price=prod.find_element_by_css_selector("div.info_price").text

            detail = [[shop_name, href, info_price, img]]
            df = df.append(detail)
df.to_csv(f'./{shop_name}_{gender}_{type_}.csv')
    


driver.quit()

