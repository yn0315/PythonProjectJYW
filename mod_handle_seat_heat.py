handle_heat_on_or_off = 0 #핸들열선 on/off변수
seat_heat_on_or_off = 0 # 시트열선 on/off변수
seat_wind = 0
seat_wind_strength = ""

#######################################################################################################################

# 핸들 열선 on함수
def handle_heat_on():
    handle_heat_on_or_off = 1
    print("핸들 열선 ON")
    return handle_heat_on_or_off

# 핸들 열선 off함수
def handle_heat_off():
    handle_heat_on_or_off = 0
    print("핸들 열선 OFF")
    return handle_heat_on_or_off

# 핸들 열선함수
def handle_heat():
    print("a.핸들 열선 ON s.핸들 열선 OFF")

#######################################################################################################################

# 시트열선 on함수
def seat_heat_on():
    seat_heat_on_or_off = 1
    return seat_heat_on_or_off

# 시트열선 off함수
def seat_heat_off():
    seat_heat_on_or_off = 0
    return seat_heat_on_or_off

# 시트열선 함수
def seat_heat():
    print("a. 저온 s. 중온 d. 고온 ")

# 시트열선 저온함수
def seat_heat_temperature1():
    handle_hit_temperature = "저온"
    print("시트열선온도 : {}".format(handle_hit_temperature))
    return handle_hit_temperature

# 시트열선 중온함수
def seat_heat_temperature2():
    handle_hit_temperature = "중온"
    print("시트열선온도 : {}".format(handle_hit_temperature))
    return handle_hit_temperature

# 시트열선 고온함수
def seat_heat_temperature3():
    handle_hit_temperature = "고온"
    print("시트열선온도 : {}".format(handle_hit_temperature))
    return handle_hit_temperature

#######################################################################################################################

# 통풍시트 ON함수
def seat_wind_on():
    seat_wind_on_or_off = 1
    return seat_wind_on_or_off

# 통풍시트 OFF함수
def seat_wind_off():
    seat_heat_on_or_off = 0
    return seat_heat_on_or_off

# 통풍시트함수
def seat_wind():
    print("a.통풍시트ON s.통풍시트OFF")

#######################################################################################################################

# 핸들, 시트열선, 통풍시트함수
def handle_seat():

# 시트 열선, 통풍시트
    try:
        print("a. 핸들열선 s. 시트열선 d. 통풍시트")


    except Exception as e:
        print("hit", type(e), e)
