import requests
from bs4 import BeautifulSoup


def scrape_weather(): # [오늘의 날씨]
   
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    cast = soup.find("p", attrs={"class" : "cast_txt"}).get_text()
    curr_temp = soup.find("p", attrs={"class" : "info_temperature"}).get_text().replace("도씨", " ")
    min_temp = soup.find("span", attrs={"class" : "min"}).get_text()
    max_temp = soup.find("span", attrs={"class" : "max"}).get_text()

    moring_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()

    print("[오늘의 날씨]")
    print("현재 {} (최저 {} / 최고{})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(moring_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))

if __name__ == "__main__":
    scrape_weather()