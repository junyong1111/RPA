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
        
