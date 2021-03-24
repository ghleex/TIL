import functools


def compose2(func1, func2):
    return lambda x: func2(func1(x))


# 순서대로 적용될 함수 리스트
pipes = [lambda x: x + 1, lambda x: x * 2, lambda x: x * 10]

# reduce를 이용하여 func2와 함께 새로운 함수를 만드는 일을 반복
comp_func = functools.reduce(compose2, pipes)

for i, x in enumerate(range(5, 10)):
    print(f'{i}: {comp_func(x)}')


# 0: 120
# 1: 140
# 2: 160
# 3: 180
# 4: 200
# reduce에 대해서, 어떻게 사용하는지 등에 대하여 알 필요가 있음
