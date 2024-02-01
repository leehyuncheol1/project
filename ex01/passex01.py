# 텍스트 파일(exfile01.txt, exfile02.txt)에 안녕하세요 라는 내용을 
# 두가지 방법으로 저장하시오

f = open('exfile01.txt', 'a', encoding='utf-8')
f.write('안녕하세요')
f.close()

with open('exfile02.txt', 'a', encoding='utf-8') as f:
    f.write('안녕하세요')