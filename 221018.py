# 221018
# 함수

# 키워드 매개변수
# 가변과 기본을 같이 써도 되나?
# 가변과 기본이 둘 다 있으면 가변에 주어진 값들이 어디서 끝인지 알 수 있는 방법?

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요","즐거운","파이썬 프로그래밍", 3)

# 가변과 기본 구분을 위해 키워드 매개변수 사용
print_n_times("안녕하세요","즐거운","파이썬 프로그래밍", n = 3)
# 기본 매개변수에 들어갈 값에 매개변수명 = 값 형태로 지정해야한다.

print("안녕하세요", end=" ") # end=의 기본값은 줄바꿈인데 공백으로 바꾸면 줄바꿈안되고 띄어쓰기됨
print("111111", end="@")
print("2222", end="\t")
print("2222", end="##############\n")

# 리스트 정렬 sort()
# 리스트.sort()
# 오름차순으로 정렬한다.
listb = [4,2,1,7,9,6]
# print(listb.sort()) # sort는 리턴값이 없는 함수라서 None이 뜸
listb.sort(reverse=False) # 리버스의 기본값은 False로 지정돼있다
print(listb)

# 기본매개변수 중 필요한 값만 입력하기
# def test(*a, b =10,c=100):
#     #print(a+b+c) # a가 튜플 데이터가 됨
#     print(a)
#     print(b)
#     print(c)
#
# test(10,20,30, b=200) # 오류남

def test(a, b=10, c=100):
    print(a+b+c)
# 기본형태
test(10,20,30)

# 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10,b=100,c=200)

# 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10,a=100,b=200)

# 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)

# return
# 반환한다

# user = input("값:")
#
# print(user)

# return은 함수 내부 정의할 때 return 키워드를 통해 return(반환)할 대상을 지정할 수 있다.
# return만 써있으면 반환값이 없다. (None)
# return 키워드는 함수에서 탈출을 뜻함
def return_test():
    print("abc")
    return 100
    print("def")

x = return_test()
print(x)

# 매개변수가 없는 함수
# 매개변수 있는 함수
# 일반/가변/기본
# 일반, 가변: 필수 입력
# 기본 : 입력 선택사항


# 리턴이 없는 함수 : 굳이 안 만들어도 되는 함수가 대부분
# 리턴이 있는 함수

# 리턴만 있는 경우 : 탈출
# 리턴 뒤에 값이 있는 경우 : 탈출과 값의 반환을 동시에 한다.

def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i

    return output

print("0, to 100: ", sum_all(0,100))
print("0, to 1000: ", sum_all(0,1000))
print("50, to 100: ", sum_all(50,100))
print("500, to 1000: ", sum_all(500,1000))

# 기본매개변수로만 작성해도 된다.
def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i

    return output

print("A", sum_all(0,100,10))
print("B", sum_all(end = 100))
print("C", sum_all(end = 100, step = 2))
print("D", sum_all())


def mul(*values):
    m = 1
    for i in values:
        m *= i
    return m

print(mul(5,7,9,10))


# 292
# 재귀함수
# 팩토리얼
# n! = n*(n - 1) * (n - 2)*...*1

# 반복문으로 팩토리얼 구하기
# 재귀함수로 팩토리얼 구하기

def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1!: ", factorial(1))
print("2!: ", factorial(2))
print("3!: ", factorial(3))
print("4!: ", factorial(4))
print("5!: ", factorial(5))

def factorial(n):
    if n == 0:
        print("1을 리턴한다.")
        return 1 # 목적지가 바로 아래에 있는 else에 써 있는 이전 재귀함수 호출문
    else:
        print(n)
        return n *factorial(n - 1)

print("1!: ", factorial(1))
print("2!: ", factorial(2))
print("3!: ", factorial(3))
print("4!: ", factorial(4))
print("5!: ", factorial(5))

# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n ==2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# print("fibonacci(1): ", fibonacci(1))
# print("fibonacci(2): ", fibonacci(2))
# print("fibonacci(3): ", fibonacci(3))
# print("fibonacci(4): ", fibonacci(4))
# print("fibonacci(5): ", fibonacci(5))

counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter # globel 전역변수임을 알리는 것, 그 이후 함수 안에 나오는 건 다 전역이다
    # 전역변수는 global을 써야 지역에서 참조할 수 있다.
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(20)
print("-----------------------")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {} 번입니다.".format(counter))

# 메모화
# 재귀함수의 반복적인 연산을 하는 문제를 해결하기 위해
# 같은 값은 한번만 계산하도록 코드를 수정하는 것

dictionary = {
    1 : 1,
    2 : 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

print("fibonacci(10) : ", fibonacci(10))
print("fibonacci(20) : ", fibonacci(20))
print("fibonacci(30) : ", fibonacci(30))
print("fibonacci(40) : ", fibonacci(40))
print("fibonacci(50) : ", fibonacci(50))

# 조기 리턴 -> 탈출
# 함수에는 읽히는 리턴은 하나만 와야한다.

# 재귀함수 활용한 리스트평탄화

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1,2,3], [4,[5,6]], 7, [8,9]]
print("원본: ", example)
print("변환: ", flatten(example))

"=================재귀함수문제 ===================="

min = 2
max = 10
total = 100
memo = {}
def sit(stand, seat):
    cnt = 0
    key = str([stand, seat])
    # 종료조건
    if key in memo:
        return memo[key]
    if stand < 0:
        return 0
    if stand == 0:
        cnt += 1
        return 1

    # 재귀처리
    #100명을 최소값부터 나누고, 나머지가 1이면 남은 사람들을 하나 많은 수로 나눔 10명까지 반복  나머지가 0이면 cnt 하나씩 올림???
    # key[0] = str(total % sit) # 남아있는 사람
    # key[1] = str(total // sit) # 앉은 사람
    # if key[0] != 0:
        # 재귀함수 들어갈 곳......같은데..........

         # key[0] = str(sit(stand, seat +1))
    # else:
    #     cnt += 1

    for i in range(seat, max + 1):
        cnt += sit(seat,-i,i)

    # 메모화 처리
    memo[key] = cnt

    # 종료
    return cnt

print(sit(total, min))
