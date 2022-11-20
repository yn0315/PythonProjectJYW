handle_heat = 0 #핸들열선 on/off변수
seat_heat_on_or_off = 0 # 시트열선 on/off변수
seat_wind = 0 # 통풍시트 on/off변수
seat_heat_temperature = 1 # 시트 온도변수

#######################################################################################################################

# 핸들 열선 on/off함수
def handle_heat_on_or_off():
    try:
        global handle_heat
        if handle_heat == 0:
            handle_heat = 1
        elif handle_heat == 1:
            handle_heat = 0
        return handle_heat
    except Exception as e:
        print("handle_seat_heat, handle_heat_on_or_off", type(e), e)

#######################################################################################################################


# 시트열선 on함수
def seat_heat_on():
    try:
        global seat_heat_on_or_off
        if seat_heat_on_or_off == 0: # 꺼짐
            seat_heat_on_or_off = 1 # 켜짐
        elif seat_heat_on_or_off == 1: # 켜짐
            seat_heat_on_or_off = 0 # 꺼짐
        return seat_heat_on_or_off
    except Exception as e:
        print("handle_seat_heat", type(e), e)

# 시트열선 저온함수
def seat_heat_temperature123():
    try:
        global seat_heat_temperature
        if seat_heat_temperature == 1:  # 약
            seat_heat_temperature = 2  # 중
            return seat_heat_temperature
        elif seat_heat_temperature == 2:  # 중
            seat_heat_temperature = 3  # 강
            return seat_heat_temperature
        elif seat_heat_temperature == 3:  # 강
            seat_heat_temperature = 0  # 꺼짐

            return seat_heat_temperature
        elif seat_heat_temperature == 0:  # 꺼짐
            seat_heat_temperature = 1  # 약
            return seat_heat_temperature
    except Exception as e:
        print("handle_seat_heat, seat_heat_temperature123", type(e), e)

#######################################################################################################################

# 통풍시트 ON함수
def seat_wind_on():
    try:
        global seat_wind
        if seat_wind == 0: # 꺼짐
            seat_wind = 1 # 켜짐
        elif seat_wind == 1: # 켜짐
            seat_wind = 0 # 꺼짐
        return seat_wind
    except Exception as e:
        print("handle_seat_heat, seat_wind_on", type(e),e)



#######################################################################################################################

