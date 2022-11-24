# 221124

# 모듈 __name__ __main__

# 프로그램 진입점 : 엔트리 포인트, 메인

print(__name__)


# __name__을 출력해보면 __main__이 출력된다.
# 파이썬 파일을 실행했을 때, 자기 자신의 코드이면 __main__ 파일 내부로 표현된다.

# 모듈 작성시 if __name__ == '__main__'의 의미는 모듈이 모듈로서 사용되고 있는지,
# 모듈의 코드를 모듈로서 사용되지 않고 직접 실행하고 있는지를 구분할 수 있는 근거
# 즉 엔트리 포인트로 실행되는지 확인 가능

# if __name__ == '__main__':
#     fk()
#     fa()
# 다른 곳에서 임포트는 못하고 이 파일에서는 실행할 수 있음, 메인파일이다라는 의미, 모듈로 배포했을 때 실행되지 않았으면 하는 것들을 넣어두면 됨

# 텍스트 데이터
# 바이너리 데이터


# 클래스

# 양식, 틀
# 추상화
# 프로그램에 필요한 요소만 사용해서 객체를 표현하는 것을 추상화
#

# 클래스가 없다면 이렇게..
# students = [
#     {"name": "윤인성", "korean": 87,"math": 98, "english": 88, "science": 95 },
#     {"name": "연하진", "korean":92,"math": 98, "english": 96, "science": 98 },
#     {"name": "구지연", "korean": 76,"math": 96, "english": 94, "science": 90 },
#     {"name": "나선주", "korean": 98,"math": 92, "english": 96, "science": 92 },
#     {"name": "윤아린", "korean": 95,"math": 98, "english": 98, "science": 98 },
#     {"name": "윤명월", "korean": 64,"math": 88, "english": 92, "science": 92 }
#             ]
#
# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     score_sum = student["korean"] +  student["math"] + student["english"] + student["science"]
#     score_average = score_sum / 4
#
#     print(student["name"], score_sum, score_average, sep="\t")
#

# 클래스 선언하기
# class 클래스명:
#     클래스 내용

# 466 예제
#
# class Student:
#     pass
# student = Student()
# student2 = Student()
#
# students = [
#     Student(),
#     Student(),
#     Student(),
#     Student(),
#     Student(),
#     Student(),
#     Student(),
#     Student(),
#     Student()
# ]
#
# print(type(student))
# print(id(student))
# print(type(student2))
# print(id(student2))
# print(type(students[0]))
# print(id(students[0]))

# 각기 다른 객체

# 생성된 대상물, 결과물을 인스턴스라고 함, 인스턴스인 동시에 객체, 받는 변수가 인스턴스이고 객체이고, 변수

# student는 클래스에 의해 만들어진 인스턴스이다.

# 생성자
# 클래스 이름과 같은 함수 : 생성자 함수
# 생성자 함수는 클래스 정의 내부에 init으로 정의한다.

class Mystudent:
    def __init__(self, name, korean, eng, math, sci):
        self.x = self
        self.name = name  # 생성자 함수 선언
        self.korean = korean
        self.eng = eng
        self.math = math
        self.sci = sci


# self : 클래스 내부 함수는 첫 매개변수로 무조건 self활용
# self는 자기자신을 뜻함

student1 = Mystudent('학생1', 1, 2, 3, 4)
print(student1.name)
print(type(student1.korean))
print(student1.x)  # 자기자신이 출력
print(student1)  # 주소값이 같음, self라는 건 자기자신


# 생성자 __init__
# 소멸자는 생성자의 반대 : 인스턴스가 소멸될 때 호출
# __del__


class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))


test = Test("A")
print("=================================================================")


# 소멸은 프로그램이 끝나기 직전에 실행됨

# 클래스 내부 함수 : 메서드

# 일반 함수와 생성방법 동일, self만 추가된다.

# 469 페이지 예제

# class Student:
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#
#     def get_sum(self):
#         return self.kor + self.math + self.eng + self.sci
#
#     def get_average(self):
#         return self.get_sum() / 4
#
#     def to_string(self):
#         return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
#
#
# students = [
#     Student("학생1", 1, 2, 3, 4),
#     Student("학생2", 1, 2, 3, 4),
#     Student("학생3", 1, 2, 3, 4),
#     Student("학생4", 1, 2, 3, 4),
#     Student("학생5", 1, 2, 3, 4),
#     Student("학생6", 1, 2, 3, 4)
#
# ]
#
# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     print(student.to_string())
#

# 클래스 변수
# 클래스 함수

# 클래스의 상속
# isinstance
class St:
    def __init__(self):
        pass

    def say(self):
        print("hello")


stu = St()
stu.say()
print(isinstance(stu, St))

print(type(stu) == St)  # 상속여부 안뜨기 때문에 위에꺼 씀


# 클래스의 상속 방법
class st2(St):
    name = 10
    name2 = 20

    def m(self, name):
        self.name = name
        print("mmmmmmmmmmmmmmmmmmm")

    def __str__(self):
        return "{}1111111".format(self.name)  # 리턴값을 기능과 관련된 값으로 줘야함


print("========================================================================================")

stu22 = st2()
stu22.say()
stu22.m("학생")
x = str(stu22)
print(x)
print(st2.name)
print(stu22.name)

print("=======================================================================================")


# 476페이지 예제
class Stu:
    def study(self):
        print("공부를 합니다.")


class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")


classroom = [Stu(), Stu(), Teacher(), Stu(), Stu()]

for person in classroom:
    if isinstance(person, Stu):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
#
#
# class S:
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#
#     def get_sum(self):
#         return self.kor + self.math + self.eng + self.sci
#
#     def get_avg(self):
#         return self.get_sum() / 4
#
#     def __str__(self):
#         return "{}\t{}\t{}\t".format(self.name, self.get_sum(), self.get_avg())
#
# sts = [
#     S("학생1",1,2,3,4),
#     S("학생2",1,2,3,4),
#     S("학생3",1,2,3,4),
#     S("학생4",1,2,3,4),
#     S("학생5",1,2,3,4),
#     S("학생6",1,2,3,4),
# ]
#
# print("이름","총점","평균",sep="\t")
# for student111 in sts:
#     print(str(student111))


# 480 예제
# class S:
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#
#     def get_sum(self):
#         return self.kor + self.math + self.eng + self.sci
#
#     def get_avg(self):
#         return self.get_sum() / 4
#
#     def __str__(self):
#         return "{}\t{}\t{}\t".format(self.name, self.get_sum(), self.get_avg())
#
#     def __eq__(self, other):
#         return self.get_sum() == other.get_sum()
#
#     def __ne__(self, other):
#         return self.get_sum() != other.get_sum()
#
#     def __gt__(self, other):
#         return self.get_sum() > other.get_sum()
#
#     def __ge__(self,other):
#         return self.get_sum() >= other.get_sum()
#
#     def __lt__(self, other):
#         return self.get_sum() < other.get_sum()
#
#     def __le____(self, other):
#         return self.get_sum() <= other.get_sum()
#
# sts = [
#     S("학생1",1,2,3,4),
#     S("학생2",1,2,3,4),
#     S("학생3",1,2,3,4),
#     S("학생4",1,2,3,4),
#     S("학생5",1,2,3,4),
#     S("학생6",1,2,3,4),
# ]
#
# st_a = S("학생2", 1,2,3,4)
# st_b = S("학생3",1,2,3,4)
#
# print("st_a == st_b = ", st_a == st_b)
# print("st_a != st_b = ", st_a != st_b)
# print("st_a >  st_b = ", st_a >  st_b)
# print("st_a >= st_b = ", st_a >= st_b)
# print("st_a <  st_b = ", st_a <  st_b)
# print("st_a <= st_b = ", st_a <= st_b)
#
# # 클래스 변수
# # 클래스 안에 있는 변수
#
# # 인스턴스
# # 객체
# # 객체명
# # 변수
# # 클래스
# # 클래스명
# # 클래스변수
# # 생성자
#
#
# class Std:
#     count = 0
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#         Std.count += 1
#         print("{}번째 학생이 생성되었습니다.".format(Std.count))
#
# sts = [
#     S("학생1",1,2,3,4),
#     S("학생2",1,2,3,4),
#     S("학생3",1,2,3,4),
#     S("학생4",1,2,3,4),
#     S("학생5",1,2,3,4),
#     S("학생6",1,2,3,4),
# ]
#
# print()
# print("현재 생성된 총 학생 수는 {}명입니다.".format(Std.name)) # 클래스 안의 함수 안에 있어서 못 부름 클래스 내부에만 있으면 부를 수 있음


import datetime

datetime.datetime.now()


# 클래스함수
# @classmethod : 데코레이터
# 클래스가 가진 메서드

# class 클래스명:
#     @classmethod
#     def 클래스함수명(cls, 매개변수):
#         수행문

# 486 예제
# class Student:
#     count = 0
#     students = []
#
#     @classmethod
#     def print(cls):
#         print("==학생목록==")
#         print("이름\t총점\t평균")
#         for student in cls.students:
#             print(str(student))
#         print("===============================")
#
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#         Student.count += 1
#         Student.students.append(self)
#
#     def get_sum(self):
#         return self.kor + self.math + self.eng + self.sci
#
#     def get_avg(self):
#         return self.get_sum() / 4
#
#     def __str__(self):
#         return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())
#
# Student("학생1",1,2,4,5)
# Student("학생2",1,2,4,5)
# Student("학생3",1,2,4,5)
# Student("학생4",1,2,4,5)
# Student("학생5",1,2,4,5)
# Student("학생6",1,2,4,5)
# Student("학생7",1,2,4,5)
# Student("학생8",1,2,4,5)
# Student("학생9",1,2,4,5)
# Student("학생10",1,2,4,5)
# Student("학생11",1,2,4,5)
# Student.print()

# 가비지 컬렉터
class T:
    def __init__(self, name):
        self.name = name
        print("{} 생성".format(self.name))
    def __del__(self):

        print("{} 파괴".format(self.name))

T("A") #변수에 넣고 안넣고에 따라 파괴의 순서가 다름
T("B")
T("C")

# 프라이빗 변수
# __radius


# 490 예제
import math
# class Circle:
#     def __init__(self,radius):
#         self.__radius = radius
#     def get_circumference(self):
#         return 2 * math.pi * self.__radius
#     def get_area(self):
#         return math.pi*(self.__radius **2)
#
# circle = Circle(10)
# print("원의 둘레 : ", circle.get_circumference())
# print("원의 넓이 : ", circle.get_area())
# print(circle.__radius) 접근못한다는 오류 뜸

# 게터 세터
# get set
# __radius

# get set을 통해 간접적으로 프라이빗 변수의 값에 접근하거나 추출할 수 있다.

# 492 예제
import math
class Circle:
    def __init__(self,radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi*(self.__radius **2)
    def get_radius(self):
        return self.__radius
    def set_radius(self,value):
        self.__radius = value


#
# circle = Circle(10)
# print("원의 둘레 : ", circle.get_circumference())
# print("원의 넓이 : ", circle.get_area())
# print()
#
# print("radius에 접근합니다.")
# print(circle.get_radius())
# print()
#
# circle.set_radius(2)
# print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
# print("원의 둘레 : ", circle.get_circumference())
# print("원의 넓이 : ", circle.get_area())

# 데코레이터를 활용한 게터 / 세터
#
# class circle:
#
#     def __init__(self,radius):
#         self.__radius = radius
#     def get_circumference(self):
#         return 2 * math.pi * self.__radius
#     def get_area(self):
#         return math.pi*(self.__radius **2)
#     def get_radius(self):
#         return self.__radius
#     def set_radius(self,value):
#         self.__radius = value
#     @property # 속성
#     def radius(self):
#         return self.radius
#     @radius.setter # 같은 이름의 함수를 쓸 수가 있다.
#     def radius(self, value):
#         if value <= 0:
#             raise TypeError("길이는 양의 숫자여야 합니다.")
#             self.__radius = value



        
# 가져올 때는 프로퍼티, 집어넣을 때는 펑션
# c = circle()
# c.radius = 1
# print(c.radius)

# 메서드 오버라이딩(덮어쓰기)


# 505 확인문제
# 이해해야함..........
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class StudentList:
    def __init__(self):
        self.students = []
    def append(self, student):
        self.students.append(student)
    def get_average(self):
        sum = 0
        for student in self.students:
             sum += student.score
        return sum / len(self.students)

    def get_first_by_score(self):
        scoreList = []
        for student in self.students:
            scoreList.append(student.score)
        scoreList.sort()
        for student in self.students:
            if student.score == scoreList[-1]:
                return student


    def get_last_by_score(self):
        scoreList = []
        for student in self.students:
            scoreList.append(student.score)
        scoreList.sort()
        for student in self.students:
            if student.score == scoreList[0]:
                return student


students = StudentList()
students.append((Student("구름", 100)))
students.append((Student("별", 49)))
students.append((Student("초코", 81)))
students.append((Student("아지", 90)))
print(f"평균 : {students.get_average()}")
print(f"높은 성적 {students.get_first_by_score().name}")
print(f"낮은 성적 {students.get_last_by_score().name}")
class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())

class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self,item):
        self.list.append(item)
    def dequeue(self):
        for i in range(len(self.list)):
            return self.list.pop(i)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())