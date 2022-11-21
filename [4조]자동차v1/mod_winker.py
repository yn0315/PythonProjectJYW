# 깜빡이(방향지시등)2세대 함수
left = 0 # 0 꺼짐 1 좌측ON
right = 0 # 0 꺼짐 1 우측ON
# 좌측 방향지시등 ON
def winker_left_on_off():

    global left
    global right
    if left == 0: # 꺼짐
        left = 1 # 좌측ON
        right = 0
    elif left == 1: # 좌측ON
        left = 0 # 꺼짐
    return left

# 우측 방향지시등 ON
def winker_right_on_off():

    global right
    global left
    if right == 0:  # 꺼짐
        right = 1  # 우측ON
        left = 0
    elif right == 1:  # 우측ON
        right = 0  # 꺼짐
    return right

#######################################################################################################################
