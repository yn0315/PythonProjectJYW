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

end_time = time.time() + 10
dict = {}

num = int (input("입력: "))
def mul(a):
    print("시작숫자: ", a)
    while time.time() < end_time:
        if a % 3 == 0:
            if '3의 배수' not in dict:
                dict['3의 배수'] =1
            dict['3의 배수'] += 1

        if a % 5 == 0:
            if '5의 배수' not in dict:
                dict['5의 배수'] = 1
            dict['5의 배수'] += 1


        if a % 3 == 0 and a % 5 == 0:
            if '공배수' not in dict:
                dict['공배수'] = 1
            dict['공배수'] += 1

        a += 1
    print("마지막 숫자: ", a)

    return print(dict)


mul(num)
