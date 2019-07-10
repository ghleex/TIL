import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
# 1. 요청 보내서 html 받기
html = requests.get(url).text

# 2. BeautifulSoup 정제
soup = BeautifulSoup(html, 'html.parser')

# 3. select method 사용하여 list 얻기
searches = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

# 4. 뽑은 list를 with 구문을 이용하여 txt파일로 작성해보자.
with open('naver_rank.txt', 'w', encoding='utf-8') as f:
    # 한글은 깨져보일 수 있으므로 별도로 인코딩 설정 필요
    # i = 1
    for search in searches:        
        f.write(f'{search.text}\n')
        # f.write(f'{i}. {search.text}\n')
        # i = i + 1

# 3.1. select method 사용하여 list 얻기
searches = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a')

# 4.1. rank, keyword 변수로 작성
with open('naver_search.txt', 'w', encoding='utf-8') as f:    
    for search in searches:        
        rank = search.select_one('span.ah_r').text
        keyword = search.select_one('span.ah_k').text
        f.write(f'{rank}. {keyword}\n')        