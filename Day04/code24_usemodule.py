#모듈 사용
# 클래스로 안 된 모듈
import math as m  # math 모듈을 m이라고 지칭..사용할 때도 m으로 사용한다

# 우리가 만든 클래스
#모듈 불러오는 방법 1
import code22_person as p
#모듈 불러오는 방법 2
from code23_car import Car

print(m.pi) 
#print(math.pi) 

print(m.tan(0))
print(m.ceil(3.1)) # 올림
print(2 ** 10)
print(m.pow(2,10))

#우리가 만들 모듈 사용 1
me = p.Person('홍길동', 155, '남성')
print(me)

#우리가 만들 모듈 사용 2
mycar = Car()
print(mycar)