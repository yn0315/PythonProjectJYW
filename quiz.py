# 1. 문자열 hellopython에서 알파벳 o를 모두 제거하여 출력
t = "hellopython"
print(t.replace("o",""))

# 2. hellopython을 이용하여 ten문자열 출력
print(t[-4] + t[1] + t[-1])
# 3. 차량번호판 43가2234에서 뒤 4자리만 출력
car = "43가2234"
print(car[3:])

# 4. 사용자입력을 통해 입력받은 텍스트에서 숫자로 변환 가능한지 검사 후 가능하면 숫자로 변환하고 불가능하면 불가능텍스트 출력

ent = input("입력: ")
if ent.isdigit():
    int(ent)
    print(ent)
else:
    print("불가능")

#5. list[1,2,3,4,5,6,7,8,9]에서 슬라이싱을 활용하여 홀수만 출력
list = [1,2,3,4,5,6,7,8,9]
print(list[::2])

#6. 1+2+3+4+...+9라고 출력(리스트관련 함수활용)아...문자열로 출력
print("==============6번=================")
# 리스트 -> 문자열

a = ""
for i in range(len(list) *2):

    if i % 2 == 0:
        list.insert(i,'+')
    a += str(list[i])


print(list)
print(a)



# 7. 6번의 결과 "1+2+3+...+9를 다시 [1,2,3,4,5,6,7,8,9]로 변경하여 출력(리스트 함수 활용)
print("================7번===================")

# while list.count("+"):
#     list.remove("+")
# for i in range(len(list)):
#     if i % 2 == 0:
#         list.pop(i)# for 문 돌면서 리스트 줄어드니까 인덱스에러....
print(list)


# 8. [2,5,2,9,11,100]리스트에서 짝수 제거 후 내림차순으로 정렬후 출력
print("==================8번====================")
list2 = [2,5,9,11,100]
for i in list2:
    if i % 2 == 0:
        list2.remove(i)
list2.sort(reverse=True)

print(list2)


# 9. 무작위로 입력받은 영문텍스트에서 가장 앞자리만 대문자이고 나머지 자리는 모두 소문자로 변경하여 출력
print("==================9번======================")

abc = input("무작위 영문: ")
p = ""
p += abc[0].upper()
for i in range(1,len(abc)):
    p += abc[i].lower()
print(p)


# 인형뽑기
# 1. 인형을 못뽑게
# 2. 집게발 힘이 없게
# 3. 인형의 위치 리스트 중첩 9 3*3 (1,1)은 입구로 지정, 층수가 있으면 3차원까지.... 어려우므로 삭제
# 4. 돈이 많은 사람
# 5. 1회 1000 12회 10000
# 6. 마지막 턴
# 7. 시간
# 8. 다른사람이 뽑는 것
# 9. 인형의 무게
# 10. 인형을 집기 위한 힘의 크기



