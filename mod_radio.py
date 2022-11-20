channel_FM = [89.1, 91.9, 93.1, 93.9, 94.5, 95.9, 96.7, 99.1, 101.9, 104.5]
channel_AM = [603, 711, 792, 837, 900, 1134]
current_channel = channel_FM[0]
current_channel_FM_or_AM = 0 # fm이면 0, am이면 1
channel_select_complete = 0 # 채널선택완료변수

# 라디오 함수
def fm_or_am(): # fm이면 0 am 이면 1
    try:
        global current_channel
        global current_channel_FM_or_AM
        if current_channel_FM_or_AM == 0:
            current_channel_FM_or_AM = 1
            current_channel = channel_AM[0]
            return current_channel, current_channel_FM_or_AM # 출력예시 603 1
        elif current_channel_FM_or_AM == 1:
            current_channel_FM_or_AM = 0
            current_channel = channel_FM[0]
            print(current_channel, current_channel_FM_or_AM)
        return current_channel, current_channel_FM_or_AM
    except Exception as e:
        print("radio, fm_or_am", type(e),e)


# 채널이동함수
def next_channel():
    try:
        global current_channel

        if current_channel_FM_or_AM == 0: # fm이라면
            for i in range(len(channel_FM)):
                if channel_select_complete == 1:
                    return current_channel
                if current_channel == channel_FM[-1]:
                    current_channel = channel_FM[0]
                    return current_channel
                if channel_FM[i] == current_channel:
                    current_channel = channel_FM[i + 1]

                    return current_channel



        elif current_channel_FM_or_AM == 1: # am이라면

            for i in range(len(channel_AM)):
                if channel_select_complete == 1:

                    return current_channel
                if current_channel == channel_AM[-1]:
                    current_channel = channel_AM[0]
                    return current_channel
                if channel_AM[i] == current_channel:
                    current_channel = channel_AM[i + 1]
                    return current_channel
    except Exception as e:
        print("radio, next_channel", type(e), e)

