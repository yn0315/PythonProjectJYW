# 영화관 클래스
import theater
import movie
import datetime
# 필요한 것
# 상영시간 배치, 예매

class Cinema:
    A_screening_time = 1570  # A관 총 상영가능시간 변수
    B_screening_time = 1570  # B관 총 상영가능시간 변수
    start_time = 830  # 상영 시작시간변수
    time_list = [0, 0, 0, 0, 0] # 영화 평점 별 러닝타임변수
    screening_timetable = [start_time] # 상영시간표 변수
    movie_list = [] # 상영시간표 인덱스에 맞는 영화목록변수
    tA = [] # A관 좌석배치도 변수
    tB = [] # B관 좌석배치도 변수
    cinema_movie_info = []



    # 예매클래스

    def __init__(self):

        now = datetime.datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        if hour < "10":# 안됩니다......
            hour = "0" + hour

        if minute < "10":# 안됩니다...............
            minute = "0" + minute
        time = hour + minute  # 예매시간 15분 전부터는 취소 못하게 하기 위한 변수
        # print(time)  # 상영시간이 00분일 때 조건문 써줘야함

        # if "830" <= time <= "2400":

        # 상영관을 가져옴
        t1 = theater.theater(10,10,"A")
        chair_countA = 0 # 좌석 변수
        # 좌석 갯수를 세는 for문
        for i in range(len(t1.seat_listA)):
            for j in range(len(t1.seat_listA[i])):
                if t1.seat_listA[i][j] == 0:
                    chair_countA += 1
        # print("chair_countA : ",chair_countA)
        Cinema.tA.append(t1.seat_listA)
        # for i in t1.seat_listA:
        #     global tA
        #     tA.append(i)
            # print(i)
        # print("=============================================================")

        t2 = theater.theater(10,20,"B")
        chair_countB = 0 # 좌석 변수
        # 좌석 갯수를 세는 for문
        for i in range(len(t1.seat_listB)):
            for j in range(len(t1.seat_listB[i])):
                if t1.seat_listB[i][j] == 0:
                    chair_countB+= 1
        # print("chair_countB : ", chair_countB)
        Cinema.tB.append(t2.seat_listB)
        # print(tB)
        # for i in t2.seat_listB:
        #     global tB
        #     tB.append(i)
            # print(i)
        # print("=============================================================")


        # 영화정보를 가져옴
        # print("==============================================================")
        movie_information = movie.movie()
        Cinema.cinema_movie_info = movie_information.movie_info
        # print(movie_information.movie_info)

        # print("==============================================================")
        # 영화 별점순위가 높은 것부터 상영시간표에 많이 배치.......
        # 시간 4자리로 바꾸기
        now = datetime.datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        time = hour + minute # 예매시간 15분 전부터는 취소 못하게 하기 위한 변수
        # print(time) # 상영시간이 00분일 때 조건문 써줘야함

        # 상영배치, 영화 상영 후 쉬는 시간 30분

        # 상영시간표 배치과정.....
        for i in range(len(movie_information.movie_info)):

            if movie_information.movie_info[i][2] == "5": # 별점이 5점이면

                five_movie_time_count = int(5 * (int(movie_information.movie_info[i][1]) + 30)/100) # 쉬는시간을 합산하여 별점에 곱한 것이 가능 상영횟수
                # print("movie_time_count",five_movie_time_count) # 하루 몇 타임 상영할 수 있는지 계산
                Cinema.time_list[0] = movie_information.movie_info[i][1] # 시간리스트 0번자리에 시간부분을 넣어라

            elif movie_information.movie_info[i][2] == "4": # 별점이 4점이면

                four_movie_time_count = int(4 *(int(movie_information.movie_info[i][1]) + 30)/100)
                # print("movie_time_count", four_movie_time_count)  # 하루 몇 타임 상영할 수 있는지 계산
                Cinema.time_list[1] = movie_information.movie_info[i][1]# 시간리스트 1번자리에 시간부분을 넣어라


            elif movie_information.movie_info[i][2] == "3":

                three_movie_time_count = int(3*(int(movie_information.movie_info[i][1]) + 30)/100)
                # print("movie_time_count", three_movie_time_count)  # 하루 몇 타임 상영할 수 있는지 계산
                Cinema.time_list[2] = movie_information.movie_info[i][1] # 시간리스트 2번자리에 시간부분을 넣어라

            elif movie_information.movie_info[i][2] == "2":

                two_movie_time_count = int(2 * int(int(movie_information.movie_info[i][1]) + 30)/100)
                # print("movie_time_count", two_movie_time_count)  # 하루 몇 타임 상영할 수 있는지 계산
                Cinema.time_list[3] = movie_information.movie_info[i][1] # 시간리스트 3번자리에 시간부분을 넣어라

            elif movie_information.movie_info[i][2] == "1":
                # print(movie_information.movie_info[i])
                # A_theater = int(A_screening_time / 6)
                # B_theater = int(B_screening_time / 6)
                one_movie_time_count = int(1 * (int(movie_information.movie_info[i][1]) + 30)/100)
                # print("movie_time_count", one_movie_time_count)  # 하루 몇 타임 상영할 수 있는지 계산
                Cinema.time_list[4] = movie_information.movie_info[i][1] # 시간리스트 4번자리에 시간부분을 넣어라
                # print(time_list)

                # one_movie_all_time = [start_time]  # 영화 상영 시간표
                # for j in range(one_movie_time_count - 1):
                #     a = one_movie_all_time[j] + int(movie_information.movie_info[i][1]) + 30
                #     one_movie_all_time.append(a)
                # for j in range(len(one_movie_all_time)):
                #     if "60" <= str(one_movie_all_time[j])[-2:]:
                #         one_movie_all_time[j] += 40  # 분 단위 시간조절
                #
                # print(one_movie_all_time)

        # 해당 별점 칸이 비어있으면 (0)이면 삭제해주는 while문
        try:
            i = 0
            while True:

                if 0 not in Cinema.time_list:
                    break
                if Cinema.time_list[i] == 0:
                    del Cinema.time_list[i]
                i += 1
            # print(time_list)
        except Exception as e:
            print("cinema생성자 1번 while문", type(e),e)


        # 상영스케줄표에 영화 돌아가면서 집어넣는 while문
        try:
            j = 0
            k = 0
            while True:

                a = Cinema.screening_timetable[j] + int(Cinema.time_list[k]) + 70 # 실제 시간에 맞춰 계산 9시 60분같은 거 안나오게
                for i in range(len(movie_information.movie_info)):
                    if movie_information.movie_info[i][1] == Cinema.time_list[k]:
                        Cinema.movie_list.append(movie_information.movie_info[i][0])

                Cinema.screening_timetable.append(a)

                Cinema.B_screening_time -= int(Cinema.time_list[k])
                if Cinema.B_screening_time < 31:
                    break
                # print(screening_timetable)
                # print(A_screening_time)

                if k == int(Cinema.time_list.index(Cinema.time_list[-1])):
                    k = 0
                else:
                    k += 1
                j += 1
        except Exception as e:
            print("cinema생성자 2번째 while문",type(e),e)

        for l in range(len(Cinema.screening_timetable)):
            if "60" <= str(Cinema.screening_timetable[l])[-2:]:
                Cinema.screening_timetable[l] += 40  # 분 단위 시간조절

        #.................................. 마감 근처에 있는 시간 삭제 알고리즘 구현못함..그냥 날려버림


        Cinema.screening_timetable.pop()
        Cinema.screening_timetable.pop()
        Cinema.screening_timetable.pop()
        Cinema.screening_timetable.pop()
        Cinema.screening_timetable.pop()
        Cinema.screening_timetable.pop()
        Cinema.movie_list.pop()
        Cinema.movie_list.pop()
        Cinema.movie_list.pop()
        Cinema.movie_list.pop()
        Cinema.movie_list.pop()

        # print(screening_timetable)
        # print(movie_list)
        # print(screening_timetable)

        # 영화관, 영화시간표 배치 후 예매함수 가져오기

    class Reservation:
        # 예매할 때 필요한 것들.....
        # 영화명, 영화시간, 인원수
        bill = [0, 0, 0, ""] # 영수증변수
        name = "" # 영화명변수
        number = 0 # 인원변수 안쓰임..?
        show_time = 0 # 시작시간변수.. 안쓰인 듯..?
        pay = 7000  # 1인 영화비용 변수

        def __init__(self):
            #               인원수, 영화명, 상영시간(4자리의 문자열로 바꿔서 입력할 수 있게)
            pass

        # 예매하기 함수

        def reservation_movie_name(self, name): # 영화명으로 예매하기
            try:
                m = Cinema.movie_list # 영화리스트
                t = Cinema.screening_timetable # 상영시간표
                print("=================================================")

                print(name)
                Cinema.Reservation.bill[0] = name
                for i in range(len(m)):

                    if m[i] == name:
                        if len(str(t[i])) == 3:
                            print("0" + str(t[i])[0], ":", str(t[i])[1:])
                        else:
                            print(str(t[i])[:2], ":", str(t[i])[2:])

                print("시간을 입력해주세요. 예) 0830, 1630")
                Cinema.Reservation.bill[1] = input(">>")
                print("인원 수를 입력해주세요.")
                Cinema.Reservation.bill[2] = input(">>")
                print("===============================================================")
                for i in range(len(Cinema.tB)): # 좌석 프린트
                    for j in range(len(Cinema.tB[i])):
                        print(Cinema.tB[i][j])

                i = 0
                while True:
                    if i == int(Cinema.Reservation.bill[2]):  # m이 인원수랑 같으면 탈출해야하는데.......
                        break

                    if i != int(Cinema.Reservation.bill[2]):
                        print("좌석을 선택해주세요. 예)A1")
                        chair = input(">>")

                        alpa = chair[:1] # 입력받은 좌석에서 열자르기 A1 ->A잘라내기
                        chair_num = int(chair[1:]) - 1 # 뒤에 번호 잘라내기
                        alpa = ord(alpa) # A 아스키코드화
                        alpa -= 65 # 65를 빼면 인덱스번호와 같아짐

                        if Cinema.tB[0][alpa][chair_num] == 0:
                            Cinema.Reservation.bill[3] = Cinema.Reservation.bill[3] + " " + chair # 영수증에 좌석정보 넣음
                            Cinema.tB[0][alpa][chair_num] = 1 # 예매된 자리 1로 변경
                            for j in range(len(Cinema.tB)):
                                for k in range(len(Cinema.tB[j])):
                                    print(Cinema.tB[j][k])
                            i += 1
                        else:
                            print("다시 입력해주세요.")
                            continue
                print("==============================================================")
                print()
                for i in range(len(Cinema.Reservation.bill)):
                    if i == 0:
                        print("영화명 : ", Cinema.Reservation.bill[0])
                    elif i == 1:
                        if len(str(Cinema.Reservation.bill[1])) == 3:
                            print("상영시간 : ","0" + str(Cinema.Reservation.bill[1])[0], ":", str(Cinema.Reservation.bill[1])[1:])
                        else:
                            print("상영시간 : ",str(Cinema.Reservation.bill[1])[:2], ":", str(Cinema.Reservation.bill[1])[2:])
                    elif i == 2:
                        print("인원 : ",Cinema.Reservation.bill[2] + "명")
                    elif i == 3:
                        print("좌석 : ",Cinema.Reservation.bill[3])



                print(f"합계 : {Cinema.Reservation.pay * int(Cinema.Reservation.bill[2]) }원")
                        
            except Exception as e:
                print("reservation_movie_name", type(e), e)


        def reservation_movie_time(self, time):
            try:
                m = Cinema.movie_list
                t = Cinema.screening_timetable
                print("=================================================")

                for i in range(len(m)):
                    Cinema.Reservation.bill[1] = time
                    if t[i] == time:
                        Cinema.Reservation.bill[0] = m[i]
                        print(m[i])
                print("인원 수를 입력해주세요.")
                Cinema.Reservation.bill[2] = input(">>")
                print("===============================================================")
                for i in range(len(Cinema.tB)):
                    for j in range(len(Cinema.tB[i])):
                        print(Cinema.tB[i][j])
                i = 0
                while True:
                    if i == int(Cinema.Reservation.bill[2]):  # m이 인원수랑 같으면 탈출해야하는데.......
                        break
                    print("bill", Cinema.Reservation.bill[2])

                    if i != int(Cinema.Reservation.bill[2]):
                        print("좌석을 선택해주세요. 예)A1")
                        chair = input(">>")

                        print(Cinema.Reservation.bill)
                        alpa = chair[:1]  # 입력받은 좌석에서 열자르기 A1 ->A잘라내기
                        chair_num = int(chair[1:]) - 1  # 뒤에 번호 잘라내기
                        alpa = ord(alpa)  # A 아스키코드화
                        alpa -= 65  # 65를 빼면 인덱스번호와 같아짐

                        if Cinema.tB[0][alpa][chair_num] == 0:
                            Cinema.Reservation.bill[3] = Cinema.Reservation.bill[3] + " " + chair  # 영수증에 좌석정보 넣음
                            Cinema.tB[0][alpa][chair_num] = 1  # 예매된 자리 1로 변경
                            for j in range(len(Cinema.tB)):
                                for k in range(len(Cinema.tB[j])):
                                    print(Cinema.tB[j][k])
                            i += 1
                        else:
                            print("다시 입력해주세요.")
                            continue
                print("==============================================================")
                print()
                for i in range(len(Cinema.Reservation.bill)):
                    if i == 0:
                        print("영화명 : ", Cinema.Reservation.bill[0])
                    elif i == 1:
                        if len(str(Cinema.Reservation.bill[1])) == 3:
                            print("상영시간 : ","0" + str(Cinema.Reservation.bill[1])[0], ":", str(Cinema.Reservation.bill[1])[1:])
                        else:
                            print("상영시간 :",str(Cinema.Reservation.bill[1])[:2], ":", str(Cinema.Reservation.bill[1])[2:])
                    elif i == 2:
                        print("인원 :",Cinema.Reservation.bill[2] + "명")
                    elif i == 3:
                        print("좌석 : ", Cinema.Reservation.bill[3])

                print(f"합계 : {Cinema.Reservation.pay * int(Cinema.Reservation.bill[2])}원")
            except Exception as e:
                print("reservation_movie_time", type(e), e)

#
#
# Cinema()