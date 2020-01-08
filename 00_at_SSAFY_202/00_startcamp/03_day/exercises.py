# str = input('문자를 입력하세요: ')
# nstr = list(str)
# print(nstr[0], nstr[-1])


# numbers = int(input('숫자를 입력하세요: '))
# for i in range(numbers):
#     print(i+1)


# number = int(input('숫자를 입력하세요: '))

# if (number % 2 == 0) and (number != 0):
#     print(f'{number} 은/는 짝수입니다.')
# elif number % 2 != 0:
#     print(f'{number} 은/는 홀수입니다.')
# else:
#     print('0을 입력하였습니다.')

# if number % 2:
#     print('홀수입니다.')
# else: 
#     print('짝수입니다.')

# Boolean: True(1) / False(0)


# kor = int(input('국어: '))
# eng = int(input('영어: '))
# math = int(input('수학: '))
# sci = int(input('과학: '))

# if kor >= 90 and eng > 80 and math > 85 and sci >= 80:
#     print(True)
# else:
#     print(False)


prices = input('물품 가격을 입력하세요: ')

# 1. 가격을 ; 기준으로 나누기
price_lists = prices.split(';')

# 2. 리스트 요소를 숫자로 바꾸기
boxes = []
for price_list in price_lists:
    boxes.append(int(price_list))

# 3. 내림차순으로 sorting
boxes.sort(reverse=True)


# 4. print
for box in boxes:
    print(box)