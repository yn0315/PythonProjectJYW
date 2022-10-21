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

large_set_burger = {"빅맥세트": 4900, "맥스파이시상하이버거세트": 4900, "1955버거세트": 6000,
                 "베이컨토마토디럭스세트": 5800, "맥크리스피디럭스세트": 6700,
                 "맥크리스피클래식세트": 5900, "맥치킨모짜렐라세트": 5000, "맥치킨세트": 5000,
                 "더블불고기버거세트": 4500, "에그불고기버거세트": 3500, "불고기버거세트": 2500,
                 "더블필레오피쉬세트": 5200, "필레오피쉬세트": 3700, "슈슈버거세트": 4700,
                 "슈비버거세트": 5800, "쿼터파운더치즈세트": 5500, "더블쿼터파운더치즈세트": 7400,
                 "트리플치즈버거세트": 5800, "더블치즈버거세트": 4500, "치즈버거세트": 2500, "햄버거세트" : 2200} # 세트햄버거 변수

mac_lunch = {"빅맥세트": 5200, "상하이버거세트": 5200, "1955버거세트": 6200, "베이컨토마토디럭스세트":6000}


# x = list(menu_all.keys()[1:][int(input("카테고리를 입력하세요 "))])
# print(x,"를 선택해서 메뉴는", menu_all[x])

drink = {"카페라떼": 3000, "아메리카노":2500, "바닐라라떼": 3500, "카푸치노": 3000, "에스프레소": 1700,
         "우유": 1500, "생수": 1200, "아이스드립커피": 1500, "탄산음료": 1500, "쉐이크": 2800}  # 음료 변수
side = {"맥너겟": 2200, "맥스파이시치킨텐더": 2700, "치즈스틱": 2500, "상하이치킨스낵랩": 2400,
        "치킨토마토스낵랩":2200, "후렌치후라이": 1800, "애플파이": 1300, "코울슬로": 1900}  # 사이드 메뉴 변수

dessert = {"맥플러리": 2700, "선데이아이스크림": 1800, "오레오아포가토": 3200, "아이스크림콘": 900, "초코콘": 1200}

menu_all = {"맥런치": mac_lunch,"버거": single_burger, "사이드": side, "음료":drink} #처음화면에 필요한 변수!!

vegitable = ["양상추", "양파", "오이피클","토마토"]
source = ["스위트 앤 사워", "스위트칠리", "케이준", "허니", "아라비아따"]
patty = ["소고기","닭고기","돼지고기"]  # 햄버거 재료 변수
burger_select_ingredients = [] # 햄버거 선택한재료  변수
side_ingredient = '소금'  # 사이드메뉴 재료변수


# 테이블 서비스 변수, 서비스 = 0, 셀프 = 1
service_self = 0

select = {}  # 장바구니 변수

# 버거 주문(단품/세트/라지세트) 함수
def select_burgermenu(burger):
    print(burger)
    sel = input("제품을 골라주세요: ")
    if sel in burger:
        select[sel] = burger[sel]
        select_ingredient() # 재료고르기
    print(select)


# 재료 고르기 함수
def select_ingredient():
    print("야채를 골라주세요.")
    print(vegitable)
    global burger_select_ingredients
    burger_select_ingredients.append(input(">>"))

    print("소스를 골라주세요.")
    print(source)
    burger_select_ingredients.append(input(">>"))

    print("패티를 골라주세요.")
    print(patty)
    burger_select_ingredients.append(input(">>"))
    print(burger_select_ingredients)

# 사이드메뉴 주문함수
def select_sidemenu():
    print("사이드메뉴를 골라주세요")
    print(side)
    s = input(">>")
    if s in side:
        select[s] = side[s]
        print(select)

# 음료주문 함수
def select_drinkmenu():
    print("음료를 골라주세요")
    print(drink)
    beverage = input(">>")
    if beverage in drink:
        select[beverage] = drink[beverage]  # 음료 장바구니에 집어넣기
        print(select)

def mac_lunch():
    print("맥런치타임입니다.")



while True:
    # #지금이 맥런치 시간인가 아닌가를 먼저 판별해야함
    # if datetime.datetime.hour > 15 and datetime.time.hour < 17:
    #     if datetime.datetime.hour == 10: #10라면
    #         if datetime.datetime.minute >= 30: # 30분 이상인가?
    #             mac_lunch()



    in_out = int(input("매장이면 0 ,포장이면 1을 눌러주세요: "))
    # 1번 프레임 끝

    # 기본카테고리 디폴트 페이지 설정해주고
    # 맥런치 시간에는 맥런치를 디폴트로
    # 그 외 시간에는 버거페이지를 디폴트로
    input("카테고리 목록 + 지금 활성화된 카테고리 메뉴, 이전버튼+ 주문완료(비활성화), 장바구니리스트, 취소")
    # 카테고리 목록변경 입력1(번)하면 목록 바뀌고 카테고리메뉴도 바뀌고 나머지 버튼 똑같이


    # 이전은 바로 전페이지 취소는 완전 처음화면으로 감
    num = input("""
    0. 이전
    1. 카테고리정보
      A.메뉴(버거페이지)
    2. 완료
    번호를 입력해주세요. >>
    """)
    if num == 0:
        break
    elif num == 1:
        category = int(input("""
    0. 취소
    1. 햄버거
    2. 음료
    3. 사이드메뉴
    번호를 입력해주세요.>>
        """))
        if category == 0:
            break
        elif category == 1:
            set = int(input("""
    0. 취소
    1. 단품
    2. 세트
    3. 라지세트
    번호를 입력해주세요.>>
            """))
            if set == 0:
                break
            elif set == 1:
                select_burgermenu(single_burger)
                print("0.완료 1.음료 2.사이드메뉴 \n추가를 원하시면 번호를 누르세요.")
                n = int(input(">>"))
                if n == 0:
                    print("주문을 완료하고 결제페이지로 이동합니다.")
                elif n == 1:
                    select_drinkmenu()
                elif n ==2:
                    select_sidemenu()

            elif set == 2:
                select_burgermenu(set_burger)
                #사이드메뉴먼저
                select_drinkmenu()

            elif set == 3:
                select_burgermenu(large_set_burger)
                #사이드메뉴먼저
                select_drinkmenu()


    elif num == 2:
        if len(select) >= 1:
            print("결제하기 화면으로 넘어갑니다.")

    break
