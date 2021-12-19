# 모듈 사용법 정리
    # math = __import__("math") # 많이 사용하지는 않음
    # import math 
    # import math as 수학
    # from math import  pi, sin
    # from math import *

# sys 모듈
    # import sys

    # print(sys.argv)  # 명령 매개변수

# datetime 모듈
    # from datetime import datetime

    # now = datetime.now()

# time 모듈
    # import time

    # print("A")
    # time.sleep(1)
    # print("B")

# urllib 모듈

# from urllib import request

# target = request.urlopen("http://hanbit.co.kr")
# content = target.read()

# print(content[:100])

# 모듈을 읽어 들입니다.
    # import os

# 현재 폴더의 파일/폴더를 출력합니다.
    # output = os.listdir(".")
    # print("os.listdir():", output)

# 현재 폴더의 파일/폴더를 구분합니다.
    # print("# 폴더와 파일 구분하기")
    # for path in output:
    #     if os.path.isabs(path):
    #         print("폴더 : ", path)
    # else:
    #     print("파일 : ", path)
    
# 모듈을 읽어들입니다
#   import os 
    
# # 폴더를 읽어 들이는 함수
    #def read_folder(path):
    #     print(path)
    #     output = os.listdir(path)
    #     # 폴더의 요소 구분하기
    #     for item in output:
    #         if os.path.isdir(path + "/" + item):
    #         # 폴더라면 계속 읽어 들이기
    #             read_folder(path + "/" + item)
    #         else:
    #         # 파일이라면 출력하기
    #             print('파일 : ', item)
    # read_folder(".")

# ------ 모듈로 날씨 가져오기 ------- #

# 모듈을 읽어드립니다.

    # from urllib import request
    # from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
    # target = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# beautifulsoup을 사용해 웹 페이지를 분석합니다.
    # soup = BeautifulSoup(target, "html.parser")

# Location 태그를 찾습니다.
    # for Location in soup.select("Location"):
# 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
    #     print("시간 : ", Location.select_one("tmef").string) 
    #     print("도시 : ", Location.select_one("city").string) 
    #     print("날씨 : ", Location.select_one("wf").string) 
    #     print("최저기온 : ", Location.select_one("tmn").string) 
    #     print("최고기온 : ", Location.select_one("tmx").string) 
    #     print("-" * 20)

# Flask 모듈

# 모듈 불러오기
    # from flask import Flask

    # app = Flask(__name__)

    # @app.route("/") # 데코레이터
    # def hello():
    #     return "Hello, World!"

# 최대값 최소값
    # 목록 =[1, 52, 273, 32, 99, 101]

    # max = 목록[0]
    # min = 목록[0]
    # for i in 목록:
    #     if max <= i:
    #         max = i
    #     if min >= i:
    #         min = i
    # print(max, "\n", min)

# 모듈을 가져옵니다.
from functools import wraps
 
# 함수로 데코레이터를 생성합니다.
def test(function):
    @wraps(function)
    
def wrapper(*arg, **kwargs):
    print("인사가 시작되었습니다.")
    function(*arg, **kwargs)
    print("인사가 종료되었습니다.")
    return wrapper

