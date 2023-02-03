# 다중입력(개수 제한 있음)
# a,b = input('두 영단어를 입력하세요(\' \'): ').split() # 공백을 기준으로 입력을 받음
# # a,b = input('두 영단어를 입력하세요(/): ').split('/') # /을 기준으로 입력을 받음
# print(a,b)

# 다중입력(개수 제한 없음)
#inputs = map(int, input('숫자를 입력하세요(\' \'): ').split())
inputs = list(map(str, input('문자를 입력하세요(\' \'): ').split()))
print(inputs) #['안녕하세요', '이수진입니다.']

inputs = list(map(int, input('정수를 입력하세요(\' \'): ').split()))
print(*inputs) # 1999 11 30