klaxon_on = 0 # 0 꺼짐 1 켜짐
# 클랙슨 함수
def klaxon():
    global klaxon_on
    if klaxon_on == 0:
        klaxon_on = 1
    elif klaxon_on == 1:
        klaxon_on = 0
    return klaxon_on