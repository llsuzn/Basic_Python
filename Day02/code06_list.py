# 복합형 리스트

# a1 = 1
# a2 = 2
# a3 = 3
# a4 = 4
# a5 = 5
# a6 = 6
# a7 = 7
# a8 = 8
# a9 = 9
# a10 = 10

# 리스트 []
# 리스트 == 배열
arr = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in arr: # arr  리스트의 값을 하나씩 변수에 대입해준다
    sum += i
print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello',13,'World!',True] # 파이썬에선 배열 선언 할 때 자료형 통일 할 필요가 없다.

print(arr3)
print(type(arr3)) # type : list형

# 빈 리스트
arr4 = []
arr5 = list()
print(arr4)
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]]
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]]
print(arr2 + arr7)

# 튜플 ()
tuple1 = (1,2,3,4)
print(tuple1)
# tuple1.append('4') -> 튜플은 값을 추가할 수 없다, 한 번 만들면 값을 바꿀수 없다(수정 불가)
print(type(tuple1))

arr5.append('4') # 리스트는 값을 수정할 수 있다
print(arr5)

# 딕셔너리{} : key와 value로 구성(순서 상관없다)
spiderman = { 'name' : 'Peter Parker',
               'age' : 18,
            'weapon' : 'Web Shooter'}
print(spiderman['name'])
print(spiderman['age']) # 자동완성 단축키 : ctrl + space
print(type(spiderman)) # type : dict

# 집합 : 중복을 혀용하지 않음
set1 = set([1,2,3,4])
print(set1)
print(type(set1)) # type : set

set1 = set('Hello')
print(set1) # 집합의 구성요소만 출력된다
