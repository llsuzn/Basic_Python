# 클래스 생성
class Person:
    name = '익명' #속성변수
    height = ''
    gender = ''
    blood_type = 'O'

    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    # def run(option): self가 없다면 sujin.run('Fast')실행 시 실행 안 됨
    def run(self,option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다')
    
    def stop(self):
        print(f'{self.name}이(가) 멈춥니다')

sujin = Person() # person 클래스로 새로운 객체(sujin) 생성
sujin.name = '이수진' # 객체 속성변수의 name에 '이수진' 대입 , sujin.name의 sujin은 Person의 인스턴스
sujin.height = '159' 
sujin.gender = 'female'
sujin.blood_type = 'RH+ O'

print(sujin.blood_type)
sujin.run('Fast')
