emergency_light_on_or_off = 0
# 비상깜빡이 on함수
def emergency_light_on_or_off():
    global emergency_light_on_or_off
    if emergency_light_on_or_off == 0:
        emergency_light_on_or_off = 1
    elif emergency_light_on_or_off == 1:
        emergency_light_on_or_off = 0
    return emergency_light_on_or_off
