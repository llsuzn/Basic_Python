# 구구단

for i in range(2,10):
    print(f'{i}단')
    for j in range(1,10):
        print(f'{i} X {j} = {i*j:<2}',end=' ')  # :>2 2칸 할당하고 오른쪽 정렬, :<2 2칸 할당하고 왼쪽 정렬 
    print(end = '\n') # print('') 단 끝날 때 마다 줄바꿈
 