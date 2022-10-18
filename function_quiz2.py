# 사용자로부터 입력받은 숫자로부터 +1 씩 증가하는 끝이 정해지지 않은 범위까지의 숫자들 중
# 3의 배수의 개수
# 5의 배수의 개수
# 3과 5의 공배수를 딕셔너리에 담아 출력하세요
# ex {"3의 배수": 20, "5의 배수: ~~, "공배수: ~~}

# 함수는 10초간 작동하고 종료 -> 스타트 타임 now.second 엔드타임 now.second + 10
# 위 함수는 딕셔너리를 리턴 -> 빈 딕셔너리 생성, return dict
# 위 함수를 입력받은 시작숫자와 마지막까지 체크한 숫자를 출력 -> 함수 시작에 한번, 마지막에 한번 출력
#
# ex 15의 경우 3의 배수 5의 배수 공배수 모두 포함

# 사용자입력 n의 배수 사용자입력 m의 배수 , n 과 m의 공배수 출력으로 변경

import time


# num = int (input("수 입력: "))
# n = int (input("배수입력1: "))
# m = int (input("배수입력2: "))

# f문자열은 연산도 됨, 선언부에도 써도 됨

def mul(a, n, m):
    dict = {}
    end_time = time.time() + 10
    print("시작숫자: ", a)
    print(time.time())
    while time.time() <= end_time:
        if a % n == 0:
            if f'{n}의 배수' not in dict:
                dict[f'{n}의 배수'] =1
            dict[f'{n}의 배수'] += 1

        if a % m == 0:
            if f'{m}의 배수' not in dict:
                dict[f'{m}의 배수'] = 1
            dict[f'{m}의 배수'] += 1


        if a % n == 0 and a % m == 0:
            if '공배수' not in dict:
                dict['공배수'] = 1
            dict['공배수'] += 1

        a += 1
    print("마지막 숫자: ", a)

    return dict,time.time() # 리턴할 때 시간찍어야 가장 정확


# print(mul(num))
print(mul(int(input("숫자입력")), int(input("n")), int(input("m"))))


