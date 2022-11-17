import time
import random

str1 = ""

accident_situation = random.randrange(0,10)
accident_title = ""
accident_txt = ""



# def speed(value) :                     # 초당 올라가는 속도??
#     # 엑셀 밟은 후부터 속도는 일정적으로 올라간다.
#     sec = 0
#     while 1:
#         if value == 1 :        # 엑셀일시
#             sec += 30
#             print(sec)
#             time.sleep(1)
#             if sec == 120 :
#                 break
#         elif value == 0 :        # 브레이크일시
#             sec -= 70
#             time.sleep(1)
#             if sec == 0 :
#                 break
#
#     return sec

def distance(value) :
    dis = 0
    while 1 :
        if value == 1 :     # 엑셀일시?
            dis += 5        # km라 가정?
            time.sleep(1)
        if value == 0 :      # 브레이크일시?
            break
    return dis

# def fuel_efficiency() :                   # 연비 계산법?
                                          # 예를 들어, 100km를 주행한 후 연료가
                                          # 총 4L가 소모 되었다면 연비는 25km/l이
                                          # 되는 것입니다.

# def fuel() :
    #distance() / 초당 연료? 고정값?

def light(value) :
    if value == 1 :         # 미등
        return '\033[30m \033[103m'+"  ○  "+'\033[0m'
    if value == 2 :         # 하이빔
        return '\033[30m \033[103m'+"  ●  "+'\033[0m'
    if value == 0 :         #안개등
        return '\033[30m \033[103m'+"  ◐  "+'\033[0m'

def winker(value) :
    if value == 0 :  # 왼쪽 깜빡이 안킴
        return '◀'
    if value == 1 :  # 오른쪽 깜빡이 안킴
        return '▶'
    if value == 2 :  # 왼쪽 깜빡이 킴
        return '\033[93m' + '◀' + '\033[0m'
    if value == 3 :  # 오른쪽 깜빡이 킴
        return '\033[93m' + '▶' + '\033[0m'

def Circulation_Button(value) :         # 내부 순환 버튼??
    if value == 0 :                    # 안켜져 있을때
        return '○'
    if value == 1 :                    # 켜져 있을때
        return '\033[30m \033[107m'+'  ●  '+'\033[0m'

def oil_title(value):          # 기름 제목 ( 기름 부족하면 빨간 글씨로 뜸)

    if value == 0 :           # 일정 이상이라면 평균값으로 설정
        return 'oil'
    elif value == 1 :         # 오일값이 일정 이하라면 으로 설정?
        return '\033[31m'+'oil'+'\033[0m'

def battery_title(value) :     # 배터리 제목 ( 부족하면 빨간색 글씨로 뜸 )

    if value == 0 :        # 배터리 역시 일정 이상 값이라면 평균 설정
        return 'battery'
    elif value == 1:       # 배터리 값이 일정 이하라면 경고문
        return '\033[31m'+'battery'+'\033[0m'

def accident(value):                # 사고 발생 상황
    global accident_situation
    if value == 5 :                       # 약한 충돌
        a = "⚠" + " 약한 충돌"
        b = "외부에 의한 약한 충돌이 있습니다"
        return a,b
    elif value == 9 :                      # 강한 충돌
        a = "⚠" + " 강한충돌"
        b = "외부에 의한 강한 충돌로 인해 에어백이 터집니다"
        return a,b
    else :                                 # 이상 없음
        a = "이상 없음"
        b = "정상 주행중입니다"
        return a,b

accident_title,accident_txt = accident(accident_situation)

def Aircon(value) :         # 에어컨
    try :
        if value == 0 :          # 에어컨 안켜져있을때
            return str1
        elif value == 1 :          # 에어컨 1단계
            return '\033[31m \033[44m'+' '+'\033[0m'
        elif value == 2 :          # 2단계
            return '\033[31m \033[44m'+' '+'\033[0m''\033[31m \033[44m'+' '+'\033[0m'
        elif value == 3:           # 3단계
            return '\033[31m \033[44m' + ' ' + '\033[0m''\033[31m \033[44m'+' '+'\033[0m''\033[31m \033[44m'+' '+'\033[0m'
    except :
        pass

def Heater(value) :               # 히터
    try :
        if value == 0 :           # 안켜져있을때
            return str1
        elif value == 1 :            # 1단계
            return '\033[31m \033[41m' + ' ' + '\033[0m'
        elif value == 2 :              # 2단계
            return '\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m'
        elif value == 3 :              # 3단계
            return '\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m'
    except :
        pass

def sit_heat_rays(value) :          # 자동차 의자 열선 엉따
    try :
        if value == 0 :
            return str1
        elif value == 1 :
            return '\033[31m \033[41m' + ' ' + '\033[0m'
        elif value == 2 :
            return '\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m'
        elif value == 3 :
            return '\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m''\033[31m \033[41m' + ' ' + '\033[0m'
    except :
        pass

def hanldle_heat_rays(value) :                # 핸들 열선
    try :
        if value == 0 :                          # 안켜져 있을때
            return str1
        elif value == 1 :                        # 켰을때
            return '\033[31m \033[41m' + ' ' + '\033[0m'
    except :
        pass


def board() :
    a = 0
    b = 1
    c = 2
    d = 3
    print(f"""-------------------------------------------------------------
    L.winker                    Light                    R.winker
       {winker(a)}                       {light(c)}                        {winker(d)}
    
    Aircon               Current temperature         Circulation button
    {Aircon(c)}                           //                       {Circulation_Button(b)}
    
    Heater                      sit_heat_rays            핸들 열선
    {Heater(c)}                          {sit_heat_rays(d)}                 　{hanldle_heat_rays(b)}
    
            Warning  -  {oil_title(a)}     {battery_title(a)}                      {accident_title}
                       //        //                       {accident_txt}
    
    Speed                  fuel_efficiency                distance
    //                           //                         {distance(a)}
    
    
                                        Break       Accel
                                          //         //
    -------------------------------------------------------------""")
    if winker(d) :
        print("오른쪽 깜빡이가 켜졌습니다")
    if Circulation_Button(b) :
        print("순환버튼이 작동되었습니다")
board()