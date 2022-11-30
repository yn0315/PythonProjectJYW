import random
import theater
import movie
import cinema
if __name__ == "__main__":
    try:
        c = cinema.Cinema()
        print()
        print("----------- 영화 정보 ------------")
        print()
        # a = movie.movie()
        for i in range(len(c.cinema_movie_info)):
            print("영화명 : ",c.cinema_movie_info[i][0], " | ", "별점 : ",c.cinema_movie_info[i][2])
        print()
        print("1.영화명으로 예매 2.상영시간으로 예매")
        num = input(">>")

        if num == "1":
                name = input("영화명 >>")

                a = c.Reservation()
                a.reservation_movie_name(name)

        elif num == "2":

            for i in range(len(c.screening_timetable)):
                # 상영시간표 4자리 숫자에서 시계처럼 보이게 프린트
                if len(str(c.screening_timetable[i])) == 3:
                    print("0" + str(c.screening_timetable[i])[0], ":",str(c.screening_timetable[i])[1:])
                else:
                    print(str(c.screening_timetable[i])[:2], ":",str(c.screening_timetable[i])[2:])

            print("상영시간을 입력해주세요. 예)0830 , 1630")
            time = int(input(">>"))

            d = c.Reservation()
            d.reservation_movie_time(time)
    except Exception as e:
        print("main", type(e), e)