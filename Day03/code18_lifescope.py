# 라이프 스코프
a = 1 # 전역변수 # ctrl + shift + L : 같은 문자 한 번에 선택/수정 가능

def vartest(): # 지역변수
    global a #전역변수 사용, 전역에 있는 a를 지역(함수)에서 가져다 씀
    a = a + 1  
    return a

a = vartest(a)# 전역변수
print(a)