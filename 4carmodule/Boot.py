import Gear
import Braeak


#0 : 시동 off
#1 : 시동 준비(배터리 사용가능)
#2 : 시동 on (배터리 및 엔진 가동중)

def boot(braeaka=1,geara=0):
    try:
        if braeaka == 0 and geara == 0:
            print("시동 on")
            return 2
        elif braeaka !=0 and geara == 0:
            print("브레이크 확인")
            return 1
        elif braeaka != 0 and geara !=0:
            print("기어 및 브레이크 ")
            return 0
        elif braeaka == 0 and geara !=0:
            print("기어를 p로 하시오")
    except:
        print("자동차 키가 부러 졌습니다.")

