from selenium import webdriver
import time
import csv
import pandas as pd


driver = webdriver.Chrome("./chromedriver.exe")
ctgr = '23'
page = 1

driver.get(f"http://www.launday.co.kr/product/list.html?cate_no={ctgr}&page={page}")
li = driver.find_elements_by_css_selector('li.xans-record-')
print(len(li))
for prod in li:
    # href = 'http://www.launday.co.kr/' + prod.find_element_by_css_selector('div.prdImg > a').get_attribute('href')
    href = prod.find_element_by_css_selector('div.thumbnail')
    # print(href)
    break

driver.quit()

