import module_2frame
# 핸들함수
def handle():
    try:
        global page
        page = 2 # 페이지를 2로 변경
        # 엔진이 돌아가지 않은 상황에서 돌리게 되면 락걸림
        e = module_2frame.engine() # 여기서 함수호출이 아니라 임포트로 가져와야 함
        # 돌발상황일 때 에어백 터지는 기능

        # 엔진이 꺼져있을 때
        if e == 0: # off
            return
        # 엔진이 켜져있을 때
        elif e == 1: # on
            print("a. 방향지시등 s.라이트 d. 클락션 w. 와이퍼")

    except Exception as e:
        print("handle", type(e), e)