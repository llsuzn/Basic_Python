# 매개변수 개수 일정하지 않은 경우

#def add(a,b,c,d,e,f):
def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(f'덧셈 결과: {add(1,2,3,4,5,6,7,8,9,10)}')

# 터미널로 입력받기
def add(list):
    result = 0
    for i in list:
        result += i
    return result

num = list(map(int,input().split()))
print(f'덧셈 결과: {add(num)}')

