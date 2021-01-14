### 모듈
import theater_module # 같은 폴더 안에 있어야지 사용가능
theater_module.price(3)
theater_module.price_moring(4)

import theater_module as mv
mv.price(3)
mv.price_moring(4)

from theater_module import *
price(3)
price_moring(4)

from theater_module import price_moring as price
price(4)

### 패키지
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

### __all__(init에서 사용)
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

### 모듈 직접 실행
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

### 패키지 모듈 위치
import inspect
import random
print(inspect.getfile(random)) # C:\Python39\lib\random.py

### pip install
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
instal; :pip install beautifulsoup4
show : pip show beautifulsoup4
upgrade : pip --upgrade beautifulsoup4
uninstall : pip uninstall beautifulsoup4

### 내장함수
# https://docs.python.org/ko/3/library/functions.html

# input
lanuage = input("lanuage?")
print("language : {0}".format(lanuage))

#dir 
print(dir())
import random
print(dir())
import pickle
print(dir())
print(dir(random))
lst = [1,2,3]
print(dir(lst))

### 외장함수
# https://docs.python.org/3/py-modindex.html
# glob : 파일 목록 조회
import glob
print(glob.glob("*.py"))

# os : 운영체제 제공 기본 기능
import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재")
    os.rmdir(folder)
    print("폴더 삭제")
else:
    os.makedirs(folder)
    print("폴더 생성")

print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print( "today :", datetime.date.today())

#timedelta
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("100일 :", today + td)