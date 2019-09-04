api 환경변수 - decouple



필수사항

명세: 파일명 - 01.py

​	targetdt - 50회 바꾸기(반복문 50번 돌아감)

​	50주간

​	마지막 일자는 7월 13일

​	다양성, 상업영화(multiMovieYn 안 건드려도 됨; default가 전체임)

​	한국/외국영화: default 전체 / repNationCd 역시 안 건드려도 됨

 모든 상영지역 포함: default 전체 / wideAreaCd도



필드가 3개 나와야 함

​	영화 대표코드, 영화명, 해당일 누적관객수

​											마지막 값을 저장시켜야 함

​	boxoffice.csv



50주간 데이터 뽑기 위하여

1주를 뽑아서 3주 양을 뽑아보고 괜찮다 싶으면 50번 뽑아라

왜냐면 API 쓸 수 있는 양이 한정(3000)되어 있으므로!

```python
from datetime import datetime, timedelta
datetime(2019, 7, 13) - timedelta(weeks=i)
						#: i 이전의 시각을 구함 if 1이면 1주 이전의 시각
targetDt.strftime('%Y%m%d') #== 20190713
pprint() 사용하면 좋음
```





# 유의사항

googling 가능

상의 가능

서로 설명 가능

다른 사람의 코드 작성해주지 말고 직접 작성

코드 가독성(변수명, 스타일 가이드)

key / api 명세(홈페이지 확인) / csv 읽고 쓰기 (DictWriter/DictReader만 사용)



## Working Flow

### 	1. 데이터 불러오기

#### 		1.1. key, url, targetDt 준비

#### 		1.2. 요청 보내서 json 데이터 받기

#### 		1.3. 위에서 받은 데이터로 원하는 데이터 리스트로 가져오기

#### 		1.4. 필드 준비 / 딕셔너리 만들기

### 	2. 결과 저장하기(csv)