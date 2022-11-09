# 하노이의 탑 문제
# 원판 : 데이터/ 기둥: 스택으로 가정하여 lifo문제, 재귀함수로 해결

start_p = [] # 시작기둥
that_p = [] # 대상기둥
assist_p = [] # 보조기둥

def rec():
    assist_p.append(start_p.pop())  # 시작기둥의 마지막 요소를 보조기둥에 넣어라

    if start_p[-1] > assist_p[-1]:  # 만약 시작기둥의 마지막 요소가 보조기둥의 마지막 요소보다 크다면
        that_p.append(start_p.pop())  # 대상기둥에 시작기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()
        that_p.append(assist_p.pop())  # 그리고 나서 대상기둥에 보조기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()
    if len(assist_p) == 0:  # 만약 보조기둥이 비어있다면
        assist_p.append(start_p.pop())  # 시작기둥의 마지막 요소를 보조기둥에 집어넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()

    if assist_p[-1] > that_p[0]:  # 만약 보조기둥의 마지막 요소가 대상기둥의 첫번째 요소보다 크다면
        assist_p.append(that_p.pop())  # 보조기둥에 대상기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()
        start_p.append(that_p.pop())  # 시작기둥에 대상기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()
        start_p.append(assist_p.pop())  # 시작기둥에 보조기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()
        that_p.append(assist_p.pop())  # 대상기둥에 보조기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()
        assist_p.append(start_p.pop())  # 보조기둥에 시작기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()
        that_p.append(start_p.pop())  # 대상기둥에 시작기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print()
        that_p.append(assist_p.pop())  # 대상기둥에 보조기둥의 마지막 요소를 넣어라
        print("보조기둥 =>", assist_p)
        print("시작기둥 =>", start_p)
        print("대상기둥 =>", that_p)
        print("=============================while문 완료")

    return

def hanoi(circle):
    for i in range(1, circle + 1): # 1부터 시작해서 circle길이 +1 만큼 돌려라
        start_p.append(i) # i 를 시작기둥에 집어 넣어라
        start_p.sort(reverse=True) # 시작기둥을 내림차순으로 정렬하라
    print("시작기둥 => ", start_p)
    print()

    while True:
        if len(assist_p) == 0 and len(that_p) == 0: # 만약 보조기둥이 비어있으면
            rec()
            break

            # assist_p.append(start_p.pop()) # 시작기둥의 마지막 요소를 보조기둥에 넣어라
            #
            # if start_p[-1] > assist_p[-1]: # 만약 시작기둥의 마지막 요소가 보조기둥의 마지막 요소보다 크다면
            #     that_p.append(start_p.pop()) # 대상기둥에 시작기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            #     that_p.append(assist_p.pop()) # 그리고 나서 대상기둥에 보조기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            # if len(assist_p) == 0: # 만약 보조기둥이 비어있다면
            #     assist_p.append(start_p.pop()) # 시작기둥의 마지막 요소를 보조기둥에 집어넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            #
            # if assist_p[-1] > that_p[0]: # 만약 보조기둥의 마지막 요소가 대상기둥의 첫번째 요소보다 크다면
            #     assist_p.append(that_p.pop()) # 보조기둥에 대상기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            #     start_p.append(that_p.pop()) # 시작기둥에 대상기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            #     start_p.append(assist_p.pop()) # 시작기둥에 보조기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            #     that_p.append(assist_p.pop()) # 대상기둥에 보조기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            #     assist_p.append(start_p.pop()) # 보조기둥에 시작기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            #     that_p.append(start_p.pop()) # 대상기둥에 시작기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #     print()
            #     that_p.append(assist_p.pop()) # 대상기둥에 보조기둥의 마지막 요소를 넣어라
            #     print("보조기둥 =>", assist_p)
            #     print("시작기둥 =>", start_p)
            #     print("대상기둥 =>", that_p)
            #
            break





def main():
    circle= int(input("원판의 갯수 : "))

    hanoi(circle)


main()