
p = 0

def bang1():
    global p
    print("1번방입니다.")
    p = 1
    print(p)
def bang2():
    global p
    print("2번방입니다.")
    p= 2
    print(p)
def bang3():
    global p
    print("3번방입니다.")
    p= 3
    print(p)
def bang4():
    global p
    print("4번방입니다.")
    p= 4
    print(p)

def fw():
    if bang1 == 0:
        pass
def fa():
    if p == 2:
        bang4()
def fs():
    if bang1 == 0:
        pass
def fd():
    if p == 0:
        bang2()

def fk1():
    pass
def fk2():
    pass
def fk3():
    pass
def fk4():
    pass

fd()
fa()