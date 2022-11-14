
#번호는 1~45

#구입
# 자동 // 수동 // 반자동 (1~5개)지정 //  지정숫자 제외기능


#1040회까지의
#1등 2등 당첨수 평균
#1등 2등 당첨금 평균

#회차별 날짜
#1040회는 11월 4일 기준


#역대 1등 번호중 가장

#txt파일안에는 지정조합/지정제외조합/자동몇개




#모듈
#os로 폴더 파일 생성 함수
#특정 회차 파일 찾아가는 함수

#로또번호 생성함수
#           지정숫자
#           지정제외
#           완전랜덤
#           완전수동

#전체 회차 총 데이터 평균 금액 저장해놓는 함수
#당첨 확인 전에 구매
#당첨 확인전에 구매복권 기대치
#당첨 확인 함수 , 당첨 확인이 완료되면 회차+1
#   총 당첨 금액 산출




import os
import time
import datetime
import random

def all_lotto_number_list_a():
    all_lotto_number_list=[] #모든 로또 번호가 있는 리스트

    for i in range(1,46):
        i=str(i)
        all_lotto_number_list.append(i)

    return all_lotto_number_list

def serch(t1):
    while 1:  # 그냥 t1은 들어가는데 -는 무조건 0 으로 하고 그냥 다른 문자열은 싹다 none으로 느끼게 해야지
        for i in t1:
            if i.isdigit() == False:
                rt = t1.split(i)
                t1 = ''
                for j in rt:
                    t1 += j
            if len(t1) == 0:
                t1 = 'None'
                return t1

        if t1.isdigit() == True:
            t1 = int(t1)
            return t1
        else:  # 공백문자열이라면 그냥 냅둔다.
            return t1

def lotto_win_data():
    lotto_data_all = {}
    ln = 1
    with open('로또당첨번호데이터.txt', 'r', encoding='UTF-8') as file:
        while 1:
            line = file.readline()
            ss = line.split('\t')
            lotto_data_all[ln] = ss
            ln += 1
            if not line:
                break
    a_key = list(lotto_data_all.keys())  # 전체 데이터 줄번호들 1번은 필요없음
    a_key.remove(1)
    # 1등 당첨금 평균 #8번 인덱스가 1등 당첨금
    # 키번호 1번은 필요없다.
    first_total_money = 0
    for i in range(1, 1042):
        first_total_money += serch(lotto_data_all[i][8])
    first_avg = first_total_money / len(a_key)  # 1등 당첨금 평균
    second_total_money = 0
    for i in range(1, 1042):
        second_total_money += serch(lotto_data_all[i][10])
    second_avg = second_total_money / len(a_key)  # 2등 당첨금 평균  번호의 마지막 숫자는 보너스 숫자

    return first_avg, second_avg

def folder_generator(n_cnt):

    df_line=os.getcwd().replace("\\","/") #\를 /로 변경해서 조작하기 편하게 변경 완료

    now_try=1041
    now_try+=n_cnt
    now_try=str(now_try)
    now_try+='회'

    now_try_n = 1041  # 텍스트명
    now_try_n+=n_cnt
    now_try_n=str(now_try_n)+".txt"

    new_line=df_line+'/'+now_try+'/'+now_try_n # #폴더경로/폴더명/텍스트명
    os.mkdir(now_try)
    with open(new_line,'w') as file: #텍스트명/add 작성해라
        file.write(' \n') #폴더명 작성완료
    return new_line

# txt=folder_generator()
def text_adder(num,tt): #가져온 랜덤번호를 해당 경로의 해당 텍스트 파일에서 작성해야한다.
         #num은 가져온 번호 , tt는 리턴된 텍스트파일까지의 경로, tp는 타입(자동, 반자동(지정,제외) 수동)
    with open(tt, 'a') as ntt:
        for i in num:
            ntt.write(i + "\t")
        ntt.write("\n")

def random_numbering(sel,set_cnt,txt,user_list,all_lotto_number_list,auto_list,appoint_in_list,appoint_out_list,manual_list):
                    #sel= 유저의 구매 타입(자동,반자동(포함or제외), 완전수동)
                    #set_cnt=구매 세트 수
                    #user_list=유저가 직접 골랐던 번호들
                    #all_lotto_number_list=전체 로또 번호(1~45번)들어있는 리스트
    # random.sample 사용 예시
    # random.sample([1, 2, 3, 4, 5], k=2)  # 리스트 요소중 랜덤으로 k개 뽑는다
    if sel == 0: #완전자동
        with open(txt,'a') as tp:
            tp.write('자동\n')
        for i in range(set_cnt):
            user_lotto_list=random.sample(all_lotto_number_list,k=6) #완전 자동 생성기
            auto_list.append(user_lotto_list)
            text_adder(user_lotto_list,txt)

    elif sel == 1: #반자동 지정 포함
        with open(txt,'a') as tp:
            tp.write('반자동(지정포함)\n')
        for i in user_list:
            all_lotto_number_list.remove(i) #유저가 고른 숫자가 제외된다 //지정포함이기때문에 완전체는 user_list와 더해진다.

        for i in range(set_cnt):
            user_lotto_list=random.sample(all_lotto_number_list,k=6-len(user_list)) #이때 k는 6개- 유저가 고른숫자 갯수
            user_lotto_list=user_list+user_lotto_list #1회 완성본
            appoint_in_list.append(user_lotto_list)
            text_adder(user_lotto_list,txt)

        for i in user_list: #text에 쓰고 나면 다시 지웠던 번호를 살려준다.
            all_lotto_number_list.append(i)

    elif sel ==2: #반자동 지정 제외
        with open(txt,'a') as tp:
            tp.write('반자동(지정제외)\n')
        for i in user_list:
            all_lotto_number_list.remove(i)  # 유저가 고른 숫자가 제외된다
        for i in range(set_cnt):
            user_lotto_list = random.sample(all_lotto_number_list, k=6)  # 이때 k는 유저가 고른것을 제외한 6개
            appoint_out_list.append(user_lotto_list)
            text_adder(user_lotto_list,txt)

        for i in user_list:  # text에 쓰고 나면 다시 지웠던 번호를 살려준다.
            all_lotto_number_list.append(i)

            #이때 리스트는 user_lotto_list

    elif sel ==6: #완전 수동 생성
        with open(txt,'a') as tp:
            tp.write('완전수동\n')
        user_lotto_list=user_list
        for i in range(set_cnt):
            manual_list.append(user_lotto_list)
            text_adder(user_lotto_list,txt)
        pass #이때는 user_list가 생성번호 그 자체다

def get_money(th,lst,price):
    if len(lst)>=1: #당첨이 있다면
        print('────────────────────────────────────────')
        print(f'{th}등 상금은 {int(price):,}원에 {len(lst)}만큼 당첨 되셨습니다. ')
        print(f'{th}등 총 상금 {int(price)*len(lst):,}원 입니다. ')

        win_p=int(price)*len(lst)
        return win_p
    else:
        return 0

def try_win(winning,bonus,user_buy_type_dict):
    avg_1_2=lotto_win_data()

    first_list=[]
    second_list=[]
    third_list=[]
    fourth_list=[]
    fifth_list=[]
    win_count = 0

    for k in user_buy_type_dict:
        for i in user_buy_type_dict[k]:
            for j in i:
                if j in winning:
                    win_count += 1
            if win_count == 6:  # 1등!
                first_list.append(1)
            elif win_count == 5:  # 5개 일치시
                if bonus in i:  # 보너스 번호가 있다면
                    second_list.append(2)  # 2등
                else:  # 보너스번호가 없다면
                    third_list.append(3)  # 3등
            elif win_count == 4:  # 4등
                fourth_list.append(4)
            elif win_count == 3:  # 5등
                fifth_list.append(5)
            else:  # 꽝!
                pass
            win_count = 0

    fir_m=get_money(1,first_list,avg_1_2[0]) #리턴값은 각각의 당첨금 총액
    se_m=get_money(2,second_list, avg_1_2[1])
    th_m=get_money(3,third_list,1500000)
    fo_m=get_money(4,fourth_list,500000)
    fiv_m=get_money(5,fifth_list,5000)

    total_win_money=fir_m+se_m+th_m+fo_m+fiv_m #총상금





    print(f'총 당첨 금액은 {total_win_money:,}입니다.')

def winning_number(all_lotto_number_list,user_buy_type_dict):
    total_buy_money = 0
    for i in user_buy_type_dict:
        total_buy_money += len(user_buy_type_dict[i]) #시행횟수

    # total_buy_money *= 5000 #사용자의 총 구매 금액
    #각등수별 확률
    #1등 1/8,145,060
    #2등  1/1,357,510
    #3등 1/35,724
    #4등 1/733
    #5등 1/45

    one=total_buy_money*(1/8145060) #각 등수에 대한 기대 확률
    two=total_buy_money*(1/1357510)
    three=total_buy_money*(1/35724)
    four=total_buy_money*(1/733)
    five=total_buy_money*(1/45)

    total_buy_money *= 5000 #사용자의 총 구매 금액

    print(f'총 구매금액은{total_buy_money:,}입니다.')
    print(f'각 등수별 당첨 기대확률은')
    print(f'1등 {one:0.3f}%')
    print(f'2등 {two:0.3f}%')
    print(f'3등 {three:0.3f}%')
    print(f'4등 {four:0.3f}%')
    print(f'5등 {five:0.3f}%')
    print('입니다.')


    print()
    winning = random.sample(all_lotto_number_list, k=7)  # 당첨번호 뽑기는 전체에서 7개 (6개 + 보너스 1개)

    bonus = winning[-1]  # 보너스번호 저장
    winning.pop()  # 위닝에선 보너스번호 팝시킨다 일단 위닝은 6개로 줄어든다

    print('당첨 번호는')
    time.sleep(10)
    for i in winning:
        print(i, end=", ")
    print('보너스', bonus, ' 입니다.')
    try_win(winning,bonus,user_buy_type_dict)

def start():
    count = 0
    all_lotto_number_list = all_lotto_number_list_a()
    now=datetime.datetime.now()
    # print()
    # print('#timedelta로 시간 더하기')
    week=0
    # print(after.strftime(f'%Y{"년"}%m{"월"}%d{"일"}%H{"시"}%M{"분"}%S{"초"}'))
    # print()
    while 1:
        user_buy_type_dict = {}  # 구매타입:[[번호들],[번호들],[번호들],[번호들]]
        auto_list = []  # 자동 번호
        appoint_in_list = []  # 지정 포함 번호
        appoint_out_list = []  # 지정 제외 번호
        manual_list = []  # 수동 번호
        after = now + datetime.timedelta(weeks=week)
        txt=folder_generator(count)
        while 1:
            try:
                print('─────────────────────────────────────────────────')
                print(after.strftime(f'%Y{"년"}%m{"월"}%d{"일"}'))
                print(f'현재 회차 <{1041+count}>')
                print('로또 구매하기')
                print('당첨 확인하러 가기는 777을 입력해주세요')
                print('프로그램 종료는 0을 입력해주세요')
                print('─────────────────────────────────────────────────')
                lotto=input('숫자를 입력해주세요> ')


                if lotto != '777' and lotto != '0': #구매로 향하는 길
                    user_list=lotto.split(" ")


                    if user_list!=[""]:
                        for i in user_list:
                            if i in all_lotto_number_list:
                                pass
                            else: #없는 숫자가 있다면
                                raise NotImplementedError

                    print(user_list)

                    if user_list==[""]:
                        print('입력하신 숫자가 없습니다.')
                        print('자동으로 번호가 생성됩니다.')
                        print('몇 세트를 구매하시겠습니까?')
                        print('─────────────────────────────────────────────────')
                        while 1:
                            set_count=input('숫자를 입력해주세요>')
                            if set_count.isdigit():
                                set_count=int(set_count)
                                break


                        select=0
                        random_numbering(select,set_count,txt,user_list,all_lotto_number_list,auto_list,appoint_in_list,appoint_out_list,manual_list)

                    elif len(user_list)<6: #반자동
                        print('1. 지정 숫자 포함')
                        print('2. 지정 숫자 제외')


                        while 1:
                            select=input('숫자를 입력해주세요>')
                            if select.isdigit():
                                select=int(select)
                                break

                        if select==1: #지정숫자 포함
                            print('지정 숫자 포함을 선택하셨습니다.')
                            print('몇 세트를 구매하시겠습니까?')
                            while 1:
                                set_count=input('숫자를 입력해주세요>')
                                if set_count.isdigit():
                                    set_count=int(set_count)
                                    break

                            random_numbering(select, set_count,txt,user_list,all_lotto_number_list,auto_list,appoint_in_list,appoint_out_list,manual_list)

                        elif select==2:#지정숫자 제외
                            print("지정숫자 제외를 선택하셨습니다.")
                            print('몇 세트를 구매하시겠습니까?')

                            while 1:
                                set_count=input('숫자를 입력해주세요>')
                                if set_count.isdigit():
                                    set_count=int(set_count)
                                    break

                            random_numbering(select, set_count,txt,user_list,all_lotto_number_list,auto_list,appoint_in_list,appoint_out_list,manual_list)

                    elif len(user_list)==6:
                        print('수동으로 번호를 전부 입력하셨습니다.')
                        print('몇 세트를 구매하시겠습니까?')
                        while 1:
                            set_count=input('숫자를 입력해주세요>')
                            if set_count.isdigit():
                                set_count=int(set_count)
                                break

                        select=6
                        random_numbering(select, set_count,txt,user_list,all_lotto_number_list,auto_list,appoint_in_list,appoint_out_list,manual_list)

                elif lotto == '777':
                    count += 1
                    week+=1
                    print('당첨번호를 발표하겠습니다.')
                    break

                elif lotto =='0':
                    print('프로그램을 종료합니다.')
                    break

            except:
                print('숫자는 1~45까지')
                print('6개만 입력가능합니다')
                print('번호별 로 스페이스바를 눌러 띄어 쓰기를 해주세요')
        if lotto=='0':
            break
        else:
            pass
        user_buy_type_dict['자동']=auto_list
        user_buy_type_dict['지정포함']=appoint_in_list
        user_buy_type_dict['지정제외']=appoint_out_list
        user_buy_type_dict['수동']=manual_list
        winning_number(all_lotto_number_list,user_buy_type_dict) #당첨번호 생성
                                                #당첨 확인하러 가기




#start() 주석 해제 하고 실행 하면 실행 가능
#start()





































































