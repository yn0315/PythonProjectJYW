class A:
    def __init__(self, name):
        self.name = name
    class B: #A클래스의 내부클래스
        def __init__(self, name2):
            self.name2 = name2
        class C :
            def __init__(self, name3):
                self.name3 = name3

# 클래스의 중첩
# B클래스는 A클래스의 내부클래스
# f : 필드 : 인스턴스의 변수
# c : 클래스
# 중첩클래스에서는 outer.inner

# x = A("이름1")
y = A.B("이름2")
# z = A.B.C("이름3")

# print(x.name)

print(y.name2)
print()
# print(z.name3)

class sample:
    def __init__(self, name):
        self.name = 10
    def hello(self):
        print("hello")

m = sample("이름")
m.hello()

