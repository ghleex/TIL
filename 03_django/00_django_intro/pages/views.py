# django imports style guide
# 1. standard library: 내장 모듈
# 2. third-party
# 3. django
# 4. local django

import random
from django.shortcuts import render

# Create your views here.
def index(request): # 첫 번째 인자는 반드시 request
    return render(request, 'index.html')


def introduce(request):
    return render(request, 'introduct.html')


def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)


def image(request):
    return render(request, 'images.html')


# variable routing
# 동적 라우팅: 주소 자체를 변수처럼 사용
def hello(request, name):    
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick}
    return render(request, 'hello.html', context)

