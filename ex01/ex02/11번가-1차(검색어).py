import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import openpyxl
import re

def is_valid_search_query(query):
    # Check if the query has no spaces and is a combination of English letters, numbers, and Korean characters
    return ' ' not in query and bool(re.match('^[a-zA-Z0-9ㄱ-ㅎㅏ-ㅣ가-힣]+$', query))

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(options=options)

def search_and_scrape(driver, search_query):
    data = []  # data 변수 정의
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = '11번가 상품 정보'

    try:
        if is_valid_search_query(search_query):
            driver.get('https://www.11st.co.kr/')

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tSearch"]/form/fieldset/input')))
            search_input = driver.find_element(By.XPATH, '//*[@id="tSearch"]/form/fieldset/input')

            # Use the search query directly
            ActionChains(driver).send_keys_to_element(search_input, search_query).perform()

            ActionChains(driver).send_keys(Keys.ENTER).perform()

            # Wait for the search results to load
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'c-card-item')))

            # Extract product data
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            product_items = driver.find_elements(By.CSS_SELECTOR, '#section_commonPrd .c-card-item')

            if product_items:
                for item in product_items:
                    # Extract product information
                    pName = item.find_element(By.CLASS_NAME, 'c-card-item__name').text.strip('상품명\n')


                    pPrice = item.find_element(By.CLASS_NAME, 'c-card-item__price').text.strip('~')
                    pPrice = pPrice.replace(',', '').strip('원')

                    
                    pDelivery_fee = ''
                    pDelivery_date = ''
                    pDelivery = item.find_element(By.CLASS_NAME, 'c-card-item__delivery').text

                    if pDelivery != '배송':
                        pDelivery = pDelivery.split('\n')
                        pDelivery_fee = pDelivery[1].strip('배송비 ')
                        pDelivery_date = '' if len(pDelivery) < 3 else pDelivery[2]

                    pUrl = item.find_element(By.CLASS_NAME, 'c-card-item__anchor').get_attribute("href")
                    pImgUrl = item.find_element(By.CSS_SELECTOR, '.c-lazyload.c-lazyload--ratio_1x1 img').get_attribute("src")

                    data.append([pName, pPrice, pDelivery_date, pDelivery_fee, pUrl, pImgUrl])

                # Save the data to Excel
                ws.append(['Product Name', 'Price', 'Delivery Date', 'Delivery Fee', 'URL', 'Image URL'])
                for product_info in data:
                    ws.append(product_info)

                wb.save('11st_product_info.xlsx')
                print("Data extraction and saving completed.")

            else:
                print("No data found. Please check the HTML structure.")

        else:
            print("Invalid search query. Please provide a valid search term.")

    except Exception as e:
        print(f"An exception occurred: {e}")

    finally:
        wb.save('11st_product_info.xlsx')
        print("Program execution completed.")

# 검색어 입력
search_query = input('검색할 단어 : ')

# 드라이버 초기화 및 함수 호출
driver = initialize_driver()
search_and_scrape(driver, search_query)