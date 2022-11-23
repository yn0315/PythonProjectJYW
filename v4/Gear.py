#P
#R
#N
#D
#L

a=0

def gear_up():
    global a
    try:
        if 0 <= a <= 3:
            if a==0:
                return a
            else:
                a -= 1
                return a
        else:
            pass
    except:
        pass

def gear_down():
    global a
    try:
        if 0 <= a < 3:
            a += 1
            return a
        else:
            a=3
            return a
    except:
        pass
