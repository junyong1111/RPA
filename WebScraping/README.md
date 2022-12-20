# WebScraping

- **웹페이지에서 내가 원하는 데이터를 추출하는 행위**

### WebCrawling 차이점

- 웹페이지내에 링크들을 따라가며 모든 데이터를 가져옴
- 다음과 같은 조건이 존재
    - 서점 —> 갑자기 이벤트 당첨 —> 비어있는 카트에 30초동안 모든 책을 담음 —> 가장 윗줄에 책은 담으면 안됨
- 학교시험 —> 필기내용을 한 장의 종이에 적을 수있음 —> 중요한부분만 종이에 적음

웹 크롤링 —> 웹 페이지내에서 허용된 이벤트를 마구잡이로 가져옴

웹 스크랩핑 —> 웹 페이지내에서 원하는 데이터만을 가져옴

### **WEB**

**Web은 3가지 구성요소가 존재하며 집으로 비유한다면 다음과 같다.**

1. **HTML**
    1. **집의 구조 및 뼈대를 만드는 작업** 
    2. 뼈대만 있어도 살수는 있지만 이쁘지는 않음
    3. 거실, 방, 화장실 등 구분정도만 되어있음
2. **CSS**
    1. **인테리어**
    2. 디자인 부분
3. **JS(JavaScrpit)**
    1. 집에서 화장실 이용
    2. 거실에서 음식 및 식사 등등
    3. **웹을 살아있게 만들어 줌**

**webScraping에서는 HTML에 대한 이해정도만 필요로 함**

# - 참고 해당 실습이후 웹페이지 구조가 변할 수 있으므로 따라하는게 아닌 이해가 필요

### HTML(Hyper Text Markup Language)

- **웹페이지를 만들 때 사용하는 언어**

# -Vscode 확장팩에서 open in browser을 입력하여 최상단 확장팩 설치

![스크린샷 2022-12-18 오전 1 25 28 작게](https://user-images.githubusercontent.com/79856225/208252290-76923503-f2c8-4ecd-8a60-9147d112c2f2.jpeg)

![스크린샷 2022-12-18 오전 1 26 56 작게](https://user-images.githubusercontent.com/79856225/208252291-cb2837ee-5850-4adc-beb8-ae02775638be.jpeg)


# -Webscraping_basic 폴더를 생성하고 실습 진행

- 1_HTML.html 파일 생성

**HTML은 태그로 구성되어 있다.**

- **<html></html> 태그**
    - html의 시작과 끝을 알려주는 태그
- **<head></head>태그**
    - 웹페이지에 제목을 선언
- **<body></body>태그**
    - 웹페이지에 본문을 정의하는 부분

```html
<!DOCTYPE html> <!--현재 문서는 html로 작성되었다는 의미-->
<html lang="ko">  <!--html문서로 시작하고 언어를 한국어로 설정-->
<head> <!--브라우저의 정보입력 시작-->

    <meta charset="UTF-8"> <!--meta정보를 입력-->
    <title> 타이틀을 입력해주세요 </title> <!--주소탭에 지정될 타이틀-->
    <body> <!--문서 내용입력 시작-->
        <h1>문서의 내용을 입력해주세요.</h1>
    </body> <!--문서 내용입력 끝-->   
</head> <!--브라우저의 정보입력 끝-->
```

**로그인 페이지 만들기**

- **<input> 태그**
    
    <img width="755" alt="스크린샷 2022-12-18 오전 1 38 41" src="https://user-images.githubusercontent.com/79856225/208252293-0d7e7f61-9c91-48b2-9432-07f3f596cd32.png">
    
    ```html
    <body> <!--문서 내용입력 시작-->
            <input type="text" value="아이디를 입력하세요">
            <input type="password" value="비밀번호를 입력하세요">
            <input type="button" value="로그인">
    </body> <!--문서 내용입력 끝-->
    ```
    
    <img width="378" alt="스크린샷 2022-12-18 오전 1 39 40" src="https://user-images.githubusercontent.com/79856225/208252294-40cb9b9c-a51a-4d2c-a74b-2650f8fd2512.png">
    
- **<a>태그**
    - 하이퍼링크를 입력하여 해당링크로 연결해주는 태그
    
    ```html
    <a href = "https://github.com/junyong1111/Web/blob/main/Project/Hotel/2022-03-01-Html-기본문법.md">html기본 문법 정리페이지로 이동하기</a>
    ```
### 2. XPATH

- html문서는 보통 복잡한 요소들로 구성되어있다.
- 특정요소의 경로로 연결할 때 사용
    - 비슷한 요소를 지칭할 때 어떠한 요소를 호출하는지 명시해야함
    - 브라우저가 자동으로 알아서 해주므로 따로 걱정x
    - Chrome 브라우저 사용
    

### 3. Requests

- 웹페이지 문서 정보를 가져올 때 사용하는 라이브러리
- 다음 명령어를 터미널에 입력하여 라이브러리 설치

```bash
pip install requests
```

- 2_Requests_basic.py 파일 생성

### 4. 정규식

```python
#-- requests 라이브러리 import 
import requests

#-- requests.get("URL") 함수를 이용하여 원하는 웹페이지 정보 가져오기
res = requests.get("URL")

print("응답코드 확인 ", res.status_code) #-- 200이면 정상
res.raise_for_status() #-- 올바르게 데이터를 가져오지 못하면 에러 발생

#-- 가져온 정보텍스트 길이 확인
print(len(res.text))

#-- 파일로 저장하여 확인
with open("./myUrl.html", "w", encoding= 'utf8') as f:
    f.write(res.text)
```

- 정해진 형태의 식
    - 주민등록번호
        - 000123 - 1xxxxxx
        - abcdef - bbbccc → 이런건 주민번호 형식이 아님
    - 핸드폰 번호
        - 010-xxxx-xxxx
    - 이메일 주소
        - 이메일주소@mail.com
- 3_[**re.py](http://re.py) 파일 생성**
    
    ```python
    #-- 정규식 라이브러리 import
    import re
    
    #-- 4개의 문자 중 3개만 기억이 남 --> ca?e
    
    pattern = re.compile("ca.e") 
    #-- . (ca.e) : 하나의 문자를 의미 --> care, cafe, case...(O) | caffe(X) 등등
    #-- ^ (^de) : 문자열의 시작  --> desk, destination...(O)  | fade(X) 등등 de로 시작하는 문자열을 의미
    #-- $ (se$) : 문자열의 끝 --> case, base... (O) | face(X) 등등 문자열의 끝이 se로 끝나는 것
    
    #-- 매치되지 않다면 에러가 발생
    def print_matchs(matchs):
        if matchs: 
            print("matchs.group() :", matchs.group()) #-- 일치하는 문자열 반환
            print("matchs.string :", matchs.string) #-- 입력받은 문자열 반환
            print("matchs.start() :", matchs.start()) #-- 일치하는 문자열의 시작 Index
            print("matchs.end() : ", matchs.end()) #-- 일치하는 문자열의 끝 Index
            print("matchs.span() : ", matchs.span()) #-- 일치하는 문자열의 시작/끝 Index
        else:
            print("Not Match")  
    
    #-- 비교하는 값이 처음부터 매치되는지 확인
    matchs = pattern.match("caseless") 
    print_matchs(matchs)
    
    #-- 주어진 문자열 중에 일치하는게 있는지 확인
    matchs = pattern.search("good care")
    print_matchs(matchs)
    
    #-- 일치하는 모든것을 리스트형태로 반환
    matchsList = pattern.findall("good care case")
    print(matchsList)
    ```
    

### 5. User Agent

- 사람이 아닌 컴퓨터가 무단으로 접속시 거부가 날 수 있음
- 해당 사이트에서 자신의 User Agent 값 확인 후 복사

[](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)

- 4_UserAgent[**.py](http://re.py) 파일 생성**

```python
import requests
url = "https://ceo.yapen.co.kr/"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

res = requests.get(url, headers= headers)
print("응답코드 확인 ", res.status_code)
res.raise_for_status() 

with open("./yapendata.html", "w", encoding= 'utf8') as f:
    f.write(res.text)
```

### 6. Beautiful Soup4

- 해당 명령어를 터미널에서 실행하여 beautifulsoup4 라이브러리 설치
- 해당 명령어를 터미널에서 실행하여 lxml 라이브러리 설치
    - 어떤 구문을 분석하는 parser

```bash
pip install beautifulsoup4
pip install lxml
```

- **5_bs4.py 파일 생성**
    
    ```python
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
    ```
    

**네이버웹툰에서 원하는 정보 빼오기**

- 6_bs4_webtoon.py 파일 생성
    
    ```python
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
    ```
    

**무신사에서 원하는 정보 빼오기**

- 쿠팡은 크롤링 차단…
- 7_bs4_musinsa.py 파일 생성
- 무신사 숏패딩 중 시즌오프 상품들만 찾아보기
    
    ```python
    import re
    import requests
    from bs4 import BeautifulSoup as bs
    
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"}
    
    for i in range(1,6):
        print("현재 페이지 :",i )
        url = "https://www.musinsa.com/categories/item/002012?d_cat_cd=002012&brand=&list_kind=small&sort=pop_category&sub_sort=&page={}&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=".format(i)
        
        res = requests.get(url, headers= headers)
        res.raise_for_status()
        soup = bs(res.text, "lxml")
    
        items = soup.find_all("li", attrs= {"class":re.compile("^li_box")})
        for item in items:
            sale_badge = item.find("span", attrs= {"class":"icon-reverse label-campaign01"})
            if sale_badge :
                print("시즌 오프 상품")
                itemTitle =  item.find("a", attrs = {"class":"img-block"})
                itemPrice = item.find("div", attrs = {"class":"article_info"})
                # print(item)
                title = itemTitle['title']
                prices = itemPrice.find("p",attrs = {"class":"price"}).get_text().replace(" " , "").strip().splitlines()
                if len(prices) >1:
                    price = prices[0]
                    saleprice = prices[1]
                else:
                    price =prices[0]
                    saleprice = "세일 가격 없음"
                
                link = itemTitle["href"]
                link = link[2:-1]
            
                print("제품명 : ", title)
                print("세일전 가격 : ", price)
                print("세일 가격 : ",saleprice)
                print("상품 링크 : " ,link)
                print("-"*100)
    ```
    

**최신영화 이미지 가져오기**

- 8_bs4_movie.py 파일 생성
    
    ```python
    import re
    import requests
    from bs4 import BeautifulSoup as bs
    
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"}
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
    ```

### 7. CSV로 저장

네이버 금융에서 시가총액 순위로 200위까지를 CSV파일로 저장하기 

- 9_csv_stock.py 파일 생성

### 8. Selenium

- 웹페이지 테스트를 자동화할 수 있는 유명한 프레임워크
- 현재까지 배운 내용으로는 디테일한 작업이 불가능하므로 셀레니움을 사용하여 해결
- 다음 명령어를 사용하여 selenium 설치
    
    ```bash
    pip install selenium
    pip install webdriver_manager
    ```
    
- **셀레니움 사용시 추가적으로 웹 드라이버를 설치해야함**
    - 현재 4.x 버전으로 업그레이드 되면서 코드로 설치 가능
- ~~맥 사용시 해당 드라이버 폴더로 이동 후 다음 명령어 실행~~
    
    ```bash
    ~~xattr -d com.apple.quarantine chromedriver~~
    ```
    
- ~~while문을 사용하여 크롬드라이버가 꺼지는걸 방지해야함~~
- ~~코드를 확인하기 위해서는 터미널에서 한 줄씩 사용하는걸 추천~~
    
    ```python
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    #-- 다음 코드들로 자동으로 설치 가능
    ```
    
- 셀레니움 명령어 문서

[https://wikidocs.net/177133](https://wikidocs.net/177133)

```python
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
browser.get("https://www.naver.com")

browser.find_element(By.ID, "id").send_keys("ID")
#-- 입력 데이터 지우기
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("ID")

browser.find_element(By.ID, "pw").send_keys("PW")
browser.find_element(By.ID, "pw").send_keys(Keys.ENTER)

#-- html 정보 출력

print(browser.page_source)
# browser.close() #-- 현재 탭만 종료
browser.quit() #-- 브라우저 전체 종료

time.sleep(5.0)
```

**—# 로딩때문에 셀레니움이 원하는 데이터를 조회 못할 수 있다 이 때 다음과 같은 코드를 사용**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

try:
	elem = wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "Xpath"))).click()
	#-- 이 값에 해당하는 요소가 나올때까지 최대 10초간 브라우저를 대기 후 클릭하기
	print(elem.text) #-- 결과값 출력
except:
	borswer.quit()
```

—# 셀레니움으로 자바스크립트를 제어해서 스크롤 내리기

```python
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
browser.get("https://www.naver.com"
#-- 2초에 한 번씩
interval = 2

prev_height = browser.ececute_script("return  document.body.scrollHeight)")

while True:
	#-- 화면 가장 아래쪽으로 스크롤 내리기
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
	time.sleep(interval)
	
	#-- 현재 높이 업데이트
	curr_height = browser.ececute_script("return  document.body.scrollHeight)")
	#-- 높이 변화가 없다면 종료
	if curr_height == prev_height:
		break
	prev_height = curr_height
```

—# 브라우저에서 바로 soup객체 만들기

```python
soup =  bs(browser.page_source, "lxml")
```