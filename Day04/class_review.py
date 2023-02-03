# 클래스

# 덧셈,뺄셈
class Cal:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    
    def sum(self):
        return f'{self.a} + {self.b} = {self.a + self.b}'
    
    def sub(self):
        print(f'{self.a} - {self.b} = {self.a - self.b}')
    
abc = Cal(5,4)
print(abc.sum())
abc.sub()


# 박씨네 집
class HousePark:
    def __init__(self,name) -> None:
        self.name = name
    
    def fullname(self):
        self.fullname = '박'+self.name
        print(self.fullname)

    def travel(self,where):
        self.where = where
        return f'{self.fullname}이 가고싶은 여행지는 {self.where}이다.'

pe = HousePark('수진')
pe.fullname()
print(pe.travel('부산'))

# 연산자 오버로딩/클래스의 상속
class HouseLee:
    def __init__(self,lastname,name) -> None:
        self.lastname = lastname
        self.name = name
        self.fullname = self.lastname + self.name

    def travel(self,where):
        print(f'{self.fullname},{where}여행을 가다!')

    def love(self,other):
        print(f'{self.fullname},{other.fullname} 사랑에 빠졌네!')

    def __add__(self,other):
        print(f'{self.fullname},{other.fullname} 결혼했네!')

class HouseKim(HouseLee):
    def __init__(self, lastname, name) -> None:
        super().__init__(lastname, name)

    def travel(self, where):
        return super().travel(where)

romio = HouseLee('리','두딘')
juliet = HouseKim('김','줄리엣')
romio.love(juliet)
romio + juliet
juliet + romio
juliet.love(romio)


# 클래스 최종 복습
# 박응용은 부산에 놀러 가고 김줄리엣도 우연히 3일동안 부산에 놀러간다
# 둘은 사랑에 빠져 결혼하게 된다
# 그러다가 바로 싸우고 이혼한다
class HousePark:
    lastname = '박'

    def __init__(self,name) -> None:
        self.fullname = self.lastname + name
    
    def travel(self,where):
        print(f'{self.fullname},{where}여행을 가다.')
    
    def love(self,other):
        print(f'{self.fullname},{other.fullname} 사랑에 빠졌네')

    def __add__(self,other):
        print(f'{self.fullname},{other.fullname} 결혼했네')

    def fight(self,other):
        print(f'{self.fullname},{other.fullname} 싸우네')

    def __sub__(self,other):
        print(f'{self.fullname},{other.fullname} 이혼했네')

class HouseKim(HousePark):
    lastname = '김'

    def travel(self, where,day):
        print(f'{self.fullname},{where} 여행 {day}일 가다.')

pey = HousePark('응용')
juliet = HouseKim('줄리엣')
pey.travel('부산')
juliet.travel('부산',3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet