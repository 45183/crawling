import csv

f = open("./example.csv", 'w', newline = '')                
# newline 넣지 않을 경우 데이터 들어갈때마다 행 하나씩 건너뜀
# 길동    철수    영희
# 
# 10      20      30
# 
# 파이썬  C       자바



wtr = csv.writer(f)

# 열 제목 작성
wtr.writerow(['이름', '나이', '언어'])

# 데이터 생성
name_list = ['길동', '철수', '영희']
age_list = [10, 20, 30]
lan_list = ['파이썬', 'C', '자바']

# 각 행에 데이터 작성
for i in range(3):
    name = name_list[i]
    age = age_list[i]
    language = lan_list[i]
    wtr.writerow([name, age, language])

# 파일 닫기
f.close()