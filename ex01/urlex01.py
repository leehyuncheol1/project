import requests
url = 'https://medium.com/museion/%ED%81%AC%EB%A1%A4%EB%9F%AC-%EB%A7%89%EA%B8%B0-5c24f20024c5'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
res_data = requests.get(url, headers=headers)

res_data.raise_for_status() #접근에 문제가 있을경우  익셉션을 발생시키고 프로그램 종료
#res_data = requests.get(url)
# if res_data.status_code == requests.codes.OK:
#     print("정상적으로 처리되는 내용")
#     pass
# else:
#     print("크롤링 실패 ")
#효과적인 크롤링을 위해서는 정규표현식을  사용할줄 알아야 한다
