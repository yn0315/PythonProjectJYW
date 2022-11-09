# 221109_2

# 구문오류와 예외처리
# 프로세스가 예상치 못한 상황에 빠져 종료되는 것에 대비

# 오류의 종류
# 프로그램이 시작 전에 발생하는 오류 : 구문에러
# 프로그램이 돌다가 발생하는 오류 : 예외 or 런타임에러(네임에러같은거)

# 구문에러 : SyntaxError
# 예외 : exception
# 런타임에러 : runtime error

# 기본예외처리
# 1. 조건문을 사용하여 예외 처리
# 2. try 키워드를 이용한 예외 처리


# user_input_a = input("정수 입력: ")
#
# if user_input_a.isgigit():
#     number_input_a = int(user_input_a)
#
#     print("원의 반지름: ", number_input_a)
#     print("원의 둘레: ", 2 * 3.14 * number_input_a)
#     print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
# else:
#     print("정수를 입력하지 않았습니다.")


# try:
#   내가 실행하려는 모든 코드
#   예외상황발생 가능성이 있는
# except:
#   try 자식들이 실행되는 중 문제가 생기면
#   except로 진입한다.(에러 발생 시키지 않는다.)


user_input_a = input("정수 입력: ")

try:
    number_input_a = int(user_input_a)

    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2 * 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

# 368 예제

lista = ["52","273","32","스파이","103"]

list_num = []
for item in lista:
    try:
        float(item)
        list_num.append(item)
    except:
        pass
print("{}내부에 있는 숫자는".format(lista))
print("{}입니다.".format(list_num))



