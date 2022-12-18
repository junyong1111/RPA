import requests
from bs4 import BeautifulSoup as bs

url = "https://ceo.yapen.co.kr/"
res = requests.get(url)
res.raise_for_status()

soup =  bs(res.text, "lxml")
# print(soup.title) #-- 타이틀 정보가져오기 
# print(soup.title.get_text()) #-- 타이틀에 텍스트만 가져오기
# print(soup.a.attrs)

info = soup.find("input", attrs={ "class": "yapen-loginInput"})
print(info.attrs)

#-- 다음 형제로 넘어가기
info = info.next_sibling
info = info.find.next_sibling("원하는 태그")
#-- 이전 형제로 넘어가기
info = info.previous.sibling
#-- 한번에 모두 찾기
info = info.find.next_siblings("원하는 태그")