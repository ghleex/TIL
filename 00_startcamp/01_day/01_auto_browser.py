import webbrowser

# 1. 리스트 필요
# websites = ['www.google.com', 'www.youtube.com', 'www.naver.com']

# idols = ['bts', 'finkl', 'hot', 'babyvox']
# url = 'https://search.naver.com/search.naver?query='

# 2. 반복문(for) 내에서 webbrowser.open() 이 실행되어야 함
#for i in range(3):
#   webbrowser.open(websites[i])
## 리스트 자리를 i값을 통해 이용

# for site in websites:
#     webbrowser.open_new(site)
# 리스트 자체를 사용하는 것

# for idol in idols:
#     webbrowser.open_new(url + idol)


## 정보 스크랩하기
import requests

response = requests.get('https://www.naver.com').status_code
print(response)


