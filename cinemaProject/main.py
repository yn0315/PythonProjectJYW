import random
import theater
if __name__ == "__main__":
    number1 = random.randint(4, 20)
    number2 = random.randint(10, 20)
    num = random.randint(1, 3)
    # cinema_type = ""
    # if num == 1:
    #     cinema_type = "A"
    # elif num == 2:
    #     cinema_type = "B"
    # elif num == 3:
    #     cinema_type = "C"
    # print(cinema_type)

    cinema1 = theater.theater(number1, number2, "A")
    print("=====================================================")
    # cinema2 = theater.theater(number1, number2, "B")
    print("=====================================================")
    # cinema3 = theater.theater(number1, number2, "C")


