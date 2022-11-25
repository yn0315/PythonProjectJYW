import calculate_button
import tkinter as tk
win = tk.Tk()
number_and_button = ""

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====")
class cc:
    num = 1
    def __init__(self):
        self.result = ""
        print(cc.num, "계산기 생성")
        cc.num += 1

    def n1(self):
        self.result += "1"
    def n2(self):
        self.result += "2"
    def n3(self):
        self.result += "3"
    def plus(self):
        # if self.result[-1]가 부호면 지워주고 다음걸로 더해주면된다
        self.result += "+"
    def show_res(self):
        print(eval(self.result))


c1 = cc()
c1.n3()
c1.n3()
c1.n3()
c1.n3()
c1.plus()
c1.n3()
c1.n3()
c1.show_res()

# while 1:
#     moving = input('>>')
#
#     if "=" in moving:
#         break
#     else:
#         number_and_button += moving


#
# print(eval(number_and_button))

# 비동기 프록래밍을 위한 모듈
# 작업을 비동기로 처리
# 동기는 순차적으로 진행되는 것
# 비동기는 개별적으로 운용되는 것

# 동기처리는 작업이 끝나야 다음 작업을 처리하는 방식
# 비동기처리는 여러 작업을 개별로 처리하도록 예약한 뒤 작업, 동일한 출발선에서 시작
import random
import asyncio # 비동기처리
cal_list = [] # 정적생성
async def show(count):
    x = random.sample([1,2,3,4,5],k=1)
    await asyncio.sleep(x[0])
    print(count,"번째 show의 지연 초 : ", x)
    cal_list.append(cc()) # 동적생성


async def main():
    # 작업하려는 대상을
    # await asyncio.gather()
    await asyncio.gather(
        show(1),
        show(2),
        show(3),
        show(4),
        show(5),
    )

asyncio.run(main())

print(cal_list)
cal_list[0].n1()
cal_list[0].n1()
cal_list[0].n1()
cal_list[0].plus()
cal_list[0].n1()
cal_list[0].n1()
cal_list[0].n1()
cal_list[0].n1()
cal_list[0].n1()
cal_list[0].show_res()
