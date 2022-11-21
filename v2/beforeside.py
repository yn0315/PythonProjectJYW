# sid
import engine
import threading
import time

# 불러와야할 값
gasolineTank = 50 # 기름통
engineOiltemp = 0 # 온도
batteryCharge = 30 # 베터리량

def battery(value):
    global batteryCharge
    if value == engine.engines:
        if batteryCharge < 100:
            batteryCharge += 2
        if batteryCharge == 100:
            pass
        return batteryCharge

    if value == engine.engines:
        if batteryCharge > 0:
            batteryCharge -= 2
        elif batteryCharge == 0:
            pass
        return batteryCharge

def engineoil(value):
    global engineOiltemp
    if value == engine.engines:
        if engineOiltemp <= 140:
            engineOiltemp += 1
        elif engineOiltemp == 140:
            pass
        return engineOiltemp

    if value == engine.engines:
        if engineOiltemp > 0:
            engineOiltemp -= 1
        elif engineOiltemp == 0:
            pass
        return engineOiltemp

def gasoline(value):
    global gasolineTank
    if value == engine.engines:
        if gasolineTank > 0:
            gasolineTank -= 1
        elif gasolineTank == 0:
            pass
        return gasolineTank

def gasolineCharge(value): # 기름을 넣을 때 벨류 값을 10씩 넣기
    global gasolineTank
    if 0 <= gasolineTank < 100:
        if gasolineTank + value > 100:
            gasolineTank = 100
            print(f"기름탱크가 가득차 {value - ((gasolineTank + value) - 100)}L 만 주입하였습니다.")
        elif gasolineTank + value <= 100:
            gasolineTank += value

TimerOBJ=0
def set_interval(func, sec, value):
    global TimerOBJ
    def func_wrapper():
        set_interval(func, sec, value)
        func(value)
    TimerOBJ = threading.Timer(sec, func_wrapper)
    TimerOBJ.start() # 쓰레드 작동 시작
    #return t
    # threading.join() 부모 스레드의 진행을 멈추고
    # 자식 스레드의 종료를 기다림


# def play(sec):
#     global TimerOBJ
#     print("xxxxxxxxxxxxxxxxx")
#     print("다시시작")
#     TimerOBJ=set_interval(battery, 1, 1)
#     for i in range(sec):
#         time.sleep(1)
#     TimerOBJ.cancel()
# play(5)

def baterryIng():
    global TimerOBJ
    if engine.engines == 1:
        TimerOBJ=set_interval(battery, 1, 1)
    elif engine.engines == 0:
        TimerOBJ=set_interval(battery,1,0)

def engineOilIng():
    global TimerOBJ
    if engine.engines == 1:
        TimerOBJ=set_interval(engineoil, 1, 1)
    elif engine.engines == 0:
        TimerOBJ=set_interval(engineoil,1,0)

def gasolineIng():
    global TimerOBJ
    if engine.engines == 1:
        TimerOBJ=set_interval(gasoline, 1, 1)
    elif engine.engines == 0:
        TimerOBJ.cancel()



