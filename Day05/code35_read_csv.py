# 공공데이터포털 csv파일 읽기
# 부산광역시 시내버스, 마을버스 현황
import csv
fileName = 'busanbus.csv'
dirName = 'C:/Source/StudyPython2023/'
fullPath = dirName + fileName

file = open(fullPath ,'r', encoding='utf-8')
reader = csv.reader(file, delimiter=',')
next(reader) # next() - 반복 가능 객체(csv)의 다음 요소 반환

for line in reader:
    print(line)

file.close() # 파일을 열면 반드시 닫아줘야 한다.