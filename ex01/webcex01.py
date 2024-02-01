import requests 
from bs4 import BeautifulSoup
import time #=> option 이기때문에 다른 라이브러리로 대치 할 수 있다

#time.sleep(5) # 웹크롤링에서는 서버에서 완전하게 데이터를 전달 받을수 있도록 지연시킬 필요가 있음.
useraentvalue = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
#searchlist = ['new', 'genre']
#for search in searchlist:
#url= 'https://comic.naver.com/index' 
url= "https://news.naver.com/" 
res = requests.get(url, headers=useraentvalue)
res_data = requests.get(url, headers=useraentvalue)
res_data.raise_for_status() # requests 를 사용하면 반드시 들어가는 구문
soup = BeautifulSoup(res.text, 'lxml')

#seldiv = soup.find_all( "div" , attrs={'class' : 'cjs_news_tw'})
seldiv = soup.select('div.cjs_news_tw')
print(seldiv)
for seldata in seldiv:
    print("===================================")
#    print( seldata.prettify())
    eletitle =  seldata.div
    elecon = seldata.p
    # #titleinfo 와 conInfo를 persistence(excel, db, textfile)에 저장 시킨다
    print(" title내용  :" , eletitle.get_text() )
    print(" con내용  :" , elecon.get_text() )
    print("elecon요소의  속성값", elecon['class'][0])

sellink = soup.append
print("===============>", sellink['href'], type(sellink['href']) )    