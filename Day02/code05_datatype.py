# 자료형


# 1. None : 값이 없는 값
None # None은 정의할 수 없는 형태이다

print(None)
print(0 == None)
print('' == None)

# 2. 숫자형
val = 3 # val은 int형
print(type(val)) # type : 변수의 자료형을 알려준다

val = 3.14 # val은 float형
print(type(val))

val = 'Hello' # str은 문자열
print(type(val))

val = 0b1010
print(type(val))

val = 4_520_000 # 숫자 3칸마다 언더바 사용해서 읽기 쉽게 한다(출력은 언더바 없이)
print(val)

val = 3.125_657
print(val)

# 3. 문자형
val = 'Life is short, You need python'
print(val)
print(type(val))

val = 'Hell\nworld!'
print(val)

val = 'Hell\t\bworld!' # \t:tab, \b:back space
print(val)

val = '''Life is short,
You need python''' 
 # '''문장을 적고 싶을 때'''

# 4. 불형...type : bool : 참/거짓 판별
# 내장함수 : bool()
참 = True
거짓 = False
print(type(거짓))
print(1+1 == 1) # False

print(참 == True)
print(참 == False)
print(거짓 is False) # 참조가 같은지 확인을 합니다.

print(bool(0)) # 0은 거짓
print(bool(1)) # 0을 제외한 나머지 숫자는 참이다.