import re #정규식을 만들기 위한 모듈 추가

#정규식에서 . => 문자 하나 yang
#정규식에서 ^ => 시작
#정규식에서 $ => 끝
p = re.compile('^yang') 
k = p.match("yangdoll")
if k:
    print(k.group()) #정규식에 맞는 단어를 출력
    print(k.string) #정규식에 테스트 되는 단어를 출력 = yangdoll
    # 위치 값을 반환하는 메서드 k.start(), k.end(), k.span()
    # print (k.start(), type(k.start()))
    # print (k.end(), type(k.end))
    # print (k.span(), type(k.span()))
    startindex, endindex = k.span()
    print( startindex)
else :
    print('주어진 단어는 일치 하지 않음')    