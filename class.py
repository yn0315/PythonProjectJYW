import time
import random
from threading import Timer

class Auction:
    def __init__(self):
        self.s_a = ["신발", "시계", "대본", "OMEGA 빈티지 남성시계", "신호등", "선글라스", "조커 피규어", "사인볼"]
        self.a_a = ["조선초기 분청사기", "청자흑백상감화조두문주병", "금추 이남호 서생의 고사 인물도", "청화백자 팔각주병", "백자주병"]
        self.b_a = ["교지", "1학년 독서교실 10권 세트", "배달의 별", "동의사상신편", "종보백병변종록", "원피스 만화책"]
        self.h_a = ["보드", "골프채", "미싱기계", "농구 카드", "와인", "레고"]
        self.u_a = ["커피도구", "YAZOLE 남성요 검정가죽 손목시계", "은수저 세트", "스피커", "LG 플립 휴대폰"]
        self.all_products = {"스타의 애장품": self.s_a, "미술품": self.a_a, "도서": self.b_a, "취미/수집": self.h_a, "중고생활용품": self.u_a}
        self.basket = " "  #경매물품 장바구니
        self.price = [1000, 10000, 50000, 10000, 500000, 10000, 10000]  #시작가 리스트
        self.list1 = list(self.all_products.keys())  #all_products의 key만 리스트
        self.list2 = list(self.all_products.values())  #all_products의 value만 리스트
        self.player_dict = {}
        self.total_list = []
        self.n = (range(100))
        self.timeout = 6

    def Welcome(self):
        acting = True
        while acting:
            print("※ 파이썬 경매 사이트에 오신 걸 환영합니다 ※")
            ask = input("경매 사이트를 둘러보시겠습니까? (y/n) ")
            if ask == "y":
                pass
                acting = False
            else:
                Auction.Welcome(self)
                acting = False


    def Product_menu(self):
        i = 0
        try:
            while i < len((self.all_products.keys())):
                for j in self.all_products.keys():
                    print(i,".", j)
                    i += 1
            self.ask1 = int(input("원하는 카테고리를 선택하시오 : "))

            i = 0
            while i < len(self.all_products.values()):
                if self.list1[self.ask1] :
                    for j in self.list2[self.ask1]:
                        print(i, ".", j)
                        i += 1
            self.ask2 = int(input("원하는 카테고리를 선택하시오 : "))
            time.sleep(1)
            print()
        except:
            print()
            print("해당되지 않는 번호를 선택하셨습니다.", end="\n")
            print()
            at.Product_menu()

    def Basket(self):
        acting = True
        while acting:
            if self.ask2 in range(0, len(self.list2[self.ask1])):
                self.basket = self.basket.replace(" ",str(list(self.list2)[self.ask1][self.ask2]))
                print(f"{self.basket}의 경매에 응하셨습니다")
                print()
                time.sleep(1.5)
                acting = False
            else:
                print("해당되지 않는 번호를 선택하셨습니다.", end="\n")
                print()
                Auction.Product_menu(self)
                acting = True

    def Price(self):
        self.start_prince = random.choice(self.price)
        self.present_price = self.start_prince
        self.bidding_unit = random.choice(self.price[0:2])
        if self.start_prince == 1000:
            self.bidding_unit = 1000

    def Auction_Start(self):
        print("경매를 시작하겠습니다")
        time.sleep(2)
        print(f"『{self.basket}』 입찰을 시작합니다")
        time.sleep(3)
        print(f"<시작가 {self.start_prince}>, <입찰단위 {self.bidding_unit}>부터 시작합니다")

    def Data(self):
        self.name = input("성함을 입력해 주세요 : ")
        self.bidding_price = int(input("입찰 가격을 입력해 주세요: "))
        print()
        self.player_dict[self.name] = self.bidding_price
        if self.bidding_price >= self.present_price:
            if self.bidding_price % self.bidding_unit == 0:
                self.present_price = self.bidding_price
            else:
                print("입찰단위를 확인해 주세요")
                print()
                Auction.Data(self)
        else:
            print("진행 중인 입찰가보다 더 낮은 금액을 제시하셨습니다")
            print()
            Auction.Data(self)

        # self.total_list.append(self.player_dict)

    def Extra_player(self):
        acting = True
        # self.timeout = 10
        while acting:
            question = str("더 응찰하실 분 계십니까? (y/n)")
            self.timeout = 10
            answer = input(question)
            self.t = Timer(self.timeout, print, ["더 이상 입찰자 안 계시면 카운트하겠습니다"])
            self.t.start()
            self.t.cancel()
            if answer == "y":
                print()
                Auction.Data(self)
            else:
                acting = False
        # self.timeout = 10
        # self.t = Timer(self.timeout, print, ["더 이상 입찰자 안 계시면 카운트하겠습니다"])
        # self.t.start()
        # self.t.cancel()


    def Result(self):
        time.sleep(2)
        print("\r3!!", end="")
        time.sleep(3)
        print("\r2!!!!", end="")
        time.sleep(3)
        print("\r1!!!!", end="\n")
        time.sleep(2)
        print("경매가 종료되었습니다")
        print()
        time.sleep(3)
        print(f"낙찰자 : {max(self.player_dict.keys())}")
        print(f"낙찰 금액 : {max(self.player_dict.values())}")







at=Auction()
at.Welcome()
at.Product_menu()
at.Basket()
at.Price()
at.Auction_Start()
at.Data()
at.Extra_player()
at.Result()










