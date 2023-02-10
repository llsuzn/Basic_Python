import email
import os

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):
      command = 'cls'
  os.system(command)

class Contact:
  def __init__(self, name, phone_number, e_mail, addr):
      self.__name = name
      self.__phone_number = phone_number
      self.__e_mail = e_mail
      self.__addr = addr

  def __str__(self) -> str:
      str_res = (f'이  름: {self.__name}\n'
                 f'핸드폰: {self.__phone_number}\n'
                 f'이메일: {self.__e_mail}\n'
                 f'주  소: {self.__addr}')
      return str_res

  def isNameExist(self, name):
      if self.__name == name:
          return True
      else:
          return False
   
def set_contact():
  name, phone_num, e_mail, addr = input('정보입력(이름, 폰번호, 이메일, 주소[구분자/]) : ').split('/')
  # print(name, phone_num, e_mail, addr)
  contact = Contact(name, phone_num, e_mail, addr)
  return contact

def get_menu():
  str_menu = ('주소록 프로그램 v1.0\n'
              '1. 연락처 추가\n'
              '2. 연락처 출력\n'
              '3. 연락처 삭제\n'
              '4. 종료\n')
  print(str_menu)
  menu = input('메뉴입력: ')
  return int(menu)

def run():
  lst_contact = []

  clearConsole()
  while True:
      sel_menu = get_menu()
      if sel_menu == 1:
          clearConsole()
          contact = set_contact()
          lst_contact.append(contact)
          input()
          clearConsole()
      elif sel_menu == 2:
          clearConsole()
          get_contacts(lst_contact)
          input()
          clearConsole()
      elif sel_menu == 3:
          clearConsole()
          name = input('삭제할 이름을 입력 : ')
          del_contact(lst_contact, name)
          input()
          clearConsole()
      elif sel_menu == 4:
          break

def get_contacts(lst_contact):
  for item in lst_contact:
      print(item)

def del_contact(lst_contact, name):
  for i, item in enumerate(lst_contact):
      if item.isNameExist(name):
          del lst_contact[i]

if __name__ == '__main__':
  run()