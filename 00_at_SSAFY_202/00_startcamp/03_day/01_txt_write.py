# 1. 변수에 만들고 싶은 파일을 open() 해야 한다.
# open() 시.. r: 읽기 / w: 쓰기(덮어쓰기) / a: 추가

# 1~10까지 한 줄씩 입력되도록 파일을 만들 것
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')
f.close()

# with 구문 (context manager): 더욱 직관적임
with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line {i+1}.\n')

# writelines(): list를 넣어주면, 요소 하나 당 한 줄씩 작성
with open('ssafy.txt', 'w') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])



# escape문자
# \n: 개행문자(다음 줄 이동)
# \t: 탭
# \\: "\" 출력 backward-slash
# \': ' 출력
# \": " 출력
