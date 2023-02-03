# 좀 더 복잡한 계산기

def calc(option, *args):
    result = 0
    if option == 'add':
        for i in args:
            result += i

    elif option == 'mul':
        for i in args:
            result = result * i
    
    elif option == 'sub':
        result = args[0]
        for i in args[1:]:
            result -= i
    
    elif option == 'div':
        result = args[0]
        for i in args[1:]:
            result //= i
    return result

# 여러값을 리턴할 땐 튜플 사용
def new_calc(x,y):
    return (x*y,x//y,x-y,x+y)
#받을 땐 튜플(소괄호) 생략 가능
#(res1,res2,res3,res4) = mul_and_div(10,2)
res1,res2,res3,res4 = new_calc(10,2)

# if __name__ == '__main__':  제일 마지막에 써야함
if __name__ == '__main__': # code28에서 import할 때 실행 안 됨
    print(calc('add',180,5,3,3,2))
    print(calc('mul',180,5,3,3,2))
    print(calc('sub',180,5,3,3,2))
    print(calc('div',180,5,3,3,2))
    print(f'곱셈 {res1}\n나눗셈 {res2}\n뺄셈 {res3}\n덧셈 {res4}')
            