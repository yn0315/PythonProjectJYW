
# 근로소득 같이세액표

# f = with open("근로소득간이세액표.txt",'r') as file:
#     contents = mydoc.read() # 텍스트파일 내부 컨텐츠를 한 덩어리로 다 가져옴
# print(contents)

# ex 연봉 2400
# 월 200
# 국민연금 200의 4.5프로
# 건강보험 200의 3.495프로
# 요양보험은 건강보험료 결과의  12.27프로
# 고용보험은 200의 0.9프로
# 근로소득세는 세액표 : 33,570원
# 지방소득세는 근로소득세의 10프로 : 3,350원
# 모든 금액 계산 결과에서 10원 아래 1자리 수는 절삭


re_item_list = [[]]
grand_re_item_list = []
count = 0
f = open("근로소득간이세액표.txt", 'r', encoding = 'UTF-8')
with open("근로소득간이세액표.txt",'r', encoding='UTF-8') as file:
    for line in file:
        (earned_income_tax) = line.strip().split("\n")  # 근로소득세 변수생성 "\n"으로 나눔
        earned_income_tax = list(filter(None, earned_income_tax)) # 빈문자열로 엔터쳐있는 거 없앰
        # print(earned_income_tax)

        for item in earned_income_tax:

            for i in range(len(earned_income_tax)):

                re_item_list[i] = item.replace(",","")# 쉼표를 없애고 새로운 리스트변수에 집어넣음

                if "/" in re_item_list[i]:
                    re_item_list[i] = re_item_list[i].replace("/","")# 슬래시 없앰


                for j in range(len(earned_income_tax)): # grand_item_list에 분해해서 집어넣음

                    grand_re_item_list = re_item_list[j].split('\t')

        earned_income_tax = grand_re_item_list # 원래 데이터에 집어넣음
        print(earned_income_tax)

        # 리스트의 크기 13개인지 .....
    # for i in range(len(earned_income_tax)):
        # count 변수 생성
        # i를




# 계산기 시작
# def main():
#     print("연봉을 입력하세요.")
#     annual_income= input(">>")
#
#
#
#
#
#
#     # 결과창
#     print(f"실수령액은 {}입니다.")