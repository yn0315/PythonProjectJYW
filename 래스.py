####노래방 기계 클래스####
import time
import random
import threading
import os

class Karaoke:
    check = 0      #스레드를 멈추기 위한 키를 만듦
    double_check = 0  #재시작 관련 키
    sel_reserve=0   #예약 관련 키
    screen = 0   #line_screen함수에 관여하는 키

    df = os.getcwd().replace("\\", "/")   #'가사 모음'이라는 폴더 생성 과정
    makedir = df + "/" + "가사모음"
    if os.path.isdir(makedir) == True:
        pass
    else:
        os.mkdir(makedir)
    file_list = os.listdir(makedir)

    for i in range(len(file_list)):
        file_list[i] = file_list[i][:-4]   #파일명 뒤 '.txt'를 지우는 과정 (파일명을 차트리스트로 불러올 것이므로)

    def __init__(self):
        self.sel_num = 0
        self.temp_song = self.file_list[self.sel_num]
        self.sel_key = 0
        self.sel_tem = 0
        self.rhythm = random.randint(3,4)

        Karaoke.chart(self)

    def chart(self):
        print("┌─────────────────────────────────────────────────────┐")
        print(" ---------------------- 인기 차트 ---------------------")
        for i in Karaoke.file_list:
            print(i)
        print("                          s (시작)  ss(취소시작) b(취소)")
        print("▶",self.temp_song,"            r (예약)  x(예약 취소)")
        print("└─────────────────────────────────────────────────────┘")

    def line_screen(self):
        if Karaoke.screen == 0:
            print("┌─────────────────────────────────────────────────────┐")
            print("  🎤", self.one_line.strip(),)
            print("└─────────────────────────────────────────────────────┘")

        else:
            Karaoke.screen = 0
            print("┌─────────────────────────────────────────────────────┐")
            print(" ---------------------- 인기 차트 ---------------------")
            for i in Karaoke.file_list:
                print(i)
            print("                          s (시작)  b(취소)  bs(취소시작)")
            print("▶", self.temp_song, "          r (예약)  x(예약 취소)")
            print("┌─────────────────────────────────────────────────────┐")
            print("  🎤", self.one_line.strip())
            print("└─────────────────────────────────────────────────────┘")

    def down(self):   #차트에서 리스트를 내리는 함수
        if self.sel_num == int(len(self.file_list)) -1:  #리스트의 맨마지막 인덱스(리스트의 개수 -1)는 더이상 +가 불가하므로
            self.sel_num == 0                            #리스트 인덱스를 0으로 바꿔 출력
            self.temp_song = self.file_list[self.sel_num]
        else:
            self.sel_num += 1       #인덱스값을 1씩 더하기
            self.temp_song = self.file_list[self.sel_num]
        Karaoke.chart(self)

    def up(self):  #차트에서 리스트를 올리는 함수
        if self.sel_num == 0:
            self.sel_num = int(len(self.file_list))-1
            self.temp_song = self.file_list[self.sel_num]
        else:
            self.sel_num -= 1
            self.temp_song = self.file_list[self.sel_num]
        Karaoke.chart(self)

    def go_song(self):
        with open(Karaoke.makedir+"/"+self.temp_song +".txt", 'r',encoding='UTF-8') as file:   #폴더 안 파일 열기
            lyrics = file.readlines()     #파일 안 가사를 리스트로 담고
        for i in range(len(lyrics)):
            lyrics[i] = lyrics[i].replace("\n", "")  #줄바꿈 문자 제거
            print("♬",self.temp_song,"♩♪")
            time.sleep(2)
            luru_list=["♬","♪","♬","♩","♬","♬","♪","♩"]  #간주 출력
            for i in range(len(luru_list)):
                print(luru_list[i],end=" ")
                time.sleep(0.4)
            print()
            pre_list=["3","2","1","시작!"]   #준비 문구 출력
            for i in range(len(pre_list)):
                print("┌─────────────────────────────────────────────────────┐")
                print(" ",pre_list[i])
                print("└─────────────────────────────────────────────────────┘")
                time.sleep(0.8)
            for i in range(len(lyrics)):   # for문으로 리스트에 담긴 가사 불러오기
                if Karaoke.check == 0:    #가사 출력 스레드를 멈추기 위한 확인 과정(멈춰야 할 때 check값을 1로 줌)
                    self.one_line = lyrics[i]
                    Karaoke.line_screen(self)
                    time.sleep(self.rhythm)  #time_sleep으로 템포 설정   #템포함수와 연결되어 rythm값이 결정됨

            if Karaoke.check == 0:
                for i in range(len(luru_list)):
                    print(luru_list[i],end=" ")
                    time.sleep(0.4)
                time.sleep(2)
                print("노래가 끝났습니다")
                time.sleep(2)
                print("과연 점수는?!")
                time.sleep(1)
                heart_list = ["♡", "♥"]
                for i in range(8):
                    print(random.choice(heart_list), end=' ')
                    time.sleep(0.5)
                score = random.randint(50, 100)
                print(score, "점!")
                time.sleep(1)
                if 50 <= score < 70:
                    print("듣기 좀 힘들었습니다.. 힘내세요~")
                elif 70 <= score < 80:
                    print("애매한 노래 실력! 나쁘진 않았어요.")
                elif 80 <= score < 90:
                    print("꽤나 잘 부르는 군요~")
                elif 90 <= score <= 100:
                    print("가수... 어때요?")
                time.sleep(4)

            #재시작 키
            if Karaoke.double_check == 0:   # 재시작이 없다는 뜻
                #예약 키
                if Karaoke.sel_reserve == 0:   #메인에서 r(예약) 입력 시 sel_reserve를 1로 변경함
                    Karaoke.check = 0
                    Karaoke.double_check = 0
                    Karaoke.chart(self)  #재시작이 없고 예약도 없으므로 차트를 불러오고
                    break      #멈춤

                elif Karaoke.sel_reserve == 1:
                    Karaoke.sel_reserve = 0
                    Karaoke.check = 0
                    Karaoke.double_check = 0
                    Karaoke.go_song(self)
                    break


            elif Karaoke.double_check == 1:  #메인에서 ss(취소시작) 입력 시 값을 1로 변경해
                Karaoke.double_check = 0
                Karaoke.check = 0
                Karaoke.go_song(self)       #재시작할 수 있게 함
                break

    def key(self):     # 메인의 k입력과 연결되는 함수로
        self.sel_key += 1
        if self.sel_key % 2 == 1:
            print("------------------남자키로 설정 됐습니다------------------")
        elif self.sel_key % 2 == 0:   # k 입력 횟수에 따라 , 남키 여키가 번갈아 나오도록 함
            print("------------------여자키로 설정 됐습니다------------------")

    def tempo(self):   #메인의 t입력과 연결되는 함수
        self.sel_tem += 1
        if self.sel_tem % 3 == 0:
            self.rhythm = random.randint(2,4)   #키 함수와 비슷하게, t 입력 횟수에 따라 값이 돌도록 만듦
            print("-----------------일반 템포로 변경 됐습니다-----------------")
        elif self.sel_tem % 3 == 1:
            self.rhythm = random.randint(1,2)
            print("-----------------빠른 템포로 변경 됐습니다-----------------")
        elif self.sel_tem % 3 == 2:
            self.rhythm = random.randint(4,5)
            print("-----------------느린 템포로 변경 됐습니다-----------------")


kr = Karaoke()
s = threading.Thread(target=kr.go_song)

################버튼 입력#################

s.start()

while True:
    i = input()
##########효과 관련#############

    if i == "k":      #키 변경 버튼
        kr.key()

    if i == "t":      #템포 변경 버튼
        kr.tempo()

    if i == "p":      #박수 효과 버튼
        print("👏🏻👏🏻👏🏻👏🏻👏🏻👏🏻👏🏻👏🏻👏🏻")

############차트 관련#############

    if i == "cu":     #차트 올리기
        Karaoke.screen = 1
        #키를 줘서 line_screen 함수의 조건을 바꿈

    if i == "cd":     #차트 내리기
        Karaoke.screen = 0

    if i == "u":       # 곡 선택 업
        Karaoke.screen = 1
        kr.up()

    if i == "d":      #곡 선택 다운
        Karaoke.screen = 1
        kr.down()

###########흐름 관련############

    if i == "b":      #노래 중단 버튼
        Karaoke.check = 1

    if i == "ss":  #취소시작 버튼   # 노래 도중에 새로운 곡 시작 가능함
        Karaoke.double_check = 1   # 순서가
        Karaoke.check = 1      # 중요했음

    if i =="s":   #시작 버튼
        s = threading.Thread(target=kr.go_song)  #스레드는 정의 후 한번 사용 가능하므로? 재정의 후 스레드 시작
        s.start()     #노래 도중에 누르면
                      #전 스레드가 멈추지 않고 겹쳐서 나와, 취소시작 버튼을 만듦..

############예약 기능 관련###########

    if i == "r":   #예약 버튼(한곡만 가능)
        print("--------------------예약 되었습니다----------------------")
        Karaoke.sel_reserve = 1

    if i == "x":   #예약 취소
        print("-------------------예약이 취소 되었습니다-----------------")
        Karaoke.sel_reserve = 0
