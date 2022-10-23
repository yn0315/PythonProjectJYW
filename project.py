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
                 "트리플치즈버거세트": 5800, "더블치즈버거세트": 4500, "치즈버거세트": 2500, "햄버거세트" : 2200}

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


# 테이블 서비스 변수, 서비스 = 0, 셀프 = 1
service_self = 0

select = {}  # 장바구니 변수

# 화면 초기화
def clear():
    for i in range(30):
        print()

# 버거 주문(단품/세트/라지세트) 함수//int로 바꾸고 전부 다 번호로 받아버리면??훨씬 편할듯
def select_burgermenu(sel):
    if sel in single_burger:
        select[sel] = single_burger[sel]
        select_ingredient()  # 재료고르기
    elif sel in set_burger:
        select_ingredient()
        select[sel] = set_burger[sel]+1800
    elif sel in large_set_burger:
        select[sel] = large_set_burger[sel]+2400
        select_ingredient()
    print(select)

# 버거주문시작
def start(s):

    num = int(input("""
    0. 취소
    1. 단품
    2. 세트
    3. 라지세트
    번호를 입력해주세요.>>
    """))
    clear()
    if num == 0:
        pass
    elif num == 1:
        select_burgermenu(s)
        clear()
        print("0.완료 1.음료 2.사이드메뉴 \n추가를 원하시면 번호를 누르세요.")
        n = int(input(">>"))
        clear()
        if n == 0:
            print(select)
        elif n == 1:
            select_drinkmenu()

        elif n == 2:
            select_sidemenu()


    elif num == 2:
        select_burgermenu(s+"세트")
        clear()
        select_sidemenu()
        clear()
        select["감자튀김"] = 0
        select["콜라"] = 0
        print("0.완료 1.음료 2.사이드메뉴 \n추가를 원하시면 번호를 누르세요.")
        n = int(input(">>"))
        clear()
        if n == 0:
            print(select)
        elif n == 1:
            del select["콜라"]
            select_drinkmenu()

        elif n == 2:
            select_sidemenu()



    elif num == 3:
        select_burgermenu(s+"라지세트")
        clear()
        select_sidemenu()
        clear()
        select["감자튀김"] = 0
        select["콜라"] = 0
        print("0.완료 1.음료 2.사이드메뉴 \n추가를 원하시면 번호를 누르세요.")
        n = int(input(">>"))
        clear()
        if n == 0:
            for k,v in select.items():
                print(k,v)
        elif n == 1:
            del select["콜라"]
            select_drinkmenu()

        elif n == 2:
            select_sidemenu()





# 재료 고르기 함수
def select_ingredient():
    print("야채를 골라주세요.")
    print()
    for i in range(len(vegitable)):
        print(vegitable[i])
    global burger_select_ingredients
    burger_select_ingredients.append(input(">>"))
    clear()

    print("소스를 골라주세요.")
    print()
    for i in range(len(source)):
        print(source[i])
    burger_select_ingredients.append(input(">>"))
    clear()

    print("패티를 골라주세요.")
    print()
    for i in range(len(patty)):
        print(patty[i])
    burger_select_ingredients.append(input(">>"))
    clear()
    print(burger_select_ingredients)


# 사이드메뉴 주문함수
def select_sidemenu():
    print("사이드메뉴를 골라주세요")
    print()
    for k, v in side.items():
        print(k, v)
    s = input(">>")
    clear()
    if s in side:
        select[s] = side[s]
    for k, v in select.items():
        print(k, v)

# 음료주문 함수
def select_drinkmenu():
    print("음료를 골라주세요")
    for k, v in drink.items():
        print(k,v)
    beverage = input(">>")
    clear()

    if beverage in drink:
        select[beverage] = drink[beverage]  # 음료 장바구니에 집어넣기
    for k, v in select.items():
        print(k, v)

# 맥런치 타임시 주문
def mac_lunch():
    print(" |+맥런치+| 버거 | 이전 | 주문완료 |  ")
    print()
    for k, v in mac.items():
        print(" ",k, v)
    b = input(" >>제품명을 입력하세요. : ")
    clear()
    if b =="버거":
        clear()
        print(" | 맥런치 |+버거+| 이전 | 주문완료 |  ")
        default_print_burger()
        start(b)

    elif b in mac:
        select_ingredient()
        clear()
        select[b] = mac[b]
        select_sidemenu()
        clear()
        select["감자튀김"] = 0
        select["콜라"] = 0

    for k,v in select.items():
        print(k,v)

# 버거 정렬 & 출력
def default_print_burger():

    print()
    for k, v in single_burger.items():
        if k == "맥치킨":
            s = input(" >> 제품명을 입력하세요. 이전은 0, 주문완료는 1\n    더보기를 원하시면 엔터를 눌러주세요. : ")
            if s == "0":
                break
            elif s == "":
                print(" ", k, v)
            elif s == "1":
                if len(select) < 1:
                    print("주문내역이 없습니다.")
                    break
                else:
                    for k, v in select.items():
                        print(k, v)
            elif not s.isdigit():
                start(s)
                break

        elif k == "슈비버거":
            s = input(" >> 더보기를 원하시면 엔터를 눌러주세요. : ")
            if s == "":
                print(" ", k, v)

            elif not s.isdigit():
                start(s)
                break
        else:
            print(" ", k, v)

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
 # 10:30 ~ 2시는 맥런치타임

while True:

    in_out = int(input("매장이면 0 ,포장이면 1을 눌러주세요: "))
    print()
    # 맥런치타임
    if ismac_lunch_time():
        mac_lunch()

    # 일반주문시간
    elif not ismac_lunch_time():
        print(" |+버거+| 이전 | 주문완료 |  ")
        print()

        # 버거 메뉴 출력
        for k, v in single_burger.items():
            default_print_burger()
            break


        # 1번 프레임 끝

        # 기본카테고리 디폴트 페이지 설정해주고
        # 맥런치 시간에는 맥런치를 디폴트로
        # 그 외 시간에는 버거페이지를 디폴트로
        # input("카테고리 목록 + 지금 활성화된 카테고리 메뉴, 이전버튼+ 주문완료(비활성화), 장바구니리스트, 취소")
        # 카테고리 목록변경 입력1(번)하면 목록 바뀌고 카테고리메뉴도 바뀌고 나머지 버튼 똑같이
        # 처음 3줄 프린트하고 2줄씩 더보기하면? 더보기 완료

        # 이전은 바로 전페이지 취소는 완전 처음화면으로 감
