import requests
# res = requests.get("https://ceo.yapen.co.kr/")
res = requests.get("https://ceo.yapen.co.kr/")
print("응답코드 확인 ", res.status_code) #-- 200이면 정상

res.raise_for_status() #-- 올바르게 데이터를 가져오지 못하면 에러 발생
print(len(res.text))

with open("./yapendata.html", "w", encoding= 'utf8') as f:
    f.write(res.text)