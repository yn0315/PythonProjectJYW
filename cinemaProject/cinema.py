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

            A_screening_time = 1570
            B_screening_time = 1570

            for i in range(len(movie_information.movie_info)):
                if movie_information.movie_info[i][2] == "5":
                    A_screening_time = int(A_screening_time / 2)
                    all_time = int(movie_information.movie_info[i][1]) + 30
                    count = int(A_screening_time / all_time)
                    print("count",count) # 하루 몇 타임 상영할 수 있는지 계산
                    

                    print(A_screening_time)
                    print(B_screening_time / 2)
                if movie_information.movie_info[i][2] == "4":
                    print(A_screening_time / 2)
                    print(B_screening_time / 2)
                if movie_information.movie_info[i][2] == "3":
                    pass
                if movie_information.movie_info[i][2] == "2":
                    pass
                if movie_information.movie_info[i][2] == "1":
                    pass

        # 영화관, 영화시간표 배치 후 예매함수 가져오기


Cinema()