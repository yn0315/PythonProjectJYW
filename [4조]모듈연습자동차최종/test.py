import engine
import threading
batteryCharge = 30 # 베터리량

def battery():
    global batteryCharge
    if engine.engines == 1:
        if batteryCharge < 100:
            batteryCharge += 1
        if batteryCharge == 100:
            pass
        return batteryCharge
    elif engine.engines == 0:
        if batteryCharge > 0:
            batteryCharge -= 0.05
        elif batteryCharge == 0:
            pass
        return batteryCharge

TimerOBJ=0
def set_interval(func, sec):
    global TimerOBJ
    def func_wrapper():
        func()
        print(1)
        set_interval(func, sec)
        print(2)
        print("베터리차지 :",batteryCharge)
    TimerOBJ = threading.Timer(sec, func_wrapper)
    TimerOBJ.start() # 쓰레드 작동 시작

TimerOBJ=set_interval(battery, 1)