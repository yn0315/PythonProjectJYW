# 와이퍼 2세대 함수
wiper_on_off= 0
# 와이퍼 가동함수
def wiper_on():
    wiper_on_off = 1  # 와이퍼 켜진상태
    return wiper_on_off


# 와이퍼 중단함수
def wiper_off():
    wiper_on_off = 0
    return wiper_on_off


########################################################################################################################
# 와이퍼 함수
def wiper():
    try:
        speed = 1

        print("a. 와이퍼 가동 s. 속도1 d. 속도2 w. 워셔액 k. 와이퍼 가동중단")
        print()

    except Exception as e:
        print("wiper", type(e), e)