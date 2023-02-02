# 함수만 포함된 모듈(mod01)
import mod01

print(mod01.sum(4,5))

# 클래스나 변수 등을 포함한 모듈(mod02)
import mod02 as m2

abc = m2.Math()
result = abc.sum(8,9)
print(result)
