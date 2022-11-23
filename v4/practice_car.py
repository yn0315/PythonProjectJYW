# import time
# import random
# import light
# import mod_winker
# import side
# import engine
# import mod_winker
# import mod_wiper
# import mod_handle_seat_heat
# import Gear
# import Braeak
# import Boot
# import Accel
# import mod_radio


# main_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31.0,0,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# main_list[1] = 0
# main_list[3] = 0
# main_list[21] = 1 # 안개등
# main_list[30] = 1 # 미등
# main_list[16] = 1 # 상향등
# main_list[15] = 1 # 하향등
# main_list[7] = 0
# list = ['💡']

#======== 중요버튼 ==========
#check_list[0] = 부트
#check_list[1] = 브레이크
#check_list[2] = 엑셀
#check_list[3] = 기어
#===========================

#=================================
#check_list[4] = 핸들 열선 on / off
#check_list[5] = 시트 열선 On / Off
#check_list[6] = 통풍 시트 on / off
#check_list[7] = 비상등 on / off
#check_list[15] = 노멀라이트
#check_list[16] = 하이빔
#check_list[17] = 좌측방향등
#check_list[18] = 우측방향등
#check_list[19] = 브레이크등
#check_list[20] = 후진등
#check_list[21] = 안개등
#check_list[22] = 배터리량
#check_list[23] = 오일온도
#check_list[24] = 기름량  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#check_list[25] = 클락션  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#check_list[26] = 에어컨 히터 0 , 1 , 2
#check_list[28] = 에어컨 히터 풍량 조절 1, 2, 3







accident_situation = random.randrange(0,10)
accident_title = ""
accident_txt = ""
accident_number = 0

accel = 0       # 사고 발생 화면 만들기인데 아직 미사용

AA = 0          # 악셀 받을 지역변수

radio_channel = ''          # 라디오 채널 받을 문자열
radio_decibel = ''          # FM / AM 받을 문자열

sound = 0                    # 볼륨 업 다운

def radio() :                             # 라디오 문자, 채널??
    radio_value = mod_radio.fm_or_am()
    for i in range(len(radio_value)) :
        c = radio_value[0]
        d = radio_value[1]
        return c,d

radio_channel,radio_decibel = radio()

def under_light_mark(value) :             # 하향등 계기판 on/off 표시 나타냄
    try :
        if value == 0 :            # 꺼졌을때
            return '💡'
        elif value == 1 :           # 켜졌을때
            return '\033[32m'+'💡'+'\033[0m'
    except :
        pass

def high_light_mark(value) :              # 상향등 계기판 on/off 표시 나타냄
    try :
        if value == 0 :                # 꺼졌을때
            return '💡'
        elif value == 1 :              # 켜졌을때
            return '\033[34m' + '💡' + '\033[0m'
    except :
        pass

def tail_light_mark(value) :              # 미등 계기판 on/off 표시 나타냄
    try :
        if value == 0 :                    # 꺼졌을때
            return '▶◀'
        if value == 1 :                    # 켜졌을때
            return '\033[32m'+'▶◀'+'\033[0m'
    except :
        pass

def log_map_mark(value) :                       # 안개등 계기판 on/off 표시 나타냄
    try :
        if value == 0 :                           # 꺼졌을때
            return '☁'
        elif value == 1 :                          # 켜졌을때
            return '\033[34m' + '☁' + '\033[0m'
    except :
        pass

def Emergency_Button(value) :        # 깜빡이 버튼 on / off 표시 나타냄
    try :
        if value == 0 :             # 깜빡이 버튼 꺼져 있을때
            return '🔺'
        elif value == 1 :           # 깜빡이 버튼 켜져 있을때
            return '\033[31m' + '🔺' + '\033[0m'
    except :
        pass

def left_winker_mark(value) :
    try :
        if value == 0 :
            return '◀'
        elif value == 1 :
            return '\033[33m' + '◀' + '\033[0m'
    except :
        pass

def right_winker_mark(value) :
    try :
        if value == 0 :
            return '▶'
        elif value == 1 :
            return '\033[33m' + '▶' + '\033[0m'
    except :
        pass

def left_winker(value) :
    try :
        if value == 0 :
            return '■■■■■■■■■■■■'
        elif value == 1 :
            return '\033[33m' + '■■■■■■■■■■■■' + '\033[0m'
    except :
        pass

def right_winker(value) :
    try :
        if value == 0 :
            return '■■■■■■■■■■■■'
        elif value == 1 :
            return '\033[33m' + '■■■■■■■■■■■■' + '\033[0m'
    except :
        pass

# def rear_light(Break=1,Gear_R=0,tail_light=0,log_map=0,under_light=0,high_light=0,emergency_light=0) :
#     try :
#         if Break == 0 :
#             return '             '
#         elif Break == 1 :
#             return '\033[31m \033[41m' + '■■■■■■■■■■' + '\033[0m'
#
#         if Gear_R == 0 :
#             return '             '
#         elif Gear_R == 2 :
#             return '\033[31m \033[41m' + '■■■■■■■■■■' + '\033[0m'
#
#         if tail_light == 0 :
#             return '             '
#         elif tail_light == 1 :
#             return '\033[93m' + '   ■■■■      ' + '\033[0m'
#
#         if log_map == 0 :
#             return '             '
#         elif log_map == 1 :
#             return '\033[93m' + '   ■■■■      ' + '\033[0m'
#
#         if under_light == 0 :
#             return '             '
#         elif under_light == 1 :
#             return '\033[33m' + '  ■■■■■■■■ ' + '\033[0m'
#
#         if high_light == 0 :
#             return '             '
#         elif high_light == 1 :
#             return '\033[33m \033[43m' + '■■■■■■■■■■' + '\033[0m'
#
#         if emergency_light == 0 :
#             return '             '
#         elif emergency_light == 1 :
#             return '\033[31m' + '   ■■■■      ' + '\033[0m'
#     except :
#         pass

def rear_light(Break=0,Gear_R=0,tail_light=0,log_map=0,under_light=0,high_light=0,emergency_light=0) :
    try :
        if Break == 0 and Gear_R == 0 and tail_light == 0 and log_map == 0 and under_light == 0 and high_light == 0 and emergency_light == 0:
            return '             '
        elif (Break == 1 or Gear_R == 1) and tail_light == 0 and log_map == 0 and under_light == 0 and high_light == 0 and emergency_light == 0 :
            return '\033[31m \033[41m' + '■■■■■■■■■■' + '\033[0m'
        elif Break == 0 and Gear_R == 0 and (tail_light == 1 or log_map == 1) and under_light == 0 and high_light == 0 and emergency_light == 0:
            return '\033[93m' + '   ■■■■      ' + '\033[0m'
        elif Break == 0 and Gear_R == 0 and tail_light == 0 and log_map == 0 and under_light == 1 and high_light == 0 and emergency_light == 0 :
            return '\033[33m' + ' ■■■■■■■' + '\033[0m' + '     '
        elif Break == 0 and Gear_R == 0 and tail_light == 0 and log_map == 0 and under_light == 0 and high_light == 1 and emergency_light == 0 :
            return '\033[33m \033[43m' + '■■■■■■■■' + '\033[0m' + '    '
        elif Break == 0 and Gear_R == 0 and tail_light == 0 and log_map == 0 and under_light == 0 and high_light == 0 and emergency_light == 1 :
            return '\033[31m' + '   ■■■■      ' + '\033[0m'
        elif Break == 0 and Gear_R == 0 and tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 1 :
            return '\033[33m' + ' ■■■■' + '\033[0m' + '\033[31m' + '■■■■    ' + '\033[0m'
        elif Break == 0 and Gear_R == 0 and tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 0 :
            return '\033[33m \033[43m' + '■■■■■■■■■■' + '\033[0m'
        elif Break == 1 and Gear_R == 0 and tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 0 :
            return '\033[33m' + ' ■■■■' + '\033[0m' + '\033[31m' + '■■■■    ' + '\033[0m'
        elif Break == 1 and Gear_R == 0 and tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 1 :
            return '\033[33m' + ' ■■■■' + '\033[0m' + '\033[31m' + '■■■■    ' + '\033[0m'
        elif Break == 1 and Gear_R == 1 and tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 1 :
            return '\033[33m \033[43m' + ' ■■■■' + '\033[31m \033[41m' + '■■■■' + '\033[0m'+ '  '
    except :
        pass

# def front_light(tail_light=0,log_map=0,under_light=0,high_light=0,emergency_light=0) :
#     try :
#         if tail_light == 0 :
#             return ''
#         elif tail_light == 1 :
#             return '\033[93m' + '   ■■■■      ' + '\033[0m'
#         if log_map == 0 :
#             return ''
#         elif log_map == 1 :
#             return '\033[93m' + '   ■■■■      ' + '\033[0m'
#
#         if under_light == 0 :
#             return ''
#         elif under_light == 1 :
#             return '\033[33m' + '  ■■■■■■■■ ' + '\033[0m'
#
#         if high_light == 0 :
#             return ''
#         elif high_light == 1 :
#             return '\033[33m \033[43m' + '■■■■■■■■■■' + '\033[0m'
#
#         if emergency_light == 0 :
#             return ''
#         elif emergency_light == 1 :
#             return '\033[31m' + '   ■■■■      ' + '\033[0m'
#     except :
#         pass

def front_light(tail_light=0,log_map=0,under_light=0,high_light=0,emergency_light=0) :
    try:
        if tail_light == 0 and log_map == 0 and under_light == 0 and high_light == 0 and emergency_light == 0:
            return '             '
        elif (tail_light == 1 or log_map == 1) and under_light == 0 and high_light == 0 and emergency_light == 0:
                return '\033[93m' + '   ■■■■      ' + '\033[0m'
        elif tail_light == 0 and log_map == 0 and under_light == 1 and high_light == 0 and emergency_light == 0:
            return '\033[33m' + '  ■■■■■■■■ ' + '\033[0m'
        elif tail_light == 0 and log_map == 0 and under_light == 0 and high_light == 1 and emergency_light == 0:
            return '\033[33m \033[43m' + '■■■■■■■■■■' + '\033[0m'
        elif tail_light == 0 and log_map == 0 and under_light == 0 and high_light == 0 and emergency_light == 1:
            return '\033[31m' + '   ■■■■      ' + '\033[0m'
        elif tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 1:
            return '\033[33m' + ' ■■■■' + '\033[0m' + '\033[31m' + '■■■■    ' + '\033[0m'
        elif tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 0:
            return '\033[33m \033[43m' + '■■■■■■■■■■' + '\033[0m'
        elif tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 0:
            return '\033[33m' + ' ■■■■' + '\033[0m' + '\033[31m' + '■■■■    ' + '\033[0m'
        elif tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 1:
            return '\033[33m' + ' ■■■■' + '\033[0m' + '\033[31m' + '■■■■    ' + '\033[0m'
        elif tail_light == 1 and log_map == 1 and under_light == 1 and high_light == 1 and emergency_light == 1:
            return '\033[33m \033[43m' + ' ■■■■' + '\033[31m \033[41m' + '■■■■' + '\033[0m' + '  '
    except:
        pass

def Circulation_Button(value) :         # 내부 순환 버튼??
    if value == 0 :                    # 안켜져 있을때
        return '  🌀  '
    if value == 1 :                    # 켜져 있을때
        return '\033[34m'+'  🌀  '+'\033[0m'

def oil_title(value):          # 기름 제목 ( 기름 부족하면 빨간 글씨로 뜸)
    try :
        if value >= 31 :           # 일정 이상이라면 평균값으로 설정
            return 'Oil'
        elif value <= 30.9 :         # 오일값이 일정 이하라면 으로 설정?
            return '\033[31m'+'Oil'+'\033[0m'
    except :
        pass

def oil_text(value) :          # 기름 부족 계기판 표시
    try :
        if value >= 31 :                # 평균 이상일때
            return '⛽'
        elif value <= 30.9 :              # 기름 부족할때
            return '\033[31m'+'⛽'+'\033[0m'
    except :
        pass

def battery_title(value) :     # 배터리 제목 ( 부족하면 빨간색 글씨로 뜸 )

    if value >= 31 :        # 배터리 역시 일정 이상 값이라면 평균 설정
        return 'Battery'
    elif value <= 30.9 :       # 배터리 값이 일정 이하라면 경고문
        return '\033[31m'+'Battery'+'\033[0m'

def battery_text(value) :         # 배터리 계기판 표시
    try :
        if value >= 31 :              # 배터리 충분할 때
            return '🔋'
        elif value <= 30.9 :            # 배터리 모자랄 때
            return '\033[31m'+'🔋'+'\033[0m'
    except :
        pass

def accident(value):                # 사고 발생 상황
    global accident_situation
    if value == 5 :                       # 약한 충돌
        a = "⚠" + " 약한 충돌"
        b = "외부에 의한 약한 충돌이 있습니다"
        return a,b,5
    elif value == 9 :                      # 강한 충돌
        a = "⚠" + " 강한충돌"
        b = "외부에 의한 강한 충돌로 인해 에어백이 터집니다"
        return a,b,9
    else :                                 # 이상 없음
        a = "이상 없음"
        b = "      정상 주행중입니다"
        return a,b,0

accident_title,accident_txt,accident_number = accident(accident_situation)

def Air_Conditioning(light=0,step=0) :         # 에어컨 / 히터
    try :
        if light == 0 :          # 에어컨 / 히터 안켜져있을때
            return '      '
        if light == 1 :               # 에어컨 켜졌을때
            if step == 1 :          # 에어컨 1단계
                return '\033[31m \033[44m' + ' ' + '\033[0m' + ' ' + '   '
            elif step == 2 :          # 2단계
                return '\033[31m \033[44m'+' '+'\033[0m''\033[31m \033[44m'+' '+'\033[0m'+'  '
            elif step == 3:           # 3단계
                return '\033[31m \033[44m' + ' ' + '\033[0m''\033[31m \033[44m'+' '+'\033[0m''\033[31m \033[44m'+' '+'\033[0m'
            else:
                return '      '
        if light == 2 :               # 히터 켜졌을때
            if step == 1:  # 1단계
                return '\033[31m \033[41m' + ' ' + '\033[0m' + ' ' + '   '
            elif step == 2:  # 2단계
                return '\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m'+'  '
            elif step == 3:  # 3단계
                return '\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m'
            else:
                return '      '
    except :
        pass

def sit_heat_rays(value) :          # 자동차 의자 열선 엉따
    try :
        if value == 0 :
            return '      '
        elif value == 1 :
            return '\033[31m \033[41m' + ' ' + '\033[0m' + '    '
        elif value == 2 :
            return '\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m' + '  '
        elif value == 3 :
            return '\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m'
    except :
        pass

def hanldle_heat_rays(value) :                # 핸들 열선
    try :
        if value == 0 :                          # 안켜져 있을때
            return '    '
        elif value == 1 :                        # 켰을때
            return '\033[31m' + '■■■■' + '\033[0m'
    except :
        pass

def accel_mark(value) :                        # 악셀 계기판
    try :
        if value == 0 :                          # 안밟았을때
            return '\033[31m'+'❌'+'\033[0m'
        elif value == 1 :                        # 밟았을때
            return '🦶'
    except :
        pass

def break_mark(value) :
    try :
        if value == 0 :
            return '\033[31m'+'❌'+'\033[0m'
        elif value == 1 :
            return '🦶'
    except :
        pass

def gear_mark(value) :                  # 기어 계기판 표시
    try :
        if value == 0 :                                #  기어가 P(파킹) 일때
            return '\033[34m'+'P'+'\033[0m'
        elif value == 1 :                              #  기어가 R(후진) 일때
            return '\033[34m'+'R'+'\033[0m'
        elif value == 2 :                              #  기어가 N(중립) 일때
            return '\033[34m'+'N'+'\033[0m'
        elif value == 3 :                              #  기어가 D(전진) 일때
            return '\033[34m'+'D'+'\033[0m'
    except :
        pass

def drive_title(value) :                # 이건 넣어도 되고 안넣어도 되고 / 주행중일때 문자열 표시
    try :
        if value == 3 :        # 기어가 D일 경우
            return '\033[32m'+' 안전 운전'+'\033[0m'
        else :                # 기어가 D가 아닐 경우
            return '        '         # 공백으로 둔다
    except :
        pass

def drive_text(value) :                # 이건 넣어도 되고 안넣어도 되고 / 주행중일때 임티 표시
    try :
        if value == 3 :        # 기어가 D일 경우
            return '\033[34m'+'🚘 '+'\033[0m'
        else :                # 기어가 D가 아닐 경우
            return '  '         # 공백으로 둔다
    except :
        pass

# def radio_voulme_up(value) :
#     try :
#         if value == 0 :
#             return '🔼'
#         elif value == 1 :
#             return '\033[31m'+'🔼'+'\033[0m'
#     except :
#         pass
#
# def radio_voulme_down(value) :
#     try :
#         if value == 0 :
#             return '🔽'
#         elif value == 1:
#             return '\033[31m' + '🔽' + '\033[0m'
#     except :
#         pass
#
# def radio_volume_emoji(up,down) :
#     try :
#         if up == 0 and down ==0 :
#             return '🔇'
#         elif 1 <= up <= 50 and 1 <= down <= 50 :
#             return '🔉'
#         elif 51 <= up <= 100 and 51 <= down <= 100 :
#             return '🔊'
#     except :
#         pass
#
# def radio_volume(Boot=0) :
#     try :
#         if Boot >= 1 :
#             return 0
#         else :
#             return ''
#     except :
#         pass
#
# def volume_Up_Down() :                             # 얘네는 업 다운 버튼이 나뉘어야할 거 같음?????
#     global sound
#     try :
#         if radio_volume(main_list[1]) == 0 and main_list[2] >= 1 :
#             sound = radio_volume(main_list[1]) + main_list[2]
#             if radio_volume(main_list[1]) == 0 and main_list[3] >= 1 :
#                 sound = radio_volume(main_list[1]) - main_list[3]
#             else :
#                 pass
#         else :
#             pass
#         return sound
#     except :
#         pass

def board() :             # 계기판
    global AA
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    AA = Accel.accel()
    print(f"""                              {front_light(main_list[30],main_list[21],main_list[15],main_list[16],main_list[7])}                                                     {front_light(main_list[30],main_list[21],main_list[15],main_list[16],main_list[7])}
                               --------------------------------------------------------------------------
                                L.winker            상향등    하향등    미등    안개등               R.winker
         ----------------------    {left_winker_mark(main_list[17])}                  {high_light_mark(main_list[16])}       {under_light_mark(main_list[15])}      {tail_light_mark(main_list[30])}      {log_map_mark(main_list[21])}                     {right_winker_mark(main_list[18])}    ----------------------
        ==                        주행거리                           속도                              연비                        ==
    　 ==　                      200,000KM                         120KM                             15 l                         ==
     ==       {left_winker(main_list[17])}     {battery_title(main_list[22])}        {oil_title(main_list[24])}             현재 온도          내부 순환       {drive_title(main_list[3])}       {right_winker(main_list[18])}        ==
     ==                          {battery_text(main_list[22])} {main_list[22]}%      {oil_text(main_list[24])}                 //              {Circulation_Button(main_list[6])}            {drive_text(main_list[3])}                            ==
    　 ==                                                    Emergency_Button                                                    ==
        ==                                                          {Emergency_Button(main_list[7])}              A / C      💺      ⚙                       ==
         ----------------------         📻                                         {Air_Conditioning(main_list[26],main_list[28])}    {sit_heat_rays(main_list[5])}  {hanldle_heat_rays(main_list[4])} ---------------------- 
                               ====================                                Break       Accel
                                     {radio_channel} / {radio_decibel}                                        {break_mark(main_list[1])}           {accel_mark(main_list[2])} 
                               --------------------------------------------------------------------------                         ㅡㅡㅡㅡㅡㅡ상황 발생ㅡㅡㅡㅡㅡ
                              {rear_light(main_list[1],main_list[3],main_list[30],main_list[21],main_list[15],main_list[16],main_list[7])}                                                     {rear_light(main_list[1],main_list[3],main_list[30],main_list[21],main_list[15],main_list[16],main_list[7])}        기어                   {accident_title}   
                                                                                                                      {gear_mark(main_list[3])}           {accident_txt} 
                                                                                                                                  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ""")
board()
#
#
# def board1() :             # 계기판
#     global AA
#     a = 0
#     b = 1
#     c = 2
#     d = 3
#     e = 4
#     AA = Accel.accel()
#     print(f"""                              {front_light(e)}                                                     {front_light(e)}
#                                --------------------------------------------------------------------------
#                                 L.winker            상향등    하향등    미등    안개등               R.winker
#          ----------------------    {winker_mark(a)}                  {high_light_mark(b)}      {under_light_mark(b)}       {tail_light_mark(b)}      {log_map_mark(b)}                     {winker_mark(b)}    ----------------------
#         ==                        주행거리                           속도                              연비                       ==
#     　 ==　                      200,000KM                         120KM                             15 l                        ==
#      ==       {winker(a)}     {battery_title(b)}        {oil_title(main_list[24])}             현재 온도          내부 순환       {drive_title(a)}        {winker(b)}       ==
#      ==                           {battery_text(b)}           {oil_text(main_list[24])}                //              {Circulation_Button(a)}            {drive_text(a)}                             ==
#     　 ==                                                    Emergency_Button                                                    ==
#         ==                                                          {Emergency_Button(a)}              A / C      💺      ⚙                        ==
#          ----------------------         📻                                         {Air_Conditioning(c)}    {sit_heat_rays(a)}  {hanldle_heat_rays(b)} ----------------------
#                                ====================                                Break       Accel
#                                      {radio_channel} / {radio_decibel}                                        {break_mark(b)}           {accel_mark(AA)}
#                                --------------------------------------------------------------------------                         ㅡㅡㅡㅡㅡㅡ상황 발생ㅡㅡㅡㅡㅡ
#                               {rear_light(e)}                                                     {rear_light(e)}           기어                    {accident_title}
#                                                                                                                      {gear_mark(a)}           {accident_txt}
#                                                                                                                                   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ""")
