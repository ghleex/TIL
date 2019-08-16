# django imports style guide
# 1. standard library: 내장 모듈
# 2. third-party
# 3. django
# 4. local django

import random
from datetime import datetime
from pprint import pprint
import requests
from django.shortcuts import render


# Create your views here.
def index(request): # 첫 번째 인자는 반드시 request
    return render(request, 'pages/index.html')


def introduce(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'pages/introduct.html', context)


def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)


def image(request):
    return render(request, 'pages/images.html')


# variable routing
# 동적 라우팅: 주소 자체를 변수처럼 사용
def hello(request, name):    
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick}
    return render(request, 'pages/hello.html', context)


def times(request, num1, num2):
    mul = num1 * num2
    context = {'num1': num1, 'num2': num2, 'times': mul,}
    return render(request, 'pages/times.html', context)


def area(request, r):
    area = (r ** 2) * 3.14
    context = {'area': area, 'r': r,}
    return render(request, 'pages/area.html', context)


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
    return render(request, 'pages/template_language.html', context)

def isitgwangbok(request):
    datetimenow = datetime.now()
    context = {'datetimenow': datetimenow}
    return render(request, 'pages/isitgwangbok.html', context)


def isitgwangbok2(request):
    today = datetime.now()
    if datetime.month == 8 and datetime.day == 15:
        result = True
    else:
        result = False
    context = {'result': result}
    return render(request, 'pages/isitgwangbok2.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    # request 라는 요청 속에 데이터가 저장되어 있음
    # 저장된 데이터를 통해서 throw catch
    # pprint(request)
    # pprint(request.scheme)
    # pprint(request.path)
    # pprint(request.method)
    pprint(request.GET)
    # pprint(request.META)
    message = request.GET.get('message')    # 없으면 None 반환
    # request에서 받아온 message를 catch 페이지로 넘겨줄 것임
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)


def art(request):
    return render(request, 'pages/art.html')


def result(request):
    # 1. art 에서 form 으로 보낼 데이터 받기
    word = request.GET.get('word')

    # 2. ARTII API fonts_list 에 요청 보내어 text 로 응답 받기
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    # 3. string을 리스트로 바꿈(랜덤으로 돌려서 url에 붙여주기 위하여 리스트로 바꾸는 것임)
    fonts = fonts.split('\n')

    # 4. fonts list 안에 들어 있는 요소 중 하나를 선택하여 변수에 저장
    font = random.choice(fonts)

    # 5. 위에서 만든 word 와 font 를 이용하여 요청을 다시 만들어 보낸 후 응답 받기
    # .text 안 붙이면 객체 자체가 되므로 꼭 붙이자
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text    

    context = {'response': response,}

    return render(request, 'pages/result.html', context)
    
# 아래는 POST 방식을 이용한 것임
def user_new(request):
    return render(request, 'pages/user_new.html')


def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,}
    return render(request, 'pages/user_create.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')

