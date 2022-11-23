import Boot
engines = 0
def enginestart(value):
    global engines
    if value == 2:
        engines = 1
        return print("엔진 상태",engines)
    else:
        engines = 0
        return print("엔진 상태",engines)
