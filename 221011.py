# 숫자 데이터 (자료형)

# 파이썬에서는 숫자를 소수점이 없는 숫자와 소수점이 있는 숫자로 구분한다.
# 소수점이 없는 숫자 : 정수형
# 소수점이 있는 숫자 : 실수형

# 정수(int)의 예 : 0, 1, 100, 123 등
# 실수(float)의 예 : 0.0, 0.5, 3.14 , -100.1 등
# 같은 숫자라도 .0이 붙어있으면 실수형으로 분류
# 같은 크기를 나타내도 소수점이 있냐 없냐에 따라서 숫자의 자료형이 달라진다.

print(type(100))

print(type(23.333))

# 실수는 부동소수점이라고 표현 가능

print(type(0))
print(type(0.0))

# 숫자 사칙연산 가능
# + - * /

print("5 + 7 =", 5 + 7, 100+100)
print("5 - 7 =", 5 - 7)
print("5 * 7 =", 5 * 7)
print("5 / 7 =", 10/3)

# 나누기 연산자의 다른 형태 // : 나눗셈의 몫을 구하는 연산자, 정수형태

print("5 / 7 =", 10//3)

# 나머지를 구하는 연산자 %

print(10 % 3)

# ** 제곱을 구하는 연산자

# 2**10 2 의 10 제곱

print(2 ** 10)

# 파이썬 연산자들의 우선순위가 있다.
# 곱하기와 나누기가 더하기나 빼기보다 먼저

# 정수와 정수의 나누기 결과는 항상 실수형태로 나온다.

print(2 + 2 - 2 * 2 / 2 * 2)

# 정수와 실수형의 덧셈 뺄셈은 결과가 실수형태로 나온다.
print(2 + 2.0)

print(2 - 2 + 2 / 2 * 2 + 2)

print((5 + 3) * 10)

print(5 + ( 3 * 2))

# 우선순위를 괄호로 지정해주는 것이 좋은 방법이다.

# print("abc" + 3)

# 문자는 문자끼리 숫자는 숫자끼리 연산이 가능하다.

print("안녕" + "하세요" * 3)
print(("안녕" + "하세요") * 3)
print("안녕" + ("하세요" * 3))

# 변수
# 변할 수 있는 데이터를 담는 칸
# 데이터를 저장하는, 담는 칸
# 데이터를 담는 칸의 이름
# 중간매개체

age = 1
# age라는 저장 공간에 1이라는 숫자(정수형)데이터를 담아 놓는다.
# 1이라는 데이터가 필요할 때 age라는 식별자(변수명)을 통해 호출하여 사용한다.

pi = 3.141592
# 3.14...을 pi에 넣는다. 오른쪽부터 읽어나감

# 변수를 선언하다
# 변수를 선언한다라는 것은 변수를 생성하는 것

# 변수에 값을 할당하다
# 변수에 값을 넣는다는 뜻

# 변수의 참조
# 변수에서 값을 꺼내는 것

# 초기화

# 식별자 규칙에 맞는 변수명 선언

# 데이터가 할당된 상태로 메모리에 저장돼있다.
# 변수 안의 데이터는 재할당될 수 있다. (변경가능하다)
name = 100
print(name)
name = 10.1 # 재할당
print(name)
subject = 1
season = 1
month = 1

# 변수의 참조
print(type(name))

str1 = "py"
str2 = "thon"

print(str1 + str2)

int1 = 10
int2 = 30

print(int1 + int2)

print(str1 * int1)

# print(str1 + int1)

print(int2 /3 + 10)

# 변수 선언과 할당
pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2 * pi * r)
print("원의 넓이 =", pi * r * r)

# 변수의 할당에 쓰인 대입 연산자 =

# 복합 대입 연산자

# 선 연산 후 대입

# += : 숫자 덧셈 후 대입
# -= : 숫자 뺄셈 후 대입
# *= : 숫자 곱셈 후 대입
# /= : 숫자 나눗셈 후 대입
# %= : 숫자 나머지 구한 후 대입
# **= : 숫자 제곱 후 대입

aaa = 10
print(aaa)
aaa = aaa + 100
print(aaa)

aaa += 100
print(aaa)

str3 = "Hello"
print(str3)
str3 += "python"
print(str3)
str3 *= 3
print(str3)

# 종료코드 1은 문제있음

# 프로세스 : 진행중인 작업물

# 사용자 입력받는 기능
# 사용자가 입력할 때까지 대기 (종료코드 어쩌구 안뜸, 밑에 창이 콘솔창)

# print(input())

#input() 함수에 입력한 사용자 입력값은 무조건 문자열로 인식된다.

#사용자에게 입력받은 데이터를 변수 user에 할당하고 user에 저장된 데이터의 길이와
#타입을 출력하는 코드를 작성하세요.

# user = input()
#
# print(len(user))
#
# print(type(user))



# input 함수의 괄호 안에 출력 텍스트
# 사용자가 입력한 값에 3을 곱한 값을 출력하는 코드 작성

# 자료(데이터) 형태의 변환 : 형 변환 : 캐스트
# input으로 입력받은 데이터는 무조건 문자열로 인식
# 따라서 input으로 입력받은 문자열을 숫자로 변환해야 한다.

# 형변환 함수를 사용한다.
# 문자열을 숫자(정수)로 변환해주는 함수 : int()
# 문자열을 숫자(실수)로 변환해주는 함수 : float()

# print(int(input("숫자를 입력하세요 : "))*3) 변수생성 안되므로 속도면과 메모리면에서 효율적이나 나중에 써야할 경우 문제되는 코드
#오류발생 많으므로 이렇게 한 줄로 쓰지말 것.......

# 기본 정답
# user = input("입력값")
# user = int(user)
# user *= 3
# print(user)

# string_a = input("입력A> ")
# int_a = int(string_a)
#
# string_b = input("입력B> ")
# int_b = int(string_b)

# print("문자열 자료:", string_a + string_b)
# print("숫자자료:", int_a + int_b)

# print(type(str(int(input("문자열로 변경할 숫자 입력 : ")))))

# str() 함수 : 숫자를 문자열로 변환한다.

# output_a = str(52)
# output_b = str(52.273)
# print(type(output_a), output_a)
# print(type(output_b), output_b)

# 사용자 입력을 통해 몸무게와 키를 입력받아 BMI 수치를 계산하여 출력하는 코드를 작성
# BMI 계산 식 : 몸무게 / 키의 제곱
# kg/ m 단위


# W = float(input("몸무게를 입력하세요 : "))
# H = float(input("키를 입력하세요 : "))
#
# BMI = W / (H**2)
#
# print(BMI)

# 네이버 이자계산기
money = int(input("예치금액 : "))
year = int(input("예금기간 : "))
interest = int(input("연 이자율 : "))


before = year * int((money * (interest / 100)))
plus_interest= int((before * 0.154))

print(money + before - plus_interest)



# 식별자 뒤에 () : 함수
# 함수란 function, 기능
# 특정 문자열에 . 을 찍으면 문자열에 사용할 수 있는 함수들이 나타난다!!!!
# . 찍고 나타나는 함수들을 '관련함수'하고 한다.

# format() 함수
# 문자열 관련 함수
# 사용방법

str4 = "{}".format(10)
print(str4)
# {}의 수와 format의 대상물 수(함수의 재료)가 같아야 함, 칸에 하나하나 배치함
str5 = "{} {}".format(10, 20)
print(type(str5))

# str5 = "10 20" 이렇게 만드나 위처럼 만드나 똑같음

sample = "현재온도 : {} 습도 : {} 시간 : {}"

# str6 = "{} 2222 {} xxxxx {}".format(10, 20, 50) # 이렇게 중간에 집어넣어야 할 데이터를 섞을 수 있음
str6 = sample.format(10, 20, 50) # 변수 만들어서 집어넣어도 됨
print(str6)
print(type(str6))

#format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

# format함수의 재료로 어떤 자료형을 넣더라도 결과는 문자열로 출력

# format 함수의 숫자 관련 기능

# 정수
output_a = "{:d}".format(52) # 안의 d는 10진수를 표현한 것

# 특정 칸에 출력하기
output_b = "{:5d}".format(52) # 5칸
output_c = "{:10d}".format(52) # 10칸

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52) # 양수
output_e = "{:05d}".format(-52) # 음수

print("#기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

# format 함수 정수보단 소수점 때문에 사용하는게 더 많음
output_a = "{:15.3f}".format(52.273) # 15자리로 만들고 소수점 셋째자리까지
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273) # 자동으로 반올림됨

print(output_a)
print(output_b)
print(output_c)

# format 정수 0 실수 0.0
# format 함수 {} 안에 :g 를 사용하면 실수형에 .0을 제거가능

# 문자열 관련 함수1
# upper() 함수
# 영문자를 대문자로 변환
# lower(0 함수
# 영문자를 소문자로 변환
# 관련함수 . 찍고 사용한다.

sample1 = "hello"
# print(sample1.upper())
sample1 = sample1.upper()

print(sample1)

# 함수 분류방식
# 내장함수(전역함수)와 관련함수(.찍고 쓰는 함수들...) 중요

# 변수에 담긴 원본 데이터를 건드는 함수 : 파괴적 함수
# 변수에 담긴 원본은 건들지 않는 함수 : 비파괴적 함수

# 할당을 통해 바인딩이 됨 기억해두겠다는 뜻 중요

# 문자열 관련 함수 2
# 공백 제거함수
# strip()
# lstrip()
# rstrip()

# 문자열 관련함수 3
# 문자열 구성 파악 함수 불타입
# isalnum() : 문자열이 알파벳 or 숫자로만 구성되어 있는지 확인
# isalpha() : 문자열이 알파벳으로만 구성되어 있는지 확인
# isdecimal() : 문자열이 정수 형태인지 확인
# isdigit() : 문자열이 숫자로 인식될 수 있는 문자열인지 확인, 보통 이걸 씀
# islower() : 문자열이 소문자로만 구성되어 있는지
# isupper() : 문자열이 대문자로만 구성되어 있는지


# a = input("입력: ")
# print(a.isdigit())

# print함수는 반환이 없는 함수로 그저 출력만 함

print(input("입력>>").isdigit())

# 문자열 관련 함수 5
# find()
# 문자열 내부에 특정 문자가 어디에 위치하는지 찾는 함수
# find() : 왼쪽에서부터 찾는다.
# rfind() : 오른쪽에서부터 찾는다.

sample2 = "안녕안녕하세요"

# 중복검출할 때 사용할 수 있음
print(sample2.find("안녕"))
print(sample2.rfind("안녕"))

# find 대신 사용가능한 in 키워드, 여부체크용
print("안ㄷ녕" in "안녕하세요")

# 문자열 관련 함수 6
# split()
# 문자열을 잘라줍니다.
a = "10 20 30 40 50".split(" ") # 공백 기준으로 자름
print(a)

print(type(a))

# list는 하나의 행으로 보면 됨

#


























