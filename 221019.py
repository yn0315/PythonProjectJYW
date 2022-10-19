# 221019

# 함수 고급
# 튜플
# 튜플은 함수와 함께 많이 사용되는 데이터 형태
# 리스트와 비슷하지만 차이점이 몇 가지 있다.

# 람다
# 함수를 간단하게 선언하고 사용하는 방법


listx = [1,2,4,5]
listx[0] = 1111
print(listx)

# 튜플은 한번 배치된 요소는 바뀌지 않는다.

# (요소,요소,요소...)

tp = (10,20,30)
print(tp)
print(type(tp))

# tp[0] = 1111 # 안됨 에러발생
# print(tp)

print(tp[0])
# 튜플도 리스트와 마찬가지로 인덱싱을 통해 값 참조 가능

listx = [200]
tp = (200,) # 값을 하나 쓰더라도 쉼표 꼭 써야함

# 리스트와 튜플의 공통점
# 인덱싱 사용가능
# 여러 요소 담는 데이터 형태

# 괄호 없는 튜플 , 리스트
[a,b] = [30,40]
(c,d) = (50,60)
(e,f) = [70,80] # 들어가는 자료형은 상관없음, 요소를 빼서 넣는것이기 때문에, e,f 타입찍으면 int나옴
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("=======================괄호없는 튜플=======================")
# 괄호가 없는 튜플
tuple_test = 10,20,30,40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test: ", tuple_test)
print("type(tuple_test): ", type(tuple_test))
print()

# 괄호가 없는 튜플 활용
a,b,c = 10,20,30 # 튜플형태로 묶였다가 배치를 하나씩 해주는게 맞는 것, 변수를 여러개 할당하는게 아님

print("# 괄호가 없는 튜플을 활용한 할당")
print("a: ", a)
print("b: ", b)
print("c: ", c)

# 함수에 여러가지 리턴해도 알아서 튜플로 묶어줘서 편리

#튜플과 함수
#튜플은 함수의 리턴에서 많이 보인다.

print("=================여러개의 값 리턴하기===================")
def test():
    return (10,20)
a, b = test()
print("a: ", a)
print("b: ", b)

# 이것보다 한 덩어리로 받아 len()써서 찢어버리는 게 나음

# 람다
# 함수 매개 리턴
# 대부분 함수는 매개변수를 사용하는 경우가 많다
# 람다 lambda 는 함수를 효율적으로 작성하는 기능
# 함수를 매개변수로 전달한다.

"============= 함수의 매개변수로 함수 전달하기=============="
# 매개변수로 받은 함수를 10번 호출하는 함수
# 매개변수로 함수를 전달할 때는 함수명만 적는다. ()없이
# def call_10_times(func):
#     for i in range(10):
#         func()
#
# # 간단한 출력하는 함수
# def print_hello():
#     print("안녕하세요")
#
# # 조합하기
# call_10_times(print_hello())

# 안녕하세요를 출력하는 함수 1개
# 안녕히 가세요 함수 1개
# 어서오세요 1개
#
# 총 3개의 함수를 매개변수로 받는 함수 1개
# 이 함수 안에서 상황에 따라 적절한 멘트를 출력하게
# 사용쟈의 입력
# 어서오세요: 무조건출력
# 안녕하세요: 사용자가 입장
# 안녕히가세요: 사용자가 퇴장
# 사용자 입력 케이스 2가지 : 입장 or퇴장

#
# 처음 프로그램 실행

# 일단 어서오세요 출력, 이것도 매개변수로 받아
# 입장퇴장 input받기
# 입장 or퇴장인지 조건문으로 판단해서 멘트보냄

#
# list_stu = ["김학생",'박학생','김','이']
# def hello_bye(func1,func2,func3, x):
#
#     for i in x:
#         text = input("입장/퇴장을 입력해주세요: ")
#         func1(i)
#         if text == "입장":
#             func2()
#         elif text == "퇴장":
#             func3()
#
# def hello(name):
#     print(name)
#
#     print("어서오세요")
# def hi():
#     print("안녕하세요")
# def bye():
#     print("안녕히 가세요")


# hello_bye(hello, hi, bye, list_stu) # 함수명만 전달, 함수도 여러개 전달
# 매개변수의 입력은 호출되는 라인을 체크
# list_stu = ["김학생",'박학생','김','이']
# print(range(0,100))
# print(type(list_stu))
# dict = {"a": a}
# print(type(dict.keys()))
#
# def hello_bye(x, *func):
#     for i in x:
#         text = input("입장/퇴장을 입력해주세요: ")
#         func[0](i)
#         if text == "입장":
#             func[1]()
#         elif text == "퇴장":
#             func[2]()
#
# def hello(name):
#     print(name)
#
#     print("어서오세요")
# def hi():
#     print("안녕하세요")
# def bye():
#     print("안녕히 가세요")


# hello_bye( list_stu, hello, hi, bye) # 함수명만 전달, 함수도 여러개 전달
# 매개변수의 입력은 호출되는 라인을 체크

# filter() 함수
# map() 함수
# 두 함수는 함수를 매개변수로 사용하는 대표적 함수, 내장함수

# map() 함수는 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수

# filter()함수는 리스트의 요소를 함수에 넣고 리턴된 값이
# True인 것으로 새로운 리스트를 구성해주는 함수
# map(함수명, 리스트)
# filter(함수명, 리스트)

# def power(item):
#     return item *item
# def under_3(item):
#     return item < 3
#
# list_input_a = [1,2,3,4,5]
#
# output_a = map(power, list_input_a)
# print("#map()함수의 실행결과")
# print("#map(power,list_input_a): ", output_a)
# print("#map(power,list_input_a): ", list(output_a))
# print()
#
# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행 결과")
# print("filter(under_3, list_input_a): ", output_b)
# print("#map(under_3,list_input_a): ", list(output_b))

print("======================map문제==============")
# 리스트[3,4,5,6,7]
# for문을 이용해서 위 리스트의 모든 요소에 +5씩된 결과를 리스트로 출력하세요

# list = [3,4,5,6,7]
# listx = []
#
# # for i in list:
# #     listx.append(i + 5)
# # return listx
#
# # map함수를 사용해서 위와같은 작업을 수행
#
# def sum (list):
#     return list + 5
#
#
# print(list(map(sum,list)))

# filter()함수와 map()함수의 결과로
# map obj 와 filter obj가 나오는데
# 이를 제너레이터라고 부른다.

# 람다식
# 매개변수로 함수를 전달하기 위해 함수를 정의하는 게 번거롭고
# 코드 라인 낭비라고 생각이 들 때
# lambda 매개변수: 리턴값
# 매개변수로서 함수를 활용 + 정의를 동시에 한다

"=================람다식======================"
# 선언만 람다로 해놔서 .....다음문제처럼 써야함
# 호출과 동시에 해야 함
power = lambda x: x * x
under_3 = lambda x : x < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print("#map()함수의 실행결과")
print("#map(power,list_input_a): ", output_a)
print("#map(power,list_input_a): ", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a): ", output_b)
print("#map(under_3,list_input_a): ", list(output_b))




















