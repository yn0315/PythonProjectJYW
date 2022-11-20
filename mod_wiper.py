# 와이퍼 2세대 함수
wiper_on_off= 0 # 와이퍼 켜졌는지 여부 변수
wiper_speed_level = 0 # 와이퍼 속도 변수
fluid = 0 # 워셔액 변수
wiper_step = 0 # 와이퍼 업다운 변수
# 와이퍼 가동함수
def wiper_on():
    try:
        global wiper_on_off
        if wiper_on_off == 0: # 와이퍼 꺼짐
            wiper_on_off = 1  # 와이퍼 가동
            return wiper_on_off
        elif wiper_on_off == 1:
            wiper_on_off = 0
            return wiper_on_off
    except Exception as e:
        print("wiper, wiper_on", type(e),e)

# 와이퍼 속도함수
def mod_wiper_up():
    global wiper_step
    try:
        if 0 <= wiper_step <= 2:

            wiper_step+=1
            return wiper_step
        else:
            wiper_step
            return wiper_step
    except Exception as e:
        print("wiper, mod_wiper_up", type(e), e)

def mod_wiper_down():
    global wiper_step
    try:
        if 0 <= wiper_step <= 2:
            if wiper_step == 0:
                return wiper_step
            else:
                wiper_step -= 1
                return wiper_step
        else:
            pass
    except Exception as e:
        print("wiper, mod_wiper_down", type(e), e)

# 와이퍼 워셔액 함수
def wiper_washer_fluid():
    try:
        global fluid
        if fluid == 0:
            fluid = 1
        elif fluid == 1:
            fluid = 0
        return fluid
    except Exception as e:
        print("wiper, wiper_washer_fluid", type(e), e)


########################################################################################################################

