# 함수
def add(x,y): # 함수정의(기본 구조)
    result = x + y
    return result

def sub(x,y):
    result = x - y
    return result

def mul(x,y):
    result = x * y
    return result
def div(x,y):
    result = x // y
    return result

a,b = map(int, input().split()) # map(function, iterable)
# 함수 디버깅 하려면 f5 + f11
print('뎃셈', add(a,b))
print(f'뺄셈 {sub(a,b)}') # 함수 드래그 + f12 누르면 함수로 이동, ctrl + 함수 클릭도 마찬가지
print(f'곱셈 {mul(a,b)}')
print(f'나눗셈 {div(a,b)}')

