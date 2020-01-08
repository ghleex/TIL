## pip install bs4 -- bash에서 미리 수행 필요

import requests
from bs4 import BeautifulSoup

# 1. 원하는 주소로 요청 보내고 받은 응답을 저장
html = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text
print(kospi)