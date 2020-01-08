# DOCstring
"""
문서 자체를 주석 같이 처리함.
함수의 사용설명 등에 사용

다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 reverse_quest.txt 파일로 저장
3
2
1
0
"""
# # 1. 파일 만들기
# with open('quest.txt', 'w') as f:
#     for i in range(4):
#         f.write(f'{i}\n')

# # 2.1. 만든 파일 읽어 들이기
# with open('quest.txt', 'r') as rf:
#     lines = rf.readlines()
#     print(lines)

# # 3.1. 읽은 것을 기반으로 뒤집어서 작성
# with open('reversed_quest.txt', 'w') as wf:  
#     for line in reversed(lines):
#         wf.write(f'{line}')
#         print(line.strip())

# 2.2. 읽어 들이기 다른 방법(아예 리스트 순서를 바꿔버림)
with open('quest.txt', 'r') as rf:
    lines = rf.readlines()
    lines.reverse()
    print(lines)

# 3.2. 역순으로 쓰기
with open('reversed_quest.txt', 'w') as wf:
    # for line in lines:
    #     wf.write(f'{line}')
    #     print(line.strip())
    wf.writelines(lines)