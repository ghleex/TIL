from flask import Flask, render_template, request
import requests
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello():
    return 'Hi there!'


@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')


# webhook 역할하는 함수 설정(아무나 받으면 안되므로 token을 넣어줌)
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 1. 데이터 구조 terminal에 출력(telegram이 flask로)
    from_telegram = request.get_json()

    # 메시지 내용 비어 있으면 보낼 필요 없음
    if from_telegram.get('message') is not None:
        # 2. echoing(bot to person) / 에러나지 않도록 .get()사용
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        
        # 3. 한글 키워드 받기("/한영 "을 입력했을 때 파파고 번역 동작)
        if text[0:4] == '/한영 ':
            print("ok")
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            source_lang = 'ko'
            target_lang = 'en'
            data = {'source': source_lang, 'target': target_lang, 'text': text[4:]}
            
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') # 번역 결과

        if text[0:5] == '/한중번 ':            
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            source_lang = 'ko'
            target_lang = 'zh-TW'
            data = {'source': source_lang, 'target': target_lang, 'text': text[5:]}
            
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') # 번역 결과

        if text[0:5] == '/한중간 ':            
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            source_lang = 'ko'
            target_lang = 'zh-CN'
            data = {'source': source_lang, 'target': target_lang, 'text': text[5:]}
            
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') # 번역 결과

        if text[0:4] == '/한불 ':            
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            source_lang = 'ko'
            target_lang = 'fr'
            data = {'source': source_lang, 'target': target_lang, 'text': text[4:]}
            
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') # 번역 결과


        if text[0:4] == '/로또 ':
            
            # 1. 회차 번호 받아오기
            num = text[4:]                    
            # 2. 동행복권 웹사이트에 요청 보낸 후 응답 받음
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            # 3. json형태로 바꾸어준다.(chrome에서 보는 결과와 동일한 형태)
            lotto = res.json()

            # 4. 6개 당첨번호 가져오기(빈 리스트 만들어서 하나씩 추가하기)
            winner = []
            for i in range(1, 7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            text = f'로또 {num}회 당첨번호는 {winner}입니다. 보너스 번호는 {bonus_num}입니다.'

        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return '', 200


