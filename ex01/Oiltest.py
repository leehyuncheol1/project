from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import openpyxl
import re
import time

# Chrome WebDriver 옵션 설정
options = Options()
options.add_argument('--start-maximized')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# WebDriver 인스턴스 생성
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://www.opinet.co.kr/user/main/mainView.do')
    driver.implicitly_wait(10)

    # 원하는 지역 (경기도)를 선택
    element = driver.find_element(By.XPATH, '//*[@id="SIDO02_AVG_P"]')
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    oilprace = driver.find_element(By.XPATH, '//*[@id="sido_price1"]/span[1]').text
    ttprace = driver.find_element(By.XPATH, '//*[@id="oilcon1"]/div/dl[1]/dd/span[1]').text
    print(ttprace)
    print(oilprace)

    # 현재 유가 정보 text출력

    selectBox = driver.find_element(By.XPATH, '//*[@id="selected1"]')
    select = Select(selectBox)
    select.select_by_visible_text('수원시')
    select_option = select.first_selected_option
    suwon = select_option.text
    print(suwon)
    # 원하는 지역 셀렉트박스에서 선택

    praceSelect = driver.find_element(By.XPATH, '//*[@id="selected2"]')
    Praselect = Select(praceSelect)
    Praselect.select_by_visible_text('저가순')
    select_option_prace = Praselect.first_selected_option
    prace = select_option_prace.text
    print(prace)
    driver.implicitly_wait(10)
    # 원하는 지역의 저가순으로 변경

    prace_list = driver.find_element(By.XPATH, '//*[@id="os_t1"]/tbody')
    prace_texts = prace_list.find_elements(By.XPATH, './tr/td/a')
    for prace_text in prace_texts:
        text = prace_text.get_attribute('textContent')
        print(text)
    # 우리동네 싼 주유소 Top5 목록 가져오기
        
    fpath = r'C:\Users\user\Desktop\저가주유소.xlsx'

    workbook = openpyxl.load_workbook(fpath)
    sheet = workbook['저가주유소']
    sheet['B2'] = ttprace
    sheet['B3'] = oilprace

    row = len(prace_texts)
    for prace_text in prace_texts:
        text = prace_text.get_attribute('textContent')
        sheet['A' + str(row)] = text
        row += 1

    driver.find_element(By.XPATH, '//*[@id="os_t1"]/tbody/tr[1]/td[2]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="os_dtail_info"]/div[3]/a/img').click()

    area_oil = driver.find_element(By.XPATH, '//*[@id="body1"]')
       
    area_oil_pracelist = area_oil.find_elements(By.XPATH,'./tr/td[1]')
    area_oil_1_list = area_oil.find_elements(By.XPATH,'./tr/td[2]')
    area_oil_2_list = area_oil.find_elements(By.XPATH,'./tr/td[3]')

    row1  = len(prace_texts)-3
    for area_oil_prace,area_oil_1,area_oil_2 in zip(area_oil_pracelist,area_oil_1_list,area_oil_2_list):
        print(area_oil_prace.text, area_oil_1.text, area_oil_2.text)
    for area_oil_prace,area_oil_1,area_oil_2 in zip(area_oil_pracelist,area_oil_1_list,area_oil_2_list):
        text1 = area_oil_prace.get_attribute('textContent')
        text2 = area_oil_1.get_attribute('textContent')
        text3 = area_oil_2.get_attribute('textContent')
        sheet['D'+ str(row1)] = text1
        sheet['E'+ str(row1)] = text2
        sheet['F'+ str(row1)] = text3
        row1 += 1

    workbook.save(fpath)

    #input()    

except Exception as e:
    print(e)
finally:
    driver.quit()



