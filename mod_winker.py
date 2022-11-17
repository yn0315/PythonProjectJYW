# 깜빡이(방향지시등)2세대 함수

# 좌측 방향지시등 ON
def left_winker_on():
    return 1


# 좌측 방향지시등 OFF
def left_winker_off():
    return 2


# 우측 방향지시등 ON
def right_winker_on():
    return 3


# 우측 방향지시등 OFF
def right_winker_off():
    return 4


#######################################################################################################################
# 깜빡이(방향지시등) 함수
def winker():
    global page
    page = 3
    try:

        # on/off기능 좌 우 기능
        print("a. 좌측 방향지시등 ON s. 좌측 방향지시등 OFF d. 우측 방향지시등 ON w. 우측 방향지시등 OFF")

    except Exception as e:
        print("winker", type(e), e)