import requests   #서버에 요청하는 것    html파일을 가져오는 것은 request객체
from bs4 import BeautifulSoup       #가져온 텍스트파일에서 데이터를 추출하는 것
import csv  #csv에 저장을 위해서  (csv가 엑셀이며 csv로 만들고 엑셀에서 불러올 수 있다) -> 반드시 엑셀로 넣을 필요가 없다.
import time  #시간을 지연시킬 상황이 필요할 때 
#import os, sys #, os를 통해 폴더도 만들고, 지우고, 이름도 바꾸고 등등, sys는 환경변수의 값을 얻어오고자 할 때
#import 긴모듈명 as a,  긴모듈명 as b    =>이런식으로 별명을 한 번에 나타낼 수 있음

danlist = ['','','','','','','','','','','','단위(억)']
title_list = 'N          종목명     현재가     전일비     등락률     액면가     시가총액       상장주식수     외국인비율     거래량     PER     ROE     토론실'.split("\t")
f= open('주식 시총200.csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f, delimiter=',')
writer.writerow(title_list)
writer.writerow(danlist)

for i in range(1,200//50+1):
    url="https://finance.naver.com/sise/sise_market_sum.naver?&page=" + str(i)
    # url=f"https://finance.naver.com/sise/sise_market_sum.naver?&page={i}" 
    # url="https://finance.naver.com/sise/sise_market_sum.naver?&page={}" .format(i)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)   #주소에 있는 데이터를 가져오는데 헤더값으로 준 것으로 넘어가면서 가져오도록 한다   --프로그램으로 접근하면은 차단을 당할 수 있으니 브라우저가 접속한 것처럼 헤더값을 바꿔주는 것
    #print(res.text)   # 가져온 res(객체)데이터(정적인 문서)를 beautifulsoup에 넘겨주며 쉽게 사용할 수 있도록
    res.raise_for_status() #에러가 발생하면 익셉션 발생시키고 끝내라
    #print(r'D:\zeromo\workspace\pythonws\ex03\webcex02.py')  #경로 안에 \가 붙어있는 문자열이 있다면 역슬래시를 하나 더 붙이거나  r을 붙이도록

    soup = BeautifulSoup(res.text,'lxml')
    rows = soup.find('table' ,attrs={'class':'type_2'}).find('tbody').find_all('tr') # find_all 또는 find에서첫 번째로는 태그이름을 준다 , attrs는 객체형태로 주도록 한다
  
   # print(title_list)

    print("가져온 행의 수 : " , len(rows))
    for row in rows :
        columns = row.find_all('td')
        if len(columns) <= 1 :    #내용물이 없는 행일경우 반복문 처음으로 넘어가라    (불필요한 자료 제거해주는 필터링 작업)
            continue
        data_list =[] 
        for column in columns : 
            get_text = column.get_text() #선택한 요소(element) 안에 text[node]를 얻는 것
            data_list.append(get_text.strip()) #가져온 문자열을 list에 추가한다.   (strip을 사용하여 불필요한 공백 제거 => 필터링 작업)

    # print(data_list)
        writer.writerow(data_list)
