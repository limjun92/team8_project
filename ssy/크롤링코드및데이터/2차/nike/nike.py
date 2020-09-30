from selenium import webdriver
import time
import csv
import pandas as pd
# 환경 변수로 등록한 경우
# driver = webdriver.PhantomJS()
# 절대 경로로 실행시킬 경우
import datetime
    
def doScrollDown(whileSeconds):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=whileSeconds)
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)
        if datetime.datetime.now() > end:
            break
from selenium.webdriver.common.keys import Keys

def scroll():
    body = driver.find_element_by_css_selector('body')
    for i in range(50):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

driver = webdriver.Chrome("../chromedriver.exe")



shop_name = 'nike'
# top = ['01002002002008', '01002002002005', '01002002002004', '01002002002003', '01002002002001', '01002002002018', '01002002002017']     
# bottom = ['01002002002009', '01002002002014', '01002002002016']
# gender = 'W'
top = ['hoodies-crews', 'jackets-vests', 'tops-tshirts']
bottom = ['pants-tights', 'shorts']
gender = 'M'

df = pd.DataFrame()
for ctgr in top:
    page = 0
    type_='T'

    
    driver.get(f"https://www.nike.com/kr/ko_kr/w/men/ap/{ctgr}?sort=price%20desc")
    time.sleep(30) # 접속하는 동안 대기

    # 무한스크롤
    # from selenium.webdriver import ActionChains

    # # id가 something 인 element 를 찾음
    # some_tag = driver.find_element_by_id('something')

    # # somthing element 까지 스크롤
    # action = ActionChains(driver)
    # action.move_to_element(some_tag).perform()

    # print(driver.page_source) # 해당 페이지 전체 HTML 반환
    print(f'-------------------------------------{ctgr}:page{page}------------------------------------')

    inner=driver.find_elements_by_css_selector("div.ncss-container > ul > li") # bs4 기능 일부 지원
    print(len(inner))
    if len(inner)==0:break

    for prod in inner:
        
        href = prod.find_element_by_css_selector("div > div.a-product-image.item-imgwrap.action-hover > a").get_attribute('href')
        img = prod.find_element_by_css_selector("div.a-product-image-primary > img").get_attribute('src')
        price = prod.find_element_by_css_selector('div.product-price.ta-md-r > p').text
        print(href)
        # print(img)
        # print(price)
        detail = [[shop_name, href, price, img]]
        df = df.append(detail)
    df.to_csv(f'./{shop_name}_{ctgr}_{page}_{gender}_{type_}.csv')
    



driver.quit()

