import requests 
from bs4 import BeautifulSoup
import time 

useraentvalue = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

url= "https://search.shopping.naver.com/search/all?adQuery=%EC%BB%B4%ED%93%A8%ED%84%B0&frm=NVSHATC&origQuery=%EC%BB%B4%ED%93%A8%ED%84%B0&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%BB%B4%ED%93%A8%ED%84%B0&sort=price_asc&timestamp=&viewType=list" 
res = requests.get(url, headers=useraentvalue)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
pricelist = soup.select('.price_num_S2p_v')
for pricedata in pricelist:
    comprice = pricedata.em.get_text()
    print( comprice)