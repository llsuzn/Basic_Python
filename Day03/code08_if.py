# if문
name = '수진'
state = '미열'
if name == '수진':
    print('진료실 입장')
    if state == '미열':
        print('해열제 처방')
elif name == '규수':
    print('잠시 대기')
else:
    print('진료실 입장불가')


