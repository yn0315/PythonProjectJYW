
class theater:
    number1 = 0 # 행갯수
    number2 = 0 # 열갯수
    seat_listA = [] # A관 자리배치변수
    seat_listB = [] # B관 자리배치변수

    def __init__(self, number1,number2, type):
        self.number1 = number1
        self.number2 = number2
        self.type = type # A관이냐 B관이냐

        # print(self.seat_list)

        # 이차원배열 만들기
        if self.type == "A":
            for i in range(0, number1):
                line_list = []
                for j in range(0, number2):
                    line_list.append(0)
                self.seat_listA.append(line_list)

            # 통로만들기 통로는 2 빈자리 0
            n = int(number2/3)
            for i in range(number1):
                self.seat_listA[i][n] = 2
                self.seat_listA[i][-n - 1] = 2

            # for i in self.seat_listA:
            #     print(i)

        elif self.type == "B":
            for i in range(0, number1):
                line_list = []
                for j in range(0, number2):
                    line_list.append(0)
                self.seat_listB.append(line_list)

            # 통로만들기
            n = int(number2 / 3)
            m = int(n / 2)
            for i in range(number1):

                self.seat_listB[i][n] = 2
                self.seat_listB[i][-n - 1] = 2

            # self.seat_list[0]행의 n 다음부터 -n 전까지 2 집어넣기
            for i in range(n + 1):
                self.seat_listB[0][n + i] = 2
                self.seat_listB[number1 - 1][i] = 2
                self.seat_listB[number1 - 1][- i - 1] = 2
            for i in range(m):
                self.seat_listB[number1- 2][i] = 2
                self.seat_listB[number1 - 2][- i - 1] = 2

            # for i in self.seat_listB:
            #     print(i)



        #
        # for i in theater.seat_listB:
        #     print(i)


#
#
# t= theater(10,20,"B")
#




