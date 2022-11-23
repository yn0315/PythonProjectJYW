import Accel
import Gear
import Braeak


#0 : 시동 off
#1 : 시동 준비(배터리 사용가능)
#2 : 시동 on (배터리 및 엔진 가동중)
boots = 0
def boot(braeaka=1,geara=0):
    global boots
    try:
        if braeaka != 0 and geara == 0:
            boots = 2
            print("시동 on")
            return boots
        elif braeaka ==0 and geara == 0:
            boots = 1
            print("브레이크 확인, 전자기기 사용 가능")
            return boots
        elif braeaka != 0 and geara !=0:
            boots = 0
            print("기어를 p로 하시오 ")
            return boots
        elif braeaka == 0 and geara !=0:
            print("브레이크 기어 확인")
    except:
        print("자동차 키가 부러 졌습니다.")
