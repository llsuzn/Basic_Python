# 클래스 생성(매개변수 필요없다)
class Person:
    name = '익명' #속성변수
    height = ''
    gender = ''
    blood_type = 'O'

    # 1. 초기화 추가 __init__

    # 파라미터 X
    # def __init__(self) -> None:
    #     self.name = '리수진'
    #     self.height = '160'
    #     self.gender = 'female'
    #     self.blood_type = 'O'
    # 파라미터O
    def __init__(self,name = '홍길동',height = 170,gender = 'male') -> None: # name,height,gender는 매개변수
        self.name = name # self.name의 name은 속성변수(전역), 오른쪽 name은 매개변수(지역)// 구분할 수 있어야함
        self.height = height
        self.gender = gender
    # __<>__ : 매직 메서드
        
    def walk(self):
        print(f'{self.name}이(가) 걷습니다')

    # def run(option): self가 없다면 sujin.run('Fast')실행 시 실행 안 됨
    def run(self,option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다')
        elif option == 'Slow':
            print(f'{self.name}이(가) 천천히 뜁니다')
    
    def stop(self):
        print(f'{self.name}이(가) 멈춥니다')

    # 2. 생성자의 매직 메서드(function) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'





sujin = Person('이수진',160,'female') # person 클래스로 새로운 객체(sujin) 생성(클래스의 실체를 만드는 것) => ()필요
# sujin.name = '이수진' # 객체 속성변수의 name에 '이수진' 대입 , sujin.name의 sujin은 Person의 인스턴스
# sujin.height = '159' 
# sujin.gender = 'female'
# sujin.blood_type = 'RH+ O'

print(sujin.blood_type)
sujin.run('Fast')
print(sujin)

# 1. 초기화 후 객체생성
lee = Person()
lee.run('Slow')
print(lee)

print('='*25)
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리',165,'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)

print(ashely) # <__main__.Person object at 0x00000180A27F66D0> : __str__ 매직메서드 안쓰면 나오는 결과