emergency_light = 0
# 비상깜빡이 on함수
def emergency_light_on_or_off():
    try:
        global emergency_light
        if emergency_light == 0:
            emergency_light = 1
        elif emergency_light == 1:
            emergency_light = 0
        return emergency_light
    except Exception as e:
        print("emergency_light, emergency_light_on_or_off", type(e),e)

