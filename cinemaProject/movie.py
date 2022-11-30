import theater
import random



class movie:
    # 영화클래스는 텍스트파일에서 정보를 가져오는 과정이 필요, 삭제, 수정과정 필요

    # 관 클래스, 관마다 구조 다르게 종류(리클라이너), 예약, 발권, 취소 등
    name = ""
    time = 0 # 러닝타임
    show_time = 0
    movie_info = []
    name_list = []
    time_list = []
    # 영화 생성할 때 영화관 랜덤배치 X
    def __init__(self):
        try:
            with open("movie.txt", 'r', encoding='UTF-8') as file:
                for line in file:
                    self.movie_info.append(line.strip().split("\t"))

                      # 공백 없애는 함수
        except Exception as e:
            print("파일불러오기", type(e), e)



    @staticmethod
    def add_write_movie(name, time, star):
        # 영화 생성하면 파일에 텍스트 추가하는 작업
        try:
            with open("movie.txt", 'a', encoding='UTF-8') as file:
                file.write("\n" + name + "\t" + str(time) + "\t" + str(star)+ "\n")

        except Exception as e:
            print("파일에 내용추가", type(e), e)

    # def readMovie(self):





#
# b = movie()
# print(b)