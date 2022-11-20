current_temperature = 18 # 현재온도변수
select_temperature = 18 # 선택온도변수
aircon_on_or_off = 0 # 에어컨 켰는지 여부 변수 0 꺼짐 1 에어컨 2 히터
wind_strength = 1 # 에어컨 바람세기 변수 0 꺼짐 1 약 2 중 3 강
heater_wind_strength = 1 # 히터 바람세기 변수
wind_direction = 0 # 바람 방향 변수 0 위 1 아래


#######################################################################################################################

# 에어컨 온도선택완료함수
def aircon_select_complete():
    try:
        return select_temperature
    except Exception as e:
        print("airconditioner, aircon_select_complete", type(e),e)

# 에어컨 온도상승함수
def aircon_temperature_go_up():
    try:
        global select_temperature
        select_temperature += 1  # 선택온도를 올려준다

        if select_temperature == 30:
            select_temperature = 30

            aircon_select_complete()
            return select_temperature
    except Exception as e:
        print("airconditioner, aircon_temperature_go_up", type(e), e)

# 에어컨 온도하락함수
def aircon_temperature_go_down():
    try:
        global select_temperature
        select_temperature -= 1  # 선택온도를 내려준다

        if select_temperature == 16:
            select_temperature = 16

            aircon_select_complete()
            return select_temperature
    except Exception as e:
        print("airconditioner, aircon_temperature_go_down", type(e),e)

#######################################################################################################################

# 에어컨 바람세기 함수
def aircon_wind_strength_123():
    try:
        global wind_strength
        if wind_strength == 1: # 약
            wind_strength = 2 # 중

        elif wind_strength == 2: # 중
            wind_strength = 3 # 강

        elif wind_strength == 3: #강
            wind_strength = 0 # 꺼짐

        elif wind_strength == 0: #꺼짐
            wind_strength = 1 # 약

        return wind_strength
    except Exception as e:
        print("airconditioner, aircon_wind_strength_123", type(e), e)

#######################################################################################################################
# 에어컨 풍향 위쪽 함수
def aircon_direction_go_up_down():
    try:
        global wind_direction
        if wind_direction == 0: # 위쪽
            wind_direction = 1 # 아래쪽
        elif wind_direction == 1: # 아래쪽
            wind_direction = 0 # 위쪽
        return wind_direction
    except Exception as e:
        print("airconditioner, aircon_direction_go_up_down", type(e),e)

#######################################################################################################################
#######################################################################################################################

# 에어컨 히터 메인함수 0 꺼짐 1 에어컨 2히터
def air_conditioner_heater():
    try:
        global aircon_on_or_off
        if aircon_on_or_off == 0:  # 꺼짐
            aircon_on_or_off = 1  # 에어컨

        elif aircon_on_or_off == 1:  # 에어컨
            aircon_on_or_off = 2 # 히터

        elif aircon_on_or_off == 2: # 히터
            aircon_on_or_off = 0 # 꺼짐
        return aircon_on_or_off

    except Exception as e:
        print("air_conditioner, air_conditioner_heater", type(e), e)
