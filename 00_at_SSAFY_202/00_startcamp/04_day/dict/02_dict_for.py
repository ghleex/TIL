# 딕셔너리 기준으로 반복문 사용하기
lunch = {
    '중국집': '02-1234-5678',
    '일식집': '02-9876-5432',
    '분식집': '031-2345-6789'
}

# 1. 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

# 2. ".items()" 사용하기
for key, value in lunch.items():
    print(key, value)

# 3. value 값만 가져오기 ".values()"
for value in lunch.values():
    print(value)

# 4. key 값만 가져오기 ".keys()"
for key in lunch.keys():
    print(key)