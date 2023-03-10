# StudyPython2023
IoT 파이썬 학습 리포지토리

## 단축키 안내 ##
1. 단어 모두 선택/편집 
    - ctrl + shift + L
2. 단어 검색
    - ctrl + F
3. 단어 하나씩 추가로 선택
    - ctrl + D
4. 단어 검색해서 바꾸기 
    - ctrl + H
5. 작업관리자 창 띄우기
    - ctrl + shift + esc 

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
    ```
    ```python
    # 리스트(수정가능)
    arr = [1,2,3,4,5,6,7,8,9,10]
    ```
    ```python
    # 튜플(수정불가능)
    tuple1 = (1,2,3,4)
    ```
    ```python
    # 딕셔너리{} : key와 value로 구성(순서 상관없다)
    spiderman = { 'name' : 'Peter Parker',
                   'age' : 18,
                'weapon' : 'Web Shooter'}
    ```
    ```python
    # 집합 : 중복을 혀용하지 않음
    set1 = set('Hello')
    print(set1)
    ```
    - 연산자
    ```python
    # + - * / % **(승수) //(정수나눗셈)

    # print(6 / 0) 불가능(무한대는 계산 안된다)

    print(2 ** 10) # 2의 10승
    ```
    ```python
    # 문자열 연산
    first = 'Hello'
    second = 'world'
    print(first + ' ' + second) # Hello world
    print('hell' * 3) # hellhellhell
    ```
    ```python
    # 문자열 길이 : len() 함수
    print(len(first))
    ```
    ```python
    # 인덱스 슬라이싱
    current = '2023-01-31 15:14:02' # 현재시간
    print(current[11:]) # [11번째 인덱스 : ] = 15:14:02
    ```
    ```python
    que.append(10) # <변수>.append()함수 => 리스트에 인자 추가
    que.insert(1,6) # <변수>.insert()함수 => 원하는 인덱스에 원하는 값 삽입(추가)
    asd.remove(1) # 중복되는 값이 있다면 낮은 인덱스 번호부터 차례대로 제거된다.
    ```
    ```python
    # 문자열 == 문자열 리스트
    title = 'hello world'
    print('H' + title[1:6] + 'W' + title[7:])
    ```
    ```python
    # 문자열 포맷팅
    print("I'm so happy {0} {1}!!".format(2,'you')) # 구식
    print(f"I'm so happy {'2'} {'you'}!!") # 최신식 문자열 포맷팅
    ```
    ```python
    # split() : 문자열을 특정문자로 자르기
    full_name = 'lee su.jin'
    vals = full_name.split() # 공백 기준으로 문자열 쪼갬
    ```
    ```python
    # replace()
    print(full_name.replace('lee','kim'))
    ```
    ```python
    # 문자열 공백 없애기 lstrip() retrip() strip()
    hi = '          Hello~ Bye~          '
    print(hi.lstrip() + '|') # 왼쪽 공백 지움
    print(hi.rstrip() + '|') # 오른쪽 공백 지움
    print(hi.strip() + '|') # 공백 모두 제거
    ```
    ```python
    # 모든 단어를 대/소문자로 변경
    print(full_name.upper()) # 대문자
    print(full_name.lower()) # 소문자
    ```


## Day3
1. 파이썬 기본
    - 흐름제어
        - if
        ```python
        if name == '수진':
            print('진료실 입장')
        elif name == '규수':
            print('잠시 대기')
        else:
            print('진료실 입장불가')
        ```
        - for
        ```python
        for item in arr: # arr리스트의 첫 인덱스 요소부터 차례대로 변수에 할당
            print(f'{item:2.2f}') # {:2.2f}에서 :2의 의미는 결과값의 정수 자리에 2칸을 할당하라는 의미이고, ".2f"의 의미는 소수점 둘째 자리까지 표현하라는 의미이다
        
        # 리스트 선언에서도 사용가능
        val = [i for i in range(1,11)]
        print(val)
        ```
        - while
        ```python
        hit = 0
        while hit < 11:
            hit += 1 
            print(f'나무를 {hit:2d}번 찍었습니다') # :2d는 2칸 확보 후 10진수로 출력, 2b는 2진수
        ```
        - 구구단 프로그램
         ```python
         for i in range(2,10):
         print(f'{i}단')
         for j in range(1,10):
            print(f'{i} X {j} = {i*j:<2}',end=' ')  # :>2 2칸 할당하고 오른쪽 정렬, :<2 2칸 할당하고 왼쪽 정렬 
         print(end = '\n') # print('') 단 끝날 때 마다 줄바꿈
         ```
        - 함수
         ```python
          def add(x,y): # 함수정의
            result = x + y
            print('덧셈 결과')
            return result

          a,b = map(int, input().split()) # map(function, iterable)
          print(add(a,b))
         ```

## Day4
1. 파이썬 기본
    - 가상환경
        - pip install virtualenv (가상개발환경 설치)
        - 가상환경 스위치
    - 객체지향  OPP
        - 클래스(속성과 함수로 구성),매개변수 필요없음
        ```python
            class Person:
                name = '익명' #속성변수
                
                def run(self,option):
                    if option == 'Fast':
                        self.walk()
                        print(f'{self.name}이(가) 빨리 뜁니다')
                    else:
                        print(f'{self.name}이(가) 천천히 뜁니다')

            sujin = Person() # person 클래스로 새로운 객체(인스턴스..sujin) 생성
            sujin.name = '이수진' # 객체 속성변수의 name에 '이수진' 대입
            print(sujin.name)
            sujin.run('Fast')
        ```
        - 생성자() 
        ```python
            lee = Person()
        ```
        ```python
            class Car:
                def __init__(self,number = '88호 8888') -> None:
                    self.__number = number
            
            yourcar = Car('99진 9999')
        ```
        - 상속 (부모 클래스/ 자식 클래스)
    - 패키지, 모듈(클래스X, 클래스O)
    ```python
        import <모듈이름>
        <모듈이름>.<모듈함수>()

        또는

        from <모듈이름> import <모듈함수>
        <모듈함수>()
    ```
    ```python
        # 함수만 포함된 모듈
        import mod01

        print(mod01.sum(4,5))
    ```
    ```python
        # 클래스 포함된 모듈
        import mod02 as m2

        abc = m2.Math()
        result = abc.sum(8,9)
        print(result)
    ```
## Day5
1. 파이썬 기본
    - 패키지 계속
        - urllib 패키지
        ```python
            from urllib.request import Request,urlopen

            req = Request('https://www.naver.com') # reauest 클래스로 객체 생성/웹사이트 요청
            res = urlopen(req) # 결과 : 200
            print(res.status) # https 코드 (주소 (숫자) 로도 웹주소 표현가능) / ex)404는 page not found
        ```
        - requests 패키지 설치 및 실행
        ```python
            # pip install requests 터미널 창 실행 후
            import requests

            res = requests.get('https://www.naver.com')
            print(res.status_code)
            print('=' * 200)
            print(res.content) # 웹페이지 정보(.html)
        ```
        - ramdom 모듈 사용(use_module.py)
    - 입출력 다시
        - 입력 : input()
            - 다중입력
            ```python
            # 다중입력(개수 제한 없음)
            #inputs = map(int, input('숫자를 입력하세요(\' \'): ').split())
            inputs = list(map(str, input('문자를 입력하세요(\' \'): ').split()))
            print(inputs) #['안녕하세요', '이수진입니다.']

            # []없이 출력
            inputs = list(map(int, input('정수를 입력하세요(\' \'): ').split()))
            print(*inputs) # 1999 11 30

            # []없이 and ' '없이 출력
            for i in range(len(inputs)):
                print(f'{inputs[i]}',end='')
            ```
            - 파일 쓰기
            ```python
            file = open('./Day05/sample.txt', 'w', encoding='utf-8')
            file.write('hello.\n') # w : O [hello.]
            
            file.close()
            ```
            - 파일 읽기
            ```python
            file = open('./Day05/sample.txt','r',encoding='utf-8')
            while True:
            text = file.read()

            if not text: break

            print(text)

            file.close()
            ```
            - cvs 파일 읽기
            ```python
            import csv
            fullPath = 'C:/Source/StudyPython2023/busanbus.csv'
            file = open(fullPath ,'r', encoding='utf-8')
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for line in reader:
                print(line)

            file.close()
            ```

    - 예외처리 
    ```python
    try:
        print(div(x,y))
    except Exception as e:
        print(e)
    ```
        
## Day6
1. 파이썬 기본
    - 콘솔출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속
        - 다중상속

2. 파이썬 응용
    - 주소록 프로그램 [소스](https://github.com/llsuzn/Python/blob/main/Project/address_app.py)
    - 파일 텍스트 DB
   
   
   ![실행화면](https://github.com/llsuzn/Python/blob/main/images/address_app.png?raw=true)
    - 주피터 노트북

## Day7
1. 파이썬 응용
    - 주피터 노트북 사용법
        - 노트북 생성[파일 -> 새파일(ctrl+alt+윈도우+N)]
        - esc -> m : 마크다운, y : 파이썬
        - folium 지도사용법
        [Folium 지도사용법](Day07/code43_folium_tutorial.ipynb)
    - 리스트 연산 추가
    - 라이브러리 사용법
        - folium (지도 라이브러리)사용법
        [Folium 지도사용법](Day07/code43_folium_tutorial.ipynb)
    - json
    ```json
    # json 기본 구조
    {
    "ionic" : {
        "price" : 20000000,
        "year" : "2022"
    },
    "genesis" : {
        "price" : 80000000,
        "year" : "2021"
    }
    }
    ```

## Day8
1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹 크롤링
        - 기상청 오늘의 날씨 크롤링
        - 데이터 포털 OpenAPI 크롤링
        ![실행화면](https://github.com/llsuzn/Python/blob/main/images/folium.png?raw=true)
        - BeautifulSoup 크롤링

## Day9
1. 파이썬 응용
    - GUI 개발
        - Tkinter 소개
        - PyQt 소개, 설치
        - PyQt 기본 사용법
        - 위젯

## Day10
1. 파이썬 응용
    - GUI 개발
        - PyQt 위젯 계속
        - PyQt 다이얼로그
        
          PyQt 실행화면 [file_dialog source](Day10/code60_pyqt_filedialog.py)       
          ![실행화면](https://github.com/llsuzn/Python/blob/main/images/dialog.png?raw=true)

## Day11
1. 자료구조 알고리즘