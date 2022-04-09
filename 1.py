# 정적 크롤링
# 네이버 웹툰의 요일 별 상위 웹툰 이름

import requests
import bs4

req = requests.get("https://comic.naver.com/webtoon/weekday")
#print(req.text)

html = bs4.BeautifulSoup(req.text, 'html.parser')
#print(html)

columns = html.find_all('div', {'class':'col_inner'})

for column in columns:
    day = column.find('h4').text
    webtoons = column.find_all('a', {'class' : 'title'})[:5]
    print(day)
    for index in range(len(webtoons)):
        title = webtoons[index].text
        print(f"{index+1}. {title}")
    print()