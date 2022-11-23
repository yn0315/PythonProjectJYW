import winsound

def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 1000     # 1000 ms ==1second
    winsound.Beep(fr, du) # winsound.Beep(frequency, duration)
beepsound()