class theater:
    number1 = 0
    number2 = 0
    seat_list = []

    def __init__(self, number1,number2, type):
        self.number1 = number1
        self.number2 = number2
        self.type = type

        # print(self.seat_list)
        # 이차원배열 만들기
        for i in range(0, number1):
            line_list = []
            for j in range(0,number2):
                line_list.append(0)
            self.seat_list.append(line_list)
            
        if self.type == "A":
            # 통로만들기
            n = int(number2/3)
            for i in range(number1):
                self.seat_list[i][n] = 2
                self.seat_list[i][-n - 1] = 2

        elif self.type == "B":
            # 통로만들기
            n = int(number2 / 3)
            m = int(n / 2)
            for i in range(number1):

                self.seat_list[i][n] = 2
                self.seat_list[i][-n - 1] = 2

            # self.seat_list[0]행의 n 다음부터 -n 전까지 2 집어넣기
            for i in range(n + 1):
                self.seat_list[0][n + i] = 2
                self.seat_list[number1 - 1][i] = 2
                self.seat_list[number1 - 1][- i - 1] = 2
            for i in range(m):
                self.seat_list[number1- 2][i] = 2
                self.seat_list[number1 - 2][- i - 1] = 2

        elif self.type == "C":
            # 보류
            # 통로만들기
            n = int(number2 / 3)
            m = int(n / 2)
            for i in range(number1):

                self.seat_list[i][n] = 2
                self.seat_list[i][-n - 1] = 2


            # self.seat_list[0]행의 n 다음부터 -n 전까지 2 집어넣기
            for i in range(n + 1):
                self.seat_list[0][n + i] = 2
                self.seat_list[number1 - 1][i] = 2
                self.seat_list[number1 - 1][- i - 1] = 2
            for i in range(m):
                self.seat_list[number1 - 2][i] = 2
                self.seat_list[number1 - 2][- i - 1] = 2


        for i in theater.seat_list:
            print(i)


#
#
t= theater(10,20,"C")
#




