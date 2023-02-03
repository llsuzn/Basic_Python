# 외부 패키지 사용
import requests

res = requests.get('https://www.naver.com')
print(res.status_code)
print('=' * 200)
print(res.content) # 웹페이지 정보(.html)
