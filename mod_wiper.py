# 와이퍼 2세대 함수
wiper_on_off= 0 # 와이퍼 켜졌는지 여부 변수
wiper_speed_level = 0 # 와이퍼 속도 변수
fluid = 0 # 워셔액 변수

# 와이퍼 가동함수
def wiper_on():
    wiper_on_off = 1  # 와이퍼 
    print("a.속도 s.워셔액")

# 와이퍼 중단함수
def wiper_off():
    wiper_on_off = 0
    return wiper_on_off

# 와이퍼 속도함수
def wiper_speed():
    global wiper_speed_level
    if wiper_speed_level == 3: # 속도가 3이 되면
        wiper_speed_level = 0 # 0으로 초기화하라
        return wiper_speed_level

    else:
        wiper_speed_level += 1 # 그 외에는 1씩 증가하라
        print(wiper_speed_level)

# 와이퍼 워셔액 함수
def wiper_washer_fluid():
    global fluid
    fluid = 1
    print("워셔액 분사")
    return fluid



########################################################################################################################
# 와이퍼 함수
def wiper():
    try:
        print("w. 와이퍼 가동 s.와이퍼 가동중단")
        wiper_on()

    except Exception as e:
        print("wiper", type(e), e)

wiper()