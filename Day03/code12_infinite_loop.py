# 무한반복문(DB연동의 핵심)
# key = input('숫자 입력 : ')
# print(f'입력받은 수: {key}')

num = 0

while True:
    print('메뉴를 선택하세요.')
    print(' 1. 회원입력')
    print(' 2. 회원검색')
    print(' 3. 회원수정')
    print(' 4. 회원삭제')
    print(' 5. 프로그램 종료')
    num = int(input('메뉴번호 입력 > ')) # input 함수는 기본적으로 '문자'를 입력받기 때문에 int형으로 형변환 해준다
    #또는 num = int(num) 추가해줘도 괜찮음

    if num == 1:
        print('회원입력 시작')
        pass # 실행할 코드가 없는 것..다음 실행문으로 넘어간다
    elif num == 2:
        print('회원검색 시작')
    elif num == 3:
        print('회원수정 시작')
    elif num == 4:
        print('회원삭제 시작')
    elif num == 5:
        print('프로그램 종료')
        break
    else:
        continue
