from selenium import webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import re
import openpyxl
import time

options = Options()
options.add_argument('--start-maximized')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# WebDriver 인스턴스 생성
driver = webdriver.Chrome(options=options)
try:
    driver.get('https://www.hira.or.kr/main.do')

    mainclick = driver.find_element(By.XPATH, '//*[@id="shortcut01"]/ul/li[2]/a').click()
    driver.implicitly_wait(2)
    titleclick = driver.find_element(By.XPATH, '//*[@id="uuid-1j"]').click()
    popclick = driver.find_element(By.XPATH, '//*[@id="uuid-tj"]/div/div/div/div[1]/div')
    driver.implicitly_wait(2)
    time.sleep(3)
    if popclick:
        popclick = driver.find_element(By.XPATH, '//*[@id="uuid-tj"]/div/div/div/div[1]/div').click()
        popclick1 = driver.find_element(By.XPATH, '//*[@id="uuid-tl"]/div/div/div/div/div[1]/div').click()
        popclick2 = driver.find_element(By.XPATH, '//*[@id="uuid-tm"]/div').click()
    else:
        print('팝업이 없습니다.')
    selectDo = driver.find_element(By.XPATH,'//*[@id="uuid-ip"]/div/div[2]').click()  
    Doclick = driver.find_element(By.ID,'pt-ip/i7').click()
    selectSigun = driver.find_element(By.XPATH, '//*[@id="uuid-iq"]/div/div[2]').click()
    PDselect = driver.find_element(By.XPATH,'//*[@id="uuid-iq"]/div/div[1]')
    PDselect.send_keys(Keys.PAGE_DOWN,Keys.PAGE_DOWN,Keys.PAGE_DOWN)
    
    siclick = driver.find_element(By.ID,'pt-iq/i17').click()
    selectgu = driver.find_element(By.XPATH, '//*[@id="uuid-ir"]/div/div[2]').click()
    PDselect = driver.find_element(By.XPATH,'//*[@id="uuid-ir"]/div/div[1]')
    
    #PDselect.send_keys(Keys.PAGE_DOWN,Keys.PAGE_DOWN,Keys.PAGE_DOWN,Keys.PAGE_DOWN)
    # sendkeys를 여러번 입력하면 웹브라우저에서 중복된 키 입력을 무시하는 경우가 있다.
    PDselect.send_keys(Keys.PAGE_DOWN)
    PDselect.send_keys(Keys.PAGE_DOWN)
    PDselect.send_keys(Keys.PAGE_DOWN)
    PDselect.send_keys(Keys.PAGE_DOWN)
    guclick = driver.find_element(By.ID,'pt-ir/i17').click()
    inputHospital = driver.find_element(By.XPATH,'//*[@id="uuid-j3"]/div/div[1]/input').send_keys("정형외과")
    phsioclick = driver.find_element(By.XPATH,'//*[@id="uuid-j9"]/div/div/div[2]/div[5]/div/div[1]/div/div').click()
    dosuclick = driver.find_element(By.XPATH,'//*[@id="uuid-y5"]/div/div/div[1]/div/div/div[2]/div[5]/div/div[2]').click()
    acceptclick = driver.find_element(By.XPATH,'//*[@id="uuid-ya"]/div/a/div').click()
    checkboxclick = driver.find_element(By.XPATH,'//*[@id="uuid-k8"]/div/div/div[3]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div/div/span').click()
    boxclick = driver.find_element(By.XPATH,'//*[@id="uuid-jr"]/div').click()
    time.sleep(3)
    Alert(driver).accept()
    fpath = r'C:\Users\SAMSUNG\Desktop\교육자료\교육사업\글로벌직업전문학교 24년1월\의료기관정보조회.xlsx'

    workbook = openpyxl.load_workbook(fpath)
    sheet = workbook['의료기관 정보조회']
    original_char = 'A'

    boxresult = driver.find_element(By.XPATH,'//*[@id="uuid-js"]/div/a').click()
    for i in range(1, 9):
        xpath = f'//*[@id="uuid-122"]/div/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div[{i}]/div[2]/div/div/div'
        new_char = chr(ord(original_char) + i)
        element = driver.find_element(By.XPATH, xpath)
        print(element.text)
        sheet['A' + str(i+1)] = element.text 
                                   
        for j in range(1,7):
            new_char = chr(ord(original_char) + j)
            xpath1 = f'//*[@id="uuid-122"]/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div/div[{i}]/div[{j}]/div/div/div'
            element1 = driver.find_element(By.XPATH, xpath1)
            sheet[new_char + str(i+1)] = element1.text 
            
            print(element1.text) 
          
    workbook.save(fpath)

              

    
    
except Exception as e:
    print(e)
finally:
    driver.quit()
    #print(e)
    