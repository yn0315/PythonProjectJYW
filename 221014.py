# 221014 while 반복문

# for 반복문 : 반복범위 (문자열, range, 리스트, 딕셔너리)
# while 반복문 : 어떤 횟수만큼 / 특정 시간동안 / 어떤 조건이 될 때까지

list1 = [10,11,13,17]
list2 = []
for i in list1:
    print('리스트의 ', list1.index(i)+1,'번째 요소는',i,'이다.')
    print(len(list2))

for i in range(len(list1)):
    print('리스트의 ', i + 1, '번째 요소는', list1[i], '이다.')

# 리스트의 1번째 요소는 1이다
# 리스트의 2번째 요소는 11이다
# 리스트의 3번째 요소는 13이다
# 리스트의 4번째 요소는 17이다

# for 반복문 반대로 반복
# 역반복문
print(range(100))

print(list(range(0, 10, 1)))
print(list(range(10, 0, -1)))

x = -1
for i in range(4, x, -1): # 안에 식이 들어가도 됨, 변수 들어가도 됨
    print(i)

for i in reversed(range(5)):
    print(i) # 4322210

# reversed() 함수는 range객체를 반대로 뒤집는다

star = ""
for i in range(0,5):
    for j in range(0, i):
        star += '*'
        print(star)


star2 = ''
for i in range(0, 10):
    for j in range(9, i, -1):
        star2 += " "
    for k in range(0, 2 * i - 1):
        star2 += '*'
    star2 += '\n'
print(star2)


# print함수의 옵션값
# ene= "": 프린트 출력 뒤 내용에 기본적으로 줄바꿈이 된다.
# sep= "": 프린트문 출력문들 사이에 내용을 넣는다.
print("a",'b','c', sep="123")
print('hello', end=" ")
print('hi')
# end 옵션 뒤에 텍스트를 붙여주거나 줄바꿈효과 줌,
# sep 옵션 , sep = 2는 2기준으로 분리하겠다.


# long = int(input("몇 칸?"))
# star3 = ''
# for i in range(1, num, 2):
#     star3 += (" ") * int(i/2)
#     star3 += '*'
#     for j in range(num -1, i, -1):
#         star3 += "@"
#     for k in range(0,-1):
#         star3
#         star3 += '*'
#     star3 += '*\n'
# 
# print(star3)

# 선생님 정답
# x = 0
# str = ""
# for i in range(int(long/2)):
#     for s in range(0,x):
#         str+=" "
#     x +=1
#     str +="*"
#     for j in range(long - (x*2)):
#         if len(range(long -(x*2)))>= 2:
#             str +="@"
#     str +="*"
#     print(str)
#     str = ""

# while
# 리스트나 딕셔너리 등 대상이 있을 때 그 내부 요소를 가지고 순회하는 경우는 for문
# 특정 시점까지는 while을 쓴다

# while 조건식:
#    수행문
#
# while 뒤에 조건식이 참인 동안 아래 수행문을 계속 반복한다.

 # while True:  while 뒤에 문자열 써도 참이라 실행됨
 #     print(".", end="")

i = 0
while i < 10:
    print(i)
    i += 1

# 사용자에게 세자리 숫자 하나를 입력받아서 그 숫자부터 0까지 1씩 줄어드는 모든 숫자를 출력

# i = int(input("세자리 숫자?:"))
# while i >= 0:
#     print(i)
#     i -= 1


list_test = [1,2,1,2]
value = 2

# while value in list_test: # 실행 세번 됨 이 방식이 여기선 더 효율적
#     list_test.remove(value) #실행 두번 됨
#
# print(list_test) # 실행 두번 됨

for i in list_test: # 여기서 i는 리스트의 요소니까 네번 돔!!!!!
    if 2 in list_test:
        list_test.remove(2)
    print(list_test)

# while 사용 예
# utc 협정세계시

import time
number = 0
# tick 한 움직임의 단위
# 5초 동안 반복
# target_tick = time.time() + 5
# print(time.time())
#
# while time.time() < target_tick:
#     number += 1
# print("5초동안 {}번 반복했습니다.".format(number))
# print(time.time())


while True:
    print("안녕하세요")
    break

# break는 키워드
# break의 기능은 탈출
# break를 품고 있는 while문

i = 0

# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i = i+1
#
#     inp = input("종료?(y/n): ")
#     if inp in ["y","Y"]:
#         print("반복종료")
#         break

i = int(input("수 입력: "))
while True:
    print(i)
    i -= 1
    if i < 0:
        break

print("=======================")
# continue
# 반복문을 다음 반복으로 넘어갈 때
# continue 코드를 읽으면 반복문의 처음으로 올라간다.

numbers = [5,15,6,20,7,25]

for number in numbers:
    if number < 10:
        continue
    print(number)

print("====================반복문 예제===================")

key_list = ["name", "hp",'mp','level']
value_list = ["기사", 200,30, 5]
character = {}

for i in range(len(value_list)):
    character[key_list[i]] = value_list[i]
print(character)

limit = 10000
i = 1
sum_value = 0

while sum_value >= 10000:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i - 1, limit, sum_value))


max_value = 0
a = 0
b = 0

for i in range(1,100):
    j = 100 -i
    if max_value < i * j:
        max_value = i * j
        a = i
        b = j


print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))
