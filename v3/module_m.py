import Gear, Accel, Boot, Braeak, mod_airconditioner,mod_radio,\
    mod_wiper,mod_winker,mod_handle_seat_heat,mod_klaxon,\
mod_volume,mod_emergency_light,light,random,side, engine
import time
import Sound
import snow
import threading




import datetime
from timeit import default_timer as timer
from datetime import timedelta
import os
# os.system('cls')

mainList =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
p = 0
bang1point = 0
bang2point = 1
bang3point = 0
bang4point = 0
bang5point = 0
bang6point = 0
accel1 = 0
accel2 = 0
accelfinal = 0
braeak1 = 0
braeak2 = 0
braeakfinal = 0
accelCount = 0
braeakCount = 0
count = 0
car_speed=0
mainList[32] = accelCount
mainList[33] = braeakCount






# mainList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31.0,0,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# mainList[1] = 0
# mainList[3] = 0
# mainList[21] = 1 # 안개등
# mainList[30] = 1 # 미등
# mainList[16] = 1 # 상향등
# mainList[15] = 1 # 하향등
# mainList[7] = 0
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

def boot_on_off(value) :
    try :
        if value == 0 :
            return '시동이 꺼져 있습니다'
        elif value == 2 :
            return print('시동이 켜져 있습니다')
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

def break_light(value) :                         # 후진등
    try :
        if value == 0 :
            return '             '
        elif value == 1 :
            return '\033[93m \033[41m' + ' ■■■■■■■■ ' + '\033[0m'
    except :
        pass

def Gear_R_light(value) :                        # 브레이크등
    try :
        if value == 0 :
            return '             '
        elif value == 1 :
            return '\033[31m \033[41m' + '■■■■■■■■■■' + '\033[0m'
    except :
        pass

def log_map_light(value) :                         # 안개등
    try :
        if value == 0 :
            return '             '
        elif value == 1 :
            return '\033[36m' + '   ■■■■      ' + '\033[0m'
    except :
        pass

def tail_light(value) :                            # 미등
    try :
        if value == 0 :
            return '             '
        elif value == 1 :
            return '\033[93m' + '   ■■■■      ' + '\033[0m'
    except :
        pass

def emergency_light(value) :                           # 비상 깜빡이
    try :
        if value == 0 :
            return '             '
        elif value == 1 :
            return '\033[31m' + '■■■■■' + '\033[0m'
    except :
        pass

def high_light(value) :                             # 상향등 - 하이빔
    try :
        if value == 0 :
            return '             '
        elif value == 1 :
            return '\033[33m \033[103m' + '■■■■■■■■■■' + '\033[0m'
    except :
        pass

def under_light(value) :                            # 하향등
    try :
        if value == 0 :
            return '             '
        elif value == 1 :
            return '\033[33m' + '  ■■■■■■■■ ' + '\033[0m'
    except :
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
    global count
    if value == 5 :                       # 약한 충돌
        a = "⚠" + " 약한 충돌"
        b = "외부에 의한 약한 충돌이 있습니다"
        return a,b
    elif value == 9 :                      # 강한 충돌
        a = "⚠" + " 강한충돌"
        b = "외부에 의한 강한 충돌로 인해 에어백이 터집니다"
        return a,b

    ###################################################################################################################
    elif value == 10:
        a = "⚠" + " 사고위험"
        b = "눈이 내립니다. 와이퍼를 켜주세요"
        return a,b

    elif value == 20:
        a = "⚠" + " 감속구간"
        b = "어린이 보호구역입니다. 브레이크를 밟아주세요."
        return a,b

    elif value == 30:
        a = "⚠" + " 사고위험"
        b = "고라니가 출몰하였습니다. 브레이크를 밟아주세요."
        return a,b

    elif value == 40:
        a = "⚠" + " 차량점검"
        b = "   엔진오일이 과열되었습니다. 시동을 꺼주세요."
        return a,b

        #############################################################################################################
    else :                                 # 이상 없음
        a = "이상 없음"
        b = "      정상 주행중입니다"
        return a,b


accident_title,accident_txt = accident(count) # 매개변수에 카운트!!

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
#         if radio_volume(mainList[1]) == 0 and mainList[2] >= 1 :
#             sound = radio_volume(mainList[1]) + mainList[2]
#             if radio_volume(mainList[1]) == 0 and mainList[3] >= 1 :
#                 sound = radio_volume(mainList[1]) - mainList[3]
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

    print(f"""                 
                               {log_map_light(mainList[21])}                                                   {log_map_light(mainList[21])}    
                               {tail_light(mainList[30])}                                                   {tail_light(mainList[30])}    
                               {high_light(mainList[16])}                                                   {high_light(mainList[16])}    
                               {under_light(mainList[15])}                                                   {under_light(mainList[15])}
                         {emergency_light(mainList[7])} -------------------------------------------------------------------------- {emergency_light(mainList[7])}
                                L.winker            상향등    하향등    미등    안개등               R.winker
         ----------------------    {left_winker_mark(mainList[17])}                  {high_light_mark(mainList[16])}      {under_light_mark(mainList[15])}      {tail_light_mark(mainList[30])}      {log_map_mark(mainList[21])}                     {right_winker_mark(mainList[18])}  ----------------------
                                  주행거리                           속도                              연비                        
    　   　                      200,000KM                         120KM                             15 l                        
              {left_winker(mainList[17])}     {battery_title(mainList[22])}        {oil_title(mainList[24])}             현재 온도          내부 순환       {drive_title(mainList[3])}         {right_winker(mainList[18])}       
                                 {battery_text(mainList[22])} {round(mainList[22],1)}%      {oil_text(mainList[24])}                 //            {Circulation_Button(mainList[6])}            {drive_text(mainList[3])}                          
    　                                                       Emergency_Button                                                    
                                                                   {Emergency_Button(mainList[7])}               A / C      💺      ⚙                     
         ----------------------         📻                                         {Air_Conditioning(mainList[26],mainList[28])}    {sit_heat_rays(mainList[5])}  {hanldle_heat_rays(mainList[4])} ---------------------- 
                               ====================         {boot_on_off(mainList[0])}       Break       Accel       기어
                                     {radio_channel} / {radio_decibel}                                        {break_mark(mainList[1])}           {accel_mark(mainList[2])}         {gear_mark(mainList[3])}
                         {emergency_light(mainList[7])} -------------------------------------------------------------------------- {emergency_light(mainList[7])}    
                               {break_light(mainList[1])}                                                   {break_light(mainList[1])}                      ㅡㅡㅡㅡㅡㅡ상황 발생ㅡㅡㅡㅡㅡ
                               {log_map_light(mainList[21])}                                                   {log_map_light(mainList[21])}                               {accident_title} 
                               {Gear_R_light(mainList[3])}                                                   {Gear_R_light(mainList[3])}                                      
                               {tail_light(mainList[30])}                                                   {tail_light(mainList[30])}                      {accident_txt} 
                                                                                                                                  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ""")


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
#
#                                 L.winker            상향등    하향등    미등    안개등               R.winker
#          ----------------------    {winker_mark(a)}                  {high_light_mark(b)}      {under_light_mark(b)}       {tail_light_mark(b)}      {log_map_mark(b)}                     {winker_mark(b)}    ----------------------
#         ==                        주행거리                           속도                              연비                       ==
#     　 ==　                      200,000KM                         120KM                             15 l                        ==
#      ==       {winker(a)}     {battery_title(b)}        {oil_title(mainList[24])}             현재 온도          내부 순환       {drive_title(a)}        {winker(b)}       ==
#      ==                           {battery_text(b)}           {oil_text(mainList[24])}                //              {Circulation_Button(a)}            {drive_text(a)}                             ==
#     　 ==                                                    Emergency_Button                                                    ==
#         ==                                                          {Emergency_Button(a)}              A / C      💺      ⚙                        ==
#          ----------------------         📻                                         {Air_Conditioning(c)}    {sit_heat_rays(a)}  {hanldle_heat_rays(b)} ----------------------
#                                ====================                                Break       Accel
#                                      {radio_channel} / {radio_decibel}                                        {break_mark(b)}           {accel_mark(AA)}
#                                --------------------------------------------------------------------------                         ㅡㅡㅡㅡㅡㅡ상황 발생ㅡㅡㅡㅡㅡ
#                               {rear_light(e)}                                                     {rear_light(e)}           기어                    {accident_title}
#                                                                                                                      {gear_mark(a)}           {accident_txt}
#                                                                                                                                   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ""")

def bang1():
    global p
    p = 1
    #  ／ ｜ ￣ ― ∥ ＼ ┐┘┌└ ┓ ┛ ┏ ┗ 『』 【 】 ―
    if bang1point == 0:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                   
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                          ● ● ●       ----               핸들              ----        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                  ● ● ●
                                                       --------


                ------------------------------------------------------------------------""")
    if bang1point == 1:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                  
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                                      ----              핸들               ----       
                                      ----                                ----
                                           ----                        ----
                          ▼ ▼ ▼                ----                ----                  
                          ▼ ▼ ▼                    ----        ----                  ● ● ●
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 2:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                          ▲ ▲ ▲                    ----        ----                   
                          ▲ ▲ ▲                ----                ----
                                           ----                        ----
                                      ----                                ----
                                      ----               핸들              ----        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                  ● ● ●
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 3:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                   
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                          ●하향●       ----               핸들             ----        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                  ● ● ●
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 4:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                   
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                          ●상향●       ----               핸들             ----        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                  ● ● ●
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 5:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                   
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                          ●오토●       ----               핸들             ----        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                  ● ● ●
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 6:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                   
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                          ●안개등●     ----               핸들             ----        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                  ● ● ●
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 7:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                   
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                          ● ● ●       ----               핸들             ----       ● 1 ●        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                   
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 8:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                  ● 2 ●                   
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                          ● ● ●       ----               핸들             ----        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                   
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 9:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----            
                                               ----                ----
                                           ----                        ----
                                      ----                                ----
                          ● ● ●       ----               핸들             ----        
                                      ----                                ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                  ●워셔액●                   
                                                       --------


                ------------------------------------------------------------------------""")
    elif bang1point == 10:
        print(f"""------------------------------------------------------------------------

                    핸들
                                                       --------
                                                   ----        ----                   
                                               ----                ----
                                           ----                        ----
                                      ----              ● ● ●              ----
                          ● ● ●       ----              클락션              ----        
                                      ----              ● ● ●              ----
                                           ----                        ----
                                               ----                ----                  
                                                   ----        ----                  ● ● ●
                                                       --------


                ------------------------------------------------------------------------""")


#         print(f"""------------------------------------------------------------------------
#
#             우측지시등  좌측지시등   하향등   상향등     오토     와이퍼온  와이퍼속도2  워셔액
#              ┏  ┓      ┏  ┓     ┏  ┓     ┏  ┓      ┏  ┓     ┏  ┓     ┏  ┓     ┏  ┓
#               ｜
#              ┗  ┛      ┗  ┛     ┗  ┛     ┗  ┛      ┗  ┛     ┗  ┛     ┗  ┛     ┗  ┛
#
# ------------------------------------------------------------------------""")

def bang2():
    global p
    p = 2
    #  ／ ｜ ￣ ― ∥ ＼ ┐┘┌└ ┓ ┛ ┏ ┗ 『』 【 】 ―
    if bang2point == 1: # 에어컨을 키고 히터로 넘어가고 다시 0으로 돌아오는 기능을 넣기.
        print(f"""------------------------------------------------------------------------

            에어컨   핸들열선   열선시트  내부순환   비상깜빡이   
             ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓ 
              ｜
             ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛ 
                
------------------------------------------------------------------------""")
    elif bang2point == 2:
        print(f"""------------------------------------------------------------------------

            에어컨   핸들열선   열선시트  내부순환   비상깜빡이   
             ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓      
                       ｜
             ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛      

------------------------------------------------------------------------""")
    elif bang2point == 3:
        print(f"""------------------------------------------------------------------------

            에어컨   핸들열선   열선시트  내부순환   비상깜빡이   
             ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓     
                                   ｜
             ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛      

------------------------------------------------------------------------""")
    elif bang2point == 4:
        print(f"""------------------------------------------------------------------------

            에어컨   핸들열선   열선시트  내부순환   비상깜빡이   
             ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓     
                                             ｜
             ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛     

------------------------------------------------------------------------""")
    elif bang2point == 5:
        print(f"""------------------------------------------------------------------------

            에어컨   핸들열선   열선시트  내부순환   비상깜빡이   
             ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓     
                                                         ｜
             ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛ 

------------------------------------------------------------------------""")

#     elif bang2point == 6:
#         print(f"""------------------------------------------------------------------------
#
#             에어컨   핸들열선   열선시트  내부순환   비상깜빡이   음상    음하   라디오
#              ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓      ┏  ┓    ┏  ┓    ┏  ┓
#                                                                    ｜
#              ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛      ┗  ┛    ┗  ┛    ┗  ┛
#
# ------------------------------------------------------------------------""")
#     elif bang2point == 7:
#         print(f"""------------------------------------------------------------------------
#
#             에어컨   핸들열선   열선시트  내부순환  비상깜빡이
#              ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓
#
#              ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛
#
# ------------------------------------------------------------------------""")
#     elif bang2point == 8:
#         print(f"""------------------------------------------------------------------------
#
#             에어컨   핸들열선   열선시트  내부순환   비상깜빡이
#              ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓
#
#              ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛
#
# ------------------------------------------------------------------------""")



def bang5(): # 에어컨 옵션들 만들기, 뒤로가기 버튼(bang2()로 이동 버튼으로 만들기, 방5내부에선 wasd 방향키사용 불가 에어컨 온도 결정후 돌아가는 기능
    global p  # 에어컨과 히터가 켜진 상태에서의 기능을 넣기.
    p = 5
    if bang5point == 0:
        if mod_airconditioner.aircon_on_or_off == 0:
            print(f"""------------------------------------------------------------------------
            에어컨
    
                                                                              ⚪
                                                                             / /
                {mod_airconditioner.heater_aircon()}                                                   ／／ 

            에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                 ｜
                ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


------------------------------------------------------------------------""")
        else:
            if mod_airconditioner.wind_direction == 0:
                print(f"""------------------------------------------------------------------------
                에어컨
    
                    희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                    바람세기 : {mod_airconditioner.wind_strength}                                          →→   / /
                    {mod_airconditioner.heater_aircon()}                                                   ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                     ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


    ------------------------------------------------------------------------""")
            else:
                print(f"""------------------------------------------------------------------------
                에어컨
                
                   희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                   바람세기 : {mod_airconditioner.wind_strength}                                               / /
                   {mod_airconditioner.heater_aircon()}                                               ↘↘  ／／ 
            
                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                     ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     
            
            
        ------------------------------------------------------------------------""")

    elif bang5point == 1:
        if mod_airconditioner.aircon_on_or_off == 0:
            print(f"""------------------------------------------------------------------------
            에어컨

                                                                              ⚪
                                                                             / /
                {mod_airconditioner.heater_aircon()}                                                   ／／ 

            에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                             ｜
                ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


------------------------------------------------------------------------""")
        else:
            if mod_airconditioner.wind_direction == 0:
                print(f"""------------------------------------------------------------------------
                에어컨

                    희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                    바람세기 : {mod_airconditioner.wind_strength}                                          →→   / /
                    {mod_airconditioner.heater_aircon()}                                                   ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                 ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


    ------------------------------------------------------------------------""")
            else:
                print(f"""------------------------------------------------------------------------
                에어컨

                   희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                   바람세기 : {mod_airconditioner.wind_strength}                                               / /
                   {mod_airconditioner.heater_aircon()}                                               ↘↘  ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                 ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


        ------------------------------------------------------------------------""")
    elif bang5point == 2:
        if mod_airconditioner.aircon_on_or_off == 0:
            print(f"""------------------------------------------------------------------------
            에어컨

                                                                              ⚪
                                                                             / /
                {mod_airconditioner.heater_aircon()}                                                   ／／ 

            에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                        ｜
                ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


------------------------------------------------------------------------""")
        else:
            if mod_airconditioner.wind_direction == 0:
                print(f"""------------------------------------------------------------------------
                에어컨

                    희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                    바람세기 : {mod_airconditioner.wind_strength}                                          →→   / /
                    {mod_airconditioner.heater_aircon()}                                                   ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                            ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


    ------------------------------------------------------------------------""")
            else:
                print(f"""------------------------------------------------------------------------
                에어컨

                   희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                   바람세기 : {mod_airconditioner.wind_strength}                                               / /
                   {mod_airconditioner.heater_aircon()}                                               ↘↘  ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                            ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


        ------------------------------------------------------------------------""")
    elif bang5point == 3:
        if mod_airconditioner.aircon_on_or_off == 0:
            print(f"""------------------------------------------------------------------------
            에어컨

                                                                              ⚪
                                                                             / /
                {mod_airconditioner.heater_aircon()}                                                   ／／ 

            에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                   ｜
                ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


------------------------------------------------------------------------""")
        else:
            if mod_airconditioner.wind_direction == 0:
                print(f"""------------------------------------------------------------------------
                에어컨

                    희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                    바람세기 : {mod_airconditioner.wind_strength}                                          →→   / /
                    {mod_airconditioner.heater_aircon()}                                                   ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                       ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


    ------------------------------------------------------------------------""")
            else:
                print(f"""------------------------------------------------------------------------
                에어컨

                   희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                   바람세기 : {mod_airconditioner.wind_strength}                                               / /
                   {mod_airconditioner.heater_aircon()}                                               ↘↘  ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                       ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


        ------------------------------------------------------------------------""")
    elif bang5point == 4:
        if mod_airconditioner.aircon_on_or_off == 0:
            print(f"""------------------------------------------------------------------------
            에어컨

                                                                              ⚪
                                                                             / /
                {mod_airconditioner.heater_aircon()}                                                   ／／ 

            에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                               ｜
                ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


------------------------------------------------------------------------""")
        else:
            if mod_airconditioner.wind_direction == 0:
                print(f"""------------------------------------------------------------------------
                에어컨

                    희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                    바람세기 : {mod_airconditioner.wind_strength}                                          →→   / /
                    {mod_airconditioner.heater_aircon()}                                                   ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                                   ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


    ------------------------------------------------------------------------""")
            else:
                print(f"""------------------------------------------------------------------------
                에어컨

                   희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                   바람세기 : {mod_airconditioner.wind_strength}                                               / /
                   {mod_airconditioner.heater_aircon()}                                               ↘↘  ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                                   ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


        ------------------------------------------------------------------------""")
    elif bang5point == 5:
        if mod_airconditioner.aircon_on_or_off == 0:
            print(f"""------------------------------------------------------------------------
            에어컨

                                                                              ⚪
                                                                             / /
                {mod_airconditioner.heater_aircon()}                                                   ／／ 

            에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                                          ｜
                ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


------------------------------------------------------------------------""")
        else:
            if mod_airconditioner.wind_direction == 0:
                print(f"""------------------------------------------------------------------------
                에어컨

                    희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                    바람세기 : {mod_airconditioner.wind_strength}                                          →→   / /
                    {mod_airconditioner.heater_aircon()}                                                   ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                                              ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


    ------------------------------------------------------------------------""")
            else:
                print(f"""------------------------------------------------------------------------
                에어컨

                   희망온도 : {mod_airconditioner.select_temperature}                                              ⚪
                   바람세기 : {mod_airconditioner.wind_strength}                                               / /
                   {mod_airconditioner.heater_aircon()}                                               ↘↘  ／／ 

                에어컨*히터   온도상승   온도하락   풍력조절    풍향조절   뒤로가기
                    ┏  ┓        ┏  ┓       ┏  ┓       ┏  ┓        ┏  ┓       ┏  ┓
                                                                              ｜
                    ┗  ┛        ┗  ┛       ┗  ┛       ┗  ┛        ┗  ┛       ┗  ┛                                                                     


        ------------------------------------------------------------------------""")

def bang6(): # 라디오 옵션들 넣기 , 에어컨과 마찬가지로 뒤로가기버튼 추가, bang2()로 돌아가는 기능으로 넣기
    global p
    p = 6
    if bang6point == 0:
        print(f"""------------------------------------------------------------------------
        라디오

                                                                              ⚪
                {mod_airconditioner.aircon_select_complete()}           →→   / /
                                                                        ↘↘ ／／ 

            에어컨   핸들열선   열선시트  통풍시트   비상깜빡이   음상    음하   라디오
             ┏  ┓     ┏  ┓        ┏  ┓      ┏  ┓        ┏  ┓      ┏  ┓    ┏  ┓    ┏  ┓
                                                                                   ｜
             ┗  ┛     ┗  ┛        ┗  ┛      ┗  ┛        ┗  ┛      ┗  ┛    ┗  ┛    ┗  ┛                                                                        


------------------------------------------------------------------------""")


def bang3():
    global p
    p = 3
    #  ／ ｜ ￣ ― ∥ ＼ ┐┘┌└ ┓ ┛ ┏ ┗ 『』 【 】 ―

    if bang3point == 0:
        print(f"""------------------------------------------------------------------------

                                             _________  
                                          ---         ---
                                       ---               ---
                                     ---                   ---
                                   ---          시동          ---
                                     ---                   ---
                                       ---               ---
                                          ---         ---
                                             ￣￣￣￣￣           ┏   ┓   ┏   ┓
                                                                  ∥   ∥   ∥   ∥
                   ------------------------------------------------------------------------""")
    if bang3point == 1:
        print(f"""------------------------------------------------------------------------
    
                                             _________  
                                          --- /////// ---
                                       --- ////////////  ---
                                     ---  ///////////////  ---
                                   ---  /////// 시동 ///////  ---
                                     ---  ///////////////  ---
                                       ---  ///////////  ---
                                          --- //////// ---
                                             ￣￣￣￣￣           ┏   ┓   ┏   ┓
                                                                  ∥   ∥   ∥   ∥
           ------------------------------------------------------------------------""")
    elif bang3point == 2:
        print(f"""------------------------------------------------------------------------
    
                                             _________  
                                          ---         ---
                                       ---               ---
                                     ---                   ---
                                   ---          시동          ---
                                     ---                   ---
                                       ---               ---
                                          ---         ---
                                             ￣￣￣￣￣           ┏ ｜ ┓   ┏   ┓
                                                                  ∥ ｜ ∥   ∥   ∥
           ------------------------------------------------------------------------""")
    elif bang3point == 3:
        print(f"""------------------------------------------------------------------------
    
                                             _________  
                                          ---         ---
                                       ---               ---
                                     ---                   ---
                                   ---          시동          ---
                                     ---                   ---
                                       ---               ---
                                          ---         ---
                                             ￣￣￣￣￣          ┏   j┓   ┏ ｜ ┓
                                                                 ∥   ∥   ∥ ｜ ∥
           ------------------------------------------------------------------------""")

def bang4():
    global p
    print("4번방입니다.")
    p = 4
    #  ／ ｜ ￣ ― ∥ ＼ ┐┘┌└ ┓ ┛ ┏ ┗ 『』 【 】 ― ＿
    if bang4point == 0:
        print(f"""------------------------------------------------------------------------
    
                            ｜￣￣￣￣￣￣￣￣￣￣ ｜
                            ｜                     ｜
                            ｜   P        🎱      ｜
                            ｜                     ｜
                            ｜   R                 ｜
                            ｜                     ｜
                            ｜   N                 ｜
                            ｜                     ｜
                            ｜   D                 ｜
                            ｜                     ｜
                            ｜_____________________｜

            ------------------------------------------------------------------------""")
    elif bang4point == 1:
        print(f"""------------------------------------------------------------------------
    
                            ｜￣￣￣￣￣￣￣￣￣￣ ｜
                            ｜                     ｜
                            ｜   P                 ｜
                            ｜                     ｜
                            ｜   R        🎱      ｜
                            ｜                     ｜
                            ｜   N                 ｜
                            ｜                     ｜
                            ｜   D                 ｜
                            ｜                     ｜
                            ｜_____________________｜
    
            ------------------------------------------------------------------------""")
    elif bang4point == 2:
        print(f"""------------------------------------------------------------------------
    
                            ｜￣￣￣￣￣￣￣￣￣￣ ｜
                            ｜                     ｜
                            ｜   P                 ｜
                            ｜                     ｜
                            ｜   R                 ｜
                            ｜                     ｜
                            ｜   N        🎱      ｜
                            ｜                     ｜
                            ｜   D                 ｜
                            ｜                     ｜
                            ｜_____________________｜
    
            ------------------------------------------------------------------------""")
    elif bang4point == 3:
        print(f"""------------------------------------------------------------------------
    
                            ｜￣￣￣￣￣￣￣￣￣￣ ｜
                            ｜                     ｜
                            ｜   P                 ｜
                            ｜                     ｜
                            ｜   R                 ｜
                            ｜                     ｜
                            ｜   N                 ｜
                            ｜                     ｜
                            ｜   D        🎱      ｜
                            ｜                     ｜
                            ｜_____________________｜
    
            ------------------------------------------------------------------------""")



def speed_up(value):
    global car_speed
    count_speed = 1
    if 0 < value:
        while True:
            if count < value + 1:
                # time.sleep(0.5)
                car_speed = count_speed * 20
                count_speed += 1
            else:
                return
    else:
        while True:
            if car_speed <= 0:
                pass
            else:
                # time.sleep(0.5)
                car_speed -= 2

def speed_down(value):
    global car_speed
    while True:
        if 0 < value <= 10:
            if 0 < car_speed:
                time.sleep(0.5)
                car_speed=car_speed-20
                value-=1
            elif car_speed == 0:
                car_speed=0
                return
        else:
            return

def fw():  # 시선
    global count
    global accident_txt
    global accident_title
    global p
    count += 1
    if count == 10:  # 눈
        global bang1point
        snow.snow()
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        count += 1
        time.sleep(1)
        p = 1
        bang1point = 8
        bang1()
        accident_title, accident_txt = accident(11)
        return

    elif count == 20:  # 어린이 보호구역
        global bang3point
        snow.kid()
        time.sleep(1)
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 2
        bang3point = 2
        bang3()
        accident_title, accident_txt = accident(21)
        return

    elif count == 30:  # 고라니 출몰
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 2
        bang3point = 2
        bang3()
        accident_title, accident_txt = accident(31)
        return


    elif count == 40:  # 엔진오일 과열
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        time.sleep(1)
        p = 3
        bang3point = 1
        bang3()
        accident_title, accident_txt = accident(41)
        return

    if p == 0:
        pass
    elif p == 1:
        pass
    elif p == 2:
        pass
    elif p == 3:
        sideList()
        board()
        bang1()
        print(mainList)
    elif p == 4:
        sideList()
        board()
        bang2()
        print(mainList)
    elif p == 5:
        pass



def fa():  # 시선
    global count
    global accident_txt
    global accident_title
    global p
    count += 1
    if count == 10:  # 눈
        global bang1point
        snow.snow()
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 1
        bang1point = 8
        bang1()
        accident(11)
        return

    elif count == 20:  # 어린이 보호구역
        global bang3point
        snow.kid()
        time.sleep(1)
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 2
        bang3point = 2
        bang3()
        accident_title, accident_txt = accident(21)
        return


    elif count == 30:  # 고라니
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 2
        bang3point = 2
        bang3()
        accident_title, accident_txt = accident(31)
        return


    elif count == 40:  # 엔진오일 과열
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 3
        bang3point = 1
        bang3()
        accident_title, accident_txt = accident(41)
        return

    if p == 0:
        pass
    elif p == 1:
        pass
    elif p == 2:
        sideList()
        board()
        bang1()
        print(mainList)
    elif p == 3:
        pass
    elif p == 4:
        sideList()
        board()
        bang3()
        print(mainList)
    elif p == 5:
        pass


def fs():  # 시선
    global count
    global accident_txt
    global accident_title
    global p
    count += 1
    if count == 10:  # 눈
        global bang1point
        snow.snow()
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 1
        bang1point = 8
        bang1()
        accident_title, accident_txt = accident(11)
        return

    elif count == 20:  # 어린이 보호구역
        global bang3point
        snow.kid()
        time.sleep(1)
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 2
        bang3point = 2
        bang3()
        accident_title, accident_txt = accident(21)
        return

    elif count == 30:  # 고라니
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 2
        bang3point = 2
        bang3()
        accident_title, accident_txt = accident(31)
        return


    elif count == 40:  # 엔진오일 과열
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 3
        bang3point = 1
        bang3()
        accident_title, accident_txt = accident(41)
        return

    if p == 0:
        sideList()
        board()
        bang3()
        print(mainList)
    elif p == 1:
        sideList()
        board()
        bang3()
        print(mainList)
    elif p == 2:
        sideList()
        board()
        bang4()
        print(mainList)
    elif p == 3:
        pass
    elif p == 4:
        pass
    elif p == 5:
        pass



def fd():  # 시선
    global count
    global accident_txt
    global accident_title
    global p
    count += 1
    if count == 10:  # 눈
        global bang1point
        snow.snow()
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 1
        bang1point = 8
        bang1()
        accident_title, accident_txt = accident(11)
        return

    elif count == 20:  # 어린이 보호구역
        global bang3point
        snow.kid()
        time.sleep(1)
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 2
        bang3point = 2
        bang3()
        accident_title, accident_txt = accident(21)
        return


    elif count == 30:  # 고라니
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 2
        bang3point = 2
        bang3()
        accident_title, accident_txt = accident(31)
        return

    elif count == 40:  # 엔진오일 과열
        accident_title, accident_txt = accident(count)
        board()
        Sound.beepsound()
        time.sleep(1)
        p = 3
        bang3point = 1
        bang3()
        accident_title, accident_txt = accident(41)
        return

    if p == 0:
        sideList()
        board()
        bang2()
        print(mainList)
    elif p == 1:
        sideList()
        board()
        bang2()
        print(mainList)
    elif p == 2:
        pass
    elif p == 3:
        sideList()
        board()
        bang4()
        print(mainList)
    elif p == 4:
        pass
    elif p == 5:
        pass

def fk1(): # 방안에서 메뉴 이동 J
    global bang1point, bang2point, bang3point, bang4point, bang5point, bang6point
    if p == 1: # 핸들
        if 0 <= bang1point <= 10:
            if bang1point == 0:
                pass
            else:
                bang1point -= 1
        sideList()
        board()
        bang1()
    elif p == 2: # 내부버튼
        if 1 <= bang2point <= 5:
            if bang2point == 1:
                bang2point = 5
            else:
                bang2point -= 1
        sideList()
        board()
        bang2()
    elif p == 3: # 시동 및 엑셀,브레이크
        if 0 <= bang3point <= 3:
            if bang3point == 0:
                pass
            else:
                bang3point -= 1
        sideList()
        board()
        bang3()
    elif p == 4: # 기어봉
        Gear.gear_up()
        if 0 <= bang4point <= 3:
            if bang4point == 0:
                pass
            else:
                bang4point -= 1
        sideList()
        board()
        bang4()
    elif p == 5:
        if 0 <= bang5point <= 5: # 에어컨 기능이 몇개가 될지 모르니 일단 보류
            if bang5point == 0:
                pass
            else:
                bang5point -= 1
        sideList()
        board()
        bang5()
    elif p == 6:
        if 0 <= bang6point <= 3: # 라디오 기능이 몇개 될지 모르니 보류
            if bang6point == 3:
                pass
            else:
                bang6point += 1
        sideList()
        board()
        bang6()

def fk2(): # 방안에서 메뉴 이동 K
    global bang1point, bang2point, bang3point, bang4point, bang5point, bang6point
    if p == 1:
        if 0 <= bang1point <= 10:
            if bang1point == 10:
                pass
            else:
                bang1point += 1
        sideList()
        board()
        bang1()
    elif p == 2:
        if 1 <= bang2point <= 5:
            if bang2point == 5:
                bang2point = 1
            else:
                bang2point += 1
        sideList()
        board()
        bang2()
    elif p == 3:
        if 0 <= bang3point <= 3:
            if bang3point == 3:
                pass
            else:
                bang3point += 1
        sideList()
        board()
        bang3()
    elif p == 4:
        Gear.gear_down()
        if 0 <= bang4point <= 3:
            if bang4point == 3:
                pass
            else:
                bang4point += 1
        sideList()
        board()
        bang4()
    elif p == 5:
        if 0 <= bang5point <= 5: # 에어컨 기능이 몇개가 될지 모르니 일단 보류
            if bang5point == 5:
                pass
            else:
                bang5point += 1
        sideList()
        board()
        bang5()
    elif p == 6:
        if 0 <= bang6point <= 3: # 라디오 기능이 몇개 될지 모르니 보류
            if bang6point == 0:
                pass
            else:
                bang6point -= 1
        sideList()
        board()
        bang6()


def fk3(): #결정 L
    global accel1
    global accel2
    global accelfinal
    global accelCount

    global braeak1
    global braeak2
    global braeakfinal
    global braeakCount
    if p == 1:
        if bang1point == 0:
            mainList[17] = 0
            mainList[18] = 0
            board()
            bang1()
            return
        if bang1point ==1:
            mod_winker.winker_left_on_off()
            mainList[17] = mod_winker.left
            if mainList[18] == 1:
                mainList[18] = 0
            board()
            bang1()
            return
        elif bang1point ==2:
            mod_winker.winker_right_on_off()
            mainList[18] = mod_winker.right
            if mainList[17] == 1:
                mainList[17] = 0
            board()
            bang1()
            return
        elif bang1point ==3:
            if mainList[22] != 0:
                light.normalLight()
                mainList[15] = light.normalLights  # 노멀 라이트
            elif mainList[22] == 0:
                pass
            board()
            bang1()
            return
        elif bang1point ==4:
            if mainList[22] != 0:
                light.highBeam()
                mainList[16] = light.highBeams
            elif mainList[22] == 0:
                pass
            board()
            bang1()
            return
        elif bang1point == 5:
            if mainList[22] != 0:
                auto = light.auto()
                mainList[31] = auto
            elif mainList[22] == 0:
                pass
            board()
            bang1()
            return
        elif bang1point == 6:
            if mainList[22] != 0:
                agd = light.fogLight()
                mainList[21] = agd
            elif mainList[22] == 0:
                pass
        elif bang1point == 7:
            if mainList[22] != 0:
                wfon = mod_wiper.wiper_on()
                mainList[12] = wfon
                snow.wi()
            elif mainList[22] == 0:
                pass
            board()
            bang1()
            return
        elif bang1point == 8:
            if mainList[22] != 0:
                wfup = mod_wiper.mod_wiper_up()
                snow.wi2()
                mainList[13] = wfup
            elif mainList[22] == 0:
                pass
            board()
            bang1()
            return
        elif bang1point == 9:
            if mainList[22] != 0:
                wsa = mod_wiper.wiper_washer_fluid()
                snow.washer_fluid()
                mainList[14] = wsa
            elif mainList[22] == 0:
                pass
            board()
            bang1()
            return
        elif bang1point == 10:
            klx = mod_klaxon.klaxon()
            mainList[25] = klx
            board()
            bang1()
            return

    if p == 2:
        if bang2point == 1:
            board()
            bang5()
            return
            # mod_airconditioner.aircon_on_or_off() #에어컨페이지 작성해야함.
        elif bang2point ==2:
            hhof = mod_handle_seat_heat.handle_heat_on_or_off()
            mainList[4] = hhof
            board()
            bang2()
            return
        elif bang2point ==3:
            shof = mod_handle_seat_heat.seat_heat_on()
            mainList[5] = shof
            board()
            bang2()
            return  # mainList[5] = shof
        elif bang2point ==4:
            swof = mod_handle_seat_heat.seat_wind_on()
            mainList[6] = swof
            board()
            bang2()
            return  # mainList[6] = swof
        elif bang2point ==5:
            mod_emergency_light.emergency_light_on_or_off()
            mainList[7] = mod_emergency_light.emergency_light
            board()
            bang2()
            return  # mainList[7] = bsd
        elif bang2point ==6:
            blu = mod_volume.mod_volume_up()
            mainList[8] = blu
            board()
            bang2()
            return  # mainList[8] = blu
        elif bang2point == 7:
            bld = mod_volume.mod_volume_down()
            mainList[9] = bld
            board()
            bang2()
            return  # mainList[8] = bld
        elif bang2point == 8:
            pass # mod_radio.fm_or_am() # 라디오 페이지 작성해야함.
    if p == 3:
        if bang3point == 0:
            pass

        elif bang3point == 1:
            boots = Boot.boot(Braeak.a, Gear.a)
            mainList[0] = boots
            engine.enginestart()
            board()
            bang3()
            return

        elif bang3point == 2:
            braeakstart = time.time()
            braeak1 = braeakstart
            if braeak2 != 0:
                braeakfinal = braeak1 - braeak2
                if 0 < braeakfinal <= 1 and 0 <= braeakCount < 10:
                    braeakCount += 1
                    speed_test = threading.Thread(target=speed_down(braeakCount))
                    speed_test.start()
                elif braeakfinal > 1:
                    braeakCount = 0
            elif braeak2 == 0:
                pass
            braeaks = Braeak.braeak()
            mainList[1] = braeaks
            if mainList[2] == 1:
                Accel.acceloff()
                mainList[2] = 0
            if mainList[19] == 0:
                lbl = light.breakLight()
                mainList[19] = lbl
            braeakend = time.time()
            braeak2 = braeakend
            board()
            bang3()
            return # mainList[1] = braeaks

        elif bang3point == 3:
            accelstart = time.time()
            accel1 = accelstart
            if accel2 != 0:
                accelfinal = accel1 - accel2
                if 0 < accelfinal <= 1 and 0 <= accelCount < 10:
                    accelCount += 1
                    speed_test = threading.Thread(target=speed_up(accelCount))
                    speed_test.start()
                elif accelfinal > 1:
                    accelCount = 0
            elif braeak2 == 0:
                pass
            accels = Accel.accel()
            mainList[2] = accels
            if mainList[1] == 1:
                Braeak.braeakoff()
                mainList[1] = 0
                lbl = light.breakLight()
                mainList[19] = lbl
            accelend = time.time()
            accel2 = accelend
            board()
            bang3()
            return # mainList[2] = accels

    if p == 4:
        if bang4point == 0:
            gears = Gear.a
            print("파킹기어 상태")
            mainList[3] = gears
            board()
            bang4()
            return # mainList[3] = gears
        elif bang4point == 1:
            gears = Gear.a
            print("후진기어 상태")
            mainList[3] = gears
            lrl = light.reverseLight()
            mainList[20] = lrl
            board()
            bang4()
            return  # mainList[3] = gears

        elif bang4point == 2:
            gears = Gear.a
            print("중립기어 상태")
            mainList[3] = gears
            board()
            bang4()
            return  # mainList[3] = gears

        elif bang4point == 3:
            gears = Gear.a
            print("드라이브기어 상태")
            mainList[3] = gears
            board()
            bang4()
            return  # mainList[3] = gears

    if p == 5: # 에어컨에 들어가 들어가 있는 상황
        if bang5point == 0:
            aironoff = mod_airconditioner.air_conditioner_heater()
            mod_airconditioner.heater_aircon()
            mainList[26] = aironoff
            board()
            bang5()
            return
        elif bang5point == 1:
            odup = mod_airconditioner.aircon_temperature_go_up()
            mainList[27] = odup
            board()
            bang5()
            return
        elif bang5point == 2:
            oddw = mod_airconditioner.aircon_temperature_go_down()
            mainList[27] = oddw
            board()
            bang5()
            return
        elif bang5point == 3:
            blsg = mod_airconditioner.aircon_wind_strength_123()
            mainList[28] = blsg
            board()
            bang5()
            return
        elif bang5point == 4:
            pljj = mod_airconditioner.aircon_direction_go_up_down()
            mainList[29] = pljj
            board()
            bang5()
            return
        elif bang5point == 5:
            board()
            bang2()
            return



def fk4():
    pass

def timethreading():
    side.gasolineIng()
    side.baterryIng()
    side.engineOilIng()

timethreading()

def sideList():
    mainList[24] = round(side.gasolineTank,2)
    mainList[22] = round(side.batteryCharge,2)
    mainList[23] = round(side.engineOiltemp,2)

board()
bang1()



while 1:
    moving=input('wasd//j///i')
    if moving == 'w':
        fw()
    elif moving == 'a':
        fa()
    elif moving == 's':
        fs()
    elif moving == 'd':
        fd()
    elif moving == 'j':
        fk1()
    elif moving == 'k':
        fk2()
    elif moving == 'l':
        fk3()
        print("엑셀 카운트", accelCount)
        print("브레이크 카운트", braeakCount)
    elif moving == 'm':
        fk4()




