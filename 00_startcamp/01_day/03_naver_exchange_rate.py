import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/').text
soup = BeautifulSoup(html, 'html.parser')
# 아래와 같이 한꺼번에 위치좌표를 입력해도 값을 읽어올 수 있음
exchange_usd = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
exchange_jpy = soup.select_one('#exchangeList > li > a.head.jpy > div > span.value').text
print(exchange_usd)
print(exchange_jpy)

