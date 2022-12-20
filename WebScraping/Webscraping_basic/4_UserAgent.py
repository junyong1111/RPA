import requests
url = "https://ceo.yapen.co.kr/"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

res = requests.get(url, headers= headers)
print("응답코드 확인 ", res.status_code)
res.raise_for_status() 

with open("./yapendata.html", "w", encoding= 'utf8') as f:
    f.write(res.text)