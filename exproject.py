import math
import sys
import pandas as pd
sys.setrecursionlimit(1000)
earned_income_tax = [] # 근로소득세 변수
sum_list = 0
mark = ["/","!","~","@","#","$","%","^","&","*","_","+","=","|","<",">","?"] # 특수기호 없애기 위한 변수
MAX = 13 # 행 크기 상수
final_index = 0 # 행 붙이기의 마지막 인덱스 변수
error_list=[] # 찢겨져 있는 행 담아놓는 변수


# 빈문자열만 들어있는 리스트 삭제하는 함수
def remove_none():
    try:
        global earned_income_tax
        earned_income_tax = list(filter(None, earned_income_tax))
        for i in range(len(earned_income_tax)):  # 위 아래 다른 코드인데 하나라도 지우면 안됨, 다 있어야 됨....왜지????#1
            if "" in earned_income_tax[i]:  # 빈문자열 없앰
                earned_income_tax[i].remove("")
    except Exception as e:
        print("remove_none =>", type(e), e)

# 찢어진 행 합치는 함수
def distroyed_recovery():
    try:
        global error_list
        global sum_list
        global final_index
        if len(error_list) == 0:
            search_row() # 찢어진 행 찾는 함수실행
        print("===> ", error_list)
        for j in range(1, len(error_list)): # 에러리스트 길이만큼 반복하여 행 합치기
            print("earned_income_tax[error_list[0]] -> ",earned_income_tax[error_list[0]])
            sum_list = len(earned_income_tax[error_list[0]])

            if sum_list != MAX:
                earned_income_tax[error_list[0]] += earned_income_tax[error_list[j]] # 첫번째 나온 행번호에 다음 행들을 합친다.
                earned_income_tax[error_list[j]].clear()

                if len(earned_income_tax[error_list[0]]) ==MAX: # 만약 에러리스트 첫번째 요소에 해당하는 행의 길이가 MAX와 같다면
                    # del earned_income_tax[error_list[j]] # 뒤에 이어붙인 원본을 제거하라
                    # remove_none()
                    earned_income_tax[error_list[j]] = "" # 나중에 삭제하기 위해 빈문자열로 처리...
                    error_list[0] = ""
                    error_list[j] = ""
                    error_list = list(filter(None, error_list))
                    # final_index = j # 마지막 행번호를 저장
                    print("error_list=>", error_list)

                    distroyed_recovery()

        remove_none()


        # 행 프린트
        for j in range(len(earned_income_tax)):
            print(j, "-->", earned_income_tax[j])


    except Exception as e:
        print("distroyed_recovery", type(e), e)


# 찢어진 행 찾는 함수
def search_row():
    try:
        for i in range(len(earned_income_tax)):
            sum_list = len(earned_income_tax[i])
            if sum_list != MAX:
                error_list.append(i)
    except Exception as e:
        print("search_row", type(e), e)



# ================================================파일 불러오기==================================================
try:
    with open("근로소득간이세액표_error.txt",'r', encoding='UTF-8') as file:
        for line in file:
            earned_income_tax.append(line.strip().split("\n"))  # 근로소득세 변수생성 "\n"으로 나눔
            remove_none() # 공백 없애는 함수
except Exception as e:
    print("파일불러오기",type(e),e)

# ====================================쉼표없애고 \t로 구분해서 원래 변수에 다시 꽂기==================================
try:

    for i in range(len(earned_income_tax)):
        for j in range(len(earned_income_tax[i])):
            earned_income_tax[i][j] = earned_income_tax[i][j].replace(",","") # 쉼표 없앰
            earned_income_tax[i] = earned_income_tax[i][j].split("\t") # \t으로 구분해서 집어넣음
except Exception as e:
    print("쉼표, split",type(e), e)

# ==========================================잘못 입력된 특수문자들 삭제하기=========================================
try:
    for k in range(len(mark)):
        find_list = mark[k]
        for i in range(len(earned_income_tax)):
            for j in range(len(earned_income_tax[i])):
                earned_income_tax[i][j] = earned_income_tax[i][j].replace(find_list,"") # 특수문자 없앰
                # print(i, " = ", earned_income_tax[4:]) # 행번호 출력 earned_incmome_tax[i][j] 는 str

    # 위에 글자만 나오는 행 빼고 넣음
    earned_income_tax = earned_income_tax[4:]
    # for i in range(len(earned_income_tax)):
    #     print(i, " => ", earned_income_tax[i])
except Exception as e:
    print("노이즈삭제",type(e), e)
# ================================================찢겨져 있는 행 붙이기===========================================


try:

    distroyed_recovery()


except Exception as e:
    print("찢겨진 행 이어붙이기",type(e), e)

# ===============================================None에 값 집어넣기==============================================
try:
    none_list = [] # None값 들어있는 리스트를 옮겨담을 리스트
    none_list_num_list= [] # None값이 들어간 리스트의 행번호를 담는 변수
    a = 0 # None값이 들어가있는 인덱스의 이전요소들 중 None이 아닌 첫번째 요소
    b = 0 # None값이 들어가있는 인덱스의 이전요소들 중 None이 아닌 두번째 요소
    result = 0
    fre_i_list = [] # earned_income_tax[i - 1]
    sur_i_list = [] # earned_income_tax[i + 1]
    fre_j = 0 # earned_income_tax[i][j-1]
    sur_j = 0 # earned_income_tax[i][j + 1]
    j = 1
    try:
        print("None!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        for i in range(len(earned_income_tax)):
            if "None" in earned_income_tax[i]: # None을 찾으면
                none_list = earned_income_tax[i] # none_list에 집어넣어라
                none_list_num_list.append(i) # none이 들어있는 행번호를 넣어라
                print(none_list)
                fre_i_list = earned_income_tax[i - 1] # 이전 행을 fre_i_list에 넣어라
                sur_i_list = earned_income_tax[i + 1]
                print("fre => ",fre_i_list)
                print("sur => ",sur_i_list)
                
            else: # i가 None이면
                continue # 계속해라
            break
    except Exception as e:
        print("None값 for문", type(e),e)
    # for i in range(len(earned_income_tax)):
    #     print(earned_income_tax[i])
except Exception as e:
    print("None값", type(e), e)



# if a > b : # a가 b보다 크면
#     result = int(a) - int(b) # a - b를 해서 result에 넣어라
#     print(result)
# elif b > a : # b가 a보다 크면
#     result = int(b) - int(a) # b - a를 해서 result에 넣어라
#     print(result)
#
# for i in range(MAX): # 길이는 13으로 맞춰져 있으니 MAX만큼 돌려서
#     if earned_income_tax[none_list_num][i] == "None": # 인덱스에 None이 포함돼있으면
#         earned_income_tax[none_list_num][i] = (int(none_list[i - 1]) - int(result *0.8)) # 이전 인덱스의 값에서 result의 0.8을 곱한 값을 빼서 넣어라



# 계산기 시작

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

annual_income = 0 # 연봉
month_income = 0 # 월급
national_pension = 0 # 국민연금
health_insurance = 0 # 건강보험
care_insurance = 0 # 요양보험
employmone_insurance = 0 # 고용보험
tax_on_earned_income = 0 # 근로소득세
local_income_tax = 0 # 지방소득세
real_anuual_income = 0 # 연 실수령액
# 근로소득세 계산하기
def tax(annual_income):
    try:
        for i in range(len(earned_income_tax)):

            if annual_income > int(earned_income_tax[i][0]):
                continue
            elif annual_income <int(earned_income_tax[i][0]):
                return int(earned_income_tax[i - 1][2])
    except Exception as e:
        print("근로소득세 계산하기",type(e), e)

def main():
    try:
        print("연봉을 입력하세요.(단위 : 만 원)")
        annual_income= int(input(">>"))
        month_income = int(annual_income/12)
        national_pension = int((month_income * 0.045)*10000)
        health_insurance = int((month_income * 0.03495) *10000)
        care_insurance = int(math.floor(int(health_insurance * 0.1227))/10)*10
        employmone_insurance = int((month_income * 0.09)* 10000)
        earned_income = tax(annual_income)
        local_income_tax = int(math.floor(int(earned_income * 0.1))/10) *10

        real_month_income = int(((annual_income * 10000) / 12)- national_pension - health_insurance - care_insurance - employmone_insurance - earned_income - local_income_tax)
        real_anuual_income = int(int(real_month_income * 10000)/12)
        print("국민연금 = ",format(national_pension, ','),
              "\n건강보험 = ", format(health_insurance,','),
              "\n요양보험 = ", format(care_insurance,','),
              "\n고용보험 = ", format(employmone_insurance,','),
              "\n근로소득세 = ", format(earned_income,','),
              "\n지방소득세 = ", format(local_income_tax,','),
              "\n=================================",
              "\n년 예상 실수령액 = ", format(real_anuual_income,','),
              "\n월 환산금액 = ", format(real_month_income,','))

    except Exception as e:
        print("메인함수",type(e),e)





    # 결과창
    # print(f"실수령액은 {}입니다.")

main()
file.close()