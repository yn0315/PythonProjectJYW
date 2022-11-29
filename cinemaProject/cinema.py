# 영화관 클래스
import theater
import movie
import datetime
# 필요한 것
# 상영시간 배치, 예매
class Cinema:
    def __init__(self):
        now = datetime.datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        time = hour + minute  # 예매시간 15분 전부터는 취소 못하게 하기 위한 변수
        print(time)  # 상영시간이 00분일 때 조건문 써줘야함

        if "0830" <= time <= "2400":
            # 상영관을 가져옴
            t1 = theater.theater(10,10,"A")
            chair_countA = 0 # 좌석 변수
            # 좌석 갯수를 세는 for문
            for i in range(len(t1.seat_listA)):
                for j in range(len(t1.seat_listA[i])):
                    if t1.seat_listA[i][j] == 0:
                        chair_countA += 1
            print("chair_countA : ",chair_countA)
            for i in t1.seat_listA:
                print(i)
            print("=============================================================")

            t2 = theater.theater(10,20,"B")
            chair_countB = 0 # 좌석 변수
            # 좌석 갯수를 세는 for문
            for i in range(len(t1.seat_listB)):
                for j in range(len(t1.seat_listB[i])):
                    if t1.seat_listB[i][j] == 0:
                        chair_countB+= 1
            print("chair_countB : ", chair_countB)
            for i in t2.seat_listB:
                print(i)
            print("=============================================================")


            # 영화정보를 가져옴
            print("==============================================================")
            movie_information = movie.movie()
            print(movie_information.movie_info)

            print("==============================================================")
            # 영화 별점순위가 높은 것부터 상영시간표에 많이 배치.......
            # 시간 4자리로 바꾸기
            now = datetime.datetime.now()
            hour = str(now.hour)
            minute = str(now.minute)
            time = hour + minute # 예매시간 15분 전부터는 취소 못하게 하기 위한 변수
            # print(time) # 상영시간이 00분일 때 조건문 써줘야함


            # 상영배치, 영화 상영 후 쉬는 시간 30분

            A_screening_time = 1570 # A관 총 상영가능시간 변수
            B_screening_time = 1570 # B관 총 상영가능시간 변수
            start_time = 830 # 상영 시작시간변수
            time_list = [0,0,0,0,0]
            screening_timetable = [start_time] # 상영시간표변수

            for i in range(len(movie_information.movie_info)):
                if movie_information.movie_info[i][2] == "5":
                    print(movie_information.movie_info[i])
                    # A_theater = int(A_screening_time / 2)
                    # B_theater = int(B_screening_time / 2)
                    five_movie_time_count = int(5 * (int(movie_information.movie_info[i][1]) + 30)/100)
                    print("movie_time_count",five_movie_time_count) # 하루 몇 타임 상영할 수 있는지 계산
                    time_list[0] = movie_information.movie_info[i][1]
                    print(time_list)
                    # five_movie_all_time = [start_time] # 영화 상영 시간표
                    # for j in range(five_movie_time_count- 1):
                    #     a = five_movie_all_time[j] + int(movie_information.movie_info[i][1]) + 30
                    #     five_movie_all_time.append(a)
                    # for j in range(len(five_movie_all_time)):
                    #     if "60" <= str(five_movie_all_time[j])[-2:]:
                    #         five_movie_all_time[j] += 40 # 분 단위 시간조절
                    #
                    # print(five_movie_all_time)

                elif movie_information.movie_info[i][2] == "4":

                    print(movie_information.movie_info[i])
                    # A_theater = int(A_screening_time / 2.5)
                    # B_theater = int(B_screening_time / 2.5)
                    four_movie_time_count = int(4 *(int(movie_information.movie_info[i][1]) + 30)/100)
                    print("movie_time_count", four_movie_time_count)  # 하루 몇 타임 상영할 수 있는지 계산
                    time_list[1] = movie_information.movie_info[i][1]
                    print(time_list)
                    # four_movie_all_time = [start_time]  # 영화 상영 시간표
                    # for j in range(four_movie_time_count - 1):
                    #     a = four_movie_all_time[j] + int(movie_information.movie_info[i][1]) + 30
                    #     four_movie_all_time.append(a)
                    # for j in range(len(four_movie_all_time)):
                    #     if "60" <= str(four_movie_all_time[j])[-2:]:
                    #         four_movie_all_time[j] += 40  # 분 단위 시간조절
                    # print(four_movie_all_time)

                elif movie_information.movie_info[i][2] == "3":
                    print(movie_information.movie_info[i])
                    # A_theater = int(A_screening_time / 4)
                    # B_theater = int(B_screening_time / 4)
                    three_movie_time_count = int(3*(int(movie_information.movie_info[i][1]) + 30)/100)
                    print("movie_time_count", three_movie_time_count)  # 하루 몇 타임 상영할 수 있는지 계산
                    time_list[2] = movie_information.movie_info[i][1]
                    print(time_list)

                    # three_movie_all_time = [start_time]  # 영화 상영 시간표
                    # for j in range(three_movie_time_count - 1):
                    #     a = three_movie_all_time[j] + int(movie_information.movie_info[i][1]) + 30
                    #     three_movie_all_time.append(a)
                    # for j in range(len(three_movie_all_time)):
                    #     if "60" <= str(three_movie_all_time[j])[-2:]:
                    #         three_movie_all_time[j] += 40  # 분 단위 시간조절
                    # print(three_movie_all_time)

                elif movie_information.movie_info[i][2] == "2":
                    print(movie_information.movie_info[i])
                    # A_theater = int(A_screening_time / 4)
                    # B_theater = int(B_screening_time / 4)
                    two_movie_time_count = int(2 * int(int(movie_information.movie_info[i][1]) + 30)/100)
                    print("movie_time_count", two_movie_time_count)  # 하루 몇 타임 상영할 수 있는지 계산
                    time_list[3] = movie_information.movie_info[i][1]
                    print(time_list)

                    # two_movie_all_time = [start_time]  # 영화 상영 시간표
                    # for j in range(two_movie_time_count - 1):
                    #     a = two_movie_all_time[j] + int(movie_information.movie_info[i][1]) + 30
                    #     two_movie_all_time.append(a)
                    # for j in range(len(two_movie_all_time)):
                    #     if "60" <= str(two_movie_all_time[j])[-2:]:
                    #         two_movie_all_time[j] += 40  # 분 단위 시간조절
                    # print(two_movie_all_time)

                elif movie_information.movie_info[i][2] == "1":
                    print(movie_information.movie_info[i])
                    # A_theater = int(A_screening_time / 6)
                    # B_theater = int(B_screening_time / 6)
                    one_movie_time_count = int(1 * (int(movie_information.movie_info[i][1]) + 30)/100)
                    print("movie_time_count", one_movie_time_count)  # 하루 몇 타임 상영할 수 있는지 계산
                    time_list[4] = movie_information.movie_info[i][1]
                    print(time_list)

                    # one_movie_all_time = [start_time]  # 영화 상영 시간표
                    # for j in range(one_movie_time_count - 1):
                    #     a = one_movie_all_time[j] + int(movie_information.movie_info[i][1]) + 30
                    #     one_movie_all_time.append(a)
                    # for j in range(len(one_movie_all_time)):
                    #     if "60" <= str(one_movie_all_time[j])[-2:]:
                    #         one_movie_all_time[j] += 40  # 분 단위 시간조절
                    #
                    # print(one_movie_all_time)



            # screening_timetable.append( + int(time_list[0])
            # A_screening_time -= int(time_list[0])
            # print(screening_timetable)
            # print(A_screening_time)

            # 해당 별점 칸이 비어있으면 (0)이면 삭제해주는 while문
            i = 0
            while True:
                if 0 not in time_list:
                    break
                if time_list[i] == 0:
                    del time_list[i]
                i += 1
            print(time_list)

            # 상영스케줄표에 영화 돌아가면서 집어넣는 while문
            j = 0
            k = 0
            while True:

                screening_timetable.append(screening_timetable[j] + int(time_list[k]))
                A_screening_time -= int(time_list[k])
                if A_screening_time < 31:
                    break
                print(screening_timetable)
                print(A_screening_time)

                if k == int(time_list.index(time_list[-1])):
                    k = 0
                else:
                    k += 1
                j += 1

            screening_timetable.pop()
            screening_timetable.pop()
            print(screening_timetable)

        # 영화관, 영화시간표 배치 후 예매함수 가져오기






Cinema()