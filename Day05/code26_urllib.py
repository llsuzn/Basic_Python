# URL 라이브러리 패키지 불러오기
#urlopen 함수에 URL을 바로 넣어도 되고, Request 클래스에 URL을 넣은 뒤에 req를 생성해서 urlopen 함수에 넣어도 됩니다.
from urllib.request import Request,urlopen


req = Request('https://www.naver.com') # reauest 클래스로 객체 생성/웹사이트 요청
res = urlopen(req) # 결과 : 200
print(res.status) # https 코드 (주소 (숫자) 로도 웹주소 표현가능) / ex)404는 page not found

