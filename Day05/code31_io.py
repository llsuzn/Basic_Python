# 입출력
#number = input('숫자를 입력하세요: ') # 입력 C[scanf("숫자를 입력하세요: %d\n",&number)]
#print(f'입력받은 숫자는 {number}입니다.') # 출력

number = int(input('숫자를 입력하세요 :')) # number을 int형으로 바꿔준다
print(number * 5) # input은 문자열 형태로 입력된다 / 결과 'number number number number number'

print('life' 'is' 'short')
print('life','is','short')

a = [1,2,3,4]
for i in a:
    print(i,end='')