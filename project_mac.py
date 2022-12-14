import datetime

in_out = 0  # 식사장소 변수, 매장 = 0, 포장 = 1
# 세트선택 기본값: 감튀 + 탄산 = +1800
# 라지세트 기본값: 감튀 + 탄산 = +2400

# 기본카테고리 디폴트 페이지 설정해주고
        # 맥런치 시간에는 맥런치를 디폴트로
        # 그 외 시간에는 버거페이지를 디폴트로
        # input("카테고리 목록 + 지금 활성화된 카테고리 메뉴, 이전버튼+ 주문완료(비활성화), 장바구니리스트, 취소")
        # 카테고리 목록변경 입력1(번)하면 목록 바뀌고 카테고리메뉴도 바뀌고 나머지 버튼 똑같이
        # 처음 3줄 프린트하고 2줄씩 더보기하면? 더보기 완료
        # 이전은 바로 전페이지 취소는 완전 처음화면으로 감

single_burger = {"빅맥": 4900, "맥스파이시상하이버거": 4900, "1955버거": 6000,
                 "베이컨토마토디럭스": 5800, "맥크리스피디럭스": 6700,
                 "맥크리스피클래식": 5900, "맥치킨모짜렐라": 5000, "맥치킨": 5000,
                 "더블불고기버거": 4500, "에그불고기버거": 3500, "불고기버거": 2500,
                 "더블필레오피쉬": 5200, "필레오피쉬": 3700, "슈슈버거": 4700,
                 "슈비버거": 5800, "쿼터파운더치즈": 5500, "더블쿼터파운더치즈": 7400,
                 "트리플치즈버거": 5800, "더블치즈버거": 4500, "치즈버거": 2500, "햄버거": 2200}  # 단품 햄버거 변수

set_burger = {"빅맥세트": 6700, "맥스파이시상하이버거세트": 6700, "1955버거세트": 7800,
              "베이컨토마토디럭스세트": 7600, "맥크리스피디럭스세트": 8500,
              "맥크리스피클래식세트": 7700, "맥치킨모짜렐라세트": 6800, "맥치킨세트": 6800,
              "더블불고기버거세트": 6300, "에그불고기버거세트": 5300, "불고기버거세트": 4300,
              "더블필레오피쉬세트": 7000, "필레오피쉬세트": 5500, "슈슈버거세트": 6500,
              "슈비버거세트": 7600, "쿼터파운더치즈세트": 7300, "더블쿼터파운더치즈세트": 9200,
              "트리플치즈버거세트": 7600, "더블치즈버거세트": 6300, "치즈버거세트": 4300, "햄버거세트": 4000}  # 변수 싱글버거 하나로 통일할 수 있는 방법...

large_set_burger = {"빅맥라지세트": 7300, "맥스파이시상하이버거라지세트": 7300, "1955버거라지세트": 8400,
                    "베이컨토마토디럭스라지세트": 8200, "맥크리스피디럭스라지세트": 9100,
                    "맥크리스피클래식라지세트": 8300, "맥치킨모짜렐라라지세트": 7400, "맥치킨라지세트": 7400,
                    "더블불고기버거라지세트": 6900, "에그불고기버거라지세트": 5900, "불고기버거라지세트": 4900,
                    "더블필레오피쉬라지세트": 7600, "필레오피쉬라지세트": 6100, "슈슈버거라지세트": 7100,
                    "슈비버거라지세트": 8200, "쿼터파운더치즈라지세트": 7900, "더블쿼터파운더치즈라지세트": 9800,
                    "트리플치즈버거라지세트": 8200, "더블치즈버거라지세트": 6900, "치즈버거라지세트": 4900, "햄버거라지세트": 4600}  # 세트햄버거 변수

mac = {"빅맥세트": 5200, "상하이버거세트": 5200, "1955버거세트": 6200, "베이컨토마토디럭스세트": 6000}    # 맥런치 변수

menu_key_list = ["빅맥", "맥스파이시상하이버거", "1955버거", "베이컨토마토디럭스", "맥크리스피디럭스", "맥크리스피클래식", "맥치킨모짜렐라", "맥치킨",
                 "더블불고기버거", "에그불고기버거", "불고기버거", "더블필레오피쉬", "필레오피쉬", "슈슈버거", "슈비버거", "쿼터파은더치즈", "더블쿼터파운더치즈",
                 "트리플치즈버거", "더블치즈버거", "치즈버거", "햄버거"]                                                                        # 페이지에 필요한 변수들
menu_values_list = [4900, 4900, 6000, 5800, 6700, 5900, 5000, 5000, 4500, 3500, 2500, 5200, 3700, 4700, 5800, 5500,
                    7400, 5800, 4500, 2500, 2200]


# x = list(menu_all.keys()[1:][int(input("카테고리를 입력하세요 "))])
# print(x,"를 선택해서 메뉴는", menu_all[x])

drink = {"카페라떼": 3000, "아메리카노": 2500, "바닐라라떼": 3500, "카푸치노": 3000, "에스프레소": 1700,
         "우유": 1500, "생수": 1200, "아이스드립커피": 1500, "탄산음료": 1500, "쉐이크": 2800}  # 음료 변수
side = {"맥너겟": 2200, "맥스파이시치킨텐더": 2700, "치즈스틱": 2500, "상하이치킨스낵랩": 2400,
        "치킨토마토스낵랩": 2200, "후렌치후라이": 1800, "애플파이": 1300, "코울슬로": 1900}  # 사이드 메뉴 변수

dessert = {"맥플러리": 2700, "선데이아이스크림": 1800, "오레오아포가토": 3200, "아이스크림콘": 900, "초코콘": 1200}

menu_all = {"맥런치": mac, "버거": single_burger, "사이드": side, "음료": drink}  # 처음화면에 필요한 변수!!

vegitable = ["양상추", "양파", "오이피클", "토마토"]
source = ["스위트 앤 사워", "스위트칠리", "케이준", "허니", "아라비아따"]
patty = ["소고기", "닭고기", "돼지고기"]  # 햄버거 재료 변수
burger_select_ingredients = []  # 햄버거 선택한재료  변수
side_ingredient = '소금'  # 사이드메뉴 재료변수

# 테이블 서비스 변수, 서비스 = 1, 셀프 = 0
service_self = 0    # 테이블 서비스 변수 서비스 = 1 셀프 = 0
dict_table_service = {}   # 테이블 서비스 프린트용 변수
table_number = 0            # 테이블 번호 변수

print_inout = {}  # 식사장소 영수증에서 프린트할 변수
select = {}  # 장바구니 변수
global total
total = {"합계": 0}  # 합계변수

# global complete
# complete= False # 주문완료시 True 아직 아니면 False

# 화면 초기화
def clearscreen():
    for i in range(30):     # 화면 넘어갈 때 다음 실행문만 보이도록 이전 실행문 위로 올리는 변수
        print()


# 맥런치타임인지 판별하는 함수
def ismac_lunch_time():
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    if 10 <= h < 14:
        if h == 10:
            if 30 <= m:
                return True
        else:
            return True

# 시작
def start(s):      # 버거이름 입력 후 실행하는 함수
    while True:
        clearscreen()
        num = input("0.취소  1.단품  2.세트  3.라지세트 \n번호를 입력해주세요.>>")
        clearscreen()
        if num == "0":
            select.clear() # 취소시 장바구니 비움
            x = 0            # 취소시 while 문 조건 변수들 0으로 초기화
            y = 0
            z = 0
            w = 0
            select.clear()
            dict_table_service.clear()
            print_inout.clear()
            total["합계"] = 0
            print("주문이 취소되었습니다.")
            break

        elif num == "1":
            select_burgermenu(s)  #단품/세트/라지세트 여부에 따라 장바구니에 담아주는 변수를 실행하라.
            burger_process()      # 햄버거 주문과정 함수를 실행하라.
        elif num == "2":
            select_burgermenu(s + "세트")
            burger_process()

        elif num == "3":
            select_burgermenu(s + "라지세트")
            burger_process()
        elif not num.isdigit():
            print("잘못 입력하셨습니다. 다시 입력해주세요.")   # 숫자로 인식되지 않는 문자를 입력시 출력되는 조건문
            continue
        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")   #그 외 입력시 출력되는 조건문
            continue
        break
    return

# 버거 주문(단품/세트/라지세트) 함수
def select_burgermenu(sel):
    while True:
        global burger_select_ingredients

        if sel in single_burger:                 # 단품
            select[sel] = single_burger[sel]
            ingredient_process()
            return

        elif sel in set_burger:                    # 세트
            select[sel] = set_burger[sel]
            ingredient_process()
            return

        elif sel in large_set_burger:                  # 라지세트
            select[sel] = large_set_burger[sel]
            ingredient_process()
            return



# 음료주문 함수
def select_drinkmenu():
    while True:
        clearscreen()
        print("| 버거 |+음료+| 사이드 | 디저트 | 이전 | 주문완료 |  ")
        print()
        for k, v in drink.items():
            print(k, v)
        print("음료를 골라주세요")
        beverage = input(">>")

        if not beverage in drink:
            print("다시입력해주세요.")
            continue

        elif beverage in drink:
            select[beverage] = drink[beverage]
            # 음료 장바구니에 집어넣기
        for k, v in select.items():
            print(" ", k, v)
            return


# 사이드메뉴 주문함수
def select_sidemenu():
    while True:
        clearscreen()
        print("| 버거 | 음료 |+사이드+| 디저트 | 이전 | 주문완료 |  ")
        print()
        for k, v in side.items():
            print(k, v)
        print("사이드메뉴를 골라주세요")
        s = input(">>")
        clearscreen()
        if not s in side:
            print("다시입력해주세요.")
            continue
        elif s in side:
            select[s] = side[s]
        for k, v in select.items():
            print(" ", k, v)
            return


# 디저트메뉴 주문함수
def select_dessertmenu():
    while True:
        clearscreen()
        print("| 버거 | 음료 | 사이드 |+디저트+| 이전 | 주문완료 |  ")
        print()
        for k, v in dessert.items():
            print(k, v)
        print("디저트메뉴를 골라주세요")
        s = input(">>")
        clearscreen()
        if not s in dessert:
            print("다시입력해주세요.")
            continue
        elif s in dessert:
            select[s] = dessert[s]
        for k, v in select.items():
            print(" ", k, v)
            return

# 맥런치 타임시 주문
def mac_lunch():
    while True:
        print("|+맥런치+| 버거 | 음료 | 사이드 | 디저트 | 이전 | 주문완료 |  ")
        print()
        for c, d in mac.items():
            print(" ", c, d)

        print("이전은 0, 주문완료는 1번을 눌러주세요.")
        s = input("카테고리 or 제품명을 입력하세요. : ")

        if s in mac:
            select[s] = mac[s]                  # 입력한 값이 mac변수에 있을 시 장바구니에 담고
            burger_process()                   # 버거 주문과정함수 실행
            ingredient_process()               # 재료주문과정함수 실행
            w = 0
            break
        elif s == "0":                        # 이전
            break
        elif s == "1":
            print("주문이 취소되었습니다.")          # 주문취소
            for k, v in select.items():
                print(k, v)
                w == 0
                break
        elif s == "버거":                # 버거입력시 아래과정이 실행되는 조건문
            print("|+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
            print()
            page()              # 카테고리 페이지 나누는 함수 및 주문과정으로 들어가는 함수
            break
        elif s == "음료":
            select_drinkmenu()
            burger_process()
            break
        elif s == "사이드":
            select_sidemenu()
            burger_process()
            break
        elif s == "디저트":
            select_dessertmenu()
            burger_process()
            break
        elif not s.isdigit() and s in single_burger:
            start(s)
            break
        break
    return


# 햄버거 주문과정 함수
def burger_process():
    while True:
        clearscreen()
        print("0.완료 1.음료 2.사이드메뉴 \n추가를 원하시면 번호를 누르세요.")
        n = (input(">>"))
        clearscreen()
        if n == "0":                       # 완료시 장바구니를 출력하고 결제페이지로 넘어가는 조건문
            for e, f in select.items():
                print(e, f)
            bill()              # 결제페이지 함수
            return

        elif n == "1":         # 음료주문함수 실행 후 결제페이지로 이동하는 조건문
            select_drinkmenu()
            bill()
            return
        elif n == "2":
            select_sidemenu()   # 사이드주문함수로 실행 후 결제페이지로 이동하는 조건문
            bill()
            return
        else:
            print("다시입력해주세요.")
            continue

# 재료 주문과정
def ingredient_process():

    print("0.완료 1.버거재료 2.사이드재료 3.음료")
    s = input("번호를 입력하세요 : ")
    if s == "0":
        for k, v in select.items():
            print(k, v)
        return
    elif s == "1":
        select_ingredient()  # 재료고르기함수
        return
    elif s == "2":
        print("1.소금포함 2.취소")
        s = input("번호를 입력하세요 : ")
        if s == "1":
            burger_select_ingredients.append("소금포함")
            return
    elif s == "3":
        select_drinkmenu()
        return

# 재료 고르기 함수
def select_ingredient():
    print("야채를 골라주세요.")
    print()
    for i in range(len(vegitable)):
        print(vegitable[i])
    global burger_select_ingredients
    burger_select_ingredients.append(input(">>"))  # 재료리스트에 하나씩 담음
    clearscreen()

    print("소스를 골라주세요.")
    print()
    for i in range(len(source)):
        print(source[i])
    burger_select_ingredients.append(input(">>"))
    clearscreen()

    print("패티를 골라주세요.")
    print()
    for i in range(len(patty)):
        print(patty[i])
    burger_select_ingredients.append(input(">>"))
    clearscreen()
    print(burger_select_ingredients)
    return


# 카테고리 주문함수
def category():                            # 처음 카테고리 화면에서 실행되는 함수
    s2 = input("제품명을 입력해주세요.>>")
    if s2 == "음료":
        select_drinkmenu()
        burger_process()
        return
    elif s2 == "사이드":
        select_sidemenu()
        burger_process()
        return
    elif s2 == "디저트":
        select_dessertmenu()
        burger_process()
        return
    elif not s2.isdigit() and s2 in single_burger:      # 숫자가 아니고 single_burger에 포함되면 start함수를 실행하라.
        start(s2)
        return
    elif not s2 == "0" or not s2 == "1":
        print("다시 입력해주세요.")

#시작화면 일반버거 페이지
def page():                          # 페이지 나눔 및 버거주문과정으로 넘어가는 함수
    for i in range(7):          # 메뉴판을 7개씩만 출력하기 위한 for문

        print(menu_key_list[i] + " " + str(menu_values_list[i])) # 메뉴의 이름, 가격리스트를 합하여 출력
        if i == 6:
            print()                      # 7번째 메뉴가 출력이 됐을 때 실행하는 조건문
            n = input("이전은 0, 주문완료는 1, 다음페이지는 2, \n 주문하시려면 제품명을 입력하세요.")

            if n == "0":                  # 이전으로 이동하는 조건문
                break
            elif n == "1":                 # 주문완료시 주문내역 출력후 이전으로 이동하는 조건문
                if len(select) == 0:
                    print("주문내역이 없습니다.")        # 장바구니가 비어있다면 문장을 출력하는 조건문
                    break
                else:
                    for k, v in select.items():             # 장바구니에 메뉴가 담겨있을 시 하나씩 출력하는 for문
                        print(k, v)
                        break
            elif n == "2":             #다음페이지로 넘어가는 조건문
                clearscreen()
                print("|+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                print()
                for i in range(7, 14, 1):        # 7번째 메뉴부터 14번째 메뉴까지 출력하는 for문

                    print(menu_key_list[i] + " " + str(menu_values_list[i]))      # 메뉴의 이름과 가격리스트를 합하여 출력하는 문장
                    if i == 13:          # 14번째 메뉴가 출력됐을 시 밑에 문장을 실행하는 조건문
                        print()
                        n = input("이전은 0, 주문완료는 1, 다음페이지는 2, \n 주문하시려면 제품명을 입력하세요.")

                        if n == "0":        # 이전으로 돌아가는 조건문
                            break
                        elif n == "1":             # 주문완료시 주문내역 출력 후 이전으로 돌아가는 조건문
                            if len(select) == 0:
                                print("주문내역이 없습니다.")      # 장바구니가 비어있을 시 출력하는 조건문
                                break
                            else:
                                for k, v in select.items():        # 장바구니에 메뉴가 담겨있을 시 하나씩 출력하는 조건문
                                    print(k, v)
                                    break


                        elif n == "2":                                                 # 상동
                            clearscreen()
                            print("|+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                            print()
                            for i in range(14, 21, 1):
                                print(menu_key_list[i] + " " + str(menu_values_list[i]))
                                if i == 20:
                                    print()
                                    n = input("이전은 0, 주문완료는 1 \n 주문하시려면 제품명을 입력하세요.")

                                    if n == "0":
                                        break
                                    elif n == "1":
                                        if len(select) == 0:
                                            print("주문내역이 없습니다.")
                                            break
                                        else:
                                            for k, v in select.items():
                                                print(k, v)
                                                break
                                    elif not n.isdigit() and n in single_burger:
                                        start(n)
                        elif not n.isdigit() and n in single_burger:
                            start(n)
            elif not n.isdigit() and n in single_burger:
                start(n)


# 결제 과정 함수
def bill():
    global table_number
    while True:
        m = input(">> 0.완료 1.취소 2.메뉴변경 3.수량변경")
        if m == "0":  # 완료시
            clearscreen()

            # 테이블 서비스
            print("테이블 서비스를 받으시려면 1을, 아니면 0을 눌러주세요.")
            service_self = int(input(">>"))
            if service_self == 1:                                    # 테이블서비스 선택시 테이블서비스변수에 테이블서비스 입력후
                dict_table_service["서비스"] = "테이블서비스"           # 테이블 번호를 받는 과정을 나타내는 조건문
                print("테이블 번호를 입력해주세요.")
                table_number = int(input(">>"))
                # 영수증
                print("테이블 번호 " + str(table_number))
            elif service_self == 0:                                 # 셀프서비스 선택시 테이블서비스변수에 셀프서비스를 입력하는 조건문
                dict_table_service["서비스"] = "셀프서비스"

            # 영수증
            for i, j in print_inout.items():                        # 매장인지 포장인지 여부를 출력하는 for문
                print(i, j)
            for l, m in dict_table_service.items():                  # 테이블서비스 여부를 출력하는 for문
                print(l, m)
            for g, h in select.items():                               # 장바구니의 가격부분만을 합산하여 total변수에 대입하는, 합계를 계산하는 for문
                total["합계"] += h
            for x, y in select.items():                              # 장바구니변수를 하나씩 출력하는 for문
                print(x, y)
            for q, r in total.items():                               # 합계를 출력하는 for문
                print(q, r)

            # 결제페이지

            print("결제를 진행하시려면 0을, 취소는 1을 눌러주세요.")
            pay = input(">>")
            while True:
                if pay == "0":
                    money = input("현금 입력: ")
                    if money.isdigit() and total["합계"] > int(money):              # 숫자로 인식되며, 입력한 돈이 더 부족할 시 실행되는 조건문
                        print("금액이 부족합니다.")
                        continue

                    elif money.isdigit() and int(money) >= total["합계"]:          # 숫자로 인식되며, 돈이 충분할 시 결제페이지로 넘어가는 조건문

                        w = 0
                        payback = int(money) - total["합계"]                   # 입력한 돈에서 합계를 차감
                        # 영수증출력
                        print("테이블 번호 " + str(table_number))               # 테이블번호 출력하는 문장
                        for m, n in print_inout.items():
                            print(m, n)
                        for u, t in dict_table_service.items():
                            print(u, t)
                        for key, val in select.items():
                            print(key, val)
                        for e, h in total.items():
                            print(e, h)
                        print("거스름 돈: ", str(payback) + "원")
                        select.clear()
                        dict_table_service.clear()
                        print_inout.clear()
                        total["합계"] = 0
                        main()


                elif not money.isdigit():
                    print("잘못입력하셨습니다. 다시 입력해주세요.")   # 입력한 값이 숫자로 인식되지 않을 경우 출력하는 조건문
                    continue

                if pay == "1":                                # 취소 시 변수를 비우는 조건문
                    select.clear()
                    dict_table_service.clear()
                    print_inout.clear()
                    total["합계"] = 0
                    print("주문이 취소되었습니다.")
                    return
                return
        elif m == "1":
            select.clear()
            dict_table_service.clear()
            print_inout.clear()
            total["합계"] = 0
            print("주문이 취소되었습니다.")
            w = 0
            break
        elif m == "2":                                      # 메뉴변경
            m1 = input("변경할 메뉴를 입력해주세요. : ")
            del select[m1]
            print(" |+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
            for k, v in single_burger.items():
                print(" ", k, v)


            print("이전은 0, 주문완료는 1번을 눌러주세요.")
            s = input("카테고리 or 제품명을 입력하세요. : ")
            if s == "0":
                return
            elif s == "1":
                for ky, va in select.items():
                    print(ky, va)
                    return
            elif s == "음료":
                select_drinkmenu()
                burger_process()
                return
            elif s == "사이드":
                select_sidemenu()
                burger_process()
                return
            elif s == "디저트":
                select_dessertmenu()
                burger_process()
                return
            else:
                start(s)
                return
        elif m == "3":                                        # 수량변경
            m1 = input("변경할 메뉴를 입력해주세요.")
            amount = int(input("수량을 입력해주세요."))
            if m1 in select:

                select[m1] *= amount
                select[m1 + " " + str(amount) + "개"] = select.pop(m1)     # 키값변경 후 계산
                for a, b in select.items():
                    print(a, b)
                    continue
        else:
            clearscreen()
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            continue


# 키오스크 시작=========================================================================================================

def main():
    while True:

        in_out = (input("매장이면 0 ,포장이면 1을 눌러주세요: "))   # 식사를 매장에서 할것인지, 포장해서 가져갈 것인지 결정하는 조건문

        if in_out == "0":
            print_inout["식사장소"] = "매장"
        elif in_out == "1":
            print_inout["식사장소"] = "포장"
        elif not in_out.isdigit():
            print("다시 입력해주세요.")
            continue
        elif not in_out == "0" or in_out == "1":
            print("다시 입력해주세요.")
            continue
        print()

        # # 버거 메뉴 출력 / 프로그램실행
        while True:

            if ismac_lunch_time():  # 맥런치타임시 mac_lunch()함수 실행하는 조건문
                mac_lunch()
                # break
            # 일반주문시간

            if not ismac_lunch_time():   # 맥런치타임이 아닐시 실행하는 조건문
                print("|+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                print()
            page()
            break
        # break


main()