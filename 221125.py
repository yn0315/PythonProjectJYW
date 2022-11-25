# 221125

class myclass:
    x = 100 # 클래스변수
    y = 100
    def add(self,a,b): # 인스턴스 메서드, 객체화가 된 인스턴스들이 쓰는 메서드! self는 가상의 변수임, 아직 지정이 되지 않은
        self.x = 10 # x 는 인스턴스 변수, x는 self의 x!!
        return a + b
    def sub(self,a,b): # self가 붙어있는 것은 전부 인스턴스 전용!!
        return a - b
    def mul(self,a,b):
        return a * b
    def div(self,a,b):
        return a / b
    @staticmethod
    def st(a,b): # 단발성 작업
        return a + b
    @classmethod # 이후 작업에서 클래스가 필요할 때 쓰는 함수
    def st2(cls,a,b):
        return a + b

# 두 수를 입력해서 계산하는 계산기 클래스
m1 = myclass()
print(m1.add(4,5))

print(myclass.st(4,5))
print(myclass.st2(4,5))

print(eval("3+4/2*10")) # 문자열 계산하는 함수

# 뒤로가기, 초기화, 사칙연산에 = 있고 1234567890 숫자 있게
# 독립적으로 운용, 계산은 인스턴스메서드로 만들어야함



