

# 깜빡이(방향지시등) 함수
def winker():
    try:
        # on/off기능 좌 우 기능
        print("a. 좌측 방향지시등 ON s. 좌측 방향지시등 OFF d. 우측 방향지시등 ON w. 우측 방향지시등 OFF")
        alpa = input(">>")

        if alpa == "a":
            return 1 # 좌측 방향지시등 ON
        elif alpa == "s":
            return 2 # 좌측 방향지시등 OFF
        elif alpa == "d":
            return 3 # 우측 방향지시등 ON
        elif alpa == "w":
            return 4 # 우측 방향지시등 OFF
    except Exception as e:
        print("winker", type(e), e)

# 임시 라이트 함수
def light():
    pass

# 클락션 함수
def klaxon():
    print("빵")

# 와이퍼 함수
def wiper():
    try:
        speed = 0
        wiper_o_or_c = 0
        print("a. 속도1 s. 속도2 d. 속도3 w. 워셔액 k. 와이퍼 가동중단" )
        alpa = input(">>") + "\n"
        if alpa == "a":
            speed = 1
            wiper_o_or_c = 1 # 와이퍼 가동
            print("와이퍼 가동 : 속도 {}".format(speed))
            return speed
        elif alpa == "s":
            speed = 2
            print("와이퍼 가동 : 속도 {}".format(speed))
            return speed
        elif alpa == "d":
            speed = 3
            print("와이퍼 가동: 속도 {}".format(speed))
            return speed
        elif alpa == "w":
            print("워셔액 분사")
        elif alpa == "k":
            wiper_o_or_c = 0 # 와이퍼 가동 중단
            print("와이퍼 가동중단")
    except Exception as e:
        print("wiper", type(e), e)


# 임시 엔진함수
def engine():
    return 1

def handle():
    try:
        # 엔진이 돌아가지 않은 상황에서 돌리게 되면 락걸림
        e = engine() # 여기서 함수호출이 아니라 임포트로 가져와야 함
        # 돌발상황일 때 에어백 터지는 기능

        # 엔진이 꺼져있을 때
        if e == 0: # off
            return
        # 엔진이 켜져있을 때
        elif e == 1: # on
            print("a. 방향지시등 s.라이트 d. 클락션 w. 와이퍼")
            alpa = input(">>")
            if alpa == "a":
                winker() # 방향지시등
            elif alpa == "s":
                light() # 라이트
            elif alpa == "d":
                klaxon() # 클락션
            elif alpa == "w":
                wiper() # 와이퍼
    except Exception as e:
        print("handle", type(e), e)
#
# 7. 내부버튼 button

def button():

    air_conditioner()

# 	비상깜빡이
# 	에어컨, 히터, 온도조절버튼, 내,외부순환버튼, 에어컨 방향, 바람세기조절버튼
def air_conditioner():
    try:
        temperature = 18  # 현재온도
        select_temperature = temperature  # 선택온도
        air_or_hit = 0 # 0이면 에어컨 1이면 히터
        wind_strength = "" # 바람세기
        wind_direction = "" # 풍향
        print("현재 온도: {}".format(temperature))
        print("a. 에어컨 가동 s. 히터가동 ")
        alpa = input(">>")
        if alpa == "a":
            air_or_hit = 0
            print("a. 온도조절 s. 바람세기 d. 풍향조절")
            a = input(">>")
            if a == "a": # 온도조절 선택시
                try:
                    while True:
                        print("w. 온도상승 s. 온도하락 d. 완료")
                        b = input(">>")

                        if b == "w": # 온도상승을 선택하면
                            select_temperature += 1 # 선택온도를 올려준다
                            print("선택온도 : {}".format(select_temperature))
                            if select_temperature == 30:
                                select_temperature = 30
                                print("더 이상 올릴 수 없습니다. 온도 선택을 완료합니다.")
                                print("선택온도 : {}".format(select_temperature))
                                return select_temperature


                        elif b == "s": # 온도하락을 선택하면
                            select_temperature -= 1 # 선택온도를 내려준다
                            print("선택온도 : {}".format(select_temperature))

                        elif b == "d": # 완료를 선택하면
                            print("선택온도 : {}".format(select_temperature)) # 선택온도를 보여주고 리턴한다.
                            return select_temperature

                except Exception as e:
                    print("에어컨 온도조절", type(e), e)

            elif a == "s": # 바람세기 선택시
                print("a. 바람세기 약 s. 바람세기 중 d. 바람세기 강")
                b = input(">>")
                if b == "a":
                    wind_strength = "약"
                    print("바람세기 : {}".format(wind_strength))
                    return wind_strength
                elif b == "s":
                    wind_strength = "중"
                    print("바람세기 :{}".format(wind_strength))
                    return wind_strength
                elif b == "d":
                    wind_strength = "강"
                    print("바람세기 : {}".format(wind_strength))
                    return wind_strength

            elif a == "d": # 풍향조절 선택시
                print("w. 위 s. 아래")
                b = input(">>")
                if b == "w":
                    wind_direction = "위"
                    print("바람이 {}쪽으로 나옵니다.".format(wind_direction))
                    return wind_direction
                elif b == "s":
                    wind_direction = "아래"
                    print("바람이 {}쪽으로 나옵니다.".format(wind_direction))
                    return wind_direction


        elif alpa == "s": # 히터 선택시
            air_or_hit = 1
            print("a. 온도조절 s. 바람세기 d. 풍향조절")
            a = input(">>")
            if a == "a":  # 온도조절 선택시
                try:
                    while True:
                        print("w. 온도상승 s. 온도하락 d. 완료")
                        b = input(">>")
                        if b == "w": # 온도상승을 선택하면
                            select_temperature += 1 # 선택온도를 올려준다
                            print("선택온도 : {}".format(select_temperature)) # 선택온도를 프린트한다.

                        elif b == "s": # 온도하락을 선택하면
                            select_temperature -= 1 # 선택온도를 내려준다
                            print("선택온도 : {}".format(select_temperature)) # 선택온도를 프린트한다.
                            if select_temperature == 16:
                                select_temperature = 16
                                print("더 이상 내릴 수 없습니다. 온도 선택을 완료합니다.")
                                print("선택온도 : {}".format(select_temperature))
                                return select_temperature
                        elif b == "d": # 완료를 선택하면
                            print("선택온도 : {}".format(select_temperature)) # 선택온도를 출력 후 리턴한다.
                            return select_temperature
                except Exception as e:
                    print("히터 온도조절", type(e), e)


            elif a == "s":  # 바람세기 선택시
                print("a. 바람세기 약 s. 바람세기 중 d. 바람세기 강")
                b = input(">>")
                if b == "a":
                    wind_strength = "약"
                    print("바람세기 : {}".format(wind_strength))
                    return wind_strength

                elif b == "s":
                    wind_strength = "중"
                    print("바람세기 : {}".format(wind_strength))
                    return wind_strength

                elif b == "d":
                    wind_strength = "강"
                    print("바람세기 : {}".format(wind_strength))
                    return wind_strength

            elif a == "d": # 풍향조절 선택시
                print("w. 위 s. 아래")
                b = input(">>")
                if b == "w":
                    wind_direction = "위"
                    print("바람이 {}쪽으로 나옵니다.".format(wind_direction))
                    return wind_direction
                elif b == "s":
                    wind_direction = "아래"
                    print("바람이 {}쪽으로 나옵니다.".format(wind_direction))
                    return wind_direction
    except Exception as e:
        print("air_conditioner", type(e), e)

    # 	핸들열선
def hit():
    handle_hit_temperature = ""
    seat_hit = 0
    handle_hit = 0
    seat_wind = 0
    seat_wind_strength = ""
# 시트 열선, 통풍시트
    try:
        print("a. 핸들열선 s. 시트열선 d. 통풍시트")
        a = input(">>")
        if a == "a": # 핸들열선
            handle_hit = 1
            print("a. 저온 s. 중온 d. 고온 ")
            b = input(">>")
            if b == "a":
                handle_hit_temperature = "저온"
                print("핸들열선온도 : {}".format(handle_hit_temperature))
                return handle_hit_temperature
            elif b == "s":
                handle_hit_temperature = "중온"
                print("핸들열선온도 : {}".format(handle_hit_temperature))
                return handle_hit_temperature
            elif b == "d":
                handle_hit_temperature = "고온"
                print("핸들열선온도 : {}".format(handle_hit_temperature))
                return handle_hit_temperature

        elif a == "s": # 시트열선
            seat_hit = 1
            print("a. 저온 s. 중온 d. 고온 ")
            b = input(">>")
            if b == "a":
                handle_hit_temperature = "저온"
                print("시트열선온도 : {}".format(handle_hit_temperature))
                return handle_hit_temperature
            elif b == "s":
                handle_hit_temperature = "중온"
                print("시트열선온도 : {}".format(handle_hit_temperature))
                return handle_hit_temperature
            elif b == "d":
                handle_hit_temperature = "고온"
                print("시트열선온도 : {}".format(handle_hit_temperature))
                return handle_hit_temperature
        elif a == "d": # 통풍시트
            seat_wind = 1
            print("a. 바람세기 약 s. 바람세기 중 d. 바람세기 강")
            b = input()
            if b == "a":
                seat_wind_strength = "약"
                print("바람세기: {}".format(seat_wind_strength))
                return seat_wind_strength
            elif b == "s":
                seat_wind_strength = "중"
                print("바람세기: {}".format(seat_wind_strength))
                return seat_wind_strength
            elif b == "d":
                seat_wind_strength = "강"
                print("바람세기: {}".format(seat_wind_strength))
                return seat_wind_strength

    except Exception as e:
        print("hit", type(e), e)



# 	라디오(채널 조절버튼2개)
def radio():
    # 라디오 채널 리스트
    channel_FM = [89.1, 91.9, 93.1, 93.9, 94.5, 95.9, 96.7, 99.1, 101.9, 104.5]
    channel_AM = [603, 711, 792, 837, 900, 1134]
    print("a. AM f. FM")
    a = input()
    if a == "a":
        print("AM")
        
    elif a == "f":
        print("FM")

# 	음량조절버튼
def volume():
    pass
handle()
button()


