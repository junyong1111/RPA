import csv
import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

fileName = "시가총액top200.csv"
f = open(fileName, "w", encoding="utf-8-sig", newline="")
#-- 엑셀에서 한글이 깨지면 encoding ->utf-8-sig 사용
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = bs(res.text, "lxml")
    
    dataRows = soup.find("table", attrs= {"class":"type_2"}).find("tbody").find_all("tr")
    for row in dataRows:
        cols = row.find_all("td")
        if len(cols) <= 1 : #-- 불필요한 데이터 스킵
            continue
        data = [col.get_text().strip() for col in cols]
        # print(data)
        writer.writerow(data)
