from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # return "Hello World!"
    return render_template('index.html')


@app.route('/ssafy')
def ssafy():
    return "This is SSAFY!"


@app.route('/dday')
def dday():
    # 오늘 날짜
    today_time = datetime.now() # 현재 일시 가져오기
    # 수료일
    endgame = datetime(2019, 11, 29)
    # 수료일 - 오늘 날짜
    dday = endgame - today_time

    return f'{dday.days} 일 남았습니다.'


@app.route('/html')
def html():

    return '<h1>This is HTML TAG.</h1>'


@app.route('/html_line')
def html_line():
    
    return """
    <h1>여러 줄을 보내봅시다</h1>
    <ul>
        <li>가나다라마</li>
        <li>바사아자차</li>
    </ul>
    """


# variable routing
# @app.route('/greeting/<string: name>')
@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name=name)


# 연산하기
@app.route('/cube/<int:number>') # int형 명시
def cube(number):
    # number3 = number ** 3
    # return f'{number}의 세제곱은 {number3}입니다.'
    rslt = number ** 3
    # 연산을 모두 끝내고 결과값을 cube.html에서 출력
    return render_template('cube.html', input=number, opt=rslt)


@app.route('/lunch/<int:ppl>')
def lunc(ppl):
    # 인원 수가 많아도 중복으로 나오기 가능
    menu = ['코코넛레드누들', '막국수', '닭갈비', '쌈밥', '죽']
    lunch = [random.choice(menu) for i in range(ppl)]
    return f'오늘의 메뉴: {lunch}'


@app.route('/supper/<int:people>')
def supper(people):
    menu = ['코코넛레드누들', '버거킹', '치킨', '돼지곱창', '갈비', '쌈밥']
    order = random.sample(menu, people)
    return str(order)


# render template: 위의 예시를 수정하였음


@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨', '알라딘', '기생충', '엔드게임']
    return render_template('movie.html', movies=movies)


# ping.html
@app.route('/ping')
def ping():
    return render_template('ping.html')


# pong.html
@app.route('/pong')
def pong():
    print(request)
    name = request.args.get('data')
    # name에는 ping.html의 data form에 입력된 값이 할당됨
    return render_template('pong.html', name=name)


# fake naver / fake google
# https://search.naver.com/search.naver?query=
@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/bonbon')
def bonbon():
    
    return render_template('bonbon.html')


@app.route('/bonres')
def bonres():
    name = request.args.get('name')
    character = ['매력', '돈복', '체력', '그지력', '똘끼', '지능', '원시력']        
    personalitys = random.sample(character, 3)
    return render_template('bon_result.html', name=name, personalitys=personalitys)

# @app.route('/godmademe')
# def godmademe():
#     name = request.args.get('name')
#     first_list = ['잘생김', '못생김', '어중간한']
#     second_list = ['자신감', '쑥스러움', '애교', '잘난척']
#     third_list = ['허세', '돈복', '식욕', '물욕', '성욕']
    
#     first = random.choice(first_list)
#     second = random.choice(second_list)
#     third = random.choice(third_list)
    
#     return render_template('godmademe.html', name=name, first=first, second=second, third=third)
