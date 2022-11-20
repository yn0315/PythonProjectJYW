
volume_step=0


def mod_volume_up():
    global volume_step
    try:
        if 0 <= volume_step <= 100:

            volume_step+=1
            return volume_step
        else:
            volume_step
            return volume_step
    except Exception as e:
        print("volume, mod_volume_up", type(e), e)

def mod_volume_down():
    global volume_step
    try:
        if 0 <= volume_step <= 100:
            if volume_step == 0:
                return volume_step
            else:
                volume_step -= 1
                return volume_step
        else:
            pass
    except Exception as e:
        print("volume, mod_volume_down", type(e), e)
