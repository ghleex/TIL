# django imports style guide
# 1. standard library: 내장 모듈
# 2. third-party
# 3. django
# 4. local django

import random
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request): # 첫 번째 인자는 반드시 request
    return render(request, 'index.html')


def introduce(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'introduct.html', context)


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


def times(request, num1, num2):
    mul = num1 * num2
    context = {'num1': num1, 'num2': num2, 'times': mul,}
    return render(request, 'times.html', context)


def area(request, r):
    area = (r ** 2) * 3.14
    context = {'area': area, 'r': r,}
    return render(request, 'area.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕' ,'양장피',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)

def isitgwangbok(request):
    datetimenow = datetime.now()
    context = {'datetimenow': datetimenow}
    return render(request, 'isitgwangbok.html', context)


def isitgwangbok2(request):
    today = datetime.now()
    if datetime.month == 8 and datetime.day == 15:
        result = True
    else:
        result = False
    context = {'result': result}
    return render(request, 'isitgwangbok2.html', context)