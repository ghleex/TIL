"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
scores = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
total_score = 0
for subject_score in scores.values():
    total_score = total_score + subject_score
    # total_score += subject_score
avg_score = total_score / len(scores)
print(avg_score)



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
total_score = 0
count = 0

for person_score in scores.values():
    for indivisual_score in person_score.values():
        total_score = total_score + indivisual_score
        # total_score += indivisual_score
        count = count + 1
        # count += 1

avg_score = total_score / count
print(avg_score)




# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
for name, temp in city.items():
    avg_temp = sum(temp) / len(temp)
    print(f'{name} : {avg_temp:.1f}')




# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
hot=0
cold=0
for name, temp in city.items():
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name                
    count += 1

print(f'가장 더운 곳: {hot_city}, 가장 추운 곳: {cold_city}')   




# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in city['서울']:
    print("ㅇㅇ")
else:
    print("ㄴㄴ")
