# 깜빡이(방향지시등)2세대 함수
winker_on_or_off = 0
# 좌측 방향지시등 ON
def left_winker_on():
    global winker_on_or_off
    winker_on_or_off = 1
    return winker_on_or_off


# 좌측 방향지시등 OFF
def left_winker_off():
    global winker_on_or_off
    winker_on_or_off = 2
    return winker_on_or_off


# 우측 방향지시등 ON
def right_winker_on():
    global winker_on_or_off
    winker_on_or_off = 3
    return winker_on_or_off


# 우측 방향지시등 OFF
def right_winker_off():
    global winker_on_or_off
    winker_on_or_off = 4
    return winker_on_or_off


#######################################################################################################################
# 깜빡이(방향지시등) 함수
def winker():

    try:

        # on/off기능 좌 우 기능
        print("a. 좌측 방향지시등 ON s. 좌측 방향지시등 OFF d. 우측 방향지시등 ON w. 우측 방향지시등 OFF")

    except Exception as e:
        print("winker", type(e), e)