import theater
import random
class movie:
    # 관 클래스, 관마다 구조 다르게 종류(리클라이너), 예약, 발권, 취소 등
    name = ""
    time = 0 # 러닝타임
    # 영화 생성할 때 영화관 랜덤배치 X
    def __init__(self,name,time):
        self.name = name
        self.time = time
        # number1 = random.randint(4,20)
        # number2 = random.randint(10,20)
        # num = random.randint(1,3)
        # self.type = ""
        # if num == 1:
        #     self.type = "A"
        # elif num == 2:
        #     self.type = "B"
        # elif num == 3:
        #     self.type = "C"
        # print(self.type)
        #
        # theater.theater(number1,number2,self.type)


a = movie("아아아",120)
print(a)