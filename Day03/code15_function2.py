# 함수
# 1. 파라미터 0 리턴 0
# 2. 파라미터 0 리턴 X
# 3. 파라미터 X 리턴 0
# 4. 파라미터 X 리턴 X

# 1
def add(x,y): # 함수정의(기본 구조)
    result = x + y
    return result 

# 2
def sub(x,y):
    result = x - y
    print(result)

def mul(x,y):
    result = x * y
    print(result)


def div(x,y):
    result = x // y
    print(result)

def hello(): #매개변수가 없고 반환값도 없는 경우
    print('hello')

a,b = map(int, input().split()) # map(function, iterable)
# 함수 디버깅 하려면 f5 + f11

print(add(a,b))
sub(a,b)
mul(a,b)
div(a,b)
hello()
