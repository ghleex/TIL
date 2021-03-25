# reduce:  반복 가능한 객체에서 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적하여 반환하는 함수

from functools import reduce


def f(x, y):
    return x + y
a = [1, 2, 3, 4, 5]
print(reduce(f, a))
# ((((1 + 2) + 3) + 4) + 5)
# 15

# 위의 함수 f를 lambda를 이용하면 아래와 같음
print(reduce(lambda x, y: x + y, a))

# 다음과 같이 초기값을 주면 초기값부터 계산
print(reduce(lambda x, y: x + y, a, 10))
# 25


# 다양한 형태로 표현 가능
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(5))
# 120