a=0

def accel():
    global a
    b = a % 2
    a += 1
    try:
        if b == 0:
            return b
        elif b == 1:
            return b
    except:
        print("error : 입력값 초과")