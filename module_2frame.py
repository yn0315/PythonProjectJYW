import mod_winker
import mod_wiper
import mod_handle
page = 1

def fw():

    if page == 1:
        mod_handle.handle()  # 페이지가 1이면 핸들 연결

def fs():
    if page == 1:
        button() # 페이지가 1이면 내부버튼 연결

    elif page == 2:
        klaxon() # 페이지가 2이면 클랙슨 연결

def fa():
    if page == 2:
        light() # 페이지가 2이면 light 연결

def fd():
    if page == 2:
        mod_wiper.wiper()

def f1():
    if page == 2:
        mod_winker.winker()


#######################################################################################################################
# 임시 라이트 함수
def light():
    pass

# 클락션 함수
def klaxon():
    print("빵")
#######################################################################################################################

# 임시 엔진함수
def engine():
    return 1

#######################################################################################################################

#
# 7. 내부버튼 button

def button():
    print("a.에어컨/히터 s.비상깜빡이 d.열선시트 w.핸들열선 j.라디오 k.음량조절")
    air_conditioner()

# 	비상깜빡이
# 	에어컨, 히터, 온도조절버튼, 내,외부순환버튼, 에어컨 방향, 바람세기조절버튼

# 에어컨 on/off함수

# 에어컨 바람세기함수

# 에어컨 풍향함수

# 히터 on/off함수

# 히터 바람세기함수

# 히터 풍향함수



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
        if a == "a": # 핸들열선 on/off만
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


# 라디오 함수
def fm():
    channel_FM = [89.1, 91.9, 93.1, 93.9, 94.5, 95.9, 96.7, 99.1, 101.9, 104.5]
    current_channel = channel_FM[0]
    print("")



# 	라디오(채널 조절버튼2개)
def radio():
    # 라디오 채널 리스트
    # 디폴드값 FM 89.1

    channel_AM = [603, 711, 792, 837, 900, 1134]
    fm()

# 	음량조절버튼
def volume():
    pass
fw()

