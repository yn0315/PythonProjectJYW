
engines = 0
def enginestart():
    global engines
    if engines == 0:
        engines = 1
        return engines
    elif engines == 1:
        engines = 0
        return engines
