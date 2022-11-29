# 예매클래스
import theater
import movie
class Reservation:
    # 예매할 때 필요한 것들.....
    # 영화명, 영화시간, 인원수
    name = ""
    number = 0
    show_time = 0

    def __init__(self):
        #               인원수, 영화명, 상영시간(4자리의 문자열로 바꿔서 입력할 수 있게)
        pass

    # 예매하기 함수
    def reservation_movie(self, name, number, show_time):
        self.name = name
        self.number = number
        self.show_time = show_time


            
    




