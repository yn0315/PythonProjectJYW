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
count = 1041
str_count = str(count+1)

print(os.getcwd())
df = os.getcwd().replace("\\","/")
makedir = df + "/" + str(count) + "회"
filepath = []
file = []
is_file_create = False
number_list = [] # 로또번호 리스트
# PATH_DEF = ""# 기본경로 저장
# path = PATH_DEF + "/" + str_count + "/" + enc #로 파고 들어간다....
# with open(path,'r')


# 폴더 생성 및 파일 생성, 글쓰기

try: # 파일이 없으면 셍성해라
    if not(os.path.isdir(str(count) + "회")):
        os.makedirs(os.path.join(makedir))
        filepath.append(os.path.join(makedir, str(count) + enc))
        print("filepath ===>",filepath)
        with open(filepath[0]+ enc, "w") as f:
            f.write("지정조합\n지정제외조합\n자동")

except OSError as e:
    print("Failed to create directory!!!!!")

with open(filepath[0] + enc, 'r')as f2:
    for line in f2:
        file.append(line.strip().split("\n"))

    print(file)

# 특정회차의 파일을 찾아가는 함수

def search(count):
    pass


# 로또번호 자동 생성함수
def lotto_num(n):
    random_number = 0

    # 자동 반자동 수동 입력받아서 걸러낸 후에 range 범위를 정해주면??
    if n == "0":
        for i in range(7):
            number_list.append(random.randint(1, 45))
            print(number_list[i])
    elif n == "1":
        while True:
            print("넣고 싶은 숫자를 입력하세요. 그만 넣으시려면 0을 눌러주세요")
            num = int(input(">>"))

            if num == 0:
                break
            else:
                number_list.append(num)
    for i in range(7 - num):

        random_number = random.randint(1,45)
        if random_number in number_list:
            del random_number
            continue
        else:
            random_number = random.randint(1,45)
            number_list.append(random_number)
        break
    print(number_list)
# 메인함수
def main():

    print("0. 자동 1. 반자동 2. 수동")
    n = input(" 번호를 입력하세요 : ")

    lotto_num(n)

    search(1040)

main()
