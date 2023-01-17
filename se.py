from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

url = 'https://www.melon.com'
driver.get(url)
# 키워드를 입력받아 검색창의 xpath에 send_keys 함수로 키워드 입력

#search_box = driver.find_element_by_css_selector('.rank_item .song a')
songname_xpath = driver.find_elements(By.CLASS_NAME,value='ellipsis.mlog')
for i in range(10):
    print(songname_xpath[i].get_property(name='title'))
#search_box2 = driver.find_element_by_css_selector('.rank_number nth7 .song a')



#print(search_box.text)
