import os

# 1. 해당 파일들이 있는 위치로 이동
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\change_file_names')

# 2. 현재 폴더 안에 모든 파일 이름 수집
filenames = os.listdir('.')

# 3. 반복문을 통해 각각의 파일명 변경하기
# for filename in filenames:
#     os.rename(filename, f'SAMSUNG_{filename}')

# 4. SAMSUNG을 SSAFY로 변경
for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG_', 'SSAFY_'))