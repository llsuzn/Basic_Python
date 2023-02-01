# for문
# for 문은 리스트/튜플과 사용하면 좋음

arr = [1,2,3,4,5] #리스트
sum = 0

for item in arr: # arr리스트의 첫 인덱스 요소부터 차례대로 변수에 할당
    print(f'{item:2.2f}') # {:2.2f}에서 :2의 의미는 결과값의 정수 자리에 2칸을 할당하라는 의미이고, ".2f"의 의미는 소수점 둘째 자리까지 표현하라는 의미이다
    sum = sum + item

print('합계는', sum)

# 리스트 편하게 만드는 방법(for 사용)
# vals = [1,2,3,4,5,6,7,8,9,10]
# print(vals)
val = [i for i in range(1,11)]
print(val)

num = 0
for item in val:
    num += 1
    if num % 2 == 0: # 2의배수
        continue # for문 시작으로 돌아가서 계속 실행
        #break # 반복문 빠져나감
    else: 
        print(num, '수는', item, '입니다') # 홀수만 출력

print(range(10))

