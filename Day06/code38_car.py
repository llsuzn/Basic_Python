# 객체지향_차에 대한 부모 클래스

class Car:
    __name = '자동차' # __ : 수정 불가능
    __color = 'white'
    __plate_number = ''
    __product_year = 1900

    def __str__(self) -> str: 
        return '부모 클래스'

    def get_name(self):
        return self.__name

    def run(self):
        return '차가 달립니다'

    def stop(self):
        return '차가 멈춥니다'

    if __name__ == '__main__': # code28에서 import할 때 실행 안 됨
        print('부모클래스 파일 실행 중입니다.')
            
