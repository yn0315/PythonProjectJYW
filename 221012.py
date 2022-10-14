# format 함수 대신 f문자열 포매팅 방법 활용하기
# 3.6버전부터 f문자열 포매팅 기능 생겼다.

# 문자열 앞에 f 접두사를 붙여서 사용

name = "학생1"
age = 20

print(f'나의 이름은 {name}이고 나이는 {age}이다.')
# 접두사 f 포매팅 방법은 name, age 와 같은 변수를 참조할 수 있다.

print("나의 이름은 "+ name +"이고 나이는 " + str(age) +"이다.")

# 변수에 데이터 형태를 가리지 않고 문자열로 변환한다.

pi= 3.141592
print(f'{pi:0.4f}') # 소수점 4자리까지 표현
print(f'{pi:10.3f}') # 총 자리수 10에 소수점 3자리까지 표현
print(f'{pi:0.1f}') # 소수점 1자리까지 표현

# 문자열 관련 함수
# count() 함수
# 문자의 개수 카운트

str1 = 'hello'
print(str1.count('l')) # find함수는 위치, 이건 개수 찾는 함수
# find()함수는 위치를 찾아준다

print(str1.find('x'))
# find 함수에서 찾는 문자열이 없는 경우에는 -1을 반환한다.

# index()함수
# 위치를 알려준다.

str2 = "life is too short"
print(str2.find('ta'))
# print(str2.index('ta')) # 공백 붙여쓰면 에러남, 없는 것 찾을 때도 find랑 다르게 에러 뜸

# 문자열 관련 함수
# join()
# 문자열 삽입
str3 = "o"
print(str3.join("hello"))

# 문자열 관련 함수
# replace()
# 문자열 바꾸기 함수

str4 = 'life is too short'
print(str4.replace("life", 'abce'))
#         바꾸고 싶은 문자열, 바꿀 문자열
# 전처리 = 불필요한 텍스트를 지우거나 변환하는 행위

# 반지름, 겉넓이 문제
# pi = 3.141592
# r = int(input('구의 반지름을 입력해주세요: '))
# volume = 4/3 * (pi*r**3)
# area = 4 * (pi*r**2)
#
# print(f'구의 부피는 {volume}입니다.')
# print(f'구의 겉넓이는 {area}입니다.')

# 피타고라스 정리
# a = float(input('밑변의 길이를 입력해주세요: '))
# b = float(input('높이의 길이를 입력해주세요: '))
# c = (a**2 + b**2) **(1/2)
#
# print(f'빗변의 길이는 {c}입니다.')

# 조건문
# if 조건문
# 불/불리언/불린 Bool
# 불은 True / False
# 참 / 거짓

print(True)
print(type(True))
print(type(False))

# 비교연산자

# 같다 ==
# 크다 >
# 작다 <
# 작거나 같다 <=
# 크거나 같다 >=
# 같지 않다 !=

print(10 < 5)
print(10 > 5)
print(10 <= 10)
print(5 == 10)
print(10 != 9)

print("가방" == "가방")
print("가방" == "하마")
print("가방" < "하마") # True

# 사전 순으로 비교
print("a" < "c")

# 비교연산자로 범위 비교
x = 20
print(10 < x < 30)
print(40 < x < 50)

# 불 사이의 논리 연산

# 논리 연산자 종류
# 1. not : 아니다의 뜻
# 2. and : 그리고의 뜻
# 3. or : 또는의 뜻

# 단항 연산자와 이항 연산자
# 단항 연산자는 피연산자가 한 개 : -10의 마이너스
# 이항 연산자는 피연산자가 두 개 : 10 + 10

# not은 단항 연산자
print(not True)
print(not False)

# 반대로 바꿀 때 사용한다

x = 10
under_20 = x < 20 # under_20 = (x < 20)
print("under_20: ", under_20)
print("not under_20: ", not under_20)

# and 와 or는 이항연산자
# and 와 or을 기준으로 양쪽에 관여한다.
# and 연산자는 좌변과 우변 결과값이 모두 True여야 결과적으로 True이다.
# and 연산자는 좌,우변 중 하나라도 거짓이면 결과적으로 거짓이다.

# or는 좌변과 우변 중 하나만 참이면 결과적으로 참이다.

print(True and True)
print(True or True)
print(True and False)
print(True or False)


# if 조건문
# 조건에 따라서 수행문을 실행한다.
# 탭을 꼭 써야 함
# if 조건식 :
#    수행문1
#    수행문2

if True:# 조건문에는 비교식이나 변수 불값 다 올 수 있다.
    print("True입니다...!")
    print("정말 True입니다...!")

if False:
    print(123)

# if문의 조건문이 거짓이면 진입을 안해 수행문을 실행하지 않는다.
#
# number = input("정수 입력:")
# number = int(number)
#
# if number >= 0:
#     print("양수입니다")
#
# if number <= 0:
#     print("음수입니다")
#
# if number == 0:
#     print("0입니다")

# money = 1000 # 0은 False로 취급
# if money:
#     print("돈 있음")
#
# money1 = "ㅁㅁㅁ"
# if money:
#     print("돈 있음")
#
# money2 = " " # ""는 False로 취급
# if money:
#     print("돈 있음")
#

# money = int(input("입력>>"))
# if money >= 0:
#     print("양수")
# elif money <= 0:
#     print("음수")
# elif money == 0:
#     print("0")

# elif 키워드는 if 조건에 부합하지 않는 다른 조건을 작성할 때 사용
# elif 특징 : 여러개 사용 가능
# if 특징 : 하나만 쓸 수 있다. if는 한 세트를 의미한다. if는 새로운 조건식 시작을 의미

#
# money = int(input("입력3"))
# if money > 0:
#     print("양수")
#     print("양수")
# elif money < 0:
#     print("음수")
# else:
#     print("양수도 음수도 아니다.")

# else는 else위에 나온 case들에 전부 진입하지 못했을 때 진입한다.
# else는 조건식을 작성하지 않고 :  만 씀
# else도 1개만 가능

# 사용자입력을 통해 돈을 입력받음
# 3000원 이상이면 택시
# 1000이상~3000원미만이면 버스
# 1000원 미만이면 걸어라
# if 문으로 1세트로 구성

# m = int(input("버스비: "))
#
# if m >= 3000:
#     print("택시")
# elif 1000 <= m and money < 3000:
#     print("버스")
# else:
#     print("걷는다")
#
# # if 1: 도 가능
# # if "s" in "score":
#     #print(123)
#
# # if문 한줄로 작성하기 수행문이 짧을 때만
# if 's' in 'score':pass
# # else: print("xxx") 형식지켜 쓰는 거 권장
#
# str5 = "score"
# if "s" in str5:
#     print("123")
#     str5= "hello"
#
# print(str5)

# #날짜 / 시간과 관련된 기능을 가져옴
import datetime
#
# 현재 날짜 / 시간을 구함
now = datetime.datetime.now()
#
# #출력
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
#
# # 오전 구분
# if now.hour < 12:
#     print("현재 시각은 {}시로 오전입니다".format(now.hour))
#
# # 오전 구분
# if now.hour >= 12:
#     print("현재 시각은 {}시로 오후입니다".format(now.hour))
#
# number = input("정수 입력> ")

# 마지막 자리 추출
# last_character = number[-1]
# # 숫자 변환
# last_number = int(last_character)

# 짝수확인
# if last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8:
#     print("짝수입니다.")
#
# # 홀수확인
# if last_number == 1 \
#     or last_number == 3 \
#     or last_number == 5 \
#     or last_number == 7 \
#     or last_number == 9:
#     print("홀수입니다.")
#

# 현재 날짜/시간을 구하고 쉽게 사용할 수 있게 월을 변수에 저장
# now = datetime.datetime.now()
# month = now.month

# 조건문으로 계절을 확인
# if 3 <= money <= 5:
#     print("현재는 봄입니다.")
#
# elif 6 <= money <= 8:
#     print("현재는 여름입니다.")
#
# elif 9 <= money <= 11:
#     print("현재는 가을입니다.")
#
# else:
#     print("현재는 겨울입니다.")


# False로 변환되는 값
# 0
# 0.0
# 빈 컨테이너 (""빈문자열, 빈 리스트, 빈 자료형들)
# None
# print(None)

# 이외의 것들은 전부 True

# pass
# 그냥 넘어가라.
# 수행문 자리채우기 용도
# if str1:
    #pass 잠깐 채워놓고 싶을 때나 실행 안해도 되는 경우 지나가게
#else:
    #print(";;;;;;;;;;;")


# 사용자한테 입력 받아서 그 수가 네자리수(1000) 이상이고, 3의 배수이면 '통과' 멘트와 함께 사용자가 입력한 숫자를 출력
# 그렇지 않으면 실패를 출력하는 코드 작성
#
# num = int(input("입력: "))
#
# if num >= 1000 and num % 3 == 0:
#     print(f"통과, {num}")
# else:
#     print("실패")

# 다른 정답
# if int(num)//1000>= 1 and int(num) % 3 == 0:
#     print("통과")

#
# number = input("정수입력")
# number = int(number)

# raise 강제 에러발생코드
# if number > 0:
#     pass
    # print("1")
    # raise NotI
# mplementedError  # 아직 구현 안됐음을 알리는 에러
# 파일에 에러메시지 발생한 횟수같은 거 저장하기도 함
# else:
#     pass
    # raise NotImplementedError

# print("xxxxxxxxxxxxxx") 에러 띄웠으므로 안 읽힘


# 대화 프로그램
# print("============대화프로그램===============")
# conv = input("입력: ")
#
# if "안녕" in conv:
#     print("> 안녕하세요")
# elif "몇 시" in conv or "몇시" in conv:
#     print(f"지금은 {now.hour}시입니다.")
# else:
#     print(conv)

# 나누어 떨어지는 숫자

# n = int(input("정수를 입력해주세요: "))
#
# if n % 2 == 0:
#     print(f"{n}은 2로 나누어 떨어지는 숫자입니다.")
# else:
#     print(f"{n}은 2로 나누어 떨어지는 숫자가 아닙니다.")
# if n % 3 == 0:
#     print(f"{n}은 3로 나누어 떨어지는 숫자입니다.")
# else:
#     print(f"{n}은 3로 나누어 떨어지는 숫자가 아닙니다.")
# if n % 4 == 0:
#     print(f"{n}은 4로 나누어 떨어지는 숫자입니다.")
# else:
#     print(f"{n}은 4로 나누어 떨어지는 숫자가 아닙니다.")
# if n % 5 == 0:
#     print(f"{n}은 5로 나누어 떨어지는 숫자입니다.")
# else:
#     print(f"{n}은 5로 나누어 떨어지는 숫자가 아닙니다.")
#
# 사용자에게 나이를 입력받고 해당하는 요금을 안내하는 코드 작성하세요.
# 노인(65세 이상) 요금 : 700원
# 청소년(19세 이하) 요금 : 500원
# 일반요금 : 1000원
# 노인은 짝수 초마다 무료로 이용가능
# 직원은 항상 50% 할인가격이용

employee = int(input("직원이시면 0, 아니면 1을 눌러주세요.: "))
age = int(input("나이 입력: "))
old = 700
young = 500
dpay = 1000


if age >= 65:
    if employee == 0:
        print(f"요금은 {int(old/2)}원입니다.")
        if now.second % 2 == 0:
            print(f"지금은 무료로 이용가능합니다. {now.second}")
    else:
        print(f"요금은 {old}원입니다.")
        if now.second % 2 == 0:
            print(f"지금은 무료로 이용가능합니다. {now.second}")

elif age <=19:
    if employee == 0:
        print(f"요금은 {int(young/2)}원입니다.")
    else:
        print(f"요금은 {young}원입니다.")

else:
    if employee == 0:
        print(f"요금은 {int(dpay/2)}원입니다.")
    else:
        print(f"요금은 {dpay}원입니다.")

# 사용자로부터 세 개의 숫자를 입력받고 그 중 가장 큰 숫자를 출력하는 코드 작성

a = int(input("숫자 1: "))
b = int(input("숫자 2: "))
c = int(input("숫자 3: "))

large_num = 0

if a > b:
    if a > c:
        large_num = a
        print(f"가장 큰 수는 {large_num}입니다.")
    else:
        large_num = c
        print(f"가장 큰 수는 {large_num}입니다.")
else:
    if b > c:
        large_num = b
        print(f"가장 큰 수는 {large_num}입니다.")
    else:
        large_num = c
        print(f"가장 큰 수는 {large_num}입니다.")
































