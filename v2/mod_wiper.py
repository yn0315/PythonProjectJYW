# 와이퍼 2세대 함수
wiper_on_off= 0 # 와이퍼 켜졌는지 여부 변수
wiper_speed_level = 0 # 와이퍼 속도 변수
fluid = 0 # 워셔액 변수
wiper_step = 0 # 와이퍼 업다운 변수
# 와이퍼 가동함수
def wiper_on():
    global wiper_on_off
    if wiper_on_off == 0: # 와이퍼 꺼짐
        wiper_on_off = 1  # 와이퍼 가동
        return wiper_on_off
    elif wiper_on_off == 1:
        wiper_on_off = 0
        return wiper_on_off

# 와이퍼 속도함수
def mod_wiper_up():
    global wiper_step
    try:
        if 0 <= wiper_step <= 100:

            wiper_step+=1
            return wiper_step
        else:
            wiper_step
            return wiper_step
    except:
        pass

def mod_wiper_down():
    global wiper_step
    try:
        if 0 <= wiper_step <= 100:
            if wiper_step == 0:
                return wiper_step
            else:
                wiper_step -= 1
                return wiper_step
        else:
            pass
    except:
        pass

# 와이퍼 워셔액 함수
def wiper_washer_fluid():
    global fluid
    if fluid == 0:
        fluid = 1
    elif fluid == 1:
        fluid = 0
    return fluid


########################################################################################################################

