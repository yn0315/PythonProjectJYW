import socketserver
import threading
import datetime
import time
import pymysql
import pickle
#import chromedriver_autoinstaller # chrome driver 자동 설치 라이브러리
from selenium import webdriver
from selenium.webdriver.common.by import By

HOST = '192.168.0.2' # 서버의 ip를 열음. (이 서버의 ip로 클라이언트가 접속을 해야 한다), 그전에 ping을 먼저 확인하도록.
PORT = 9999          # 포트번호 (같아야 함)
lock = threading.Lock()  # syncronized 동기화 진행하는 스레드 생성

#chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions() # Browser 세팅하기
options.add_argument('lang=ko_KR') # 사용언어 한국어
options.add_argument('disable-gpu') # 하드웨어 가속 안함

driver = webdriver.Chrome(options=options)
driver.get("https://kr.louisvuitton.com/kor-kr/men/ready-to-wear/shirts/_/N-t1wtp7cj?page=3")
# driver.get("https://www.musinsa.com/categories/item/003?d_cat_cd=003&brand=&list_kind=small&sort=sale_high&sub_sort=1y&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=")
driver.implicitly_wait(1)
topname = driver.find_element(By.ID,value='product-1AB6I2')
# topprice = driver.find_elements(By.CLASS_NAME,value='li_inner .price')

print(topname)
# eun=driver.find_element(By.ID,value="searchList")
# print(eun)
# print(eun.get_dom_attribute("class"))
# print(eun.get_attribute('attr'))
# e2=driver.find_element(By.XPATH,value='/html/body/div[2]/div[3]/div[11]/div[1]/div[1]/div[2]/div[3]/ul/li[8]').text
#driver.execute_script("")
# print(e2)
# for i in range(10):
#     a = '/ html / body / div[2] / div[3] / div[11] / div[1] / div[1] / div[2] / div[3] / ul / li['+str(i+1)+']/div[4]/div[2]/p[2]/a'
#     eunprice=driver.find_element(By.XPATH,value=a)
#     print(eunprice.text)
#/html/body/div[2]/div[3]/div[11]/div[1]/div[1]/div[2]/div[3]/ul/li[3]/div[4]/div[2]/p[2]/a
#/html/body/div[2]/div[3]/div[11]/div[1]/div[1]/div[2]/div[3]/ul/li[ +  VAR +'  ]/div[4]/div[2]/p[2]/a'

TOP100name = []
TOP100price = []
TOP100name.append(topname.get_property(name='a'))
# for i in range(len(topname)-1):
#     TOP100name.append(topname[i].get_property(name='a'))
# for i in range(90):
#     TOP100name.append(topname[i].get_property(name='title'))
#     a = topprice[i].text.split(' ')
#
#     if len(a) == 2: # or len(a) == 1:
#         del a[0]
#         TOP100price.append(a)
#     else:
#         pass

for i in TOP100price:
    pass

print(TOP100name)
print(TOP100price)