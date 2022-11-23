import time
import random
import light
import mod_winker
import side
import engine
import mod_winker
import mod_wiper
import mod_handle_seat_heat
import Gear
import Braeak
import Boot
import Accel
import mod_radio

check_list = [0,1,2,3,4,5,6,7,8,9,1,1,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]    # 확인할 리스트??

print(check_list[10],check_list[11])


accident_situation = random.randrange(0,10)
accident_title = ""
accident_txt = ""
accident_number = 0

accel = 0       # 사고 발생 화면 만들기인데 아직 미사용

AA = 0          # 악셀 받을 지역변수

radio_channel = ''          # 라디오 채널 받을 문자열
radio_decibel = ''          # FM / AM 받을 문자열

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

def winker_mark(value) :         # 깜빡이 계기판 표시 - winker함수와 value 값이 같아야 합니다. 연동 되어야합니다.
    if value == 0 :  # 왼쪽 깜빡이 안킴
        return '◀'
    if value == 1 :  # 오른쪽 깜빡이 안킴
        return '▶'
    if value == 2 :  # 왼쪽 깜빡이 킴
        return '\033[33m' + '◀' + '\033[0m'
    if value == 3 :  # 오른쪽 깜빡이 킴
        return '\033[33m' + '▶' + '\033[0m'

def winker(value) : # 깜빡이 넣었을떼  /  winker_mark 함수와 value 값이 같아야 합니다. 연동 되어야합니다.
    try :
        if value == 0 :       # 왼쪽 꺼져있을때
            return '■■■■■■■■■■■■'
        elif value == 1 :             # 오른쪽 꺼져있을때
            return '■■■■■■■■■■■■'
        elif value == 2 :             # 왼쪽 켜져있을때
            return '\033[33m' + '■■■■■■■■■■■■' + '\033[0m'
        elif value == 3 :               # 오른쪽 켜져있을때
            return '\033[33m' + '■■■■■■■■■■■■' + '\033[0m'
    except :
        pass

def rear_light(value) :                         # 후미등  /  하향등, 상향등, 미등, 안개등, 깜빡이 계기판 표시와 연동??
    # tail_light = 0    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 미등 뒷 등 켜질경우
    # log_map = 1    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 안개등 뒷 등 켜질경우
    # under_light = 2    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 하향등 뒷 등 켜질경우
    # high_light = 3    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 상향등 뒷 등 켜질경우
    # emergency_light = 4    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 비상등 뒷 등 켜질경우
    try :
        if rear_light1 == 1 or rear_light2 == 1 or rear_light3 == 0 :               # 후미등만 들어왔을 경우
            return '\033[31m \033[41m' + '■■■■■■■■■■' + '\033[0m'
        elif value == 0 or value == 1 :
            return '\033[93m' + '   ■■■■      ' + '\033[0m'
        elif value == 2 :
            return '\033[33m' + '  ■■■■■■■■ ' + '\033[0m'
        elif value == 3 :
            return '\033[33m \033[43m' + '■■■■■■■■■■' + '\033[0m'
        elif value == 4 :
            return '\033[31m' + '   ■■■■      ' + '\033[0m'
    except :
        pass

def front_light(value) :
    # tail_light = 0    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 미등 앞 등 켜질경우
    # log_map = 1    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 안개등 앞 등 켜질경우
    # under_light = 2    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 하향등 앞 등 켜질경우
    # high_light = 3    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 상향등 앞 등 켜질경우
    # emergency_light = 4    # 어떻게 할 줄 몰라 일단 임의 값 설정 / 비상등 앞 등 켜질경우
    try :
        if value == 0 or value == 1 :
            return '\033[93m' + '   ■■■■      ' + '\033[0m'
        elif value == 2 :
            return '\033[33m' + '  ■■■■■■■■ ' + '\033[0m'
        elif value == 3 :
            return '\033[33m \033[43m' + '■■■■■■■■■■' + '\033[0m'
        elif value == 4 :
            return '\033[31m' + '   ■■■■      ' + '\033[0m'
    except :
        pass

def Circulation_Button(value) :         # 내부 순환 버튼??
    if value == 0 :                    # 안켜져 있을때
        return '  🌀  '
    if value == 1 :                    # 켜져 있을때
        return '\033[34m'+'  🌀  '+'\033[0m'

def oil_title(value):          # 기름 제목 ( 기름 부족하면 빨간 글씨로 뜸)
    try :
        if value == 0 :           # 일정 이상이라면 평균값으로 설정
            return 'Oil'
        elif value == 1 :         # 오일값이 일정 이하라면 으로 설정?
            return '\033[31m'+'Oil'+'\033[0m'
    except :
        pass

def oil_text(value) :          # 기름 부족 계기판 표시
    try :
        if value == 0 :                # 평균 이상일때
            return '⛽'
        elif value == 1 :              # 기름 부족할때
            return '\033[31m'+'⛽'+'\033[0m'
    except :
        pass

def battery_title(value) :     # 배터리 제목 ( 부족하면 빨간색 글씨로 뜸 )

    if value == 0 :        # 배터리 역시 일정 이상 값이라면 평균 설정
        return 'Battery'
    elif value == 1:       # 배터리 값이 일정 이하라면 경고문
        return '\033[31m'+'Battery'+'\033[0m'

def battery_text(value) :         # 배터리 계기판 표시
    try :
        if value == 0 :              # 배터리 충분할 때
            return '🔋'
        elif value == 1 :            # 배터리 모자랄 때
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

def board() :             # 계기판
    global AA
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    AA = Accel.accel()
    print(f"""                              {front_light(a)}                                                     {front_light(a)}
                               --------------------------------------------------------------------------
                                L.winker            상향등    하향등    미등    안개등               R.winker
         ----------------------    {winker_mark(a)}                  {high_light_mark(b)}      {under_light_mark(b)}       {tail_light_mark(b)}      {log_map_mark(b)}                     {winker_mark(b)}    ----------------------
        ==                        주행거리                           속도                              연비                       ==
    　 ==　                      200,000KM                         120KM                             15 l                        ==
     ==       {winker(a)}     {battery_title(b)}        {oil_title(b)}             현재 온도          내부 순환       {drive_title(a)}        {winker(b)}       ==
     ==                           {battery_text(b)}           {oil_text(b)}                 //             {Circulation_Button(a)}            {drive_text(a)}                             ==
    　 ==                                                    Emergency_Button                                                    ==
        ==                                                          {Emergency_Button(a)}              A / C      💺      ⚙                        ==
         ----------------------         📻                                         {Air_Conditioning(c)}    {sit_heat_rays(a)}  {hanldle_heat_rays(b)} ---------------------- 
                               ====================                                Break       Accel
                                     {radio_channel} / {radio_decibel}                                        {break_mark(b)}           {accel_mark(AA)} 
                               --------------------------------------------------------------------------                         ㅡㅡㅡㅡㅡㅡ상황 발생ㅡㅡㅡㅡㅡ
                              {rear_light(a)}                                                     {rear_light(a)}       기어                    {accident_title}   
                                                                                                                     {gear_mark(a)}           {accident_txt} 
                                                                                                                                  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ""")
board()

def board1() :             # 계기판
    global AA
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    AA = Accel.accel()
    print(f"""                              {front_light(e)}                                                     {front_light(e)}
                               --------------------------------------------------------------------------
                                L.winker            상향등    하향등    미등    안개등               R.winker
         ----------------------    {winker_mark(a)}                  {high_light_mark(b)}      {under_light_mark(b)}       {tail_light_mark(b)}      {log_map_mark(b)}                     {winker_mark(b)}    ----------------------
        ==                        주행거리                           속도                              연비                       ==
    　 ==　                      200,000KM                         120KM                             15 l                        ==
     ==       {winker(a)}     {battery_title(b)}        {oil_title(b)}             현재 온도          내부 순환       {drive_title(a)}        {winker(b)}       ==
     ==                           {battery_text(b)}           {oil_text(b)}                //              {Circulation_Button(a)}            {drive_text(a)}                             ==
    　 ==                                                    Emergency_Button                                                    ==
        ==                                                          {Emergency_Button(a)}              A / C      💺      ⚙                        ==
         ----------------------         📻                                         {Air_Conditioning(c)}    {sit_heat_rays(a)}  {hanldle_heat_rays(b)} ---------------------- 
                               ====================                                Break       Accel
                                     {radio_channel} / {radio_decibel}                                        {break_mark(b)}           {accel_mark(AA)} 
                               --------------------------------------------------------------------------                         ㅡㅡㅡㅡㅡㅡ상황 발생ㅡㅡㅡㅡㅡ
                              {rear_light(e)}                                                     {rear_light(e)}           기어                    {accident_title}   
                                                                                                                     {gear_mark(a)}           {accident_txt} 
                                                                                                                                  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ""")
