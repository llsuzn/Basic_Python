# 연산자
# + - * / % **(승수)
val = 1 # = : 대입연산자, 할당연산...assigment

# equal 연산자 : ==

# 사칙연산
print(1 + 1)
print(10 * 10)
print(1024 / 2) # 소수 나누기
print(1024 // 2) # 정수 나누기
print(1024 % 2) # 나눗셈 나머지

first = 'Hello'
second = 'world'
print(first + ' ' + second) # Hello world
print('hell' * 3) # hellhellhell

# 문자열 길이 : len() 함수
print(len(first))
print(first[0]) # H출력
print(first[-1]) # o출력(뒤에서 첫번째)

# 리스트 자르기(슬라이싱)
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[11:]) # [11번째 인덱스 : ] = 15:14:02

# 리스트 연산 
que = [1,2,3,4,5]
que[0] = 7
print(que)
que.append(10) # <변수>.append()함수 => 리스트에 인자 추가
print(que)
que.insert(1,6) # <변수>.insert()함수 => 원하는 인덱스에 원하는 값 삽입(추가)
print(que)
que.remove(6) # 해당하는 값 제거
print(que)

asd = [1,2,1,3,5,5]
print(asd)
asd.remove(1) # 중복되는 값이 있다면 낮은 인덱스 번호부터 차례대로 제거된다.
print(asd)
asd.remove(1)
print(asd)

# que[5] = 10
# print(que) => overflow발생 , 실행 안 됨

# tup = (1,2,3)
# tup[1] = 9 => 튜플은 수정이 불가능해서 에러 뜬다

# 문자열 == 문자열 리스트
title = 'hello world'
#print[0] = 'P' # 불가능 => 문자열에선 값 변경이 안 됨
print('H' + title[1:6] + 'W' + title[7:])

# 문자열 포맷팅
print("I'm so happy {0} {1}!!".format(2,'you')) # 구식
print(f"I'm so happy {'2'} {'you'}!!") # 최신식 문자열 포맷팅
print(f"{'hello world'}")

pi = 3.141592
print(f"파이는 {pi}입니다")
print(f"파이는 {pi:0.02f}입니다") # 소수점 뒤 2자리까지
print(f"파이는 {pi:10.3f}입니다") # 빈칸 10칸 할당후 소수점 3자리까지 출력

# split() : 문자열을 특정문자로 자르기
full_name = 'lee su.jin'
vals = full_name.split() # 공백 기준으로 문자열 쪼갬
print(vals)
print(type(vals))
vals = full_name.split('.') # '.'기준으로 문자열 쪼갬
print(vals)

name = 'lee.su.jin'
vals = name.split('.')
print(vals)

# replace()
print(full_name.replace('lee','kim'))

# 문자열 공백 없애기 lstrip() retrip() strip()
hi = '          Hello~ Bye~          '
print(hi.lstrip() + '|') # 왼쪽 공백 지움
print(hi.rstrip() + '|') # 오른쪽 공백 지움
print(hi.strip() + '|') # 공백 모두 제거

# 문자열에서 값 찾기 .index() .find()
print(full_name.index('s')) # 인덱스 위치 알려줌
print(full_name.find('z')) # 인덱스 위치 알려줌, -1이 나오면 찾는 값이 없다는 뜻

print(full_name.count('e')) # 찾는 문자의 개수를 세는 함수 .count()

# 모든 단어를 대/소문자로 변경
print(full_name.upper()) # 대문자
print(full_name.lower()) # 소문자

# 연산자 우선순위
print(3 + 4 * 2) # 곱하기가 더하기보다 연산 우선순위 높다
print((3 + 4) * 2)

