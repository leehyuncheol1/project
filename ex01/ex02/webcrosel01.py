from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})
browser.get("https://www.coupang.com/")
browser.page_source
elem = browser.find_element(By.ID,'headerSearchKeyword')
time.sleep(3)
elem.send_keys("고구마")
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '#headerSearchBtn').click()

# 10번 라인부터 14번 라인까지 하나의 명령으로 만듬(동작 하지 않을수 있음 네트워크나 속도 문제등)
#browser.find_element(By.ID,'headerSearchKeyword').send_keys("고구마").send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="searchSortingOrder"]/ul/li[2]/label').click() # 저가 가격순으로 정렬된 상태

# 현재 페이지에서 데이터 추출이 완료된다면 
#1. beautifulsoup 을 이용=> browser.page_source
#2. browser.get 을 새롭게 현재 url을 가져오는 방법
titles = []
price = []
ar_date = []
# N페이지 만큼 반복문이 들어간다
url = 'https://www.coupang.com/np/search?rocketAll=false&searchId=aefc854d7fd842d2a609459b16352a98&q=%EA%B3%A0%EA%B5%AC%EB%A7%88&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=87570&component=&rating=0&sorter=salePriceAsc&listSize=36'

browser.get(url)
elems = browser.find_elements(By.CSS_SELECTOR, '.search-product .name')
for index, elem in enumerate(elems):
    if index >= 12:
        break
    titles.append(elem.text)
elems = browser.find_elements(By.CSS_SELECTOR, '.search-product .price-value')
for index, elem in enumerate(elems):
    if index >= 12:
        break
    price.append(elem.text)
elems = browser.find_elements(By.CSS_SELECTOR, '.search-product .arrival-info')
for index, elem in enumerate(elems):
    if index >= 12:
        break
    ar_date.append(elem.text)    
print(titles,"\n", price, "\n",ar_date )        

input()
