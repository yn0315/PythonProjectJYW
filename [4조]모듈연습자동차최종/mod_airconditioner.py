import datetime
import time

import threading
import engine
import asyncio
import apscheduler
current_temperature = 18 # 현재온도변수
select_temperature = 18 # 선택온도변수
aircon_on_or_off = 0 # 에어컨 켰는지 여부 변수 0 꺼짐 1 에어컨 2 히터
wind_strength = 1 # 에어컨 바람세기 변수 0 꺼짐 1 약 2 중 3 강
heater_wind_strength = 1 # 히터 바람세기 변수
wind_direction = 0 # 바람 방향 변수 0 위 1 아래
aircon_heater = '꺼짐상태'



#######################################################################################################################

def heater_aircon():
    global aircon_heater
    if aircon_on_or_off == 1:
        aircon_heater = '에어컨'
    elif aircon_on_or_off == 2:
        aircon_heater = '  히터'
    elif aircon_on_or_off == 0:
        aircon_heater = '꺼짐상태'
    return aircon_heater

def aircon_off():
    global aircon_heater
    if aircon_heater != 0:
        aircon_heater = 0
        return

# 에어컨 온도선택완료함수
def aircon_select_complete():
    return select_temperature

# 에어컨 온도상승함수
def aircon_temperature_go_up():

    global select_temperature
    select_temperature += 1  # 선택온도를 올려준다

    if select_temperature > 30:
        select_temperature = 30

        aircon_select_complete()
        return select_temperature

# 에어컨 온도하락함수
def aircon_temperature_go_down():

    global select_temperature
    select_temperature -= 1  # 선택온도를 내려준다

    if select_temperature < 16:
        select_temperature = 16

        aircon_select_complete()
        return select_temperature


# 에어컨 실시간 온도변화
# def aircon_temperature_auto():
#
#     global select_temperature
#     global current_temperature
#     if current_temperature > select_temperature: # 현재온도가 높을 경우
#
#         current_temperature -= 1
#
#     elif current_temperature < select_temperature:
#         current_temperature += 1
#
#     elif current_temperature == select_temperature:
#         return
#     threading.Timer(10, aircon_temperature_auto)
#     aircon_temperature_auto()


# note that there are many other schedulers available
# from apscheduler.schedulers.background import BackgroundScheduler
#
# sched = BackgroundScheduler()

# def some_job():
#     print('Every 10 seconds')

# async def aircon_temperature_auto():
#
#     global select_temperature
#     global current_temperature
#     if current_temperature > select_temperature: # 현재온도가 높을 경우
#         threading.Timer(10, aircon_temperature_auto).start()
#         current_temperature -= 1
#         if current_temperature == select_temperature:
#             return
#
#     elif current_temperature < select_temperature:
#         threading.Timer(10, aircon_temperature_auto).start()
#         current_temperature += 1
#         if current_temperature == select_temperature:
#             return
    # threading.Timer(10, aircon_temperature_auto).start()


    import random
    import asyncio  # 비동기처리
    cal_list = []  # 정적생성

# async def show():
    # await asyncio.sleep(10)
    # aircon_temperature_auto()
    # print(current_temperature)
# 동적생성

# async def main():
#     # 작업하려는 대상을
#     # await asyncio.gather()
#     await asyncio.gather(
#
#         aircon_temperature_auto()
#     )
    # elif current_temperature == select_temperature:
    #     return


# # seconds can be replaced with minutes, hours, or days
# sched.add_job(aircon_temperature_auto, 'interval', seconds=10)
# sched.start()
#
# ...
#
# sched.shutdown()

# now = datetime.datetime.second

# Timer=0
# def set_interval2(func, sec):
#     global Timer
#
#     def func_wrapper():
#         set_interval2(func,sec=100)
#         func()
#
#     Timer = threading.Timer(sec, aircon_temperature_auto())
#
#     Timer.start() # 쓰레드 작동 시작
#
# def temperateIng():
#     global Timer
#     if engine.engines == 1:
#         Timer=set_interval2(aircon_temperature_auto,1)
#


#######################################################################################################################

# 에어컨 바람세기 함수
def aircon_wind_strength_123():
    global wind_strength
    if wind_strength == 1: # 약
        wind_strength = 2 # 중
        return wind_strength
    elif wind_strength == 2: # 중
        wind_strength = 3 # 강
        return wind_strength
    elif wind_strength == 3: #강
        wind_strength = 1
        return wind_strength
    if aircon_on_or_off == 0:
        wind_strength = 1
        return wind_strength
    else:
        pass

    return wind_strength


#######################################################################################################################
# 에어컨 풍향 위쪽 함수
def aircon_direction_go_up_down():
    global wind_direction
    if wind_direction == 0: # 위쪽
        wind_direction = 1 # 아래쪽
        return wind_direction
    elif wind_direction == 1: # 아래쪽
        wind_direction = 0 # 위쪽
        return wind_direction


#######################################################################################################################
#######################################################################################################################

# 에어컨 히터 메인함수 0 꺼짐 1 에어컨 2히터
def air_conditioner_heater():
    try:

        global aircon_on_or_off
        if aircon_on_or_off == 0:  # 꺼짐
            aircon_on_or_off = 1  # 에어컨

        elif aircon_on_or_off == 1:  # 에어컨
            aircon_on_or_off = 2 # 히터

        elif aircon_on_or_off == 2: # 히터
            aircon_on_or_off = 0 # 꺼짐
        return aircon_on_or_off

    except Exception as e:
        print("air_conditioner", type(e), e)


# aircon_temperature_auto()