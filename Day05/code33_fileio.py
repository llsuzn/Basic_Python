# 파일 만들기 
# ASCII -> 한 단어를 표현하는 체계(영어)
# 해결방법 -> 인코딩 -> Unicode(UTF-8) : 모든 나라언어를 다 표현 가능

# file = open('C:\DEV\Temp\Bank\sample.txt', 'w', encoding='utf-8') # 파일 생성(write) : 쓰기로 만듦
# file = open('./Day05/../Day04/sample.txt', 'w', encoding='utf-8') # ./현재 경로Day05에서 상위 디렉토리로 접근 -> Day04 디렉터리에서 텍스트 생성
file = open('./Day05/sample.txt', 'w', encoding='utf-8')
file.write('hello.\n') # w : O [hello.]
file.write('두번째 파일\n') # w : X [ù��° ����]
file.write('절대경로에 파일 생성')

file.close()
print('sample.txt가 생성되었습니다.')



# 파일/폴더 경로

# 절대경로 : 절대적인 기준(최초 디렉토리)를 기준으로 경유한 경로를 모두 기입하는 방식입니다.

# 상대경로 : 상대 경로는 최초 디렉토리가 아닌 특정 경로를 기준으로 다른 경로를 표시하는 방식입니다.