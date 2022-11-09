# 221109

# 리스트 함수의 key 키워드 매개변수

# 리스트에 포함되어 있는 요소 중
# 최대, 최소를 구하는 함수
# min() max()

listx = [1,2,4,5,6,7,8]
print(min(listx))
print(max(listx))

dictx = {"다": "100", "2":"200","가":"300"}
print(min(dictx)) # 키값비교
print(max(dictx))

# 339 예제

books= [
    {
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
    },
{
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
    },
{
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
    }
]

def pay(book):
    return book["가격"]

print("# 가장 저렴한 책")
print(min(books, key=pay)) # 콜백함수
print()

print("# 가장 비싼 책")
print(max(books, key=lambda book: book["가격"])) # 람다함수
print()
# 람다함수
# lambda 매개변수 : 리턴값
# lambda 매개변수1,매개변수2: 매개변수1+매개변수2

print("# 가격 오름차순 정렬")
books.sort(key=lambda book:book["가격"])
for book in books:
    print(book)

print()

# 스택 stack

# 기본자료형 : 형태가 정형화 되어있다.
# 숫자 4바이트
# 문자 1바이트
# 불 T F 1바이트

###############################################################################
# 힙 heap

# 객체자료형 : 형태가 불규칙하다.
# 리스트
# 딕셔너리
# 튜플
z = 100
print(z)
print(type(z))
print(id(z))
print()


x = [1,2,3,4]
print(x)
print(type(x))
print(id(x))
print()

y = {1: 100,2: 200,3: 300,4: 400}
print(y)
print(type(y))
print(id(y))

# 주소 : 레퍼런스

# 345  예제
def f1(b):
    c = 10

a = 10
f1(a)

# b c 함수 아래 존재하는 것들
# a 전역에 존재하는 것

# 347 예제
def object_change1(d): # 주소값을 전달받음
    d.append(4) # 전달받은 주소값에 있는 데이터에 append해라

c = [1,2,3] # c는 주소값을 갖고 있다.
print(c)
object_change1(c)
print(c)
print()

# 변수 c에 들어있는 값은 힙에 존재하는 리스트 위치를 나타내는 '주소'

a = 10
print(id(a))
def f(b):
    a = b # 얘는 됨
    print(a)
    print(id(a))
    #a = 20 얘는 함수스택으로 들어감, 새로 선언되는 것

f(a)

# 함수 내부에서 함수 외부에 있는 변수 a를 출력
# 변수 a 스택에 있는 값을 교체

x = [1,2,3]
def ff():
    print(x)
    x.append(4)

ff()

print(x)

# x.append(4) : 힙에 있는 리스트를 변경, 스택의 값을 교체하지 않음
# x = [1,3,4,5] => x에 [1,3,4,5]를 할당
# => 변수 x의 스택에 있는 주소값을 교체하려는 시도

a = 10
b = a # a = 10 에 대한 백업역할을 함
print("================================================")
print(id(a))
def f(b):
    global a
    print(a)

    a = 20
    #a = 20 얘는 함수스택으로 들어감, 새로 선언되는 것

f(a)
print(a)
print(id(a))
print(id(b))

# 352부터 문제
# 1번
# numbers = [1,2,3,4,5,6]
#
#
# print("::".join(str(numbers).split(",")))

# 2번
# numbers = list(range(1,10 + 1))
#
# # 홀수 추출하기
# def is_odd(numbers):
#     listy = []
#     for i in numbers:
#         if i % 2 == 1:
#             listy.append(i)
#         else:
#             continue
#     print(listy)
#
# # 3 이상 7 미만 추출하기
#
# def plus_three(numbers):
#     listy = []
#     for i in numbers:
#         if 2 < i < 7:
#             listy.append(i)
#         else:
#             continue
#     print(listy)
#
# # 제곱해서 50미만 추출
# def pow_minus_fifty(numbers):
#     listy = []
#     for i in numbers:
#         if i * i < 50:
#             listy.append(i)
#
#     print(listy)
#
# print("# 홀수만 추출하기")
# print(list(filter(is_odd(numbers),numbers)))
# print()
#
# print("# 3이상, 7 미만 추출하기")
# print(list(filter(plus_three(numbers), numbers)))
# print()
#
# print("# 제곱해서 50 미만 추출하기")
# print(list(filter(pow_minus_fifty(numbers), numbers)))

x = 10 # x 10
y = x # y 10
x = x + 1 # x 11
z = 10 # y랑 같음 10이라는 객체가 이미 생성이 돼서
zz = 11  # x랑 같음
print("zz => ",id(zz))
zz = zz - 1 # y랑 같음
print("zz => ",id(zz))
zz = 9
print("zz => ",id(zz))
# def m(x):
#     z = x
#     print(z)
#
# m(y)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("x => " ,id(x))
print("y => " ,id(y))
print("z => " ,id(z))
print("zz => ",id(zz))

print(type(y))

# 파이썬의 모든 것은 객체이다.
# 변수에 특정 데이터를 할당하면
# 예를 들어 x = 100 을 실행하면
# 100 숫자객체가(object) 생성돼
# x가 100숫자 객체를 가리키도록 설정하는 것

# 그래서 type으로 숫자객체를 출력해보면
# class int

# class 추상적 객체를 만드는 규격
# object 구체적인 (가리킬 수 있는 , 지목할 수 있는, 고착화된) 결과물

def my2(x):
    x = x + 1
    print("my2의 x =>", id(x))
    return x
def my1(x):
    x = x * 2
    print("my1의 x =>", id(x))
    y = my2(x)
    print("my1의 y =>", id(y))
    return y
y = 5
z = my1(y)

print("z의 id =>",id(z))
# 주소값이 같은게 3개..객체가 생성되면 전역이든 지역이든 같은 주소값을 가리킴

# 1. 전역 y = 5할당
# y로 my1을 호출
# 스택에 my1()함수에 대한 영역이 생성

# my1에서 x- x*2 식을 통해 숫자 객체 10 생성
# x는 10을 가리킨다

# 스택에 my2() 영역이 생성
# x = x + 1 숫자 객체 11이 생성
# y 는 11 숫자 객체를 가리킨다.

# 메모리(RAM)의 4 구조

# 1. 코드영역(텍스트영역)
# 실행하려는 프로그램의 코드가 저장되는 영역
# cpu가 코드 영역을 읽어 처리

# 2. 데이터 영역
# 전역변수가 저장되는 영역
# 프로그램 시작 동시에 할당, 프로그램이 종료되면 소멸

# 3. 스택영역
# 함수변수, 지역변수, 매개변수 등
# 지역 요소의 호출과 함께 할당
# 함수 호출이 종료되면 소멸
# 후입선출

# 4. 힙영역
# 데이터 객체들의 할당 공간
# 선입선출

# 3,4 힙과 스택영역은 같은 공간을 서로 공유해서 나눠쓴다. 유동성이 있다.

# stack overflow : stack영역이 heap영역을 침범
# heap overflow : heap영역이 stack영역을 침범
import sys
sys.setrecursionlimit(10**6)
def func1(n):
    print(n)
    return func1(n + 1)
func1(1)


a1 = 10
a2 = 10
print("///////////////////////////////////////////////////////")
print(id(a1))
print(id(a2))


def mm():
    x1 = 9
    x2 = 17
    x3 = 13

    print(id(x1))
    print(id(x2))
    print(id(x3))

mm()

