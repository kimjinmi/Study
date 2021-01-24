import requests
import re
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

for i in range(1, 6):


    url = " https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    print(items[1].find("div",attrs={"class":"name"}).get_text())
    for item in items:

        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            #print("  <광고상품제외>  ")
            continue


        name = item.find("div",attrs={"class":"name"}).get_text()
        
        if "Apple" in name :
            #print("  <Apple상품제외>  ")
            continue

        price = item.find("strong",attrs={"class":"price-value"}).get_text()
        
        rate = item.find("em",attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            #print("  <평점없는상품제외>  ")
            continue
            
        rate_cnt = item.find("span",attrs={"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            #print("  <평점없는상품제외>  ")
            continue

        link = item.find("a",attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >=100 :    
            #print(name, price, rate, rate_cnt)
            print(f"name : {name}")
            print(f"price : {price}")
            print(f"rate : {rate}")
            print(f"rate_cnt : {rate_cnt}")
            print("link : {}".format("https://www.coupang.com" + link))
            print("  ---------------  ")