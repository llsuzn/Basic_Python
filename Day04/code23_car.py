# Car 클래스 생성
class Car:
    __number = '12라 3456' # __number 상속변수를 ____number로 바꾸면 값 수정 불가

    def get___number(self) -> str:
        return self.__number

    # 클래스 내부함수 이용하여 값 바꾸기 .. __사용하면 내부함수 이용해야만 값 변경 가능
    def set_number(self,number) -> str:
        self.__number = number


    def __init__(self,number = '88호 8888') -> None:
        self.__number = number
        print('__init__')

    # def __new__(cls): # 메직메서드는 우선순위가 다름, new 잘 안 씀
    #     print('__new__')
    #     return super().__new__(cls) # 녹색 글자 :class ,,,, super : '부모' 클래스(상속)

    def __str__(self) -> str:
        return f'차번호는 {self.__number} 입니다 '

yourcar = Car('99진 9999')
print(yourcar)
yourcar.__number = '44라 4444' # 외부에서는 멤버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar) # __str__은 print해야만 출력됨
print(f'제 차번호는 {mycar.get___number()}입니다')

mycar.__number = '65가 4321'
print(mycar)