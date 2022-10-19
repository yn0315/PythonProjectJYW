# 221013 파이썬 개념

# 리스트와 반복문
# 리스트는 사전적 의미로 목록.
# 여러 가지 데이터를 저장할 수 있다.
# 데이터를 여러 개 저장하고 있는 데이터 형태이다.
# []

# 리스트 기본 형태
list1 = [1,2,3,4,5]

print(list1)

# 요소 5개가 들어있다.
# 데이터 5개가 들어있다.
# element

# 리스트의 특징
# 리스트는 한 가지 자료형만 가질 수도 있다.
# 리스트는 여러 자료형을 가질 수 있다.
# 숫자 문자 혼합

list2 = ["a", 'b', 'c', 'd'] # 따옴표는 혼합해도 됨

list3 = ["1", 1, "s", 2, 3, 4] # 가능

str = "hello"

# 리스트에도 인덱싱을 사용할 수 있다.

print(list3[0]) # 문자
print(list3[1]) # 숫자

# 리스트는 특정 요소의 값을 변경할 수 있다.

listx = [273, 32, 103, "sss", True, False]
listx[0] = "ccccc"
print(listx)

# 문자열과 인덱싱을 통해 값을 얻는 방법은 동일하지만
# 문자열은 인덱싱을 통해 새로운 값을 할당하는 것은 안된다.
# 리스트는 가능하다.

print(listx[-1])
print(listx[-2])
print(listx[-3])

# 리스트 접근 연산자([]치고 들어가는 것, 인덱싱하는 거를 다중으로 사용할 수 있다.
print(listx[-3][0])

# 리스트는 리스트를 포함할 수 있다.
listy = [1,2,3,[1,2,3]]
print(listy[3][1])
# 위랑 같음 print(listy[-1][-2])

listy[3] = [4,5,6]
print(listy)

listM = [[1], [2], [3,4,5], 6, 7]
listN = [0,[1,2,[3,4,5,[6,7,8]]]] # 요소가 두개

print(listN[1][2][3][2])

# print(listN[3])

# 문자열과 리스트 공통점
# 1. 인덱싱
# 2. 데이터의 열 구조이다.
# 3. 연산이 가능하다. +, *
# 4. len() 활용

# 문자열과 리스트의 차이점
# 1. 문자열은 값을 바꿀 수 없다.

# 리스트의 연산 +

lista = [1,2,3]
listb = [4,5,6]
print(lista + listb)

# 리스트의 연산 *
list1 = [10,20,30]
print(list1 * 3)

# 리스트의 len()
print(len(list1))

# 리스트 관련 함수
# append()
# 리스트에 요소를 추가한다.
# 가장 뒤에 추가된다. 무조건, 더 많이 사용

list1.append("x")
print(list1)

# insert()
# insert는 위치를 지정해서 추가 가능
# 리스트.insert(위치, 요소)

list1.insert(0, 100)
print(list1)

# extend()함수
# extend함수는 리스트를 요소로 추가한다.(갖다 붙인다)

list1.extend([4,5,6])
# list2 = [4,5,6]
# print(list1 + list2)
print(list1)

# extend와 + 연산자의 차이는 원본이 바뀌는지 안바뀌는지


# 리스트 요소 삭제
# 1. 인덱스로 제거
# 2. 값으로 제거

# del 키워드
# del 리스트명[인덱스] 띄어쓰기 잘 해야 함
# del 는 범위 삭제가 가능하다.

listb = [0,1,2,3,4,5,6,7]
del listb[3:5]
print(listb)

# pop()함수 사용 괄호 안채우면 맨 뒤 삭제, 채우면 해당 인덱스 요소 삭제
print("==========리스트 요소제거=========")
list_a = [0,1,2,3,4,5]
print("#리스트의 요소 하나 제거하기")
print()

# 제거방법 1 del 키워드
del list_a[1]
print("del list_a[1]: ", list_a)
print()
# 제거방법 2 pop()
list_a.pop(2)
print("pop(2): ", list_a)

# 리스트에 [:] 연산자로 리스트 슬라이싱 가능
numbers= [1,2,3,4,5,6,7,8]
print(numbers[0:5]) # 슬라이싱은 잘라서 들고 있는 것

print(numbers[0:5:2]) # start, stop, step, 어디서부터 어디까지 몇 개씩
print(numbers[::-1]) # 거꾸로 출력

# [::] 슬라이싱에서
# 첫자리는 start
# 두번째 stop
# 세번째 step


# 값으로 제거 : remove()
# 리스트 내부에 있는 요소의 값을 통해 제거
# 리스트.remove(값)

list3 = [1,2,1,2]
list3.remove(2)
print(list3)

# remove는 처음 발견되는 값을 제거한다.

# 전부 제거하기 clear()
list3.clear()
print(list3)

# 리스트 내부 값의 위치 찾기
# index()

lista = [1,2,3]
print(lista.index(3)) # 3이 어디 인덱스에 있는지 알아내라

# 리스트 정렬 sort()
# 리스트.sort()
# 오름차순으로 정렬한다.
listb = [4,2,1,7,9,6]
# print(listb.sort()) # sort는 리턴값이 없는 함수라서 None이 뜸
listb.sort()
print(listb)

# 함수는 리턴값이 있고없고와 내장함수인지 관련함수인지, 원본을 파괴하는지 안하는지로 나눌 수 있음

# 내림차순으로 정렬하는 방법

listb = [4,2,1,7,9,6]
listb.sort(reverse=True) # 목차에 p라고 뜨는 건 속성
print(listb)

# count함수
# 리스트에 포함된 요소 개수 세기
list3 = [1,2,3,1]
print(list3.count(1))

# 리스트 내부에 요소가 있는지 확인
# in, not in

list4 = [2,3,4,5,6,7]
print(2 in list4)

if 7 in list4:
    print("리스트에 7이 있다.")

if 8 not in list4:
    print("8은 없다.")

# 반복문
# 특정 코드를 반복하고 싶을 때 사용

for i in range(100): # 몇 번 반복할 것인지
    print("안녕하세요")

# for 반복문
# for 변수 in 반복범위:
#   수행문(반복하고자하는 코드)

print(range(100)) # (0,100)으로 뜨는데 0부터 100까지 범위 생성하는 함수

# for문의 반복범위 만드는 방법
# 1. range함수
# 2. 문자열
# 3. 리스트
# 4. 딕셔너리

# 리스트를 선언
array = [273, 32, 103, 57, 52]

#리스트에 반복문 적용
for element in array:
    print(element)

listx = [1,10,20,33,60]
# for문을 이용하여 listx의 요소의 총 합을 구하는 코드 작성

res = 0
for i in listx:
    res += i
print(res)

# range()의 활용방법 3가지

# range(10) 0 ~ 9 숫자 의미: stop
# range(0,10) 0 ~ 9 숫자의미 : start stop
# range(0,10,2) 0 2 4 6 8 start stop step

for i in range(0, 10, 2):
    print(i)

for character in "안녕하세요":
    print("-", character)

# listx의 요소 중 짝수인 수만 찾아서 총 짝수가 몇 개인지를 출력하고 짝수들의 합을 출력하세요
listx = [1,3,4,6,8,10,11,12,13,15]

cnt = 0
sum = 0
for i in listx:
    if i % 2 == 0:
        cnt += 1
        sum += i

print(f"짝수의 개수: {cnt}")
print(f"짝수의 합: {sum}")

#위에 개념은 다 1차원

# for문의 중첩사용 하나면 1차원 두개 중첩으로 면 2차원

listb = [[1,2,3],[4,5,6],[7,8,9]]

# 중첩리스트, 2차원 리스트
# 중첩 for문을 활용해서 listtb의 모든 요소 123456789 각각 전부 출력하려면?

# for element in listb:
#     for i in element:
#         print(i)

# 구구단 출력
# input으로 사용자가 입력하는 숫자(2~9) 사이에 해당하는 구구단을 출력해라
# 2중 for문 사용
# num = int(input("몇 단?: "))


# for i in range(1,10):
#     print(f"{num} * {i} = {num*i}")
#
# for i in range(2,10):
#     for j in range(1,10):
#         print(i,"* " ,j,"=", i*j)


numbers = [273,103,5,32,65,9,72,800,99]
for n in numbers:
    if n % 2 == 0:
        print(f"{n}은 짝수입니다.")
    else:
        print(f"{n}은 홀수입니다.")

for n in numbers:
    if n // 100 >= 1:
        print(f"{n}은 3 자릿수입니다.")
    elif n // 10 >= 1:
        print(f"{n}은 2 자릿수입니다.")
    else:
        print(f"{n}은 1 자릿수입니다.")


numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number+2) % 3].append(number)

print(output)

# 딕셔너리 : 사전
# 리스트는 인덱스 기반으로 값을 저장하는 열 데이터
# 딕셔너리는 키Key를 기반으로 값을 저장하는 데이터
# {} 로 선언
# {키:값,키:값,키:값}
# {학생1: 여, 학생2: 남, 학생3: 여}
# 키:값 쌍으로 구성
# 쉼표로 구분

# 키에는 문자열, 숫자, 불 등을 쓸 수 있다.
# 값에는 문자열, 숫자, 리스트도 올 수 있다.


dictA = {'학생1': 20, '학생2': 30, '학생3': 25}
print(type(dictA))
# 딕셔너리는 키를 통해 값에 접근한다.
# 키를 통해 접근하는 방식이 인덱싱 방식하고 동일 : [키값]
print(dictA['학생2'])

# 딕셔너리 내부에는 값으로 리스트와 딕셔너리 또한 포함할 수 있다.

dict_b = {'director': ['안소니 루소','조 루소'], 'cast': ['아이언맨','타노스','토르','닥터스트레인지','헐크']}
print(dict_b['director'])

dictB = {'학생1': ['여', 20], '학생2':['남', 30], '학생3': {'나이':25, '이름':'ㅂㅂㅂ'}}
print(dictB['학생1'][1])
print(dictB['학생3']['이름'])

dictionary = {
    "name" : "7D 건조망고",
    "type": "당절임",
    "ingredient": ["망고", '설탕', '메타중아황산나트륨','치자황색소'],
    "origin": "필리핀"

}

print("name:", dictionary['name'])
print("name:", dictionary['type'])
print("name:", dictionary['ingredient'])
print("name:", dictionary['origin'])
print()

dictionary['name'] = '8D 건조망고'

print("name:", dictionary['name'])


# 딕셔너리의 문자열 키를 생성할 때 문자열은 따옴표 꼭 쓴다.

# 딕셔너리에 추가/삭제
# 딕셔너리[새로추가할키] = 새로추가할 키에 대응되는 값

dictB['학생3'] = 500
print(dictB)
# 딕셔너리 키 추가 방식으로 기존에 있는 키를 추가하면 값이 바뀐다.

# 딕셔너리 요소 제거 : del
del dictB['학생2']
print(dictB)

# print(dictB['학생2'])
# 딕셔너리에서 없는 키를 검색하면 keyError 발생
# key에러는 del을 통한 삭제과정에서도 마찬가지로 없는 키를 넣으면 발생한다.

# 딕셔너리 내부에 키 유무 확인 방법
# in 키워드 사용

# key = input("접근하고자 하는 키: ")

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")


# get() 함수
# get함수는 딕셔너리의 키로 값을 추출하는 기능이다
# get을 통해 요청한 키가 없을 때는 None을 출력한다.

value = dictionary.get("존재하지 않는 키")
print("값: ", value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")

# for 문에 반복범위로 딕셔너리를 배치할 경우
# 딕셔너리 내부의 키가 변수 i에 순서대로 대입된다.
# for i in dictB:

# 딕셔너리 관련함수
# 1. keys() 함수
# dict_keys 객체가 반환된다.
# dict_keys 객체는 list()함수로 형변환해서 활용 가능
dictC = {'name': '학생1', 'age':'20','gen':'male', 'birth':'1013'}
print(type(list(dictC.keys())[0])) # 객체형태라 인덱싱 못함 형변환해줘야 함
print(list(range(10))) # 객체형태

# for문에서 dict_key, range같은 객체를 반봅 범위로 바로 지정할 수 있다.

# 2. values() 밸류값만 모아서 밸류객체로 반환
print(list(dictC.values()))

# 3. clear()
# dictC.clear()
# print(dictC)

# A음식 재료
# 고기 버섯 양파 마늘 / 물 간장 후추
# /앞은 주재료
# /뒤에는 양념재료
# B음식 재료
# 고기 감자 당근 양파 호박/ 물 깨 소금

dict_menu = {'A음식': {'주재료': ['고기', '버섯', '양파', '마늘'], '부재료': ['물', '간장', '후추']},
              'B음식': {'주재료': ['고기', '감자','당근','양파','호박'], '부재료': ['물', '깨', '소금']}
               }

print(dict_menu.keys())
menu = input('음식명: ')

if menu.find('A') != -1:
    print('A음식의 주재료는',dict_menu['A음식']['주재료'],'이고', '부재료는',dict_menu['A음식']['부재료'],'입니다.')

    print('재료의 가짓수는',len(dict_menu['A음식']['주재료']) +
      len(dict_menu['A음식']['부재료']),'개 입니다')
elif menu.find('B') != -1:
    print('B음식의 주재료는',dict_menu['B음식']['주재료'],'이고', '부재료는',dict_menu['B음식']['부재료'],'입니다.')

    print('재료의 가짓수는',len(dict_menu['B음식']['주재료']) +
      len(dict_menu['B음식']['부재료']),'개 입니다')


pets = [
    {'name': '구름', 'age': 5},
    {'name': '초코', 'age': 3},
    {'name': '아지', 'age': 1},
    {'name': '호랑이', 'age': 1},
        ]
print("# 우리동네 애완동물들")
for i in pets:
    print(f"{i['name']} {i['age']}살")


numbers = [1,2,3,4,5,4,3,2,3,4,3,2,1,1]
counter = {}

for number in numbers:
    if counter.get(number) == None:
         counter[number] = 1
    else:
        counter[number] +=1

print(counter)


character = {
    'name': '기사',
    'level': 12,
    'items': {
        'sword': '불꽃의 검',
        'armor': '풀플레이트'
    },
    "skill": ['베기','세게 베기', '아주 세게 베기']
}

# if문에 타입으로 나눠야함
# for key in character:
#     print(key ,":", character[key])
# for k in character['items']:
#     print(k, ":", character['items'][k])
# for i in range(3):
#     print('skill :', character['skill'][i])


















