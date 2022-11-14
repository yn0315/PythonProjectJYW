# 지정숫자 제외하고 랜덤 조합
# 랜덤 번호를 생성 n개~


# os모듈을 이용해서 txt파일 생성 1041.txt / 1042.txt 저장
# 파일은 회차별로 폴더 생성해서 저장 폴더명: 1041회, 1042회..
# TIME모듈을 써서 구매 완료 후 10초 뒤 당첨번호 발표
# 당첨여부 확인
# 총 당첨금액
# 총 구매금액
# 총 기대치금액 출력 814만 분의 1 * 구매수량
# 당첨확인 후 구매를 하면 다음회차 폴더와 파일생성
import os
import time
import random

enc = ".txt"
count = 1040
str_count = str(count+1)

print(os.getcwd())
df = os.getcwd().replace("\\","/")
makedir = df + "/" + str(count + 1) + "회"
filepath= 0
file = []
is_file_create = False
number_list = [] # 로또번호 리스트
publish_number_list = [] # 당첨번호 리스트
bonus_number = 0
# PATH_DEF = ""# 기본경로 저장
# path = PATH_DEF + "/" + str_count + "/" + enc #로 파고 들어간다....
# with open(path,'r')


# 폴더 생성 및 파일 생성, 글쓰기
def create_file_and_write():
    global filepath
    try: # 파일이 없으면 생성해라
        if not(os.path.isdir(str(count + 1) + "회")):
            os.makedirs(os.path.join(makedir))
            filepath = os.path.join(makedir, str(count + 1) + enc)

        else: #파일이 있으면
            filepath = os.path.join(makedir, str(count + 1) + enc)
            print("filepath ===>", filepath)
            with open(filepath + enc, "w") as f:
                f.write("자동\n반자동\n수동")

    except OSError as e:
        print("Failed to create directory!!!!!")


def read_file():
    try:
        with open(filepath + enc, 'r')as f2:
            for line in f2:
                file.append(line.strip().split("\n"))

            print(file)
    except Exception as e:
        print("파일읽기", type(e), e)


def write_file():
    try:
        with open(filepath + enc, 'a') as f:

            file= f.write(str(number_list)+"\n")
            print("number---------->",file)
    except Exception as e:
        print("write_file", type(e),e)


# 특정회차의 파일을 찾아가는 함수
def search(count):
    pass


# 로또번호 자동 생성함수
def lotto_num():
    try:
        while True:
            print("0. 자동 1. 반자동 2. 수동")
            n = input(" 번호를 입력하세요 : ")
            random_number = 0

            # 자동 반자동 수동 입력받아서 걸러낸 후에 range 범위를 정해주면??
            if n == "0":
                try:
                    while True:  # 랜덤숫자를 돌려서 저장
                        random_number = random.randint(1, 46)
                        if random_number in number_list:  # 이미 있으면 다시 반복하라
                            continue
                        else:  # 중복이 아니면
                            number_list.append(random_number)
                            if len(number_list) == 6:
                                number_list.sort()
                                break

                    write_file()
                    break
                except Exception as e:
                    print("lotto_num 첫번째 while", type(e), e)

            elif n == "1":
                try:
                    while True:
                        print("넣고 싶은 숫자를 입력하세요. 그만 넣으시려면 0을 눌러주세요")
                        num = int(input(">>"))
                        if num == 0:
                            break
                        if num in number_list:
                            continue
                        else:
                            number_list.append(num)
                            if len(number_list) == 6:
                                number_list.sort()
                                break
                            elif len(number_list) < 6:
                                try:
                                    for i in range( 6 - len(number_list)):
                                        random_number = random.randint(1,46)
                                        if random_number in number_list:  # 이미 있으면 다시 반복하라
                                            del random_number
                                            continue

                                    else:  # 중복이 아니면
                                        if len(number_list) == 6:
                                            number_list.sort()
                                            break
                                        elif len(number_list) < 6:
                                            number_list.append(random_number)

                                except Exception as e:
                                    print("lotto_num 안의 for문", type(e), e)

                    break
                except Exception as e:
                    print("lotto_num 두번째 while", type(e),e)
                try: # 자꾸 8개가 나온다.
                    while True: # 랜덤숫자를 돌려서 저장
                        random_number = random.randint(1,46)
                        if random_number in number_list: # 이미 있으면 다시 반복하라
                            continue
                        else: # 중복이 아니면
                            number_list.append(random_number)
                            if len(number_list) == 6:
                                number_list.sort()
                                break
                        break
                except Exception as e:
                    print("lotto_num 세번째 while", type(e),e)

            elif n == "2":
                try:
                    print("넣고 싶은 숫자 6개를 입력하세요.")
                    while True:
                        num = int(input(">>"))
                        if num in number_list:
                            continue
                        else:
                            number_list.append(num)
                            if len(number_list) == 6:
                                break
                        break
                except Exception as e:
                    print("lotto_num 마지막 while", type(e),e)
            else:
                continue

            write_file()

        print(number_list)
        return
    except Exception as e:
        print("lotto_num", type(e),e)


# 로또 당첨함수
def publish_lotto():
    try:
        while True:  # 랜덤숫자를 돌려서 저장
            random_number = random.randint(1, 45)
            if random_number in publish_number_list:  # 이미 있으면 다시 반복하라
                continue
            else:  # 중복이 아니면
                publish_number_list.append(random_number)
                if len(publish_number_list) == 7:
                    publish_number_list.sort()
                    bonus_number = publish_number_list.pop()
                    break

        print("당첨번호 " , publish_number_list)
        print("보너스 번호", bonus_number)

    except Exception as e:
        print("publish_lotto", type(e),e)



# 당첨확인하는 함수
def check_lotto():
    try:
        cnt = 0
        bonus_cnt = 0
        item_list = []
        for item in number_list:
            if item in publish_number_list:
                cnt += 1
                item_list.append(item)
        if bonus_number in number_list:
            bonus_cnt += 1
            print("보너스번호", bonus_number)
        print("맞은번호 => ",item_list)
        if cnt == 6:
            print("1등")
        elif cnt == 5 and bonus_cnt == 1:
            print("2등")
        elif cnt == 4:
            print("3등")
        elif cnt == 3:
            print("4등")
        else:
            print("낙첨")
    except Exception as e:
        print("check_lotto", type(e),e)
# 메인함수
def main():
    try:
        # 폴더 및 파일 만들기
        create_file_and_write()
        # 파일 읽기
        read_file()

        # 로또번호 입력
        lotto_num()
        
        # 10초 카운트 후 발표
        time.sleep(10)
        
        # 당첨번호 발표
        publish_lotto()
        
        # 몇 개 맞았는지 확인
        check_lotto()


    except Exception as e:
        print("main", type(e),e)
main()
