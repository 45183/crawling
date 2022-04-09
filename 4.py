import requests
import bs4

URL = "https://browse.gmarket.co.kr/search?keyword=마스크"
# keyword 뒷부분 검색내용

raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

box = html.find('div', {'class' : 'section__module-wrap', 'module-design-id' : '15'})

items = box.find_all('div', {'class' : 'box__item-container'})

for item in items[:10]:
    title = item.find('span', {'class' : 'text__item'})
    price = item.find('strong', {'class' : 'text__value'})
    print("이름 : ", title.text)
    print("가격 : ", price.text)
    print()