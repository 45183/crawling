import csv

# 추가 모드 옵션 'a' 사용
f = open('./example.csv', 'a', newline = '')

wtr = csv.writer(f)

wtr.writerow(['바둑', 40, '파이썬'])
wtr.writerow(['오목', 50, 'C'])

f.close()