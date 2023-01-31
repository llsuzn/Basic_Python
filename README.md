# StudyPython2023
부경대 IoT 파이썬 학습 리포지토리

## Day1
1. 기본구성
    - 개발환경 구성
    - Git/Githib 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치
2. 파이썬 기초
    - 콘솔출력
    ```python
    # desc : 콘솔출력 - 주석
    print('Hello Python!!') # 콘솔 출력함수
    ```

## Day2
1. 파이썬 기본
    - 변수
    ```python
    val = 'Hello'
    print(val)
    ```
    - 자료형
    ```python
    val = 3 
    print(type(val)) # int type

    # 리스트(수정가능)
    arr = [1,2,3,4,5,6,7,8,9,10]

    # 튜플(수정불가능)
    tuple1 = (1,2,3,4)

    # 딕셔너리{} : key와 value로 구성(순서 상관없다)
    spiderman = { 'name' : 'Peter Parker',
                   'age' : 18,
                'weapon' : 'Web Shooter'}
                
    # 집합 : 중복을 혀용하지 않음
    set1 = set('Hello')
    print(set1)
    ```
    - 연산자
    ```python
    # + - * / % **(승수) //(정수나눗셈)
    # print(6 / 0) 불가능(무한대는 계산 안된다)
    print(2 ** 10) # 2의 10승
    # 문자열 연산
    first = 'Hello'
    second = 'world'
    print(first + ' ' + second) # Hello world
    print('hell' * 3) # hellhellhell
    # 문자열 길이 : len() 함수
    print(len(first))
    # 인덱스 슬라이싱
    current = '2023-01-31 15:14:02' # 현재시간
    print(current[11:]) # [11번째 인덱스 : ] = 15:14:02

    que.append(10) # <변수>.append()함수 => 리스트에 인자 추가
    que.insert(1,6) # <변수>.insert()함수 => 원하는 인덱스에 원하는 값 삽입(추가)
    asd.remove(1) # 중복되는 값이 있다면 낮은 인덱스 번호부터 차례대로 제거된다.
    ```
    - 흐름제어