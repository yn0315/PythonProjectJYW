import time
import random

option_first = ['택배']
option_second1 = ['우편','소포','택배']
option_thrid1 = ['등기','일반']
option_four1 = ['동일지역','타지역']
option_second2 = ['대출','적금','통장관리']
option_thrid2 = ['입금','출금']

insurance_money = {"우체국실손의료비보험":9000,"우체국암보험":30000}
loney_pancreas = 3.51
Savings_pancreas = {'6개월이상 1년미만':0.034,'1년이상 2년미만':0.0375,'2년이상 3년미만':0.0385,'3년이상 5년미만': 0.0390,'5년만기':0.0390}

class Bank:

    def file_read(self,name):
        with open(name,'r',encoding="UTF-8") as fr:
            print(fr.read())

    def interest(self,total_money,percent):
        print(total_money*percent)

    def money(self,name):
        print(insurance_money[name])

    class bank:
        def __init__(self):
            self.money = random.randrange(1000,8000000)

        def add(self,number):
            self.money += number

        def sub(self,number):
            self.money -= number

class file_list:
    def __init__(self,file):
        self.filelist = []
        self.file = file
    def file_list(self):
        with open(self.file, 'r', encoding="UTF-8") as fr:
            lines = fr.readlines()

        for line in lines:
            line_list = []
            line_list.append(line)
            self.filelist.append(line_list)

        for i in range(len(self.filelist)):
            if i < 2:
                pass
            elif 1 < i:
                for j in range(len(self.filelist[i])):
                    self.str_file = ["g", 'k', '\n']
                    for k in range(len(self.str_file)):
                        self.filelist[i][j] = self.filelist[i][j].replace(self.str_file[k],"")
                    self.filelist[i][j] = self.filelist[i][j].split("\t")

        for i in range(len(self.filelist)):
            for j in range(len(self.filelist[i])):
                if type(self.filelist[i][j]) == list:
                    self.filelist[i] = self.filelist[i][j]
                else:
                    pass
        return self.filelist

class delivery:

    class post:
        def __init__(self,file,weight):
            self.file = file
            self.weight = weight
            self.list = file_list(self.file).file_list()

        def usually(self):
            for i in range(len(self.list)):
                if i<2:
                    pass
                elif 2 <= i < 5:
                    if int(self.list[i][0]) < self.weight <= int(self.list[i][1]):
                        return str(self.list[i][2]) + "원"
                    else:
                        pass
                elif i == 5 or i ==6:
                    n = self.weight // 50
                    if i == 5 and 50 <= int(self.weight) <= 1000 :
                        n -= 1

                    elif i ==6 and 1000<=int(self.weight) <= 2000:
                        n -= 4

                    else:
                        pass
                    return str(400 + (120 * n))+"원"
                elif i == 7:
                    n = self.weight // 1000
                    n-=2
                    return str(400 +(400 * n))+"원"


        def registered(self):
            for i in range(len(self.list)):
                if i<2:
                    pass
                elif 2 <= i < 5:
                    if int(self.list[i][0]) < self.weight <= int(self.list[i][1]):
                        return str(self.list[i][2]+2100) + "원"
                    else:
                        pass
                elif i == 5 or i ==6:
                    n = self.weight // 50
                    if i == 5 and 50 <= int(self.weight) <=1000 :
                        n -=1

                    elif i ==6 and 1000<=int(self.weight) <= 2000:
                        n -= 4

                    else:
                        pass
                    return str(400 + (120 * n)+2100)+"원"
                elif i == 7:
                    n = self.weight // 1000
                    n-= 2
                    return str(400 + (400 * (n-2))+2100)+"원"

    class package:
        def __init__(self,file,weight):
            self.file = file
            self.weight = weight
            self.list = file_list(self.file).file_list()

        def usually(self):
            for i in range(len(self.list)):
                if i<2:
                    pass
                elif 1 < i:
                    if int(self.list[i][0]) <= self.weight < int(self.list[i][1]):
                        if "동일지역" in select.packge:
                            print(self.list[i][0])
                            return self.list[i][2]+"원"
                        elif "타지역" in select.packge:
                            return self.list[i][3] +"원"

        def registered(self):
            for i in range(len(self.list)):
                if i<2:
                    pass
                elif 1 < i:
                    if int(self.list[i][0]) <= self.weight < int(self.list[i][1]):
                        if "동일지역" in select.packge:
                            return str(int(self.list[i][2])+1300)+"원"

                        elif "타지역" in select.packge:
                            return str(int(self.list[i][3])+1300) + "원"

class screen:
    def screen1(self, list1, list2):
        print('┌─────────────────────────────────────────────────────┐')
        print('                  보이는 우체국 세비스')
        print('     ─────────────────────────────────────────       ')
        for i, j in enumerate(list1):
            print('\t', i + 1, '.', j, list2[i], sep='')
            list2[i] = ' '
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('└───────────────────────────────────────────────────┘')

    def screen2(self, list1, str1, str2, weight, function):
        print('┌─────────────────────────────────────────────────────┐')
        print('                  보이는 우체국 세비스')
        print('     ─────────────────────────────────────────       ')
        print('\t', list1[0], str1)
        print("\t 소지하고 있는 우편의 무게 : " + str(weight) + str2)
        print('\t', function)
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('└───────────────────────────────────────────────────┘')

    def screen3(self, list1, str1, weight, function):
        print('┌─────────────────────────────────────────────────────┐')
        print('                  보이는 우체국 세비스')
        print('     ─────────────────────────────────────────       ')
        print('\t', list1[0], list1[1], str1)
        print("\t 소지하고 있는 우편의 무게 : " + str(weight) + 'kg')
        print('\t', function)
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('└───────────────────────────────────────────────────┘')

class control:
    def __init__(self,list):
        self.list = list
        self.a =0
        self.this_list = []

        for i in range(len(self.list)):
            self.this_list.append(' ')

        self.this_list[self.a] = ' <<-'

    def up(self):
        time.sleep(0.1)
        self.a -= 1

        # for i in range(len(self.list)):
        #     self.this_list.append(" ")

        if self.a == len(self.list):
            self.a = 0

        elif self.a == -1:
            self.a =len(self.list)-1

        self.this_list[self.a] = ' <<-'


        screen.screen1(self.list,self.this_list)

    def down(self):
        time.sleep(0.1)
        self.a+=1

        # for i in range(len(self.list)):
        #     self.this_list.append(" ")

        if self.a == len(self.list):
            self.a = 0

        if self.a == -1:
            self.a = len(self.list)-1

        self.this_list[self.a] = " <<-"

        screen.screen1(self.list,self.this_list)

screen = screen()

control1 = control(option_first)
control1_2 = control(option_second1)
control1_3 = control(option_thrid1)
control1_4 = control(option_four1)
control2 = control(option_second2)




delivery=delivery()

class select:
    def __init__(self):
        self.packge = []

    def select1(self): # 택배인지 은행인지
        if control1.a == 0:  # 택배
            screen.screen1(option_second1,control1_2.this_list)

        elif control1.a ==1: # 은행
            screen.screen1(option_second2,control2.this_list)

        control1.a = 0


        for i in range(len(option_first)):
            control1.this_list.append(' ')

        if control1.a == len(option_first):
            control1.a = 0

        if control1.a == -1:
            control1.a = len(option_first) - 1

        control1.this_list[control1.a] = ' <<'

    def select1_1(self):  # 우편, 소포, 택배
        if control1_2.a == 0:  # 우편
            self.packge.append(option_second1[0])
            screen.screen1(option_thrid1, control1_3.this_list)

        elif control1_2.a == 1:  # 소포
            self.packge.append(option_second1[1])
            screen.screen1(option_thrid1, control1_3.this_list)

        elif control1_2.a == 2:  # 택배
            self.packge.append('택배')
            screen.screen1(option_four1, control1_4.this_list)

        control1_2.a = 0

        for i in range(len(option_second1)):
            control1_2.this_list.append(' ')

        if control1_2.a == len(option_second1):
            control1_2.a = 0

        if control1_2.a == -1:
            control1_2.a = len(option_second1) - 1

        control1_2.this_list[control1_2.a] = ' <<'

    def select1_2(self):  # 등기 일반
        weight1 = random.randrange(3, 6000)
        weight = weight1

        if control1_3.a == 0:  # 등기
            if self.packge[0] == '우편':  # 우편
                screen.screen2(self.packge, '등기', 'g', weight, delivery.post('우편.txt', weight).registered())

            elif self.packge[0] == '소포':
                self.packge.append(option_thrid1[control1_3.a])
                screen.screen1(option_four1, control1_4.this_list)

        if control1_3.a == 1:  # 일반
            if self.packge[0] == '우편':  # 우편
                screen.screen2(self.packge, '일반', 'g', weight, delivery.post('우편.txt', weight).usually())

            elif self.packge[0] == '소포':
                self.packge.append(option_thrid1[control1_3.a])
                screen.screen1(option_four1, control1_4.this_list)

        control1_3.a = 0

        for i in range(len(option_thrid1)):
            control1_3.this_list.append(' ')

        if control1_3.a == len(option_thrid1):
            control1_3.a = 0

        if control1_3.a == -1:
            control1_3.a = len(option_thrid1) - 1

        control1_3.this_list[control1_3.a] = ' <<'

    def select1_3(self):
        weight2 = random.randrange(2, 30)
        weight = weight2
        if control1_4.a == 0:  # 동일지역
            if self.packge[0] == '소포':
                if self.packge[1] == '등기':
                    screen.screen3(self.packge, '동일지역', weight, delivery.package('소포.txt', weight).registered())

                elif self.packge[1] == "일반":
                    screen.screen3(self.packge, '동일지역', weight, delivery.package('소포.txt', weight).usually())

            if self.packge[0] == '택배':
                screen.screen2(self.packge, '동일지역', 'kg', weight, delivery.package('택배.txt', weight).usually())


        elif control1_4.a == 1:  # 타지역
            self.packge.append('타지역')
            if self.packge[0] == '소포':
                if self.packge[1] == '등기':
                    screen.screen3(self.packge, '타지역', weight, delivery.package('소포.txt', weight).registered())

                elif self.packge[1] == "일반":
                    screen.screen3(self.packge, '타지역', weight, delivery.package('소포.txt', weight).usually())

            if self.packge[0] == '택배':
                screen.screen2(self.packge, '타지역', 'kg', weight, delivery.package('택배.txt', weight).usually())

        control1_4.a = 0

        for i in range(len(option_four1)):
            control1_3.this_list.append(' ')

        if control1_3.a == len(option_four1):
            control1_3.a = 0

        if control1_3.a == -1:
            control1_3.a = len(option_four1) - 1

        control1_3.this_list[control1_3.a] = ' <<'

select =select()

class back:
    def back1(self):
        screen.screen1(option_first,control1.this_list)
    def back2(self):
        screen.screen1(option_second1,control1_2.this_list)
    def back3(self):
        screen.screen1(option_thrid1,control1_3.this_list)

back = back()


def post_office():
    global key1
    screen.screen1(option_first,control1.this_list)
    key1 +=1


key1 =0
key2 =0
key3 = 0
key4 = 0
key5 =0

post_office()

while key1 == 1:
    put1= input()

    if put1 == 'w':
        control1.up()

    elif put1 =='s':
        control1.down()

    elif put1 == 'k':
        select.select1()
        key2 += 1

        while key2 ==1:
            put2= input()
            if put2 == 'w':
                control1_2.up()

            elif put2 == 's':
                control1_2.down()

            elif put2 == 'k':
                select.select1_1()
                key3 +=1

                if control1_2.a == 0 or control1_2.a ==1:
                    while key3 == 1 :
                        put3 = input()
                        if put3 == 'w':
                            control1_3.up()

                        elif put3 == 's':
                            control1_3.down()

                        elif put3 == 'k':
                            select.select1_2()

                            if '소포' in select.packge:
                                key4 += 1
                                while key4 == 1:
                                    put4 = input()
                                    if put4 == 'w':
                                        control1_4.up()

                                    elif put4 == 's':
                                        control1_4.down()

                                    elif put4 == 'k':
                                        select.select1_3()

                            elif '택배' in select.packge:
                                key5 +=1
                                while key5 == 1:
                                    put5 = input()
                                    if put5 == 'w':
                                        control1_4.up()

                                    elif put5 == 's':
                                        control1_4.down()

                                    elif put5 == 'k':
                                        select.select1_3()
                            else:
                                pass

                        elif put3 == 'l':
                            back.back2()
                            key3 =0

            elif put2 == 'l':
                back.back1()
                key2 = 0


