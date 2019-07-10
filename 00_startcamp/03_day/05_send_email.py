import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD: ')
# 네이버 2단계 보안 사용하는 경우 별도 비밀번호 발급 필요

msg = EmailMessage()
msg['Subject'] = '파이썬을 이용한 메일 보내기'
msg['From'] = 'glee378@naver.com'
msg['To'] = 'ghleex@gmail.com'
msg.set_content('이거 보면 성공이다')

#여러 사람
to_mail_list = ['glee378@gmail.com', 'ghleex@gmail.com']

for email in to_mail_list:
    msg = EmailMessage()
    msg['Subject'] = '파이썬을 이용한 메일 보내기'
    msg['From'] = 'glee378@naver.com'
    msg['To'] = email
    msg.set_content('이거 보면 성공이다')

    ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
    ssafy.login('glee378', password)
    ssafy.send_message(msg)

#또는
msg = EmailMessage()
msg['Subject'] = '파이썬을 이용한 메일 보내기'
msg['From'] = 'glee378@naver.com'
msg['To'] = 'glee378@gmail.com', 'ghleex@gmail.com'
msg.set_content('이거 보면 성공이다')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('glee378', password)
ssafy.send_message(msg)

print('이메일 전송 완료')