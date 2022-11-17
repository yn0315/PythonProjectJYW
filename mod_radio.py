channel_FM = [89.1, 91.9, 93.1, 93.9, 94.5, 95.9, 96.7, 99.1, 101.9, 104.5]
channel_AM = [603, 711, 792, 837, 900, 1134]
current_channel = channel_FM[0]
current_channel_FM_or_AM = 0 # fm이면 0, am이면 1
channel_select_complete = 0 # 채널선택완료변수

# 라디오 함수
def fm():
    global current_channel
    global current_channel_FM_or_AM
    current_channel = channel_FM[0]
    current_channel_FM_or_AM = 0
    print("a.채널이동")

# 라디오 함수
def am():
    global current_channel
    global current_channel_FM_or_AM
    current_channel = channel_AM[0]
    current_channel_FM_or_AM = 1
    print("a.채널이동")
    next_channel()

# 채널이동함수
def next_channel():
    global current_channel
    print("a.선택완료")

    lista = [1123, 222213, 3332, 45674, 52213]
    a = 0

    def gear_up():
        global a
        try:
            if 0 <= a <= 4:
                if a == 0:
                    return a
                else:
                    a -= 1
                    return a
            else:
                pass
        except:
            pass

    def gear_down():
        global a
        try:
            if 0 <= a < 4:
                a += 1
                return a
            else:
                a = 4
                return a
        except:
            pass

    gear_down()
    print(lista[a])

    if current_channel_FM_or_AM == 0: # fm이라면
        while True:
            for i in range(len(channel_FM)):
                print("#######B",channel_FM[i])
                if channel_select_complete == 1:
                    print(current_channel)
                    return
                if current_channel == channel_FM[-1]:
                    current_channel = channel_FM[0]
                    return print(current_channel)
                if channel_FM[i] == current_channel:
                    current_channel = channel_FM[i + 1]
                    return print(current_channel)


    elif current_channel_FM_or_AM == 1: # am이라면
        while True:
            for i in range(len(channel_AM)):
                print("#######A", channel_AM[i])
                if channel_select_complete == 1:
                    print(current_channel)
                    return
                if current_channel == channel_AM[-1]:
                    current_channel = channel_AM[0]
                    return print(current_channel)
                if channel_AM[i] == current_channel:
                    current_channel = channel_AM[i + 1]




# 	라디오(채널 조절버튼2개)
def radio():
    # 라디오 채널 리스트
    # 디폴드값 FM 89.1
    print("a.AM s.FM")
    am()



radio()
