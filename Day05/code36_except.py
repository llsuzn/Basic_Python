# 예외처리
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b # 0으로 나누면 예외 발생 (에러)

# x,y = input('두 수를 입력하세요 : ').split()
# x = int(x)
# y = int(y)
x,y = map(int,input('두 수 입력: ').split())

# 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지마세요')
#     exit()

print('calc test')

try:
    print(div(x,y))
except:
    print('나누기 실패 : 0으로 나누기 시도')

print(add(x,y))
print(mul(x,y))


