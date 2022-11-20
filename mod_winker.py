# 깜빡이(방향지시등)2세대 함수
winker_on_or_off = 0 # 0 꺼짐 1 좌측ON 2 좌측OFF 3 우측ON 4 우측OFF
# 좌측 방향지시등 ON
def winker_left_on_off():
    try:
        global winker_on_or_off
        if winker_on_or_off == 0: # 꺼짐
            winker_on_or_off = 1 # 좌측ON
        elif winker_on_or_off == 1: # 좌측ON
            winker_on_or_off = 0 # 꺼짐
        return winker_on_or_off
    except Exception as e:
        print("winker, winker_left_on_off", type(e),e)

# 우측 방향지시등 ON
def winker_right_on_off():
    try:
        global winker_on_or_off
        if winker_on_or_off == 0:  # 꺼짐
            winker_on_or_off = 1  # 우측ON
        elif winker_on_or_off == 1:  # 우측ON
            winker_on_or_off = 0  # 꺼짐
        return winker_on_or_off
    except Exception as e:
        print("winker, winker_right_on_off", type(e),e)

#######################################################################################################################
