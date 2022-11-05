import sys
# 근로소득 간이세액표

# ex 연봉 2400
# 월 200
# 국민연금 200의 4.5프로
# 건강보험 200의 3.495프로
# 요양보험은 건강보험료 결과의  12.27프로
# 고용보험은 200의 0.9프로
# 근로소득세는 세액표 : 33,570원
# 지방소득세는 근로소득세의 10프로 : 3,350원
# 모든 금액 계산 결과에서 10원 아래 1자리 수는 절삭

sys.setrecursionlimit(1000) # 재귀함수 깊이 늘리기

earned_income_tax = [] # 근로소득세 변수
error_list=[] # 찢겨져 있는 행 담아놓는 변수
mark = ["/","!","~","@","#","$","%","^","&","*","_","+","=","|","<",">","?"] # 특수기호 없애기 위한 변수
MAX = 13 # 행 크기 상수

# 빈문자열만 들어있는 리스트 삭제하는 함수
def remove_none():
    global earned_income_tax
    earned_income_tax = list(filter(None, earned_income_tax))
    for i in range(len(earned_income_tax)):  # 위 아래 다른 코드인데 하나라도 지우면 안됨, 다 있어야 됨....왜지????#1
        if "" in earned_income_tax[i]:  # 빈문자열 없앰
            earned_income_tax[i].remove("")

# 찢어진 행 이어붙이기 함수 안됨 너무 많이 돌아가......
# def plus_row(n):
#     for i in range(1, len(error_list)):  # error_list만큼 반복해서
#         earned_income_tax[error_list[n]] += earned_income_tax[error_list[i]]  # 찢어진 행의 첫번째 행에 다음 행들을 이어 붙여라
#         earned_income_tax[error_list[i]].clear()  # 이어 붙인 행은 내용물을 삭제하라
#         if earned_income_tax[i] == MAX:  # 이어붙이다 13이 되면 멈춰라
#             return
#         else:
#             plus_row(i + 1)
#             return
#     return

f = open("근로소득간이세액표.txt", 'r', encoding = 'UTF-8')
with open("근로소득간이세액표.txt",'r', encoding='UTF-8') as file:
    for line in file:
        earned_income_tax.append(line.strip().split("\n"))  # 근로소득세 변수생성 "\n"으로 나눔
        remove_none() # 공백 없애는 함수

# 쉼표없애고 \t로 구분해서 원래 변수에 다시 꽂기
for i in range(len(earned_income_tax)):
    for j in range(len(earned_income_tax[i])):
        earned_income_tax[i][j] = earned_income_tax[i][j].replace(",","") # 쉼표 없앰                     #2
        earned_income_tax[i] = earned_income_tax[i][j].split("\t") # \t으로 구분해서 집어넣음                 #3

# 잘못 입력된 특수문자들 삭제하기
for k in range(len(mark)):
    find_list = mark[k]
    print(find_list)
    for i in range(len(earned_income_tax)):
        for j in range(len(earned_income_tax[i])):
            earned_income_tax[i][j] = earned_income_tax[i][j].replace(find_list,"") # 특수문자 없앰              #4
            # print(i, " = ", earned_income_tax[4:]) # 행번호 출력 earned_incmome_tax[i][j] 는 str

# 위에 글자만 나오는 행 빼고 넣음
earned_income_tax = earned_income_tax[4:]

# 찢겨져 있는 행 붙이기
for i in range(len(earned_income_tax)):
    # print(i, " = " , earned_income_tax[i]) # 행번호 출력
    if len(earned_income_tax[i]) < MAX : # 행의 길이가 13보다 작으면
        error_list.append(i) # error_list에 행번호 집어넣어라
print(error_list)

sum_list = 0 # error_list안에 들어있는 행들의 길이 합에 이용되는 변수
for i in range(len(error_list)): 
    sum_list += len(earned_income_tax[error_list[i]]) # error_list에 포함된 행들의 길이를 합해서 변수에 넣어라
    if sum_list == MAX: # 길이가 13이면

        for j in range(1,len(error_list)): # error_list만큼 반복해서
            earned_income_tax[error_list[0]] += earned_income_tax[error_list[j]] # 찢어진 행의 첫번째 행에 다음 행들을 이어 붙여라
            earned_income_tax[error_list[j]].clear() # 이어 붙인 행은 내용물을 삭제하라
            if earned_income_tax[j] == MAX: # 이어붙이다 13이 되면 멈춰라
                break
            else:       # 13이 안됐으면 계속해라
                continue

        remove_none() # 내용물이 삭제된 행을 지워라

# None에 값 집어넣기
for i in range(len(earned_income_tax)):
    if "None" in earned_income_tax[i]:
        print(earned_income_tax[i])



# for i in range(len(earned_income_tax)):
#     print(i, " ==>" , earned_income_tax[i])











# 계산기 시작
# def main():
#     print("연봉을 입력하세요.")
#     annual_income= input(">>")






    # 결과창
    # print(f"실수령액은 {}입니다.")

# main()