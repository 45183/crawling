import requests

URL = "https://www.dhlottery.co.kr/gameResult.do?method=byWin"

raw = requests.get(URL)

# print(raw)
# <Response [200]> 출력시 정상
# print(raw.text)

target = '<div class="nums">'

if target in raw.text:
    idx = raw.text.index(target)
    print(raw.text[idx:idx + 578])
    # raw.text[idx:idx + 578] ==> 문자열 슬라이싱 / 로또홈페이지의 nums부분(target)부터 578자리까지 문자열을 가져오라는 뜻