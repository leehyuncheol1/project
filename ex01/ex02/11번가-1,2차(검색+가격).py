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
    return bool(re.match('^[a-zA-Z0-9ㄱ-ㅎㅏ-ㅣ가-힣]+$', query))

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(options=options)

def search_and_scrape(driver, search_query, price_query):
    data = []  
    total_price = 0  
    count = 0  

    try:
        driver.get('https://www.11st.co.kr/')

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tSearch"]/form/fieldset/input')))
        search_input = driver.find_element(By.XPATH, '//*[@id="tSearch"]/form/fieldset/input')

        if is_valid_search_query(search_query):
            ActionChains(driver).send_keys_to_element(search_input, search_query).perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
        else:
            print("Invalid search query. Please use a combination of English letters, numbers, and Korean characters.")
            return

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'c-card-item')))
        time.sleep(2)

        current_page = 1
        max_pages = 3  

        while current_page <= max_pages:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            product_items = driver.find_elements(By.CSS_SELECTOR, '#section_commonPrd .c-card-item')

            for item in product_items:
                try:
                    WebDriverWait(item, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'c-card-item__name')))
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

                    split_price = price_query.split('-')

                    if int(split_price[0]) <= int(pPrice) <= int(split_price[1]):
                        data.append([pName, pPrice, pDelivery_date, pDelivery_fee, pUrl, pImgUrl])

                        print("상품명: " + pName)
                        print('--------------------')
                        total_price += int(pPrice)
                        count += 1

                except Exception as e:
                    print(f"Error processing item: {e}")

            next_page_button_xpath = f'//*[@id="section_commonPrd"]/nav/ul/li[{current_page + 1}]/button'
            next_page_button = driver.find_element(By.XPATH, next_page_button_xpath)

            if "disable" not in next_page_button.get_attribute("class"):
                next_page_button.click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'c-card-item')))
                time.sleep(2)
            else:
                print(f"Next page button for page {current_page + 1} is disabled. Exiting loop.")
                break

            current_page += 1

        if not data:
            print("No data found. Please check the HTML structure")
        else:
            average_price = total_price / count
            print(f"Average Price: {average_price}")

            price_range_min = average_price * 0.5
            price_range_max = average_price * 1.5

            filtered_data = [product for product in data if price_range_min <= int(product[1]) <= price_range_max]

            if not filtered_data:
                print("No data found within the specified price range.")
            else:
                wb_filtered = openpyxl.Workbook()
                ws_filtered = wb_filtered.active
                ws_filtered.title = 'Filtered Products'
                ws_filtered.append(['Product Name', 'Price', 'Delivery Date', 'Delivery Fee', 'URL', 'Image URL'])

                for product in filtered_data:
                    ws_filtered.append(product)

                wb_filtered.save('filtered_11st_product_info.xlsx')

    finally:
        input()
        driver.quit()

search_query = input('검색할 단어: ')
price_query = input('금액 범위(ex 4000-10000): ')

driver = initialize_driver()
search_and_scrape(driver, search_query, price_query)