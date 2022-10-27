import datetime

in_out = 0  # 식사장소 변수, 매장 = 0, 포장 = 1
# 세트선택 기본값: 감튀 + 탄산 = +1800
# 라지세트 기본값: 감튀 + 탄산 = +2400

single_burger = {"빅맥": 4900, "맥스파이시상하이버거": 4900, "1955버거": 6000,
                 "베이컨토마토디럭스": 5800, "맥크리스피디럭스": 6700,
                 "맥크리스피클래식": 5900, "맥치킨모짜렐라": 5000, "맥치킨": 5000,
                 "더블불고기버거": 4500, "에그불고기버거": 3500, "불고기버거": 2500,
                 "더블필레오피쉬": 5200, "필레오피쉬": 3700, "슈슈버거": 4700,
                 "슈비버거": 5800, "쿼터파운더치즈": 5500, "더블쿼터파운더치즈": 7400,
                 "트리플치즈버거": 5800, "더블치즈버거": 4500, "치즈버거": 2500, "햄버거" : 2200}  # 단품 햄버거 변수

set_burger = {"빅맥세트": 4900, "맥스파이시상하이버거세트": 4900, "1955버거세트": 6000,
                 "베이컨토마토디럭스세트": 5800, "맥크리스피디럭스세트": 6700,
                 "맥크리스피클래식세트": 5900, "맥치킨모짜렐라세트": 5000, "맥치킨세트": 5000,
                 "더블불고기버거세트": 4500, "에그불고기버거세트": 3500, "불고기버거세트": 2500,
                 "더블필레오피쉬세트": 5200, "필레오피쉬세트": 3700, "슈슈버거세트": 4700,
                 "슈비버거세트": 5800, "쿼터파운더치즈세트": 5500, "더블쿼터파운더치즈세트": 7400,
                 "트리플치즈버거세트": 5800, "더블치즈버거세트": 4500, "치즈버거세트": 2500, "햄버거세트" : 2200} # 변수 싱글버거 하나로 통일할 수 있는 방법...

large_set_burger = {"빅맥라지세트": 4900, "맥스파이시상하이버거라지세트": 4900, "1955버거라지세트": 6000,
                 "베이컨토마토디럭스라지세트": 5800, "맥크리스피디럭스라지세트": 6700,
                 "맥크리스피클래식라지세트": 5900, "맥치킨모짜렐라라지세트": 5000, "맥치킨라지세트": 5000,
                 "더블불고기버거라지세트": 4500, "에그불고기버거라지세트": 3500, "불고기버거라지세트": 2500,
                 "더블필레오피쉬라지세트": 5200, "필레오피쉬라지세트": 3700, "슈슈버거라지세트": 4700,
                 "슈비버거라지세트": 5800, "쿼터파운더치즈라지세트": 5500, "더블쿼터파운더치즈라지세트": 7400,
                 "트리플치즈버거라지세트": 5800, "더블치즈버거라지세트": 4500, "치즈버거라지세트": 2500, "햄버거라지세트" : 2200} # 세트햄버거 변수

mac = {"빅맥세트": 5200, "상하이버거세트": 5200, "1955버거세트": 6200, "베이컨토마토디럭스세트":6000}


# x = list(menu_all.keys()[1:][int(input("카테고리를 입력하세요 "))])
# print(x,"를 선택해서 메뉴는", menu_all[x])

drink = {"카페라떼": 3000, "아메리카노":2500, "바닐라라떼": 3500, "카푸치노": 3000, "에스프레소": 1700,
         "우유": 1500, "생수": 1200, "아이스드립커피": 1500, "탄산음료": 1500, "쉐이크": 2800}  # 음료 변수
side = {"맥너겟": 2200, "맥스파이시치킨텐더": 2700, "치즈스틱": 2500, "상하이치킨스낵랩": 2400,
        "치킨토마토스낵랩":2200, "후렌치후라이": 1800, "애플파이": 1300, "코울슬로": 1900}  # 사이드 메뉴 변수

dessert = {"맥플러리": 2700, "선데이아이스크림": 1800, "오레오아포가토": 3200, "아이스크림콘": 900, "초코콘": 1200}

menu_all = {"맥런치": mac,"버거": single_burger, "사이드": side, "음료":drink} #처음화면에 필요한 변수!!

vegitable = ["양상추", "양파", "오이피클","토마토"]
source = ["스위트 앤 사워", "스위트칠리", "케이준", "허니", "아라비아따"]
patty = ["소고기","닭고기","돼지고기"]  # 햄버거 재료 변수
burger_select_ingredients = [] # 햄버거 선택한재료  변수
side_ingredient = '소금'  # 사이드메뉴 재료변수


# 테이블 서비스 변수, 서비스 = 1, 셀프 = 0
service_self = 0
dict_table_service = {}
table_number = 0

print_inout = {} # 식사장소 영수증에서 프린트할 변수
select = {}# 장바구니 변수
global total
total = {"합계" : 0} # 합계변수
global w
w= 1
global x
x= 1
global y
y = 1
global z
z = 1
# global complete
# complete= False # 주문완료시 True 아직 아니면 False

# 화면 초기화
def clearscreen():
    for i in range(30):
        print()

# 시작
def start(s):
    while True:
        clearscreen()
        num = input("0.취소  1.단품  2.세트  3.라지세트 \n번호를 입력해주세요.>>")
        clearscreen()
        if num == "0":
            select.clear()  ######################################취소되면 첫페이지로 안감
            x = 0
            y = 0
            w = 0
            z = 0
            select.clear()
            dict_table_service.clear()
            print_inout.clear()
            total["합계"] = 0
            print("주문이 취소되었습니다.")
            break

        elif num == "1":
            select_burgermenu(s)
            burger_process()
        elif num == "2":
            select_burgermenu(s + "세트")
            burger_process()

        elif num == "3":
            select_burgermenu(s + "라지세트")
            burger_process()
        elif not num.isdigit():
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            continue
        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            continue
        break
    return

# 햄버거 주문과정 함수
def burger_process():
    global w
    while True:
        if w == 1:
            clearscreen()

            print("0.완료 1.음료 2.사이드메뉴 \n추가를 원하시면 번호를 누르세요.")
            n = (input(">>"))
            clearscreen()
            if n == "0":
                for e, f in select.items():
                    print(e, f)
                bill()
                w = 0
            elif n == "1":
                select_drinkmenu()
                bill()
                w = 0
                return
            elif n == "2":
                select_sidemenu()
                bill()
                w = 0
                return
            else:
                print("다시입력해주세요.")
                continue

# 결제 과정 함수
def bill():
    global w
    global x
    global table_number
    while w == 1:
        m = input(">> 0.완료 1.취소 2.메뉴변경 3.수량변경")
        if m == "0":  # 완료시
            clearscreen()

            # 테이블 서비스
            print("테이블 서비스를 받으시려면 1을, 아니면 0을 눌러주세요.")
            service_self = int(input(">>"))
            if service_self == 1:
                dict_table_service["서비스"] = "테이블서비스"
                print("테이블 번호를 입력해주세요.")
                table_number = int(input(">>"))
                # 영수증
                print("테이블 번호 " + str(table_number))
            elif service_self == 0:
                dict_table_service["서비스"] = "셀프서비스"

            # 영수증
            for i, j in print_inout.items():
                print(i, j)
            for l, m in dict_table_service.items():
                print(l, m)
            for g, h in select.items():
                total["합계"] += h
            for x, y in select.items():
                print(x, y)
            for q, r in total.items():
                print(q, r)

            # 결제페이지

            print("결제를 진행하시려면 0을, 취소는 1을 눌러주세요.")
            pay = input(">>")
            while True:
                if pay == "0":
                    money = input("현금 입력: ")
                    if money.isdigit() and total["합계"] > int(money):
                        print("금액이 부족합니다.")
                        continue

                    elif money.isdigit() and int(money) >= total["합계"]:

                        w = 0
                        payback = int(money) - total["합계"]
                        # 영수증출력
                        print("테이블 번호 " + str(table_number))
                        for m, n in print_inout.items():
                            print(m, n)
                        for u, t in dict_table_service.items():
                            print(u, t)
                        for key, val in select.items():
                            print(key, val)
                        for e, h in total.items():
                            print(e, h)
                        print("거스름 돈: ", str(payback) + "원")
                        w = 0
                        x = 0
                        return  ################################################################# 무한루프에 빠짐

                elif not money.isdigit():
                    print("잘못입력하셨습니다. 다시 입력해주세요.")
                    continue

                if pay == "1":
                    select.clear()
                    dict_table_service.clear()
                    print_inout.clear()
                    total["합계"] = 0
                    print("주문이 취소되었습니다.")
                    return
                return
        elif m == "1":
            select.clear()
            return
        elif m == "2":
            m1 = input("변경할 메뉴를 입력해주세요. : ")
            del select[m1]
            print(" |+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
            for k, v in single_burger.items():
                print(" ", k, v)


            if x ==1:
                if w == 1:
                    print("이전은 0, 주문완료는 1번을 눌러주세요.")
                    s = input("카테고리 or 제품명을 입력하세요. : ")
                    if s == "0":
                        return
                    elif s == "1":
                        for ky,va  in select.items():
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
        elif m == "3":
            m1 = input("변경할 메뉴를 입력해주세요.")
            amount = int(input("수량을 입력해주세요."))
            if m1 in select:

                select[m1] *= amount
                select[m1 + " " + str(amount) + "개"] = select.pop(m1)
                for a,b in select.items():
                    print(a,b)
                    continue
        else:
            clearscreen()
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            continue

# 맥런치타임인지 판별하는 함수
def ismac_lunch_time():
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    if 10 <= h < 11:
        if h == 10:
            if 30 <= m:
                return True
        else:
            return True

# 맥런치 타임시 주문
def mac_lunch():
    global w
    global x
    while w == 1:
        print("|+맥런치+| 버거 | 음료 | 사이드 | 디저트 | 이전 | 주문완료 |  ")
        print()
        for c,d  in mac.items():
            print(" ", c, d)
        if w == 1:
            if x == 1:
                print("이전은 0, 주문완료는 1번을 눌러주세요.")
                s = input("카테고리 or 제품명을 입력하세요. : ")

                if s in mac:
                    select[s] = mac[s]
                    burger_process()
                    ingredient_process()
                    w = 0
                    break
                elif s == "0":
                    return
                elif s == "1":

                    for k, v in select.items():
                        print(k, v)
                        w == 0
                        break
            elif s == "버거":
                print("| 맥치킨 |+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                print()
            for k, v in single_burger.items():
                if x == 1:
                    print(" ", k, v)
                    if k == "맥치킨":
                        print("이전은 0, 주문완료는 1번을 눌러주세요. 다음페이지는 엔터를 눌러주세요.")
                        s1 = input("카테고리 or 제품명을 입력하세요. : ")

                        if s1 == "":
                            clearscreen()
                            print("|+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                            continue
                            category()
                        elif s1 == "0":
                            x = 0
                            break
                        elif s1 == "1":
                            if len(select) == 0:
                                print("주문내역이 없습니다.")
                                x = 0
                                w = 0
                                break
                            for k, v in select.items():
                                print(k, v)
                        elif s1 == "음료":
                            select_drinkmenu()
                            burger_process()
                            break
                        elif s1 == "사이드":
                            select_sidemenu()
                            burger_process()
                            break
                        elif s1 == "디저트":
                            select_dessertmenu()
                            burger_process()
                            break
                        elif not s1.isdigit() and s1 in single_burger:
                            start(s1)
                            break
                        elif not s1 == "0" or not s1 == "1":
                            print("다시 입력해주세요.")
                            break
                    elif k == "슈비버거":
                        print("이전은 0, 주문완료는 1번을 눌러주세요.")
                        s1 = input("카테고리 or 제품명을 입력하세요. : ")

                        if s1 == "":
                            clearscreen()
                            print(" |+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                            continue
                            x = 0
                        elif s1 == "0":
                            break
                        elif s1 == "1":
                            for k, v in select.items():
                                print(k, v)
                                break

                        elif s1 == "음료":
                            select_drinkmenu()
                            burger_process()
                            break
                        elif s1 == "사이드":
                            select_sidemenu()
                            burger_process()
                            break
                        elif s1 == "디저트":
                            select_dessertmenu()
                            burger_process()
                            break
                        elif not s1.isdigit() and s1 in single_burger:
                            start(s1)
                            break
                        elif not s1 == "0" or not s1 == "1":
                            print("다시 입력해주세요.")
                            break
            if x == 1:
                if w == 1:
                    category()
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
            elif not s1.isdigit() and s1 in single_burger:
                start(s1)
                break


# 버거 주문(단품/세트/라지세트) 함수
def select_burgermenu(sel):
    while True:
        global burger_select_ingredients

        if sel in single_burger:                                    # 단품
            select[sel] = single_burger[sel]
            ingredient_process()
            return

        elif sel in set_burger:                                     # 세트
            select[sel] = set_burger[sel] + 1800
            ingredient_process()
            return

        elif sel in large_set_burger:                               # 라지세트
            select[sel] = large_set_burger[sel] + 2400
            ingredient_process()
            return


# 음료주문 함수
def select_drinkmenu():
    global x
    while x == 1:
        clearscreen()
        print("| 버거 |+음료+| 사이드 | 디저트 | 이전 | 주문완료 |  ")
        print()
        for k, v in drink.items():
            print(k,v)
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
    while x == 1:
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
    while x == 1:
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

# 재료 주문과정
def ingredient_process():
    while w == 1:
        print("0.완료 1.버거재료 2.사이드재료 3.음료")
        s = input("번호를 입력하세요 : ")
        if s == "0":
            for k, v in select.items():
                print(k, v)
            break # 리턴이었음
        elif s == "1":
            select_ingredient()                                         # 재료고르기

        elif s == "2":
            print("1.소금포함 2.취소")
            s = input("번호를 입력하세요 : ")
            if s == "1":
                burger_select_ingredients.append("소금포함")
        elif s == "3":
            select_drinkmenu()


# 재료 고르기 함수
def select_ingredient():

    print("야채를 골라주세요.")
    print()
    for i in range(len(vegitable)):
        print(vegitable[i])
    global burger_select_ingredients
    burger_select_ingredients.append(input(">>"))
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
def category():
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
    elif not s2.isdigit() and s2 in single_burger:
        start(s2)
        return
    elif not s2 == "0" or not s2 == "1":
        print("다시 입력해주세요.")


# 키오스크 시작=========================================================================================================

while True:

    in_out = (input("매장이면 0 ,포장이면 1을 눌러주세요: "))

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

        w = 1
        x = 1
        if ismac_lunch_time():
            mac_lunch()

        if w == 1:
            # 일반주문시간

            if not ismac_lunch_time():
                print("|+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                print()

            for k, v in single_burger.items():

                if x == 1:
                    print(" ", k, v)
                    if k =="맥치킨":
                        print("이전은 0, 주문완료는 1번을 눌러주세요. 다음페이지는 엔터를 눌러주세요.")
                        s1 = input("카테고리 or 제품명을 입력하세요. : ")

                        if s1 == "":
                            clearscreen()
                            print("|+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                            continue
                            category()
                        elif s1 == "0":
                            x = 0
                            break
                        elif s1 == "1":
                            if len(select) == 0:
                                print("주문내역이 없습니다.")
                                x = 0
                                w = 0
                                break
                            for k, v in select.items():
                                print(k, v)
                        elif s1 == "음료":
                            select_drinkmenu()
                            burger_process()
                            break
                        elif s1 == "사이드":
                            select_sidemenu()
                            burger_process()
                            break
                        elif s1 == "디저트":
                            select_dessertmenu()
                            burger_process()
                            break
                        elif not s1.isdigit() and s1 in single_burger:
                            start(s1)
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                    elif k =="슈비버거":
                        print("이전은 0, 주문완료는 1번을 눌러주세요.")
                        s1= input("카테고리 or 제품명을 입력하세요. : ")

                        if s1 == "":
                            clearscreen()
                            print(" |+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                            continue
                            x = 0
                        elif s1 == "0":
                            break
                        elif s1 == "1":
                            for k, v in select.items():
                                print(k, v)
                                break

                        elif s1 == "음료":
                            select_drinkmenu()
                            burger_process()
                            break
                        elif s1 == "사이드":
                            select_sidemenu()
                            burger_process()
                            break
                        elif s1 == "디저트":
                            select_dessertmenu()
                            burger_process()
                            break
                        elif not s1.isdigit() and s1 in single_burger:
                            start(s1)
                            break
                        else:
                            print("다시 입력해주세요.")
                            break
                        break


            if y == 1:
                category()
                break
                clearscreen()
                print(" |+버거+| 음료 | 사이드| 디저트 | 이전 | 주문완료 |  ")
                print("이전은 0, 주문완료는 1번을 눌러주세요.")
                s = input("카테고리 or 제품명을 입력하세요. : ")
                if s == "0":
                    break
                elif s == "1":
                    if len(select) == 0:
                        print("주문내역이 없습니다.")
                    for k, v in select.items():
                        print(k, v)
                        x = 0
                        w = 0
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
                elif s in single_burger:
                    z == 0
                    category()
                    break
                else:
                    clearscreen()
                    print("다시 입력해주세요.")
                    break


        break
        # 기본카테고리 디폴트 페이지 설정해주고
        # 맥런치 시간에는 맥런치를 디폴트로
        # 그 외 시간에는 버거페이지를 디폴트로
        # input("카테고리 목록 + 지금 활성화된 카테고리 메뉴, 이전버튼+ 주문완료(비활성화), 장바구니리스트, 취소")
        # 카테고리 목록변경 입력1(번)하면 목록 바뀌고 카테고리메뉴도 바뀌고 나머지 버튼 똑같이
        # 처음 3줄 프린트하고 2줄씩 더보기하면? 더보기 완료

        # 이전은 바로 전페이지 취소는 완전 처음화면으로 감

