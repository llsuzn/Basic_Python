# Car class 상속한 제네시스 클래스
from code38_car import Car

#Child class
class Genesis(Car): # code38_car의 Car클래스 상속
    def __init__(self,name,color,
                 plate_numbe,product_year) -> None:
        super().__init__()

        self.__name = name
        self.__color = color
        self.__plate_number = plate_numbe
        self.__product_year = product_year
        print(f'{self.__name} 인스턴스 생성!')

    def set_name(self,name):
        self.__name = name

    def get_name(self): # 만들어주지 않으면 부모클래스의 get_name이 출력된다
        return self.__name

    def run(self):
        return f'{self.__name}이 달립니다.'

    def stop(self):
        return f'{self.__name}이 멈춥니다'

GV80 = Genesis('GV80','black','60가 5223','1900')
# GV80.set_name('GV80')
print(f'이 차의 이름은 {GV80.get_name()}입니다') # get_name은 부모클래스 함수이기 때문에 부모클래스 접근하게된다
print(GV80.run())
print(GV80.stop())

