handle_heat = 0 #핸들열선 on/off변수
seat_heat_on_or_off = 0 # 시트열선 on/off변수
seat_wind = 0 # 통풍시트 on/off변수
seat_heat_temperature = 1 # 시트 온도변수

#######################################################################################################################

# 핸들 열선 on/off함수
def handle_heat_on_or_off():
    global handle_heat
    if handle_heat == 0:
        handle_heat = 1
    elif handle_heat == 1:
        handle_heat = 0
    return handle_heat

#######################################################################################################################


# 시트열선 on함수
def seat_heat_on():
    global seat_heat_on_or_off
    if seat_heat_on_or_off == 0: # 꺼짐
        seat_heat_on_or_off = 1 # 켜짐
    elif seat_heat_on_or_off == 1: # 켜짐
        seat_heat_on_or_off = 0 # 꺼짐
    return seat_heat_on_or_off

# 시트열선 저온함수
def seat_heat_temperature123():
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

#######################################################################################################################

# 통풍시트 ON함수
def seat_wind_on():
    global seat_wind
    if seat_wind == 0: # 꺼짐
        seat_wind = 1 # 켜짐
    elif seat_wind == 1: # 켜짐
        seat_wind = 0 # 꺼짐
    return seat_wind



#######################################################################################################################

a= handle_heat_on_or_off()
print(a)