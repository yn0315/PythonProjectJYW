#페이
# 이용 내역, 송금, 예약 송금, 계좌 저장, 잔액, 충전
## 1. 계좌 등록 (잔액은 랜덤)
## 2. 송금 하기
## 3. 내역 갱신,잔액 갱신
## 4. 송금 했던 계좌 저장 이후 재 사용시 중복 체크

import random
import datetime
import threading
import time

bank_list = ['NH농협','KB국민','신한','카카오뱅크','IBK기업','하나','우체국']

class pay:
    def __init__(self):
        self.account_dict = {} #{은행명:[ {계좌 번호:잔액} , {계좌 번호:잔액} ]}
        self.bank_dict = {}


    def over_bank(self,bank):
        for i in self.bank_dict:
            if i == bank: #이미 등록 된 은행
                return
        self.bank_dict[bank]=[]
        return
    def over_account(self,account): #중복 계좌 번호 검출
        for i in self.bank_dict:
            for j in self.bank_dict[i]:
                for k in j:
                    if account == k:
                        print('이미 있는 계좌 번호 입니다.')
                        return False
        return True

    def new_bank(self,bank,account): #신규 정보 등록
        money = random.randrange(1000,10000,1000) #최초 등록시 보유 금액은 랜덤 으로 결정
        if account.isdigit(): #계좌 번호의 유형이 숫자 형태
            self.over_bank(bank) # 이미 등록 한적 있는 은행 인지 검토
            if self.over_account(account): #이미 등록된 계좌 번호 라면 False 은행에 관련 없이 계좌 번호는 각각 달라야 함
                self.account_dict[account] = money
                self.bank_dict[bank].append(self.account_dict)
                self.account_dict={}
                loading('pass')
            else:
                loading('fail')
        else:
            print('계좌 번호는 숫자만 입력.')

    def send_money(self,bank,account,money): # 출금
        for i in self.bank_dict[bank]:
            for j in i:
                if j == account:
                    num = self.bank_dict[bank].index(i)
                    self.bank_dict[bank][num][j] = self.bank_dict[bank][num][j]-int(money)
                    loading('pass')
                    self.print_account(bank)
                    return

    def charge_money(self,bank,account,money): # 충전
        if money.isdigit() and money >= "0":
            for i in self.bank_dict[bank]:
                for j in i:
                    if j == account:
                        num = self.bank_dict[bank].index(i)
                        self.bank_dict[bank][num][j] = self.bank_dict[bank][num][j]+int(money)
                        self.print_account(bank)
                        return True
            print('일치 하는 계좌가 없습니다.')
            return False
        else:
            print('금액을 정확히 입력 해 주세요')
            return False




    def myself_in(self,bank,account): #매개 변수가 내가 가지고 있는 데이터 내에 존재 하는지
        for i in self.bank_dict[bank]:
            for j in i:
                if j == account:
                    return True
        return False




    def print_bank(self):
        for i in self.bank_dict:
            print(f'   {i}')  #등록된 은행들 출력

    def print_account(self,key):
        print('┌────────────────────┐')
        try:
            for i in self.bank_dict[key]: #계좌별 잔액 확인
                for j in i:
                    print(f'   계좌:{j}    잔액: {i[j]}')
            return True
        except KeyError:
            print('해당 은행은 등록되지 않았습니다.')
            return False
        except Exception as error:
            print(error)
        print('└────────────────────┘')
    def print_bank_account(self):
        print('┌────────────────────┐')
        for i in self.bank_dict:
            print(f'   은행:{i}')
            for j in self.bank_dict[i]:
                for k in j:
                    print(f'   계좌번호:{k}    잔액: {j[k]}')
            print('    ─────────────────')
        print('└────────────────────┘')
    def print_money(self,key,value):
        print('┌────────────────────┐')
        for i in self.bank_dict[key]:
            for j in i:
                if j == value:
                    num = self.bank_dict[key].index(i)
                    print(f'    최대 출금 가능 금액:{self.bank_dict[key][num][j]}원')
                    print('└────────────────────┘')
                    return self.bank_dict[key][num][j]
        print('    일치하는 정보가 없습니다.')
        print('└────────────────────┘')
        return False

    @staticmethod
    def similarity_bank(name):
        for i in bank_list:
            if name in i:
                return i
        return False

class send_record: #현재 시간에 어디로 얼마를 보냈다
    list_record = []  # [  [....], [....], [....], [....]  ]
    time_list = [] # [번호, 이름, 은행, 계좌, 금액, 시간]
    num = 1
    def my_record(self, tp, bank, account, money, tt): # [[번호, 이름, 은행, 계좌 , 금액 , 시간], [.....]]
        self.time_list.append(self.num) #번호
        self.time_list.append(tp) #유형
        self.time_list.append(bank) #은행
        self.time_list.append(account) #계좌
        self.time_list.append(money) #돈
        self.time_list.append(tt) #시간

        self.list_record.append(self.time_list)
        self.time_list = []
        self.num += 1

    def print_record(self):
        if len(self.list_record) > 10:
            self.list_record.pop(0) #최근 기록 10개 까지만 출력
        print('                  <입출금 내역>')
        print('┌───────────────────────────────────────────────────────────┐')
        print('　번호    이름 　 　    　　은행　　　  　계좌 번호　　 　　금액       　　　시간')
        for i in self.list_record:
            for j in i:
                if type(j) == str:
                    if len(j) < 7:
                        x = 7 - len(j)
                        j += ("　"*x)
                    print(f'   {j}',end="  ")
                else:
                    print(f'   {j}',end=" ")
            print()

        print('└───────────────────────────────────────────────────────────┘')
    def over_record(self,bank,account):
        cnt=0
        for i in self.list_record:
            for j in i:
                if type(j) == str:
                    if j == bank:
                        cnt +=1
                    if account in j: #유사성 검토
                        cnt +=1
                    if cnt >= 2: #은행과 계좌의 유사성이 맞으면
                        print(f'은행명:{bank} 의')
                        print(f'계좌 번호:{j}는 보낸 기록이 있습니다.')
                        return j

            cnt = 0
        return "pass"

class deposit: # 확률적 으로 강제 입금

    human = ['사람1', '누군가', '친구', '가족', '사람2', '사람3', '사람4']
    opponent_list = ['0', '0', '0']

    def opponent_my(self,bank,account,money): # 입금 은행,계좌가 개인 정보에 존재 하면 담을 리스트
        self.opponent_list = [bank, account, money]

    def reset_list(self): #리스트 초기화
        self.opponent_list = ['0', '0', '0']

    def gift_pay(self): #일정 확률로 보유 계좌 정보중 랜덤 으로 입금
        try:
            gen = random.randrange(100)
            if gen >= 70:
                m=random.randrange(500,50000,500) #입금 시킬 돈
                key = list(p.bank_dict.keys())
                rand_bank = random.sample(key,k=1) #등록된 은행중 입금될 은행
                rand_account = random.sample(p.bank_dict[rand_bank[0]],k=1) # [ {계좌 번호:금액} ]
                account=list(rand_account[0].keys())
                for i in p.bank_dict[rand_bank[0]]:
                    for j in i:
                        if j == account[0]:
                            num = p.bank_dict[rand_bank[0]].index(i)
                            p.bank_dict[rand_bank[0]][num][j] = p.bank_dict[rand_bank[0]][num][j] + m
                            print(f'\n{rand_bank[0]}은행의 {account[0]}으로 {m}원이 입금되었습니다.')
                            ti = datetime.datetime.now()
                            ti = str(ti)
                            ti = ti[:-7]
                            m = str(m)
                            m = '+'+m
                            h = random.sample(self.human,k=1)
                            record.my_record(h[0]+" -> 나", rand_bank[0], account[0], m, ti)
                            return
        except Exception as error:
            # print(error)
            return

gift = deposit()
record = send_record()

# 은행, 계좌 번호
def start_frame1():
    print('┌────────────────────┐')
    print('                Py Pay               ')
    print()
    print()
    print('   1. 신규 계좌 등록')
    print('   2. 송금 하기')
    print('   3. 내역 및 잔액 확인')
    print('   4. 등록된 계좌 확인')
    print('   5. 충전 하기')
    print('└────────────────────┘')
    u = input('번호 선택>')
    return u

def frame1(): #계좌 등록
    global bank_list
    print('┌────────────────────┐')
    for i in bank_list:
        print(f'    {i}')
    print('    어떤 은행을 연결 할까요')
    user_bank = input('>')
    for i in bank_list:
        if user_bank in i:
            print(i,'은행이 선택 되었습니다.')
            print('계좌 번호를 입력 해 주세요')
            user_account = input(">")
            p.new_bank(i,user_account)
            return
    print('등록 가능한 은행이 없습니다.')


def frame2(): #송금 하기
    print('┌────────────────────┐')
    print('     출금될 은행과 계좌 번호 선택')
    p.print_bank()
    key = input("   은행명>")
    bank = p.similarity_bank(key)
    if bank == False:
        print('거래 가능한 은행이 없습니다.')
        return
    print(bank,'은행이 선택 되었습니다.')

    if p.print_account(bank):
        value = input("   계좌 번호 입력>")
        print('└────────────────────┘')
        money = p.print_money(bank, value)
        if money == False:
            return
        print('┌─────────────────────────────────────┐')
        print('    송금할 은행과 계좌 번호 입력')
        for i in bank_list:
            print(f'   {i}')
        name = input('   은행명 >')
        num = input('   계좌 번호 >')
        name = p.similarity_bank(name)
        if name == False:
            print('거래 가능한 은행이 없습니다.')
            return
        if num.isdigit():
            pass
        else:
            print('계좌 번호는 숫자만 입력.')
            return
        re = record.over_record(name,num)
        if re.isdigit():
            print("해당 계좌 번호를 사용 하시겠습니까?>")
            print(' 1. 사용함')
            print(' 1. 사용 안함')
            a = input(" 1 or 2 >")
            if a == '1':
                print('사용함')
                num = re
            elif a =='2':
                print('사용 안함')
            else:
                print('')
        m = input("   출금 금액>")
        human = '상대방 에게'

        if p.myself_in(name,num): #내가 가지고 있는 은행과, 계좌 번호 라면 True 반환
            print(f'입력 하신 은행: {name}')
            print(f'입력 하신 계좌 번호: {num} 은 보유 하신 정보 입니다. ')
            human = '나 에게'
            gift.opponent_my(name,num,m)

        if m.isdigit() and int(money) >= int(m) :
            print(f'   은행명:{name}은행 계좌 번호:{num} 으로 {int(m):,}원 입력했습니다.')
            n2 = datetime.datetime.now()
            n2 = str(n2)
            n2 = n2[:-7]
            record.my_record(human, name, num, m, n2)
        else:
            print(f'    출금 가능 최대 금액은 {money}원 입니다.')
            print('└─────────────────────────────────────┘')
            return
        print('└─────────────────────────────────────┘')
        frame2_1(bank,value,m)

def frame2_1(bank,account,money): #즉시 송금 or 예약 송금 상황
    print('┌────────────────────┐')
    print('   1. 즉시 송금')
    print('   2. 예약 송금')
    select = input(">")
    if select == '1':
        print('즉시 송금을 선택하셨습니다.')
        p.send_money(bank,account,money) # 출금

        if p.myself_in(gift.opponent_list[0],gift.opponent_list[1]): #은행과 계좌 번호가 내 정보와 일치 하면
            p.charge_money(gift.opponent_list[0],gift.opponent_list[1],gift.opponent_list[2])
            gift.reset_list()

        n1 = datetime.datetime.now()
        n1 = str(n1)
        n1 = n1[:-7]
        money = '-' + money
        record.my_record('나', bank, account, money, n1)

    elif select == '2':
        n1 = datetime.datetime.now()
        print('예약 송금을 선택하셨습니다.')
        print(f'현재 시각: {n1}')
        t = input("시간 입력 (단위 : 분)>")
        interval = int(t)*60
        p.send_money(bank, account, money)
        threading.Timer(interval,time_send,args=(bank,account,money)).start()

def time_send(bank,account,money):
    print(bank,'은행',account,'로',end="   ")
    print(money,'원만큼 예약된 송금이 진행 됩니다.')

    if p.myself_in(gift.opponent_list[0], gift.opponent_list[1]):  # 은행과 계좌 번호가 내 정보와 일치 하면
        p.charge_money(gift.opponent_list[0], gift.opponent_list[1], gift.opponent_list[2])
        gift.reset_list()

    n1=datetime.datetime.now()
    n1=str(n1)
    n1=n1[:-7]
    money = '-' + money
    record.my_record('나',bank,account,money,n1)

def frame3(): #내역 및 잔액 확인
    print('┌────────────────────┐')
    p.print_bank_account()
    record.print_record()

def frame5(): #충전 하기
    print('┌────────────────────┐')
    p.print_bank()
    b = input("은행명>")
    for i in bank_list:
        if b in i:
            print(i,'은행이 선택 되었습니다.')
            p.print_account(i)
            a = input("계좌 번호>")
            m = input("충전할 금액>")
            if m.isdigit() and m >= '0': #금액은 숫자 형태 이며 양수 여야 충전이 가능함
                if p.charge_money(i, a, m):
                    print('현재 상태')
                    p.print_bank_account()
                else:
                    print('일치 하는 계좌가 없어 충전에 실패 했습니다.')
                return
    print('일치 하는 은행이 없습니다.')

def gift_timer(): #15초 마다 호출
    gift.gift_pay()
    threading.Timer(15,gift_timer).start()

def loading(pf): # pass / fail
    list_loading = []
    # ..........'　'
    dot = '■'
    num = 0
    for i in range(20):
        list_loading.append('　')
    try:
        for i in range(len(list_loading) + 1):
            print(end='\r')
            print('[', end="")
            for j in list_loading:
                print(f'{j}', end="")
            print(f'] {num}%', end="")
            t=random.randrange(1,3)
            t=t/10
            time.sleep(t)
            num += (100 / (len(list_loading)))
            list_loading[i] = dot
    except:
        if pf == 'pass':
            print(' 성공')
        elif pf =='fail':
            print(' 실패')
        print()

if __name__ == '__main__':
    p = pay()
    gift_timer() #랜덤 자동 입금 함수
    while 1:
        user = start_frame1()
        if user == '1': #신규 계좌 등록
            frame1()
        elif user == '2': #송금 하기
            frame2()
        elif user == '3': #내역 및 잔액 확인
            frame3()
        elif user == '4': #등록된 계좌 확인
            p.print_bank_account()
        elif user == '5':
            frame5()