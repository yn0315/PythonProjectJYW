# 221110
import math as m # math를 앞으로 m으로 부르겠다. 새로운 이름으로 부르겠다.
# 373페이지

dictf = {"파일이름": 1, "파일인코딩방식": 2}

list = [1,2,3,4]
try:
    file = open("info.txt", "w")
    file.close()
    for i in range(10):
        print(list[i])
except Exception as e: # 이 상황을 e라고 부르겠다.
    print(e)
    print("오류가 발생했습니다.")

finally:
    print("# 파일이 제대로 닫혔는지 확인하기")
    print("file.closed: ", file.closed) # closed는 프로퍼티로 속성을 나타냄
    print(file.mode)
    print(file.name)
    print(file.buffer)
    print(file.encoding)
    if file.encoding == "cp949":
        print("cp949 인코딩 방식입니다.")
        dictf['파일인코딩방식'] = file.encoding

print(dictf)

# 객체에 접근 .을 찍어서
# 객체는 v,p,m을 지닐 수 있다.
# v : 변수
# p : 속성
# m : 함수


try:
    file = open("info.txt", "w")
    # 예외.발생해라()
    file.close()
except Exception as e: # 이 상황을 e라고 부르겠다.
    print(e)
    print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed: ", file.closed) # closed는 프로퍼티로 속성을 나타냄

# 파일은 finally에 가서 닫는 것이 안전하다.

try:
    file = open("info.txt", "w")
    # 예외.발생해라()
except Exception as e: # 이 상황을 e라고 부르겠다.
    print(e)
    print("오류가 발생했습니다.")
finally:
    file.close()
    print("# 파일이 제대로 닫혔는지 확인하기")
    print("file.closed: ", file.closed) # closed는 프로퍼티로 속성을 나타냄

def test(): # finally를 먼저 읽기 때문에 try를 탈출하는 것 같아도 아님
    print("test()함수의 첫 줄입니다.")
    try:
        print("try구문이 실행되었습니다.")
        return # 함수를 탈출하는 게 맞음
        print("try구문의 return키워드 뒤입니다.")
    except:
        print("except구문이 실행되었습니다.")

    else:
        print("else구문이 실행되었습니다.")

    finally:
        print("finally 구문이 실행되었습니다.")
    print("test()함수의 마지막 줄입니다.")

test()

numbers = [52,273,32,103,90,10,275]

print("# 1 요소 내부에 있는 값 찾기")
print(" - {} 는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# 2 요소 내부에 없는 값 찾기")
number = 10000
try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index((number))))

except:
    print("- 리스트 내부에 없는 값입니다.")
print()
print("---정상적으로 종료되었습니다.")

# output = 10 + "개" - 타입에러
# int("안녕하세요") - 밸류에러
# cursor.close) - 신택스 에러
# [1,2,3,4,5][10] - 인덱스에러

# Exception
# 예외객체
# 모든 예외를 하나로 전달 받는다.

# 388
# list_number = [52,273,32,72,100]
#
# try:
#     number_input = int(input("정수 입력 : "))
#     print(" - {}번째 요소.".format(number_input, list_number[number_input]))
#     print()
# except ValueError:
#     print("정수를 입력해주세요.")
# except IndexError:
#     print("리스트의 인덱스를 벗어났어요!")
#

# 389
# list_number = [52,273,32,72,100]
#
# try:
#     number_input = int(input("정수 입력 : "))
#     print(" - {}번째 요소.".format(number_input, list_number[number_input]))
#     print()
#     예외.발생()
# except ValueError as a:
#     print("정수를 입력해주세요.")
#     print(type(a), a)
# except IndexError as b :
#     print("리스트의 인덱스를 벗어났어요!")
#     print(type(b), b)
# except Exception as c:
#     print("미리 파악하지 못한 예외 발생")
#     print(type(c), c)
#
    
# raise
# 내가 만든 예외를 발생시키는 것

# 복사

x = 50
def pow(v):
    temp=v
    v = v**2
    print(temp)
    print(v)

pow(x)
import copy
a = [1,2,3,4]
b = [0]

def change(l):
    temp2 = l
    # l.append(9) # 이건 관련함수, 객체에 관련된거, 원본을 건드린다.
    l= l+[9]# 연산, 9를 더한 객체를 만들어라
    print(temp2)
    print(l)

change(a)

# 얕은 복사
# 슬라이싱, 카피함수 쓰는 거

# 깊은 복사
# copy모듈의 deepcopy(복사하려는 대상)함수를 쓰는 것

# lista = ["123",'456']
# listb = lista
# listb.append("789")
# print(lista)
# print(listb)

lista = ["123",'456']
listb = lista.copy()
print(id(listb))
print(id(lista))
print(id(lista[0])) # 같은 주소나옴
print(id(listb[0])) # 같은 주소나옴
listb.append("789")
# listb = listb + [999]  여기서는 위 설명과 다르다...
print(lista)
print(listb)

# 카피를 하면 b리스트 수정해도 a에 반영x
# 얕은 복사는 안에 요소를 공유하기 때문에 같은 결과나옴
# list_a = ["123",["456", "789"]]
# list_b = list_a.copy()
#
# list_b[1][0]="555"
# print(list_a)
# print(list_b)

list_a = ["123",["456", "789"]]
list_b = copy.deepcopy(list_a)

list_b[1][0]="555"
print(list_a)
print(list_b)
print(id(list_a[1]))
print(id(list_b[1]))

