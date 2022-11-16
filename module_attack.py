
import random
# 몬스터 공격하는 함수, 몬스터와 마주치지 않고 호출했을 시 함수 실행 안되게 막아야 함

def attack(character, monster):
    if character is None or monster is None:
        print("전투를 시작할 수 없습니다.")
        return

    # 캐릭터의 종류에 따라 공격 데미지가 다르게 들어가야 함
    if character is not None and monster is not None:
        print("j = 공격, k = 방어")
        a_or_d = input(">>")
        if a_or_d == "j":
            print(f"{character}가 공격합니다.")
            # 캐릭터와 몬스터의 hp를 띄워줘야 함
            num = random.randint(1,2)
            if num == 1:
                print(f"{monster}가 공격했습니다.")
                # 캐릭터와 몬스터의 hp를 띄워줘야 함
            elif num == 2:
                print(f"{monster}가 방어했습니다.")
                # 캐릭터와 몬스터의 hp를 띄워줘야 함
        elif a_or_d == "k":
            print(f"{character}가 방어했습니다.")
            # 캐릭터와 몬스터의 hp를 띄워줘야 함
            num = random.randint(1,2)
            if num == 1:
                print(f"{monster}가 공격했습니다.")
                # 캐릭터와 몬스터의 hp를 띄워줘야 함
            elif num == 2:
                print(f"{monster}가 방어했습니다.")
                # 캐릭터와 몬스터의 hp를 띄워줘야 함
import sys, time, msvcrt

def readInput( caption, default, timeout = 0.5):

    start_time = time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32: #space_char
                input += "".join(map(chr,byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
#           print("timing out, using default value.")
            break

#    print('')  # needed to move to next line
    if len(input) > 0:
        return input
    else:
        return default





