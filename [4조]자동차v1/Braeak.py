a=0

def braeak():
    global a
    b = a % 2
    try:
        if  b== 0:
            b += 1
            a = b%2
            #Braeak 발로 밟음
            return a
        elif  b== 1:
            b += 1
            a = b%2
            #Braeak 발을 땜
            return a
    except:
        print("error : 입력값 초과")
