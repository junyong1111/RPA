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