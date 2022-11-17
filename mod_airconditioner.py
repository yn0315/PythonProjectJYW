select_temperature = 0 # 선택온도변수
aircon_on_or_off = 0 # 에어컨 켰는지 여부 변수
heater_on_or_off # 히터 켰는지 여부 변수
wind_strength = "" # 에어컨 바람세기 변수
heater_wind_strength = "" # 히터 바람세기 변수

# 에어컨 on함수
def aircon_on():
    global aircon_on_or_off
    aircon_on_or_off = 1
    print("a. 온도조절 s. 바람세기 d. 풍향조절")
    return aircon_on_or_off
# 에어컨 off함수
def aircon_off():
    global aircon_on_or_off
    aircon_on_or_off = 0
    return aircon_on_or_off

#######################################################################################################################

# 에어컨 온도선택완료함수
def aircon_select_complete():
    return select_temperature

# 에어컨 온도상승함수
def aircon_temperature_go_up():
    global select_temperature
    select_temperature += 1  # 선택온도를 올려준다
    print("선택온도 : {}".format(select_temperature))
    if select_temperature == 30:
        select_temperature = 30
        print("더 이상 올릴 수 없습니다. 온도 선택을 완료합니다.")
        print("선택온도 : {}".format(select_temperature))
        aircon_select_complete()

# 에어컨 온도하락함수
def aircon_temperature_go_down():
    global select_temperature
    select_temperature -= 1  # 선택온도를 내려준다
    print("선택온도 : {}".format(select_temperature))
    if select_temperature == 18:
        select_temperature = 18
        print("더 이상 내릴 수 없습니다. 온도 선택을 완료합니다.")
        print("선택온도 : {}".format(select_temperature))
        aircon_select_complete()

# 에어컨 온도조절함수
def air_temperature():
    try:
        while True:
            print("w. 온도상승 s. 온도하락 d. 완료")
            b = input(">>")

    except Exception as e:
        print("에어컨 온도조절", type(e), e)

#######################################################################################################################

# 에어컨 바람세기 (약) 함수
def aircon_wind_strength_1():
    wind_strength = "약"
    print("바람세기 : {}".format(wind_strength))
    return wind_strength

# 에어컨 바람세기 (중) 함수
def aircon_wind_strength_2():
    wind_strength = "중"
    print("바람세기 : {}".format(wind_strength))
    return wind_strength

# 에어컨 바람세기 (강) 함수
def aircon_wind_strength_3():
    wind_strength = "강"
    print("바람세기 : {}".format(wind_strength))
    return wind_strength

# 에어컨 바람세기함수
def air_strength():
    print("a. 바람세기 약 s. 바람세기 중 d. 바람세기 강")

#######################################################################################################################
# 에어컨 풍향 위쪽 함수
def aircon_direction_go_up():
    wind_direction = "위"
    print("바람이 {}쪽으로 나옵니다.".format(wind_direction))
    return wind_direction

# 에어컨 풍향 아래쪽 함수
def aircon_direction_go_down():
    wind_direction = "아래"
    print("바람이 {}쪽으로 나옵니다.".format(wind_direction))
    return wind_direction

# 에어컨 풍향함수
def air_direction():
    print("w. 위 s. 아래")

#######################################################################################################################
#######################################################################################################################

# 히터 on함수
def heater_on():
    global heater_on_or_off
    heater_on_or_off = 1
    print("a. 온도조절 s. 바람세기 d. 풍향조절")
    return aircon_on_or_off
# 에어컨 off함수
def heater_off():
    global heater_on_or_off
    heater_on_or_off = 0
    return heater_on_or_off

#######################################################################################################################

# 히터 온도선택완료함수
def heater_select_complete():
    return select_temperature

# 히터 온도상승함수
def heater_temperature_go_up():
    global select_temperature
    select_temperature += 1  # 선택온도를 올려준다
    print("선택온도 : {}".format(select_temperature))
    if select_temperature == 35:
        select_temperature = 35
        print("더 이상 올릴 수 없습니다. 온도 선택을 완료합니다.")
        print("선택온도 : {}".format(select_temperature))
        aircon_select_complete()

# 히터 온도하락함수
def heater_temperature_go_down():
    global select_temperature
    select_temperature -= 1  # 선택온도를 내려준다
    print("선택온도 : {}".format(select_temperature))
    if select_temperature == 18:
        select_temperature = 18
        print("더 이상 내릴 수 없습니다. 온도 선택을 완료합니다.")
        print("선택온도 : {}".format(select_temperature))
        aircon_select_complete()

# 히터 온도조절함수
def heater_temperature():
    try:
        while True:
            print("w. 온도상승 s. 온도하락 d. 완료")
            b = input(">>")

    except Exception as e:
        print("에어컨 온도조절", type(e), e)

#######################################################################################################################

# 히터 바람세기 (약) 함수
def heater_wind_strength_1():
    global heater_wind_strength
    heater_wind_strength = "약"
    print("바람세기 : {}".format(wind_strength))
    return wind_strength

# 히터 바람세기 (중) 함수
def heater_wind_strength_2():
    global heater_wind_strength
    heater_wind_strength = "중"
    print("바람세기 : {}".format(wind_strength))
    return wind_strength

# 히터 바람세기 (강) 함수
def heater_wind_strength_3():
    global heater_wind_strength
    heater_wind_strength = "강"
    print("바람세기 : {}".format(wind_strength))
    return wind_strength

# 히터 바람세기함수
def heater_strength():
    print("a. 바람세기 약 s. 바람세기 중 d. 바람세기 강")

#######################################################################################################################
# 히터 풍향 위쪽 함수
def heater_direction_go_up():
    wind_direction = "위"
    print("바람이 {}쪽으로 나옵니다.".format(wind_direction))
    return wind_direction

# 히터 풍향 아래쪽 함수
def heater_direction_go_down():
    wind_direction = "아래"
    print("바람이 {}쪽으로 나옵니다.".format(wind_direction))
    return wind_direction

# 히터 풍향함수
def heater_direction():
    print("w. 위 s. 아래")



#######################################################################################################################

def air_conditioner_heater():
    try:
        temperature = 20 # 현재온도
        select_temperature = temperature  # 선택온도
        air_or_heat = 0 # 0이면 에어컨 1이면 히터
        wind_strength = "" # 바람세기
        wind_direction = "" # 풍향
        print("현재 온도: {}".format(temperature))
        print("a. 에어컨 가동 s. 히터가동 ")

    except Exception as e:
        print("air_conditioner", type(e), e)
