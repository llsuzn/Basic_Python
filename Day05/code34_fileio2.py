# 파일 읽어오기
file = open('./Day05/sample.txt','r',encoding='utf-8') # 상대경로

while True:
    text = file.read()

    if not text: break

    print(text)

file.close()