import datetime
from timeit import default_timer as timer
from datetime import timedelta

# start=timer()
# print("ok")
# end = timer()
# print(timedelta(seconds=end-start))


a=0



# start=timer()
def accel():
    global a
    if a == 0:
        a = 1
    return a

def acceloff():
    global a
    if a == 1:
        a = 0
    return a
# end = timer()
# s = timedelta(seconds=end-start)

# def accelreset():





# print(accelms)
# print(now.microsecond)
# print(count)
# print(a)





    # b = a % 2
    # try:
    #     if b == 0:
    #         b += 1
    #         a = b % 2
    #         # Braeak 발로 밟음
    #         return a
    #     elif b == 1:
    #         b += 1
    #         a = b % 2
    #         # Braeak 발을 땜
    #         return a
    # except:
    #     print("error : 입력값 초과")
