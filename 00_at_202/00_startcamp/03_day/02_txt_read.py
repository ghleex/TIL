# read(): 개행문자를 포함한 하나의 문자열을 읽어들임
with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    # print(all_text)

# readlines(): 파일의 모든 라인을 개별로 읽어서 개별 행을 요소를 list로 만들어 냄
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
    # print 자체에도 개행 기능이 있음
    # '문자열'.strip: 앞뒤의 모든 빈 공백을 지워줌
    # 뒤에 어떤 함수를 사용할 수 있는가? dir() 함수 활용!
        # print(dir(line))

