# random 모듈 사용
import random

# print(random.choice(range(1,7)))

numbers = [i for i in range(1,46)] # [1,2,3,4,5,6,...,45]
lottery = []

for i in range(6):
    lottery.append(random.choice(numbers)) # 6회 반복 : numbers 리스트의 수 중 랜덤으로 하나씩 lottery 리스트에 추가 
# 총 6개의 랜덤 숫자 나옴(1-45 범위 내)

print(lottery)
