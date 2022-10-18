# 221017
# 리스트
# min max sum
# [1,2,3,4,5]
# sum() : 리스트 내부 값을 모두 더환다.
# max() : 리스트 내부에서 최댓값을 찾는다.
# min() : 리스트 내부에서 최솟값을 찾는다.
import inspect

listx = [1, 2, 3, 4, 5]
print(sum(listx))
print(max(listx))
print(min(listx))

print(max(1, 2, 3, 4, 5))  # 안에 직접 데이터 넣어도 됨

# reversed() 함수 사용하지 않고 listx를 거꾸로 출력하세요

listx = [3, 100, 52, 77, 2]

for i in range(len(listx) - 1, -1, -1):
    print(listx[i])

# print(listx[::-1])

temp = [1, 2, 3, 4, 5, 6]

for i in reversed(temp):
    print("첫번째 반복문: {}".format(i))
for i in reversed(temp):
    print("두번째 반복문: {}".format(i))

# enumerate()
exlist = ["A", "B", "C"]
# 0번째 요소는 A
# 1번째 요소는 B
# 2번째 요소는 C

for i in range(len(exlist)):
    print("{}번째 요소는 {}입니다.".format(i, exlist[i]))

print("단순출력")
print(exlist)
print()

print("#enumerate() 함수 적용 출력")
print(enumerate(exlist))
print()

print("##list()함수로 강제 변환 출력")
print(list(enumerate(exlist)))  # 인덱스와 값을 갖고있는 객체다, ()로 묶여있는 것은 튜플이라고 함
print()
# enum함수의 반환값은 튜플형태의 객체

print("#반복문과 조합하기")
for i, value in enumerate(exlist):
    print("{}번째 요소는 {}입니다.".format(i, value))  # 변수 하나만 쓰면 튜플형태로 나옴

# reversed 함수나 enumerate 함수의 결과가 바로 리스트형태로 나오는 것이 아니라
# 객체형태로 반환된다. 0x00AA.....
# for문에서는 그냥 써도 된다.

# 딕셔너리의 item함수

{"name": "학생1"}

example_dict = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}
print("# 딕셔너리의 items() 함수")
print("items() : ", example_dict.items())
print()

print("#딕셔너리의 items()함수와 반복문 조합하기")

for key, element in example_dict.items():  # 딕셔너리를 리스트로 바꿀필요없다 객체 자체로 들어간다.
    print("dictionary[{}] = {}".format(key, element))

# 아래 세개는 값이 객체로 나온다.
print(example_dict.items())
print(example_dict.keys())
print(example_dict.values())

# 리스트 내포
# 리스트 만들 때 씀 근데 권장안함
# 값에 2를 더해서 반환해라.
array = [i + 2 for i in range(0, 20, 2) if i != 4]
print(array)

# 0~100까지 숫자 중 2의 배수가 아닌 숫자들만 뽑아 그 제곱값을 array에 담아 출력

# 표현식 for 반복자(변수) in 반복범위 if 조건식
array = [i ** 2 for i in range(0, 101) if i % 2 != 0]
print(array)

# number = int(input("정수입력: "))
#
# if number % 2 == 0:
#     print("""\
#         입력한 문자열은 {}입니다.
#         {}는 짝수입니다.""".format(number, number)
#           )
# else:
#     print("""\
#         입력한 문자열은 {}입니다.
#         {}는 홀수입니다.""".format(number, number)
#           )
#
# if number % 2 == 0:
#     print("""입력한 문자열은 {}입니다.
# {}는 짝수입니다.""".format(number, number))
# else:
#     print("""입력한 문자열은 {}입니다.
# {}는 홀수입니다.""".format(number, number))
#
# if number % 2 == 0:
#     print("입력한 문자열은 {}입니다. \n{}는 짝수입니다.".format(number, number))
# else:
#
#     print("입력한 문자열은 {}입니다. \n{}는 홀수입니다.".format(number, number))
#
# test = (
#     "이렇게 입력해도"
#     "하나의 문자열로 연결되어 "
#     "생성됩니다."
# )
#
# print("test: ", test)
# print("type(test): ", type(test))
#
# if number % 2 == 0:
#     print((
#         "입력한 문자열은 {}입니다. \n"
#         "{}는 짝수입니다.").format(number, number))
# else:
#     print(("입력한 문자열은 {}입니다. \n"
#            "{}는 홀수입니다.").format(number, number))

# 이터레이터
# 이터러블 : 반복가능한
# 딕셔너리 리스트 문자열 튜플
# 내부에서 요소를 차례로 꺼낼 수 있는

# 이터레이터 : 이터러블 중에서 next() 함수를 통해 하나하나 꺼낼 수 있는 요소를 이터레이터라고 한다.

number = [1, 2, 3, 4, 5]
r_num = reversed(number)

print(r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# for 반복문의 매개변수에 넣으면 반복할 때마다 next() 함수를 통해 요소를 하나하나 꺼내주는 것이다.

# 왜? reversed()함수는 리스트를 바로 리턴해주지 않고 이터레이터를 리턴할까?
# 메모리의 효율성을 위해! 객체로 주는 것은 거의 메모리 때문!

# 컴퓨터는 2진수만 사용하지만 너무 긴 2진 표현법을 변경한다.

# 2진수 : 0b(binary)
# 8진수 : 0o(oxtal)
# 16진수 : 0x(hexadecimal)

output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계: ", sum(output))



list = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dict = {}
cnt = 0
for number in list:
    if dict.get(number) == None:
        dict[number] = 1
    else:
        dict[number] += 1
    cnt = len(dict.keys())

print("{}에서 사용된 숫자의 종류는 {}개 입니다. 참고: {}".format(list,cnt, dict))

dna = input("염기서열 입력: ")
a = 0
t = 0
g = 0
c = 0
for i in dna:
    if i == "a":
        a += 1
    elif i == "t":
        t += 1
    elif i == "g":
        g += 1
    elif i == "c":
        c +=1
    else:
        pass

print(f"a의 개수: {a} ")
print(f"t의 개수: {t}")
print(f"g의 개수: {g}")
print(f"c의 개수: {c}")

print("======================3번=======================")


# dict3= {}
# if len(dna) % 3 == 0:
#     pass
#
# else:
#     for number in range(0, len(dna),3):
#         dict3 = dna[number: number + 3]
#         for i in range(len(dna)//3):
#             dict3[i] = 0
#             dict3[i] +=1
#         print(dict3)





        # if dict3[number] == dna[number]:

        # print(dict3[number])

        # else:
        #     dict[number] += 1
        # cnt = len(dict.keys())

# dicta = {}
# if str % 3 == 0:
#
#     pass
#
# else:
#     # 나머지 있으면 날려버림
#     for i range(0(len(str),3))
#
#    # 0,3,6,9 인덱스번호
#     dict[str[i:i+3]] = 1

# 정답
counter = {}
for i in range(0, len(dna), 3):
    # 3글자씩 추출
    codon = dna[i:i+3]
    #3글자로 구성되는지 확인
    if len(codon) == 3:
        # 딕셔너리에 키가 없을 경우 추가
        if codon not in counter:
            counter[codon] = 0
        # 갯수를 추가
        counter[codon] += 1

print(counter)


print("======================4번=======================")

# array = [1,2,[3,4],5,[6,7],[8,9]]
# array2 = []
#
# for i in range(len(array)):
#     if type(array[i]) == list:
#         for j in len(array[i]):
#             array2[i] = array[i][j]
#
# print(array2)

# 정답
array = [1,2,[3,4],5,[6,7],[8,9]]
output = []

for i in array:
    if type(i) == list:
        for j in i:
            output.append(j)
    else:
        # 요소가 숫자라면 그냥 추가
        output.append(i)

print(f"{array}를 평탄화하면")
print(f"{output}입니다.")

# 함수
# 파이썬에서 기본적으로 제공하는 내장함수 print 등등
# 함수는 호출한다라고 표현
# print("hello") 의 괄호내부에 들어가는 자료를 매개변수라고 한다.
# 파이썬 내장함수 프린트에 매개변수로 문자열 hello를 넣어 호출했다.
# 반환값
# 반환값이 있기도 없기도
# 반환의 여부는 변수에 대입할 수 있는 값이 나오냐 안나오냐
# 반환값이 없는 함수를 변수에 할당하면 결과가 None 이 나옴
# 반환값 = return값
# 재사용 가능성이 있고
# 복합적인 기능을 수행하는 코드를 묶어 함수로 만든다.

# def 함수이름():
#   수행문1
#   수행문2

# 코드의 집합
def print3():   # 함수의 정의
    print("1")
    print("2")
    print("3")

print3()    # 함수의 호출

# 함수에 매개변수 만들기

# def 함수이름(매개변수, 매개변수...):
#   수행문
#   수행문


def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)

#반환값이 없고 입력값은 있는 함수
print_n_times("ddddd", 5)

# 가변 매개변수
#print() 함수는 매개변수를 원하는 만큼 입력하 수 있다.
# 가변매개변수를 사용하여 정의된 함수이기 때문
# 원하는 만큼 받을 수 있는 함수를 가변 매개변수함수라고 함


def print10(a,b,*c): # c가 가변 매개변수
    print(a)
    print(type(c))

print10(1,2,3,4,5,6,7)

# 가변매개변수는 항상 일반 매개변수 뒤에 와야함
# 가변 매개변수는 하나만 선언 가능
# 가변 매개변수에 한번에 들어온 여러개의 데이터는 묶여서 하나의 튜플 형태로 저장된다.

def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬", "프로그래밍")


print(type(value))


# 두 수를 입력받아 더한 값 출력하는 더하기함수

num1 = int(input("입력1: "))
num2 = int(input("입력2: "))

def sum(a, b):
    print("a + b = " , a+b)


def subtraction(a, b):
    print("a - b = " , a - b)


def multi(a, b):
    print("a * b = " , a*b)


def division(a, b):
    print("a / b = " , int(a/b))


sum(num1,num2)
subtraction(num1,num2)
multi(num1,num2)
division(num1,num2)

print(inspect.getsource(print10))

# 기본 매개변수
# print 함수의 경우 value, sep, end, file, flush
# 매개변수가 있는데 왜 가변 매개변수가 제일 앞에 있음에도 문제가 없을까?
# -> value가 가변 매개변수
# value 뒤에 sep end file flush는 일반 매개변수가 아닌 기본 매개변수이다.

# 기본 매개변수는 매개변수=값 형태로 되어있다.
# 선택적으로 넣는 값
# 기본매개변수 뒤에 일반매개변수 못옴
# 가변과 일반매개변수를 묶어 생각하고 기본매개변수는 따로 봐야함
def print_n_times(value,n=2): # n = 2 는 기본매개변수로 값을 안 넣으면 기본적으로 2를 넣는다는 것
    for i in range(n):
        print(value)

print_n_times("안녕", 4)



