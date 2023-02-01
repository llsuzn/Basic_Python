# while 문
hit = 0
while hit < 11:
    hit += 1 
    print(f'나무를 {hit:2d}번 찍었습니다') # :2d는 2칸 확보 후 10진수로 출력, 2b는 2진수
    if hit == 10:
        print(f'{hit}번 찍어 안넘어가는 나무 없다\n')
        break
    else:
        print('나무가 아직 넘어가지 않았습니다\n')
print('나무찍기 완료')