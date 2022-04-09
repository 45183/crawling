import bs4
import requests

URL = "https://www.dhlottery.co.kr/gameResult.do?method=byWin"

raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

# print(type(raw.text))       # <class 'str'>
# print(type(html))           # <class 'bs4.BeautifulSoup'>

target = html.find('div', {'class' : 'nums'})
# print(target)

balls = target.find_all("span", {'class' : 'ball_645'})

# for ball in balls:
#     # print(ball)
#      print("당첨번호 : ", ball.text)

# 1. 태그만 사용 하는 경우
# html.find('div')

# 2. 선택자만 사용하는 경우
# html.find(id = 'example1')
# html.find(attrs = {'id':'example1'})

# 3. 태그 이름과 선택자 정보 모두 사용하는 경우
# html.find('div', {'id' : 'example1'})

print("< 최근 로또 당첨 번호 >")
for ball in balls[:-1]:
    print("당첨번호 : ", ball.text)

print("보너스 번호 : ", balls[-1].text)