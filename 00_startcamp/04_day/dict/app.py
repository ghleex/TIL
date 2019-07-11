import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# 1. 로또 회차와 내 번호 입력 페이지
@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

# 2. 로또 결과
@app.route('/lotto_result')
def lotto_result():
    # 1. 회차 번호 받아오기
    num = request.args.get('num')
        # 여기서 request는 Flask의 그것임
    # 2. 동행복권 웹사이트에 요청 보낸 후 응답 받음
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    # 3. json형태로 바꾸어준다.(chrome에서 보는 결과와 동일한 형태)
    lotto = res.json()

    # 4. 6개 당첨번호 가져오기
    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    # 5. 본인 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        # 여기서 num은 int가 아닌 str형이므로 형변환 필요
        numbers.append(int(num))

    # 6. 몇 개가 일치하는지 확인(교집합 몇 개?)
    # 나의 번호가 당첨 번호 리스트(winner)에 있는지 확인
    matched = 0    
    for num in numbers:
        if num in winner:
            matched += 1
    if matched == 6:
        result = '1등입니다! 대박'
    elif matched == 5:
        if lotto['bnusNo'] in num:
            result = '2등입니다! 1등 아까비'
        else:
            result = '3등입니다! 보너스....'
    elif matched == 4:
        result = '4등입니다! 오만원'
    elif matched == 5:
        result = '5등입니다! 오천원'
    else:
        result = '꽝!'

    return render_template('lotto_result.html',
                            winner=winner,
                            numbers=numbers,
                            result=result)
