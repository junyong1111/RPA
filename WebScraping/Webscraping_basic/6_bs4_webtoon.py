import requests
from bs4 import BeautifulSoup as bs

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

#-- 네이버 웹툰 전체 목록 가져오기
soup = bs(res.text, "lxml")
#-- class 속성이 title인 모든 'a', 요소들을 반환
cartoons = soup.find_all("a", attrs={"class" : "title"})
for cartoon in cartoons:
    title = cartoon.get_text()
    link = "https://comic.naver.com" + cartoon["href"]
    print(title, link)

