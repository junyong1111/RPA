import re
import requests
from bs4 import BeautifulSoup as bs

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
           "Accept-Language":"ko-KR, ko"}
url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=2022%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84"
res = requests.get(url,headers=headers)
res.raise_for_status()
soup =  bs(res.text, "lxml")

images = soup.find_all("div", attrs ={"class":"thumb"})
# images = soup.find_all("li")
for idx, image in enumerate (images):
    try : 
        title = image.find("img")["alt"]
    except : 
        title = "Title 없음"
        
    imageUrl = image.find("img")["src"]
    if title :
        print(title)
    imgRes = requests.get(imageUrl)
    imgRes.raise_for_status()
    
    with open("rank_{}_{}_.jpg".format(idx+1,title), "wb") as f:
        f.write(imgRes.content) #-- 파일이 가지고 있는 정보를 씀
        if idx == 4:
            break
