# 221111

# 400
# 모듈

# 표준 모듈 : 내장
# 외부 모듈 : 사용자 정의

# 모듈 ? module : 기능 단위, 독립적으로 운용될 수 있는 단위
# 함수, 클래스를 포함하고 있다.
# 이식
# 독립적
# 인터페이스 일치해야 함

# import datetime

# datetime.datetime.now()

# import math # 수학관련 기능을 가지고 있다.
#
# print(math.sin(1))
# print(math.cos(1))
# print(math.floor(2.5)) # 내림함수, 잘라버림
# print(type(math.floor(2.7)))
# print(math.ceil(2.3)) # 올림함수
#
# # 실수 정수변환 int로 처리했었는데 floor써서 소수점 뒤에 잘라버릴 수 있음
# print(round(2.51)) # 반올림

# import 방식

# from 키워드 사용

# from 모듈명 import 가져오려는 클래스 or 함수 or 변수

# from math import sin # sin만 쓸 수 있음
# from math import * # math 에 있는 거 전부 불러오고 math찍지 않고 사용가능

# from datetime import datetime
#
# datetime.now()

# as 키워드
# 모듈을 불러올 때 이름이 충돌하는 경우
# 새로운 이름을 부여
#
# import math as m # m 으로 부르겠다.
# m.floor()

# import random
#
# print("# random 모듈")
#
# print("- random(): ", random.random())
#
# print("- uniform(10,20: ", random.uniform(10,20))
#
# print("- randrange(10): ", random.randrange(10))
#
# print("- choice([1,2,3,4,5]): ", random.choice([1,2,3,4,5]))
#
# print("- suffle([1,2,3,4,5]): ", random.shuffle([1,2,3,4,5]))
#
# print("- sample([1,2,3,4,5], k = 2: ", random.sample([1,2,3,4,5],k=2))

# sys모듈
# os 모듈
# import sys
# print("=====================================================================")
# print()
# print(sys.argv[0]) # sys.argv의 0번째 인자에는 python실행파일 경로가 담겨있다.
#
# print("---")
# print("getwindowsversion: ", sys.getwindowsversion())
# print("---")
# print("copyright: ", sys.copyright)
# print("---")
# print("version: ", sys.version)
# print("======================================================================")
# print()
# print(len(sys.argv))
# for arg in sys.argv:
#     print(arg)
# sys.exit()

# f = open("근로소득간이세액표.txt","r") # 상대경로

# 절대경로
# f = open("C:/Users/16/Desktop/파이/PythonProjectJYW/venv/221111.py/근로소득간이세액표.txt","r")
#
# # 바탕화면에 문서 있는 거 속성 들어가면 백슬래시로 뜨는데 가져와서 슬래시로 바꿔줘야함
#
# import os
#
# print("현재 운영체제: ", os.name)
# print("현재 폴더: ", os.getcwd()) # !!! 절대경로 쓸때!!!
# print("현재 폴더 내부의 요소: ", os.listdir())
#
# os.mkdir("hello") # 폴더 만듦
# os.rmdir("hello") # 폴더 제거
#
# with open("original.txt", "w") as file:
#     file.write("hello")
# os.rename("original.txt", "new.txt")
#
# os.remove("new.txt")
#
# os.system("dir") # 안에 있는 통합적인 정보들 불러오는 것, 별로 쓸모없음

# import datetime
# print("# 현재시간 출력하기")
# now = datetime.datetime.now()
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print()
#
# print("# 시간을 포맷에 맞춰 출력하기")
# output_a = now.strftime("%y.%m.%d %H:%M:%S")
# output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute, now.second)
#
# output_c = now.strftime("%y{}%m{}%d{} %H{}%M{}%S{}").format(*"년월일시분초") # *찍으면 하나씩 들어감
# print(output_a)
# print(output_b)
# print(output_c)
# print()

# import datetime
# now = datetime.datetime.now()
#
# print("# datetime.timedelta로 시간 더하기")
# after = now + datetime.timedelta(weeks=1, days=1, hours=1,minutes=1,seconds=1)
#
# print(after.strftime("%y{} %m{} %d{} %H{} %M{} %S{}").format(* "년월일시분초"))

# time모듈은 특정 시간동안 코드 진행을 정지할 때 사용

# import time as t
# print("지금부터 정지")
# t.sleep(5)
# print("프로그램 종료")

# from urllib import request
# target = request.urlopen("https://google.com")
# output = target.read()
#
# from operator import itemgetter
#
# books = [
#     {
#     "제목": "혼자공부하는 파이썬",
#     "가격": 18000
#     },
#     {
#         "제목": "혼자공부하는 자바",
#         "가격": 26000
#     },
#     {
#         "제목": "혼자공부하는 머신",
#         "가격": 24000
#     }
# ]
#
# print("#가장 저렴한 책")
# print(min(books, key=itemgetter("가격")))
# print()
#
# print("#가장 비싼 책")
# print(max(books, key=itemgetter("가격")))

# 420


import os
output = os.listdir(".")
print("os.listdir(): ", output)
print()

print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더: ", path)
    else:
        print("파일", path)
print("===================================================================")
print()

def read_folder(path):
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else:
            print("파일: ", item)

read_folder(".")

from primePy import primes

print(primes.between(100,1000))

