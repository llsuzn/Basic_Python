# 콘솔출력 보충

# 1. 이스케이프 캐릭터(탈출 문자)_ \r \n \t 등
print('1.줄\r\n바꿈')
print('2.줄\n바꿈')
print('3.줄\t띄움')
print('4.한 칸\t\b백스페이스')
print('5.\'따옴표\'출력') # 소따옴표 내 소따옴표(문자열)출력하기
print('6.hello "world\"') # 소따옴표 내 큰따옴표는 이스케이프 써도 되고 안 써도 됨
print('7.\ 표현하는 방법 \\')
print('8.널문자\0')

# 2. 문자열 포맷팅_파이썬에서는 안 쓴다.(포맷코드 : %)
me = '저'
name = '이수진'
age = 25
print('%s는 %s입니다. %s는 %d입니다.' % (me,name,'나이',age))

print(f'{25.123456789}') # 최신식
print(f'{25.123456789:.2f}')
print('%10.4f' %(25.123456789))
