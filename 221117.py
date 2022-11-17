# 동시작업
# 스레딩
import time
import threading
count = 0
# def sp():
#     while 1:
#         print("속도")
#         time.sleep(1)
#
# def br():
#     print("브레이크 밟음")

# sp()
# br()
# 이렇게 하면 속도에서 탈출하지 못함

def sum(low,high):
    total = 0
    count1 = 0
    for i in range(low,high):
        total += i
    print(total,"실행")
    while 1:
        count1 +=1
        print("\n\n속도 + ",count1)
        time.sleep(1)


th1 = threading.Thread(target=sum,args=(1,10000))
th1.start()

while 1:
    count +=1
    print("\n\nhello + ", count)
    time.sleep(1)

    if count == 10:
        th1.join()
        # start()는 스레드 작동시작
        # join()부모 스레드의 진행을 멈추고 자식스레드의 종료를 기다림
