from selenium import webdriver
import time
import csv
import pandas as pd
# 환경 변수로 등록한 경우
# driver = webdriver.PhantomJS()
# 절대 경로로 실행시킬 경우

driver = webdriver.Chrome("./chromedriver.exe")

# ctgrs = driver.find_elements_by_css_selector('div.f-cagetory-sect.borderline-top > ul#category-filter-list > li > a')
# for ctgr in ctgrs:
#     if len(ctgr.text) != 0:
#         if ctgr.text in ['후디 & 크루','후디','']
#         print(ctgr.text, ctgr.get_attribute('href'))

top=['hoodies-crews','hoodies','nike-pro-compression-shirts']
bottom=['shorts','nike-pro-compression-bottom']

for ctgr in top:
    driver.get('https://www.nike.com/kr/ko_kr/w/men/ap/'+ctgr)
    time.sleep(3)

    inner=driver.find_element_by_css_selector("div.a-product-image-primary > img")
    print(inner)

driver.quit()

