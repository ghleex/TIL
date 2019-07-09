name = '이길현'
#print(f'안녕하세요, {name}입니다.')

# 점심 메뉴 추천
import random

menu = ['버거킹', '치킨', '쌈밥']
lunch = random.choice(menu)
#print(f'오늘의 점심은 {lunch}입니다.')

# 로또 번호 추천
numbers = range(1, 46)
# 오름차순 정렬: sorted(numbers)
lottery = random.sample(numbers, 6)
print(f'오늘의 당첨 번호는 {sorted(lottery)} 입니다.')

# 필요하면 이런 방법을 사용
name = '홍길동'
print('안녕하세요, ' + name + '입니다.')