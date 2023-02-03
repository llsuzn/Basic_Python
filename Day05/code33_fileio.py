# 파일 만들기 : ASCII
file = open('sample.txt', 'w') # 파일 생성(write) : 쓰기로 만듦

file.write('hello.') # w : O [hello.]
file.write('첫번째 파일') # w : X [ù��° ����]

file.close()
print('sample.txt가 생성되었습니다.')

# ASCII -> 한 단어를 표현하는 체계(영어)

#해결방법 -> Unicode(UTF-8) : 모든 나라언어를 다 표현 가능