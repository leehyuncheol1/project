import selenium 
from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument('====start-maximized')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches",["enable-logging"])

driver = wb.Chrome(options=options)
driver.get("https://comic.naver.com/index") 
webmain = driver.find_element(By.XPATH,f'//*[@id="menu"]/li[i]/a')
print(webmain.text)

for i in range(1, 6):  # Replace 6 with the actual number of elements you want to iterate over
    xpath = f'//*[@id="menu"]/li[{i}]/a'
    webmain = driver.find_element(By.XPATH, xpath)
    print(f"Element at index {i}: {webmain.text}")

    driver.quit()



try :
    driver.get("https://comic.naver.com/index")   
    elems = driver.find_elements("class name","rankingnews_box")   

    for elem in elems:
       name = elem.find_element("class name", "rankingnews_name")  
       tex = elem.find_element("class name","rankingnews_list")
       print(tex.text, end='')
    input()     
except Exception as e:
    print(e)