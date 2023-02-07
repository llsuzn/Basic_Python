# 주소록 앱
# 2023-2-6
# leesujin
# 15. 예외처리 - <1> 파일 없을 때 <2> 입력 시 ('/')갯수 다를 때 <3> 메뉴 입력 시 문자 넣을 때

import os # 운영체제 라이브러리 ...cls 사용하기 위해서
# 2. 클래스 생성
class Contact:
    # 이름 전화번호 이메일 주소
    def __init__(self,name,phone_number,e_mail,addr) -> None: # 파라미터 입력이 많으면 생성자 만들어주면 편하다
        self.__name = name
        self.__phone_number = phone_number
        self.__e_mail = e_mail
        self.__addr = addr

    # 4. __str__ 재정의
    def __str__(self) -> str: # 클래스 자체의 내용을 출력하고 싶을 때(init에서 규정한)
        str_res = (f'이  름 : {self.__name}\n'
                   f'핸드폰 : {self.__phone_number}\n'
                   f'이메일 : {self.__e_mail}\n'
                   f'주  소 : {self.__addr}')

        return str_res

    # 10. 객체 존재여부 확인 , 클래스 함수
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False

    # 12. 각 멤버변수 접근하는 함수
    #Get_Name, Get_PhoneNum, Get_Email, Get_Addr
    def Get_Name(self) -> str:
        return self.__name

    def Get_PhoneNum(self):
        return self.__phone_number

    def Get_Email(self):
        return self.__e_mail

    def Get_Addr(self):
        return self.__addr

# 5. 사용자 입력 함수
def Set_Contact():
    name, phone_number,e_mail,addr = input('정보입력[이름/폰번호/이메일/주소] : ').split('/')
    # 7. contact 객체 만들기
    contact = Contact(name,phone_number,e_mail,addr)
    return contact

# 9. 주소록 출력
def Get_Contacts(list):
    for item in list:
        print(item)
        print('='*30)

# 11. 주소록 삭제 
def del_contact(list, name):
    count = 0
    for i , item in enumerate(list): # 인덱스(index)와 원소를 동시에 접근하면서 루프를 돌릴 수 있다 , 리스트 인덱스 추가생성
        if item.isNameExist(name):
            count += 1
            del list[i] # 리스트 삭제
    
    if count > 0: # 메세지 출력
        print('삭제되었습니다.')
    else:
        print('삭제할 주소록이 없습니다.')

# 13. 주소록 파일 저장
def save_contacts(list):
    file = open('C:/Source/StudyPython2023/Project/contacts.txt','w',encoding='utf-8')

    for item in list:
        text = f'{item.Get_Name()}/{item.Get_PhoneNum()}/{item.Get_Email()}/{item.Get_Addr()}'
        file.write(f'{text}\n')

    file.close() # 파일은 종료 시 무조건 닫아야 한다

# 14. 주소록 읽어오기(txt)
def load_contacts(list):
    try: # <1> 파일이 없을 때 예외처리
        file = open('C:/Source/StudyPython2023/Project/contacts.txt','r',encoding='utf-8')
    except Exception as e:
        f = open('C:/Source/StudyPython2023/Project/contacts.txt','w',encoding='utf-8') # 예외가 발생하면 파일을 하나 새로 만든다
        f.close()
        return 

    while True:
        line = file.readline().replace('\n','') # 15. 문장 끝에 \n 제거(예외처리)
        if not line: break
    
        lines = line.split('/')
        contact = Contact(lines[0],lines[1],lines[2],lines[3])
        list.append(contact)
    
    file.close()

    



# 화면 정리 함수(cls)
def clear_console():
    command = 'clear' # 리눅스, 유닉스 운영체제 화면정리 명령어
    if os.name in ('nt','dos'): # 윈도우 운영체제 화면정리 명령어
        command = 'cls'

    os.system(command)

# 6. 메뉴함수
def get_menu():
    str_menu = ('주소록 앱 v1.0\n'
               '1. 연락처 추가\n'
               '2. 연락처 출력\n'
               '3. 연락처 삭제\n'
               '4. 앱 종료\n')

    print(str_menu)
    try: # <3> 숫자 외(문자 or 특수문자) 입력 시 예외처리
        menu = int(input('메뉴 입력:'))
    except Exception as e:
        menu = 0

    return menu

# 3. 전체실행
def run():
    contacts = [] # 정보를 담기 위한 빈 리스트 만들기 []로 만들어도 됨
    load_contacts(contacts) # 14. 주소록 읽어오기
    clear_console() 
    while True:
        sel_menu = get_menu()
        if sel_menu == 1: # 8. 주소록 추가
            try: # <2> 연락처 입력을 잘못했을 때 예외처리
                clear_console()
                contact = Set_Contact()
                contacts.append(contact)
                input('주소록 입력 성공!') # 아무것도 안 받는 입력
            except Exception as e:
                print('이름/번호/이메일/주소 입력을 똑바로 입력하세요')
                input()
            finally:
                clear_console()
        elif sel_menu == 2: # 9. 주소록 출력
            clear_console()
            Get_Contacts(contacts)
            input('주소록 출력 완료!') # 아무것도 안 받는 입력
            clear_console()
        elif sel_menu == 3: # 11. 주소록 삭제
            name = input('삭제할 이름 입력 : ')
            del_contact(contacts, name)
            input()
            clear_console()
        elif sel_menu == 4: # 앱 종료
            # 종료시 주소록 파일에 저장(txt)
            save_contacts(contacts)
            break
        else:
            clear_console()
       
# 1. 메인영역
if __name__ == '__main__':
    print('주소록 앱 시작합니다')
    run()
 