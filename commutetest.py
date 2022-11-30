import datetime
import threading
import sys
import time

class commute:
    def __init__(self):
        self.nameDict = {} # 등록된 사원리스트
        self.doubleDict = {} # 중복된이름 체크
        self.ingDict = [] # 금일하루 사원들 출근, 퇴근, 외출, 복귀 시간
        self.peopleCount = 0 # 총 회원의 수
        self.count = 0 # 사원출결 텍스트에 남길 날짜 (함수로 금일로 변환)

    def Time(self): # 현재 시간
        return datetime.datetime.now()

    def microsecond(self): # 마이크로초
        return datetime.datetime.now().microsecond

    def daytxt(self): # 카운트 현재날짜로 변환 함수
        if self.count != datetime.datetime.now().day:
            self.count = int(datetime.datetime.now().day)
        else:
            pass
        return f'{self.count}일'

    def attendance(self): # 출근시간
        attendancePeople = input("출근할 사람의 성함을 입력해 주세요")
        if self.count != datetime.datetime.now().day:
            self.count = int(datetime.datetime.now().day)
            self.ingDict = [] # 현재 날짜와 self 카운트가 다르다면 ingDict 초기화
        else:
            pass
        if attendancePeople in self.nameDict:
            for i in self.ingDict:
                if i['출근자'] == f'{attendancePeople}':
                    print("중복 출근입니다.")
                    return #self.inter()
            self.ingDict.append({'출근자':f'{attendancePeople}','출근시간':self.Time(),'퇴근시간':0,'외출시간':0,'외출복귀시간':0})
            print(self.ingDict)
        else:
            print("등록되지 않은 사람의 출입을 금합니다.")
        with open(f"{self.daytxt()}출퇴근리스트.txt", 'w', encoding='UTF-8') as self.commuteList:
            for i in self.ingDict:
                self.commuteList.write(str(i) + '\n')


    def closeTime(self): # 퇴근시간
        closeTimePeople = input("퇴근할 사람의 성함을 입력해 주세요")
        for j in self.ingDict:
            if j['출근자'] == f'{closeTimePeople}': # ingDict 출근자 키 안에 퇴근하고자 하는 사람이 있으면
                if j['외출시간'] == 0 and j['외출복귀시간'] == 0:
                    j['퇴근시간'] = self.Time() # 퇴근시간 키 에 현재시간 입력
                    print(self.ingDict)
                    with open(f"{self.daytxt()}출퇴근리스트.txt", 'w', encoding='UTF-8') as self.commuteList:
                        for j in self.ingDict:
                            self.commuteList.write(str(j) + '\n')
                    return #self.inter()
                elif j['외출시간'] != 0 and j['외출복귀시간'] != 0:
                    j['퇴근시간'] = self.Time()  # 퇴근시간 키 에 현재시간 입력
                    print(self.ingDict)
                    with open(f"{self.daytxt()}출퇴근리스트.txt", 'w', encoding='UTF-8') as self.commuteList:
                        for j in self.ingDict:
                            self.commuteList.write(str(j) + '\n')
                    return  # self.inter()
                elif j['외출시간'] != 0 and j['외출복귀시간'] == 0:
                        return

        print('입력하신 사람이 출근처리 되어 있지 않거나 외출 후 복귀처리가 되어 있지 않습니다.')
        #self.inter()


    def add(self):  # 추가
        addName = input("신규가입할 사람의 성함을 입력해주세요")
        with open("회원리스트.txt", 'a', encoding='UTF-8') as peopleList:
            if addName not in self.nameDict: # 신규등록시 새로운사원을 추가 할 때
                self.peopleCount += 1 # 현재 총 사원 수
                self.nameDict.update({f'{addName}':f'{self.microsecond()}'})
                self.doubleDict.update({f'{addName}': 1})
                peopleList.write(f"{self.peopleCount} {addName},{self.nameDict[addName]}\n")
                print(self.nameDict)
            elif addName in self.nameDict: # 신규등록시 중복된 이름이 있을 때
                self.doubleDict[addName] += 1
                self.peopleCount += 1 # 현재 총 사원 수
                self.nameDict.update({f'{addName}{self.doubleDict[addName]}': f'{self.microsecond()}'})
                peopleList.write(f"{self.peopleCount} {addName}{self.doubleDict[addName]},{self.nameDict[f'{addName}{self.doubleDict[addName]}']}\n")
                print(self.nameDict)
        #self.inter()


    def delete(self): # 삭제
        deleteName = input("회원삭제할 사람의 성함을 입력해주세요.")
        nameDictd = list(self.nameDict.keys())
        if deleteName in nameDictd:
            x = nameDictd.index(deleteName) # 등록된 사원리스트에서 삭제할 사원 인덱스 할당
            del self.nameDict[deleteName] # 딕셔너리에서 삭제할 사원 정보 삭제
            print(self.nameDict)
            with open("회원리스트.txt", 'r', encoding='UTF-8') as f:
                lines = f.readlines()
            lines.pop(x)
            lines2 = []
            for i in lines:
                lines2.append(i.split(maxsplit=1)[1]) # 회원리스트.txt에서 앞 숫자와 회원정보를 나눠 회원정보만 lines2리스트 안에 넣기
            lines3 = []
            for i , j in enumerate(lines2, start=1):
                lines3.append(f'{i} {j}') # lines3에 1부터 시작하는 번호를 추가해 lines2에 있는 회원정보와 함께 넣기
            with open("회원리스트.txt", 'w', encoding='UTF-8') as ref:
                ref.write(''.join(lines3)) # 회원리스트를 w로 열어 초기화 후 lines3에 있는 내용물 새로 쓰기
            self.peopleCount -= 1 # 현재 총 사원 수 -1

        else:
            print("삭제하고자 하는 이름이 명단에 없습니다.")


    def goOut(self): # 외출
        goOutPeople = input("외출 할 사람의 이름을 입력해 주세요")
        for j in self.ingDict:
            if j['출근자'] == f'{goOutPeople}' and j['퇴근시간'] == 0:
                j['외출시간'] = self.Time()
                print(self.ingDict)
                with open(f"{self.daytxt()}출퇴근리스트.txt", 'w', encoding='UTF-8') as self.commuteList:
                    for j in self.ingDict:
                        self.commuteList.write(str(j) + '\n')
                return #self.inter()

        print('입력하신 사람이 출근처리가 되어 있지 않거나 이미 퇴근한 사람입니다..')
        #self.inter()


    def goIn(self): #외출복귀
        goInPeople = input("외출복귀할 사람의 이름을 입력해주세요.")
        for j in self.ingDict:
            if j['출근자'] == f'{goInPeople}' and j['퇴근시간'] == 0 and j['외출시간'] != 0:
                j['외출복귀시간'] = self.Time()
                print(self.ingDict)
                with open(f"{self.daytxt()}출퇴근리스트.txt", 'w', encoding='UTF-8') as self.commuteList:
                    for j in self.ingDict:
                        self.commuteList.write(str(j) + '\n')
                return #self.inter()

        print('입력하신 사람의 출근처리 나 외출처리가 되어 있지 않습니다.')
        #self.inter()


    def allTime(self): # 총 출근시간 합산
        allTimeName = input('출근시간 합산할 사람의 성함을 입력해주세요.')
        # try:
        if allTimeName in self.nameDict:
            for i in self.ingDict:
                if i['출근자'] == f'{allTimeName}':
                    closetime = i['퇴근시간']
                    opentime = i['출근시간']
                    gointime = i['외출복귀시간']
                    goouttime = i['외출시간']
                    runTime = closetime - opentime # 근무 시간 계산
                    if runTime == 0:
                        print("입력하신 사람의 출퇴근 기록이 없습니다.")
                        return
                    gooutTime = gointime - goouttime # 외출 시간 계산
                    if gooutTime == 0:
                        alltime = runTime
                        print(f'금일 출근자 {allTimeName}님의 총 근무시간은 {alltime} 입니다')
                        return
                    else:
                        alltime = runTime - gooutTime # 근무시간 - 외출시간
                        print(f'금일 출근자 {allTimeName}님의 총 근무시간은 {alltime} 입니다')
                        return
            #self.inter()
        else:
            print("등록된 사람이 아닙니다.")
            return

    def inter(self):
        while 1:
            print()  # 5. 신규, 6. 삭제, 7. 합산 입력은되지만 보여지지 않음.
            print('1. 출근, 2, 퇴근, 3. 외출, 4. 외출복귀, 5. 신규, 6. 삭제, 7. 합산, 8. 프로그램 종료')
            select = input("메뉴를 입력해주세요")

            if select == '1' or select == '출근':
                thread = threading.Thread(target=self.attendance())
                thread.start()
            elif select == '2' or select == '퇴근':
                thread = threading.Thread(target=self.closeTime())
                thread.start()
            elif select == '3' or select == '외출':
                thread = threading.Thread(target=self.goOut())
                thread.start()
            elif select == '4' or select == '외출복귀':
                thread = threading.Thread(target=self.goIn())
                thread.start()

            elif select == '5' or select == '신규':
                self.add()
            elif select == '6' or select == '삭제':
                self.delete()
            elif select == '7' or select == '합산':
                self.allTime()
            elif select == '8':
                for i in range(3, 0, -1):
                    print(f"{i}초 뒤 프로그램이 종료 됩니다.", f' "...{i}"', end="")
                    time.sleep(1)
                    print(end='\r')
                print("0000000000000000000000000000000000000")
                sys.exit()

            else:
                print("잘못된 입력 방식입니다.")
                self.inter()




x = commute()
x.inter()





