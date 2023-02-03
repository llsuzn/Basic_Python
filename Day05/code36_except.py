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

try:
    x,y = map(int,input('두 수 입력: ').split())
except Exception as e:
    print(e)
    exit()
finally: # 무조건 출력 , except구문 후 실행
    print('계속됩니다')

# 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지마세요')
#     exit()

print('calc test')

try:
    print(div(x,y))
# except ZeroDivisionError as e:
#     print('0으로 나누면 안돼요')
except Exception as e: # except Exception는 제일 마지막에 넣어줘야한다!무조건!...에러 범위 가장 넓음
    print(e)
finally: # 예외 유무와 상관없이 무조건 실행
    print('계산은 계속됩니다')

print(add(x,y))
print(mul(x,y))


