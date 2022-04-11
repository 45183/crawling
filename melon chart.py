import requests
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
hdr = {'User-Agent':user_agent}

url = "https://www.melon.com/chart/index.htm"
resp = requests.get(url, headers=hdr)
soup = BeautifulSoup(resp.content, 'html.parser')

song_list = soup.find_all('div', 'ellipsis rank01')             # 차트 곡 제목
artist_list = soup.find_all('span', 'checkEllipsis')             # 가수 이름

file = open('melon chart top 100.txt', 'w', -1, 'utf-8')
for i in range(len(song_list)):
    title = song_list[i].text.strip()
    artist = artist_list[i].text.strip()
    data = ('%d위 %s - %s' % (i+1, artist, title))
    file.write(data + '\n')
file.close()