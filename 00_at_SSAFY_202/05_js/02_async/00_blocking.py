from time import sleep


def sleep_3s():
    sleep(3)
    print('Wake up!')


print('Start sleeping')
sleep_3s()
# 위 함수가 끝날 때까지 아래 print 는 실행되지 않음; 동기식 처리 모델
print('End of program')
