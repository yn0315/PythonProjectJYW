

# 키오스크 만들기
#반복문의 탈출시기 정확히 판단할것

# 선 그어둔 길이는 콘솔창 해상도 기준
# 파이참 내부에서 실행시 길이와 위치가 다름

# 카테고리
# 1. 버거
# 2. 사이드
# 3. 디저트
# 4. 음료+맥카페
# 5. 맥런치

import datetime #현재 시간정보 받아오기 위한 datetime 모듈
import os #콘솔창에서 다음 화면으로 이동시 프레임 변경을 위해 os 모듈 선언
now=datetime.datetime.now()  #현재 시간과 분을 받아와 now 변수에 저장

user_select='1' #메뉴판 화면에서 유저가 선택할 입력으로 1번을 그냥 선언
#햄버거 종류
burger_list=['빅맥','맥스파이시상하이버거','1955버거','베이컨토마토디럭스','맥크리스피디럭스','맥크리스피클래식','맥치킨모짜렐라','맥치킨',
                 '더블불고기버거','에그불고기버거','불고기버거','더블필레오피쉬','필레오피쉬','슈슈버거','슈비버거','쿼터파운더치즈',
                 '더블쿼터파운더치즈','트리플치즈버거','더블치즈버거','치즈버거','햄버거'] #햄버거 메뉴리스트
burger_price={'빅맥':4900,'맥스파이시상하이버거':4900,'1955버거':6000,'베이컨토마토디럭스':5800,'맥크리스피디럭스':6700,'맥크리스피클래식':5900,
              '맥치킨모짜렐라':5000,'맥치킨':3500,'더블불고기버거':4500,'에그불고기버거':3500,'불고기버거':2500,'더블필레오피쉬':5200,'필레오피쉬':3700,
              '슈슈버거':4700,'슈비버거':5800,'쿼터파운더치즈':5500,'더블쿼터파운더치즈':7400,'트리플치즈버거':5800,'더블치즈버거':4500,
              '치즈버거':2500,'햄버거':2200} #버거_가격 = { 버거이름 : 가격 }

#사이드 종류
side_list=['맥너겟','맥스파이시치킨텐더','치즈스틱','상하이치킨스낵랩','치킨토마토스낵랩','후렌치후라이','애플파이','코울슬로']
side_price={'맥너겟':2200,'맥스파이시치킨텐더':2700,'치즈스틱':2500,'상하이치킨스낵랩':2400,'치킨토마토스낵랩':2200,
            '후렌치후라이':1800,'애플파이':1300,'코울슬로':1900} #사이드 가격들
#디저트종류
dessert_list=['맥플러리','선데이아이스크림','오레오아포가토','아이스크림콘','초코콘']
dessert_price={'맥플러리':2700,'선데이아이스크림':1800,'오레오아포가토':3200,
               '아이스크림콘':900,'초코콘':1200} #디저트 가격
#음료종류
drink_list=['카페라떼','아메리카노','바닐라라떼','카푸치노','에스프레소','우유','생수','아이스드립커피','콜라','사이다','쉐이크']
drink_price={'카페라떼':3000,'아메리카노':2500,'바닐라라떼':3500,'카푸치노':3000,'에스프레소':1700,
             '우유':1500,'생수':1200,'아이스드립커피':1500,'콜라':1500,'사이다':1500,'쉐이크':2800} #음료가격

b=0
bbb_list=[] #선택한 버거이름을 저장하고 같은 이름은 몇개인지 선택한 버거가 반복선택 인지 알기위한 리스트
buy_burger_list=[] #고른 햄버거 저장공간
buy_side_list=[] #고른 사이드 저장공간
buy_dessert_list=[] #고른 디저트 저장공간
buy_drink_list=[] #고른 음료 저장공간
buy_list=[] #고른 모든 메뉴들 저장


burger_dic={} #버거 종류와 수량 저장 { 버거이름 : 수량 }
side_dic={}  #사이드 종류와 수량 { 사이드이름 : 수량 }
dessert_dic={} #디저트 종류와 수량 { 디저트이름 : 수량 }
drink_dic={} #음료 종류와 수량 { 음료이름 : 수량 }

burger_matter_dic={} #버거 속재료 구성 저장 {버거이름 : 재료들~}
final_burger_dict = {} #최종적으로 버거의 모든 정보를 다 저장할공간 {버거이름 : [재료],[세트],수량 , 버거이름:[재료],[세트],수량 }


real_h=str(now.hour)  # 시간을 문자열로
ti_min=str(now.minute) # 분을 문자열로

overlap=''  #버거 이름 (숫자)해주는 역할, 나중에 변함

def mac_time(a): #맥런치 시간에서만 등장시키기 위해 만든 함수,  #문자열상태 10시30분 = 1030
    if ti_min <'10':   #분단위가 10아래 한자리 숫자면 앞에 0을 넣어서 1101 과 같은 숫자를 만든다
        real_m='0'+ti_min
    else:
        real_m=ti_min
    real_ti=real_h+real_m #현재시간의 형태를 문자열로 '1030'과 같이 만들어준다.
    if real_ti>='1030' and '1400'>=real_ti:  # 10시30분을 1030으로 변환하고 14시를 1400으로 만들어 맥런치 타임인지 판단
        print(a) #매개변수로 작성하고 싶은 문구 작성



def burger_menu():  #카테고리 : 버거 메뉴판
    print('┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐')
    print('                                      < 버거 >                                        ')
    print()
    print('  0. 이전ㅤㅤㅤㅤㅤ빅맥ㅤㅤㅤㅤㅤ4900원ㅤㅤㅤㅤ트리플치즈버거ㅤㅤ5800원ㅤㅤㅤㅤ맥스파이시상하이버거ㅤ4900원')
    print('  1. 버거ㅤㅤㅤㅤㅤ맥치킨ㅤㅤㅤㅤ3500원ㅤㅤㅤㅤ맥치킨모짜렐라ㅤㅤ5000원ㅤㅤㅤㅤ맥크리스피클래식ㅤㅤㅤ5900원')
    print('  2. 사이드ㅤㅤㅤㅤ1955버거ㅤㅤ  6000원ㅤㅤㅤㅤ불고기버거ㅤㅤㅤㅤ2500원ㅤㅤㅤㅤ쿼터파운더치즈ㅤㅤㅤㅤ5500원')
    print('  3. 디저트ㅤㅤㅤㅤ슈슈버거ㅤㅤㅤ4700원ㅤㅤㅤㅤ더블불고기버거ㅤㅤ4500원ㅤㅤㅤㅤ베이컨토마토디럭스ㅤㅤ5800원')
    print('  4. 음료ㅤㅤㅤㅤㅤ슈비버거ㅤㅤㅤ5800원ㅤㅤㅤㅤ에그불고기버거ㅤㅤ3500원ㅤㅤㅤㅤ맥크리스피디럭스ㅤㅤㅤ6700원')
    print('                   치즈버거ㅤㅤㅤ2500원ㅤㅤㅤㅤ더블필레오피쉬ㅤㅤ5200원ㅤㅤㅤㅤ더블쿼터파운더치즈ㅤㅤ7400원')
    print('                   더블치즈버거ㅤ4500원ㅤㅤㅤㅤ필레오피쉬ㅤㅤㅤㅤ3700원ㅤㅤㅤㅤ햄버거ㅤㅤㅤㅤㅤㅤㅤㅤ2200원')
    mac_time('  7. 맥런치')
    print('  9. 주문취소                                               일반세트 1800원  라지세트 2400원 추가입니다. \n')
    mac_time('          지금은 맥런치 시간입니다. 맥런치 세트는 저렴하게 이용가능합니다.\n')
    print('└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘')
    print('  5. 선택 완료')
# 버거 메뉴 화면

def side_menu(): #카테고리 : 사이드 메뉴판
    print('┌─────────────────────────────────────────────────┐')
    print('                   <사이드>')
    print()
    print('  0. 이전ㅤㅤㅤㅤ맥너겟ㅤㅤㅤㅤㅤㅤㅤ2200원')
    print('  1. 버거ㅤㅤㅤㅤ맥스파이시치킨텐더ㅤ2700원')
    print('  2. 사이드ㅤㅤㅤ치즈스틱ㅤㅤㅤㅤㅤㅤ2500원')
    print('  3. 디저트ㅤㅤㅤ상하이치킨스낵랩ㅤㅤ2400원 ')
    print('  4. 음료ㅤㅤㅤㅤ후렌치후라이ㅤㅤㅤㅤ1800원 ')
    print('     ㅤㅤㅤㅤㅤㅤ코울슬로ㅤㅤㅤㅤㅤㅤ1900원 ')
    mac_time('  7. 맥런치')
    print('  9. 주문취소')
    print('└─────────────────────────────────────────────────┘')
    print('  5. 선택 완료')
# 사이드 메뉴화면

def dessert_menu():  #카테고리 : 디저트 메뉴판
    print('┌──────────────────────────────────────────────┐')
    print('                 <디저트>')
    print()
    print('  0. 이전ㅤㅤㅤㅤ맥플러리ㅤㅤㅤㅤㅤ2700원')
    print('  1. 버거ㅤㅤㅤㅤ선데이아이스크림ㅤ1800원')
    print('  2. 사이드ㅤㅤㅤ오레오아포가토ㅤㅤ3200원')
    print('  3. 디저트ㅤㅤㅤ아이스크림콘ㅤㅤㅤ900원 ')
    print('  4. 음료ㅤㅤㅤㅤ초코콘ㅤㅤㅤㅤㅤㅤ200원 ')
    mac_time('  7. 맥런치')
    print('  9. 주문취소')
    print('└──────────────────────────────────────────────┘')
    print('  5. 선택 완료')
#디저트 메뉴화면

def drink_menu():
    print('┌───────────────────────────────────────────────────────────────┐')
    print('                      <음료>')
    print()
    print('  0. 이전ㅤㅤㅤㅤㅤ카페라떼ㅤㅤㅤㅤ3000원ㅤㅤㅤ우유ㅤㅤ1500원')
    print('  1. 버거ㅤㅤㅤㅤㅤ아메리카노ㅤㅤㅤ2500원ㅤㅤㅤ생수ㅤㅤ1200원')
    print('  2. 사이드ㅤㅤㅤㅤ바닐라라떼ㅤㅤㅤ3500원ㅤㅤㅤ쉐이크ㅤ2800원')
    print('  3. 디저트ㅤㅤㅤㅤ카푸치노ㅤㅤㅤㅤ3000원ㅤㅤㅤ콜라ㅤㅤ1500원')
    print('  4. 음료ㅤㅤㅤㅤㅤ에스프레소ㅤㅤㅤ1700원ㅤㅤㅤ사이다ㅤ1500원')
    print('                 ㅤ아이스드립커피ㅤ1500원')
    mac_time('  7. 맥런치')
    print('  9. 주문취소                             ')
    print('└───────────────────────────────────────────────────────────────┘')
    print('  5. 선택 완료')
# 음료 메뉴화면

def mac_lunch():
    if ti_min <'10':   #분단위가 10아래 한자리 숫자면 앞에 0을 넣어서 1101 과 같은 숫자를 만든다
        real_m='0'+ti_min
    else:
        real_m=ti_min
    real_ti=real_h+real_m
    if real_ti>='1030' and '1400'>=real_ti: #맥런치 시간에만 해당 메뉴판 출력
        print('┌────────────────────────────────────────────────────────────┐')
        print('                       <맥런치>')
        print()
        print('  0. 취소ㅤㅤㅤㅤ빅맥세트ㅤㅤㅤㅤㅤㅤㅤㅤ5200원')
        print('  1. 버거ㅤㅤㅤㅤ맥스파이시상하이버거세트ㅤㅤㅤㅤㅤ5200원')
        print('  2. 사이드ㅤㅤㅤ1955버거세트ㅤㅤㅤㅤㅤㅤ6200원')
        print('  3. 디저트ㅤㅤㅤ베이컨토마토디럭스세트  6000원 ')
        print('  4. 음료')
        print('  7. 맥런치')
        print('  9. 주문취소 ')
        print('└────────────────────────────────────────────────────────────┘')
        print('  5.선택완료')
    else: #맥런치 시간에 해당되지 않으면 메뉴판출력하지 않음
        burger_menu()
        print('지금은 맥런치 시간이 아닙니다.')


def start_frame1():  #식사장소 place를 글로벌 변수로 선언 = 후에 가져오기 위함

    global place
    while 1:

        print('┌───────────────────────────────────────────────────────┐')
        print()
        print('                   맥도날드 키오스크                   ')
        print()
        print('             1.매장              2.포장               ')
        print()
        print('└───────────────────────────────────────────────────────┘')
        print()
        print('(번호로만 입력)')
        place=input('식사장소를 선택해주세요 ▶')
        if place.isdigit() == True: #입력이 숫자형태인지 판단
            place=int(place) #숫자형태가 맞다면 int형으로 전환
            if place==1 or place ==2:
                break
            else:
                os.system('cls')
                print('1 또는 2를 입력해주세요')
        else:
            os.system('cls')
            print('번호로 입력해주세요.')




def select_menu(num): #num은 유저의 카테고리선택 번호를 가져옴 해당 번호에 맞게 아래의 카테고리 출력
    if num == '1':
        burger_menu()
    elif num =='2':
        side_menu()
    elif num =='3':
        dessert_menu()
    elif num =='4':
        drink_menu()
    elif num=='7':
        mac_lunch()
# 입력받은 숫자에 따라 카테고리출력

# 버거재료구성 함수
def burger_matter(burger_name):
    while 1:
        os.system('cls') #콘솔화면 지우는 함수
        print('┌───────────────────────────────────────────────────────────────┐')
        print('                             <버거 재료 구성>')
        print('  1.기본  2. 야채1   3. 야채2   4. 소스  5. 패티  ')
        print('  6.이전     7.완료')
        print('└───────────────────────────────────────────────────────────────┘')
        print(f'    {burger_name}의 현재 구성은{burger_matter_dic[burger_name]}입니다.')
        semi_matter = input('    변경하실 재료를 선택해주세요 ▶')

        if semi_matter == '1':
            print('기본구성을 선택하셨습니다.')
            burger_matter_dic[burger_name]=['기본야채1', '기본야채2', '기본소스', '기본패티'] #여태 변경된 재료정보를 기본설정으로 되돌림
        elif semi_matter == '2':  # 야채1에 대한 변경여부
            print('┌────────────────────────┐')
            print('   1. 양상추 > 양배추')
            print('   2. 양상추 > 상추 ')
            print('   3. 변경안함')
            print('└────────────────────────┘')
            va = input('   변경하실 야채1을 선택해주세요 ▶')
            if va == '1':
                burger_matter_dic[burger_name][0] = '양배추'  #burger_matter_dic은 {버거이름 : [재료1,재료2] }의 구조
            elif va == '2':
                burger_matter_dic[burger_name][0] = '상추'#burger_matter_dic[버거이름]은 [재료1,재료2,재료3] 과 같은 리스트 구조이기때문에 해당 리스트의 인덱스 번호로 접근해 값변경
            os.system('cls')
        elif semi_matter == '3':  # 야채2에 대한 변경여부
            print('┌────────────────────────┐')
            print('   1. 양파 > 적양파')
            print('   2. 양파 > 피클')
            print('   3. 변경안함')
            print('└────────────────────────┘')
            va = input('   변경하실 야채2를 선택해주세요 ▶')
            if va == '1':
                burger_matter_dic[burger_name][1] = '적양파' #야채1변경과 동일한 원리 아래도 동일
            elif va == '2':
                burger_matter_dic[burger_name][1] = '피클'
            os.system('cls')
        elif semi_matter == '4':  # 소스변경에 대한여부
            print('┌────────────────────────┐')
            print('   1. 단맛')
            print('   2. 매운맛')
            print('   3. 짠만')
            print('   4. 변경안함')
            print('└────────────────────────┘')
            va = input('   변경하실 소스를 선택해주세요 ▶')
            if va == '1':
                burger_matter_dic[burger_name][2] = '단맛'
            elif va == '2':
                burger_matter_dic[burger_name][2] = '매운맛'
            elif va == '3':
                burger_matter_dic[burger_name][2] = '짠맛'
            os.system('cls')
        elif semi_matter == '5':  # 패티변경에 대한 여부
            print('┌────────────────────────┐')
            print('   1. 불고기패티')
            print('   2. 치킨패티')
            print('   3. 변경안함')
            print('└────────────────────────┘')
            va = input('   변경하실 패티를 선택해주세요 ▶')
            if va == '1':
                burger_matter_dic[burger_name][3] = '불고기패티'
            elif va == '2':
                burger_matter_dic[burger_name][3] = '치킨패티'
            os.system('cls')
        elif semi_matter == '6':  # 이전으로 돌아가기 입력정보 초기화
            print('재료구성을 기본으로 되돌립니다.')
            burger_matter_dic[burger_name] = ['기본야채1', '기본야채2', '기본소스', '기본패티']
            break
        elif semi_matter == '7':  # 완료 입력정보 저장후 다음으로
            break
#사이드토핑 처리함수
def side_topping(i):
    while 1:
        os.system('cls')
        print('┌────────────────────────────────┐')
        print('        <감자튀김 토핑변경>')
        print('   1. 기본')
        print('   2. 소금추가')
        print('   3. 이전')
        print('   4. 완료')
        print('└────────────────────────────────┘')
        print(f'현재 감자튀김은 {set_burger[i][0]}입니다.')
        side=input('선택해주세요 ▶ ')
        if side =='1':
            print('1. 기본을 선택하셨습니다.')
            if '+소금추가' in set_burger[i][0]: #감튀 라는 문자열 요소에 +소금추가 라는 글자가 있다면
                set_burger[i][0].split('+')    #set_burger[i] 는 [감튀,콜라] 의 리스트형태 0번 인덱스로 감튀요소에 접근 이제보니 의미 없는짓
                set_burger[i][0]=set_burger[i][0][:-5] # +소금추가는 5글자를 지우고 감튀만 다시 저장 > 기본으로 되돌림
            else:
                pass
        elif side == '2':
            print('2. 소금추가를 선택하셨습니다.')
            if '+소금추가' in set_burger[i][0]: #이미 감튀 문자열에 소금추가가 존재한다면 새로 추가하지않고 그냥 넘김
                print('이미 선택하셨습니다.')
            else:
                set_burger[i][0] += '+소금추가' #감자튀김 이라는 문자열에 +소금추가라는 문자열이 들어감
        elif side == '3':
            print('3. 이전으로 돌아갑니다.')
            if '+소금추가' in set_burger[i][0]:
                set_burger[i][0].split('+')
                set_burger[i][0]=set_burger[i][0][:-5] #이전으로 돌아가면 기본으로 설정초기화
            else:
                pass #의미없는문장
            break
        elif side == '4':
            print('선택완료')
            break
#음료변경 처리함수
def drink_change(i):
    while 1:
        os.system('cls')
        print('┌────────────────────────┐')
        print('        <음료 변경>')
        print('  1. 기본 (콜라)')
        print('  2. 사이다.')
        print('  3. 이전')
        print('  4. 완료')
        print('└────────────────────────┘')
        print(f'  현재 음료는 {set_burger[i][1]}입니다.') #set_burger[i]는 [감튀,콜라]형태의 리스트 1번 인덱스는 콜라라는 요소를 불러옴
        drink=input('선택해주세요  ▶')
        if drink =='1':
            print('1. 기본(콜라)를 선택하셨습니다.')
            if setting =='2':
                set_burger[i][1] = '콜라' #burger_matter(), side_topping() 함수와 같은원리로 동작
            elif setting =='3':
                set_burger[i][1] ='콜라(L)'
        elif drink =='2':
            print('2.사이다를 선택하셨습니다')
            if setting =='2': #일반세트
                set_burger[i][1]='사이다'
            elif setting =='3': #라지세트
                set_burger[i][1]='사이다(L)'
        elif drink =='3':
            print('3."이전"를 선택하셨습니다.')
            if setting =='2':
                set_burger[i][1]='콜라'
            elif setting =='3':
                set_burger[i][1]='콜라(L)'
            break
        elif drink=='4':
            print('4."완료"를 선택하셨습니다.')
            break
        else:
            print('번호를 정확히 입력해주세요')

#########################################################

# 변수 초기화
def clear_list():
    buy_list.clear()
    burger_dic.clear()
    side_dic.clear()
    dessert_dic.clear()
    drink_dic.clear()
    bbb_list.clear()
    buy_burger_list.clear()
    buy_side_list.clear()
    buy_drink_list.clear()
    buy_dessert_list.clear()
    final_burger_dict.clear()
    b = 0

# 지금 선택한 메뉴가 무엇인지 보여주는 함수
def what_select(buy_list, buy_category, category_dic):
    if buy_list[-1] in buy_category:  # 있다면 이미 한번 골랐던건지
        category_dic[buy_list[-1]] += 1  # 한번 고른거면 수량을 올림
    else:  # 선택한 사이드가 처음선택?
        buy_category.append(buy_list[-1])  # 중복으로 걸리게 구매사이드리스트에 추가
        category_dic[buy_list[-1]] = 1  # 없던거면 수량을 1로 해라
    os.system('cls')

# 메뉴 가격 합산을 위한 함수
def total_sum(category_dic, category_price):
    global total_price
    for i in category_dic:
        c_price = category_dic[i] * category_price[i]
        total_price += c_price

# 장바구니 정보 불러오는 함수
def come_bag(j, category_dic, category_price):
    j += 1
    print(f'  {j}.{i}')
    print(f'            수량:{category_dic[i]}개')
    print(f'            가격:{category_dic[i] * category_price[i]}원')
    print()

# 정보삭제 함수
def delete_data(category_dic, buy_category_list,change_menu):
    del category_dic[change_menu]  # 사이드 정보들삭제
    buy_category_list.remove(change_menu)

    #----------------------------------------------------------------------------아래는 코드 실행시 출력이 시작되는 부분--------------------------------------

start_frame1() #식사장소 여부 입력받고
os.system('cls')
burger_menu()  #버거메뉴판출력

#isdecimal() : 문자열이 정수형태인지 확인
#isdigit() : 문자열이 숫자로 인식될 수 있는 문자열인지 확인
num='1'
#메뉴선택화면
while 1: #와일문의 끝에는 장바구니가 출력됨 모든 if를 거치고 여기와 다른 while 을 탈출하면 장바구니가 출력됨 + 해당 while에는 break가 없어서 무한반복중

    print()
    print(' < 카테고리는 숫자로, 메뉴이름은 정확히 입력 >')
    print(' < 메뉴선택이 끝났다면 숫자 "5"를 입력       > ')
    print()
    user_select=input('  선택해주세요 ▶')
    print()
    if user_select == '9': #주문 취소 사용했던 모든 저장공간을 빈 리스트, 빈딕셔너리로 초기화
        clear_list()
        print('주문이 취소되었습니다.')
        os.system('cls')
        start_frame1()
        os.system('cls')
        burger_menu()
    elif user_select == '5': #메뉴판에서 5번 선택  # 선택한 메뉴가 1개라도 있을시 최종선택 메뉴확인 화면으로 넘어감
                            #user_select의 다른번호는 393번 라인의 while문을 닫아보면 확인가능
        while 1: #total_count는 장바구니에 물건이 1개라도 존재하는지 확인용 #해당 while문은 최종메뉴확인, 서비스형태선택, 결제여부, 결제완료의 흐름을 가지고 있음
            total_count=len(burger_dic)+len(side_dic)+len(dessert_dic)+len(drink_dic)
            if total_count == 0: #아무것도 고르지않았거나 메뉴의 삭제로 장바구니에 그무엇도 없다면 while문을 탈출하고 다시 카테고리로 돌아감
                os.system('cls')
                burger_menu()
                print('선택하신메뉴가 없습니다.')
                break
            j = 0
            os.system('cls')
            print('┌────────────────────────────────────────────────────────────────────────┐')
            print('                       【최종 메뉴 확인】')
            print('  메뉴')
            print()
            if len(burger_dic) >= 1:  # 장바구니 버거메뉴 불러오기
                for i in final_burger_dict:
                    j += 1 #j는 단순히 메뉴들의 순서를 나타내기 위한 번호기능
                    info_list = list(final_burger_dict[i])  #final_burger_dict[i] = 해당 버거이름의 모든 정보를 리스트로 변환 이유:튜플형태의 객체였기때문에 값을 활용하기 위해서 리스트로 변환함
                    print(f'  {j}.{i}')
                    print()
                    print(f'            재료{info_list[0]}')
                    if type(final_burger_dict[i][1]) == list: # final_burger_dict[i] 는 [ [재료들], [세트정보], int(수량) ] 의 리스트 구조로 리스트 요소 [재료들],[세트정보],수량 으로
                        print(f'            세트정보:{info_list[1]}') #세트라면 1번 인덱스가 리스트형태여야함
                        print(f'            수량:{burger_dic[i]}개')
                        print(f'            가격:{burger_dic[i] * burger_price[i]}원') #burger_dic의 요소는 수량이, burger_price는 가격정보가 있음 수량*가격의 형태
                        print()
                    else:
                        print(f'            수량:{burger_dic[i]}개') #1번 인덱스가 리스트가 아니라서 수량을 불러옴 final_burger_dict[i][1] = info_list[1] 도 같은 의미를 가짐
                        print(f'            가격:{burger_dic[i] * burger_price[i]}원')
                        print()
            if len(side_dic) >= 1:  # 장바구니 사이드메뉴 불러오기

                for i in side_dic:
                    come_bag(j, side_dic, side_price)

            if len(dessert_dic) >= 1:
                for i in dessert_dic:
                    come_bag(j, dessert_dic, dessert_price)

            if len(drink_dic) >= 1:
                for i in drink_dic:
                    come_bag(j, drink_dic,drink_price)

            print()
            print('└────────────────────────────────────────────────────────────────────────┘')
            print('1.메뉴변경')
            # 선택한정보만 지우고 나머지는 두고
            # 메뉴선택화면으로 돌아가야함

            print('2.삭제')
            print('3.수량변경')
            # 선택한 정보의 수량만 변경 ~~~~
            print('4.취소')
            # 현재까지의 모든정보 초기화 후 맨 첫 시작화면으로...
            print('5.결제하기')
            # 다음화면은 서비스 선택
            num = input('번호로 입력해주세요▶')
            if num == '1':  # 메뉴변경
                while 1:
                    print('메뉴변경을 선택하셨습니다.')
                    change_menu = input('변경하실 메뉴를 정확히 입력해주세요▶')
                    if change_menu in burger_dic: #변경할 메뉴가 햄버거에 있으면
                        del burger_dic[change_menu] #햄버거의 정보를 지운다 #해당 메뉴의 수량정보 삭제
                        del final_burger_dict[change_menu] #해당메뉴 버거의 모든정보 삭제
                        buy_burger_list.remove(change_menu) #구매버거리스트에서 해당메뉴 삭제
                        break #bbb_list는 중복검출에서 카운트를 해야하기때문에 지우지않음
                              # ex)bbb_list에서도 지울경우 버거(3)이 장바구니에 존재하는 상황에서 버거(2)를 지우고 다시 같은 버거를 누르면 (3)이 나와
                              #      정상적인 카운트가 진행되지 않음
                    elif change_menu in side_dic: #변경할 메뉴가 사이드에 있다면
                        delete_data(side_dic, buy_side_list,change_menu)
                        break
                    elif change_menu in dessert_dic: #메뉴가 디저트에 있다면
                        delete_data(dessert_dic, buy_dessert_list, change_menu)
                        break
                    elif change_menu in drink_dic:
                        delete_data(drink_dic, buy_drink_list, change_menu)
                        break
                    else: #메뉴 변경시 사용자의 입력이 장바구니에 존재하는 메뉴가 아닌경우 (장바구니에 담긴 이름과 모든게 일치해야함)
                        print('정확히 입력해주세요 ex) 빅맥(일반세트)')
                os.system('cls')
                burger_menu()
                break

            elif num == '2':  # 삭제
                del_menu = input('삭제하실 메뉴를 정확히 입력해주세요▶')
                if del_menu in burger_dic: #선택메뉴가 햄버거에 있다면
                    del burger_dic[del_menu]  #해당메뉴의 수량정보
                    del final_burger_dict[del_menu] #해당메뉴의 재료,세트여부
                    ser = del_menu.find('(')
                    bbb_list.remove(del_menu[:ser]) #중복선택용 리스트에서도 삭제
                    buy_burger_list.remove(del_menu) #구매확인용 리스트에서도 삭제
                if del_menu in side_dic:
                    del side_dic[del_menu] #이하 모든 카테고리별 품목들을 삭제한다
                    buy_side_list.remove(del_menu)
                if del_menu in dessert_dic:
                    del dessert_dic[del_menu]
                    buy_dessert_list.remove(del_menu)
                if del_menu in drink_dic:
                    del drink_dic[del_menu]
                    buy_drink_list.remove(del_menu)

            elif num == '3':  # 수량변경
                change_count = input('수량을 변경하실 메뉴를 정확히 입력해주세요▶')
                change_num = input(f'{change_count}의 변경하실 수량을 입력해주세요▶')
                # isdigit() : 문자열이 숫자로 인식될 수 있는 문자열인지 확인
                if change_num.isdigit() == True: #변경수량을 숫자로만 입력받으면
                    change_num=int(change_num)
                    if change_count in burger_dic:  # 수량변경메뉴가 햄버거
                        if change_num !=0: #수량이 0이 아닐때 변경
                            burger_dic[change_count] = change_num
                        else: #입력한수량이 0이되면 해당 정보들 삭제
                            del burger_dic[change_count]
                            del final_burger_dict[change_count]
                            ser = change_count.find('(')
                            bbb_list.remove(change_count[:ser])
                            os.system('cls')

                    elif change_count in side_dic:  # 수량변경메뉴가 사이드
                        if change_num != 0:  # 수량이 0이 아닐때 변경
                            side_dic[change_count] = change_num
                        else:
                            del side_dic[change_count]
                            os.system('cls')
                    elif change_count in dessert_dic:  # 수량변경메뉴가 디저트
                        if change_num !=0:
                            dessert_dic[change_count] = change_num
                        else:
                            del dessert_dic[change_count]
                            os.system('cls')
                    elif change_count in drink_dic:  # 수량변경메뉴가 음료
                        if change_count !=0:
                            drink_dic[change_count] = change_num
                        else:
                            del drink_dic[change_count]
                            os.system('cls')
                    else:
                        print('잘못된 입력입니다.')
                else: #입력이 숫자형태가 아닌 경우 break없이 수량변경상황 반복
                    print('숫자로 입력해주세요')
            elif num == '4':  # 취소
                print('결제가 취소됩니다.')
                #결제 취소시 여태 정보를 저장하기위해 사용했던 모든 리스트와 딕셔너리들을 빈 깡통으로 되돌림
                clear_list()
                os.system('cls')
                start_frame1() #식사장소 화면 출력
                os.system('cls')
                burger_menu() #버거메뉴판 출력후
                break #여기서 브레이크를 받으면 바로 장바구니 출력으로 넘어감

            elif num == '5':  # 결제 > 다음화면으로 ㄱ
                while 1:  # 서비스 선택화면 + 결제화면
                    while 1:
                        os.system('cls')
                        print()
                        print()
                        print('┌─────────────────────────────────────────────────┐')
                        print('                서비스 형태 선택')
                        print()
                        print('   1. 테이블 서비스', end="          ")  # 10번띄움
                        print('   2. 셀프서비스')
                        print()
                        print('└─────────────────────────────────────────────────┘')
                        service = input('서비스형태를 선택해주세요 ▶')  #해당 서비스 유형을 service변수에 저장 후에 사용됨
                        os.system('cls')
                        print()
                        print()
                        print()
                        if service == '1':  # 테이블서비스
                            print('"테이블" 서비스를 선택하셨습니다.')  #맞게 선택시 서비스형태선택 while을 탈출하고 결제로 넘어감
                            break
                        elif service == '2':
                            print('"셀프" 서비스를 선택하셨습니다.')
                            break
                        else: #입력이 1,2 에 해당되지 않고 다른 다른입력의 경우 서비스형태선택 while을 탈출하지 못하고 반복
                            print('번호로 입력해주세요')
                    print()
                    print()
                    print()
                    while 1:
                        print('┌───────────────────────────────────────┐')
                        print('       1. 결제             2. 취소')
                        print('└───────────────────────────────────────┘')
                        pay = input('결제하시겠습니까?')
                        if pay == '1': #결제했을경우
                            j = 0 #결제완료창에서 메뉴들에 번호를 부르기 위해 사용
                            os.system('cls')
                            print('┌──────────────────────────────────────────────────────────────────┓') # 영수증
                            print('                         결제완료')
                            print('   메뉴')
                            print()
                            if len(burger_dic) >= 1:  # 장바구니에 버거메뉴가 하나이상 존재한다면
                                for i in final_burger_dict: # 버거의 이름을 i로 받고
                                    j += 1 #메뉴순서에 번호를 달고
                                    info_list = list(final_burger_dict[i]) #선택했던 버거의 요소 ([재료],[세트정보],수량) 를 리스트로 변환
                                    print(f'  {j}.{i}') #번호 . 버거이름
                                    print()
                                    print(f'            재료{info_list[0]}') # 최종메뉴확인 창과 같은 논리
                                    if type(final_burger_dict[i][1]) == list:
                                        print(f'            세트정보:{info_list[1]}')
                                        print(f'            수량:{burger_dic[i]}개')
                                        print(f'            가격:{burger_dic[i] * burger_price[i]}원')  #burger_dic은 수량 , burger_price는 가격
                                        print()
                                    else:
                                        print(f'            수량:{burger_dic[i]}개')
                                        print(f'            가격:{burger_dic[i] * burger_price[i]}원')
                                        print()
                            if len(side_dic) >= 1:  # 장바구니에  사이드메뉴가 1개이상 존재한다면 불러오기
                                print()
                                for i in side_dic:

                                    come_bag(j, side_dic, side_price)
                            if len(dessert_dic) >= 1: # 장바구니에 디저트가 1개이상 존재한다면
                                print()
                                for i in dessert_dic:
                                    come_bag(j,dessert_dic, dessert_price)
                            if len(drink_dic) >= 1: # 장바구니에 음료가 1개이상 존재한다면
                                print()
                                for i in drink_dic:
                                    come_bag(j, drink_dic, drink_price)
                            print()

                            total_price= 0  #모든 메뉴들의 가격을 전부 합산하기 위한 변수
                            total_sum(burger_dic,burger_price)
                            total_sum(side_dic,side_price)
                            total_sum(dessert_dic,dessert_price)
                            total_sum(drink_dic,drink_price)

                            print(f'   총 합계    :'.rjust(51),  f' {total_price}원'.rjust(3))
                            if place == 1: #start_frame1 에서 선언한 글로벌 변수 place = 식사유형 가져옴 place=1 매장, 2면 포장
                                print(f'   식사장소   :'.rjust(50),' 매장'.rjust(3)) # .rjust()는 print문에서 문자열을 우측정렬하기 위한 함수
                            elif place == 2:
                                print('   식사장소 :'.rjust(50),' 포장'.rjust(3))
                            if service == '1': #서비스 입력받았던 변수 번호에따라 등장
                                print('   서비스형태 :'.rjust(49),' 테이블서비스'.rjust(3))
                            elif service == '2':
                                print('   서비스형태 :'.rjust(49),' 셀프서비스'.rjust(3))
                            print('└────────────────────────────────────────────────────────────────────┘')
                            print('결제가 완료 되었습니다.') #결제 완료 후 모든 정보 초기화
                            clear_list()
                            print()
                            print()
                            ending = input('아무키나 눌러 처음으로 돌아가기') #입력이 있을때까지 위의 결제 완료창이 출력됨
                            os.system('cls')
                            start_frame1()  #입력받으면 다시 첫 화면출력
                            os.system('cls')
                            burger_menu()
                            break

                        elif pay =='2':
                            print('결제가 취소 되었습니다.')
                            clear_list()
                            os.system('cls')
                            start_frame1()
                            os.system('cls')
                            burger_menu()
                            break
                        else:
                            os.system('cls')
                            print('번호로 정확히 입력해주세요')
                    break

    elif user_select == '0': #이전으로가기
        os.system('cls')
        start_frame1()
        os.system('cls')
        burger_menu()
    elif user_select == '1' or user_select=='2'or user_select== '3'or user_select== '4' or user_select=='7': #입력번호별 카테고리 출력
        os.system('cls')
        select_menu(user_select)
    # isdigit() : 문자열이 숫자로 인식될 수 있는 문자열인지 확인
    elif user_select.isdigit() == False:      #장바구니에 넣기위한 과정들 문자열입력시 시작
        buy_list.append(user_select)  #전체 물품 선택한 리스트들 (카테고리 구분없이 다 순서대로 추가, 입력한 메뉴는 buy_list[-1]에 존재하게 된다.
        if buy_list[-1] in burger_list:#입력한 메뉴가 메뉴에 있는 햄버거에 존재할 때 #burger_list는 버거메뉴이름들이 담긴 리스트
            if buy_list[-1] in bbb_list: #있다면 이미 한번 골랐던건지
                b=bbb_list.count(buy_list[-1]) #같은이름이 몇개인지 세보고 b에 int숫자 저장
                bbb_list.append(buy_list[-1])  # 계속 셀수 있게 추가
                overlap='('+str(b)+')' #(숫자)로 변환 ex (1) , (2) , (3)#같은이름의 햄버거 중복선택시 고유번호 추가
                burger_price[buy_list[-1] + overlap] = burger_price[buy_list[-1]]  #버거의 이름이 빅맥(1)과 같은 형태로 생성되었기때문에 가격정보에도 해당이름의 버거로 추가
                buy_list.append(buy_list[-1] + overlap)#buy_list[-1]을 항상 현재 선택메뉴로 인정하기위함                                      #후에 선택이 용이함

            else: #선택한 햄버거가 처음선택?
                bbb_list.append(buy_list[-1])  # 중복으로 걸리게 구매사이드리스트에 추가

                #빅맥
                #빅맥(1)
                #빅맥(2)
                #치즈버거
                #치즈버거(3)
                #빅맥(3) 과 같은 형식으로 중복선택을 각각의 메뉴로 인정하기 위한 과정을 거침

            matter = 1 #아래의 while문에 진입을 위한 변수 선언
            set_burger = {}  # 선택한 버거를 세트화 시키고 저장할 공간  {선택한버거1:세트구성}의 형태를 가지게 됨
            while matter != '완료':    #메뉴구성화면 matter가 완료가 될때 탈출함
                os.system('cls')
                print('┌────────────────────────────────────────────────────────────┐')
                print(f'          『{buy_list[-1]}』 의 구성을 선택해주세요')  # 현재 선택중인 버거
                print()
                print('    <0. 이전>    <1. 단품>   <2. 일반세트>    <3. 라지세트>')
                print('└────────────────────────────────────────────────────────────┘')
                setting = input('번호만입력 ▶')
                if setting == '1': #단품화
                    print()  # 단품이니까 버거구성으로 가야함
                    print('  "단품"을 선택하셨습니다.') #단품 확인용 문구 추가
                    burger_dic[buy_list[-1]+'(단품)']=1   #{버거이름(단품) :1}
                    buy_burger_list.append(buy_list[-1]+'(단품)') #구매할 버거의 이름에 (단품)이라는 문자열을 추가해 저장  [ 버거이름(단품)  ]
                    burger_price[buy_list[-1] + '(단품)'] = burger_price[buy_list[-1]] #버거가격을담당하는 딕셔너리의 키도 그에 맞게 생성

                elif setting == '2':
                    print()  # 일반세트화
                    print('일반세트를 선택하셨습니다.')
                    print('일반세트의 구성은 "감자튀김(일반),콜라" 입니다.')
                    buy_burger_list.append(buy_list[-1] + '(일반세트)')
                    burger_dic[buy_list[-1]+'(일반세트)']=1  #세트에 맞게 이름바꾸고 수량은 1로 세팅
                    set_burger[buy_burger_list[-1]] = ['감자튀김(일반)', '콜라'] #일반세트에맞게 기본세트구성 설정
                    burger_price[buy_list[-1]+'(일반세트)']=burger_price[buy_list[-1]]+1800 #세트화가 되었으니 단품가격 + 일반세트가격으로 가격 생성
                    if ti_min < '10':  # 분단위가 10아래 한자리 숫자면 앞에 0을 넣어서 1101 과 같은 숫자를 만든다
                        real_min = '0' + ti_min
                    else:
                        real_min = ti_min
                    real_time = real_h + real_min   # 맥런치 시간대에서 세트가격 변화
                    if real_time >= '1030' and real_time <= '1400':#맥런치시간대에서 일반세트가격 변화
                        if '빅맥' in buy_list[-1]:
                            burger_price[buy_list[-1]+'(일반세트)']=5200
                        elif '맥스파이시상하이버거' in buy_list[-1]:
                            burger_price[buy_list[-1]+'(일반세트)']=5200
                        elif '1955버거' in buy_list[-1]:
                            burger_price[buy_list[-1] + '(일반세트)'] = 6200
                        elif '베이컨토마토디럭스' in buy_list[-1]:
                            burger_price[buy_list[-1] + '(일반세트)'] = 6000

                elif setting == '3':
                    print()  # 라지세트화, 758라인의 elif setting == '2'와 같은 원리로 기능
                    print('라지세트를 선택하셨습니다.')
                    print('라지세트의 구성은 "감자튀김(L), 콜라(L) 입니다."')
                    buy_burger_list.append(buy_list[-1] + '(라지세트)')
                    set_burger[buy_burger_list[-1]] = ['감자튀김(L)', '콜라(L)']
                    burger_dic[buy_list[-1] + '(라지세트)'] = 1
                    burger_price[buy_list[-1] + '(라지세트)'] = burger_price[buy_list[-1]] + 2400

                    if ti_min < '10':  # 분단위가 10아래 한자리 숫자면 앞에 0을 넣어서 1101 과 같은 숫자를 만든다
                        real_min = '0' + ti_min
                    else:
                        real_min = ti_min
                    real_time = real_h + real_min   # 맥런치 시간대에서 라지세트가격 변화
                    if real_time >= '1030' and real_time <= '1400':
                        if '빅맥' in buy_list[-1]:
                            burger_price[buy_list[-1]+'(라지세트)']=5200+600 #라지세트는 일반세트에서 600원추가됨
                        elif '맥스파이시상하이버거' in buy_list[-1]:
                            burger_price[buy_list[-1]+'(라지세트)']=5200+600
                        elif '1955버거' in buy_list[-1]:
                            burger_price[buy_list[-1] + '(라지세트)'] = 6200+600
                        elif '베이컨토마토디럭스' in buy_list[-1]:
                            burger_price[buy_list[-1] + '(라지세트)'] = 6000+600

                elif setting =='0':#이전
                    os.system('cls')
                    burger_menu()      #현재 선택단계로 온 순간 bbb_list에 추가가 되어있는 상태이기 때문에 중복선택시 번호가 증가하는현상발생
                    bbb_list.pop(-1)  #카운트 수량을 하나 빼줘야 하기때문에 현재선택단계에서 추가된 버거이름에 pop()을 적용
                    break #이전으로 돌아가기위한 break

                else: #맞지않는 입력을할때 재입력을 받기 위함
                    print('정확한 번호를 입력해주세요')

                # { 버거이름 : [재료1, 재료2, 재료3]
                # burger_dic = {}  # 버거 종류와 수량 저장 {버거이름 : 수량}

                if setting == '2' or setting == '3': #setting은 입력받은 변수 2,3번은 일반세트,라지세트 였기때문에 아래는 세트를 선택할시 실행됨
                    burger_matter_dic[buy_burger_list[-1]] = ['기본야채1', '기본야채2', '기본소스','기본패티']  # 선택중인 버거의 이름으로 버거재료 구성후 저장하기
                    while 1:  # 세트를 골랐다면 실행  #세부구성화면   #burger_matter_dic = {버거이름 : [기본야채1, 기본야채2, 기본소스, 기본패티]로 딕셔너리의 값이 리스트형대로 저장되어있음
                        os.system('cls')  # 선택중인 버거세트에 대해 이야기중 예시)빅맥세트
                        print('┌─────────────────────────────────────────────────────────────────────────────────────────────┐')
                        print('                <세부구성선택화면>')
                        print(f'  〔{buy_burger_list[-1]}〕')
                        print('  0. 이전')
                        print(f'  1. 버거재료 변경ㅤㅤㅤㅤㅤㅤ현재:{burger_matter_dic[buy_burger_list[-1]]}')
                        print(f'  2. 사이드 변경ㅤㅤㅤㅤㅤㅤㅤ현재:{set_burger[buy_burger_list[-1]][0]}')
                        print(f'  3. 음료 선택ㅤㅤㅤㅤㅤㅤㅤㅤ현재:{set_burger[buy_burger_list[-1]][1]}')
                        print('  4. 완료')
                        print('└──────────────────────────────────────────────────────────────────────────────────────────────┘')
                        matter = input('선택해 주세요>')
                        # 패티는 불고기 or 치킨    소스= 매운맛,단맛,짠맛  야채1 = 양상추 추가/제거 야채2 = 양파 추가/적양파 추가
                        # 기본 디폴트 구성은 => 일반패티, 일반소스, 기본야채1, 기본야채2 라고 가정
                        if matter == '1':  # 버거재료변경선택함
                            print('1. 버거재료변경을 선택하셨습니다')
                            print('기본구성은 일반패티,일반소스,기본야채1,기본야채2 구성입니다.')
                            burger_matter(buy_burger_list[-1]) #버거재료구성 함수호출
                            # 버거 구성(기본,야채1,야채2,소스,패티)
                        elif matter == '2':  # 사이드재료변경 선택함
                            print()
                            print('2. 사이드변경을 선택하셨습니다.')
                            side_topping(buy_burger_list[-1]) #소금추가에 관련된 토핑구성함수 호출
                            # 사이드재료
                        elif matter == '3':  # 음료변경 선택함
                            print()
                            drink_change(buy_burger_list[-1]) # 음료변경함수 호출
                            # 음료선택
                        elif matter == '4':  # 완료 -> 메뉴선택화면으로 돌아가야함
                            matter = '완료' #matter='완료'를 들고가면 위의 단품,세트 선택화면 while에서 탈출됨
                            final_burger_dict[buy_burger_list[-1]] = burger_matter_dic[buy_burger_list[-1]], set_burger[buy_burger_list[-1]], burger_dic[buy_burger_list[-1]]
                            os.system('cls')
                            burger_menu()
                            break
                        elif matter == '0':  # 메뉴'구성'화면으로 돌아가기
                            bblist = list(burger_dic.keys())   #구매한 버거이름(키)를 리스트화
                            # if len(bblist) >= 1:   #구매한게 존재하면
                            del burger_dic[bblist[-1]]     #있던버거이름 지우고
                            del burger_matter_dic[bblist[-1]]  #지우고2
                            ser = bblist[-1].find('(')   #괄호찾아서  ex) 빅맥 ( 1)(단품)
                            bbb_list.remove(bblist[-1][:ser])   #원래이름지우고
                            buy_burger_list.pop(-1)
                            break
                elif setting == '1':  # 단품일때 실행
                    burger_matter_dic[buy_burger_list[-1]] = ['기본야채1', '기본야채2', '기본소스','기본패티']  # 선택중인 버거의 이름으로 재료 변경후 저장하기
                    while 1:
                        os.system('cls')
                        print('┌────────────────────────────────────────────────────────────────────────────────┐')  # 선택중인 버거세트에 대해 이야기중 예시)빅맥세트
                        print('                <세부구성선택화면>')
                        print(f'     〔{buy_burger_list[-1]}〕')
                        print('  0. 이전')
                        print(f'  1. 버거재료 변경ㅤㅤㅤㅤㅤㅤ현재:{burger_matter_dic[buy_burger_list[-1]]}')
                        print('  2. 완료')
                        print('└─────────────────────────────────────────────────────────────────────────────────┘')
                        matter = input('선택해주세요 >')
                        if matter == '1':
                            burger_matter(buy_burger_list[-1])
                        elif matter == '2':  # 메뉴선택화면으로 돌아가기
                            final_burger_dict[buy_burger_list[-1]] = burger_matter_dic[buy_burger_list[-1]], burger_dic[buy_burger_list[-1]]
                            # 최종 버거 구성 = { 버거이름1 : [재료~ ], [수량]}
                            matter = '완료'
                            os.system('cls')
                            burger_menu()
                            break
                        elif matter == '0': #이전
                            bblist=list(burger_dic.keys())
                            if len(bblist) >= 1:
                                del burger_dic[bblist[-1]]
                                del burger_matter_dic[bblist[-1]]
                            break
        elif buy_list[-1] in side_list: #현재 선택이 사이드메뉴에 있는지
            what_select(buy_list, buy_side_list, side_dic)
            side_menu()

        elif buy_list[-1] in dessert_list: #직전선택이 디저트?
            what_select(buy_list, buy_dessert_list, dessert_dic)
            dessert_menu()

        elif buy_list[-1] in drink_list: #직전선택이 음료?
            what_select(buy_list, buy_drink_list, drink_dic)
            drink_menu()
        else: #입력한 문자열이 그어떤 메뉴에도 존재하지않는 메뉴 혹은 오타 일때
            os.system('cls')
            burger_menu() #버거메뉴판을 출력하고
            print('메뉴이름을 "정확히" 입력해주세요.') #잘못된 입력임을 알려준다. 722라인의 elif가 끝나면 장바구니가 출력된다.
    else:
        os.system('cls')
        burger_menu()
        print('정확한 숫자를 입력해주세요')
    print('┌────────────────────────────────────────────────────────────────────────────┐')
    print('  『장바구니』')
    print()
    for i in burger_dic:  #burger_dic의 키는 버거이름, 값은 수량정보를 들고있음 burger_dic={버거이름:수량} , burger_price는 가격정보가 담겨있음
        print(f'  {i}',f'수량{burger_dic[i]}개'.rjust(30-len(i),'ㅤ'),f'{burger_dic[i] * burger_price[i]}원'.rjust(10)) #rjust()는 우측정렬하기 위해 사용됨
    for i in side_dic:
        print(f'  {i}',f'수량{side_dic[i]}개'.rjust(30-len(i),'ㅤ'),f'{side_dic[i] * side_price[i]}원'.rjust(10))
    for i in dessert_dic:
        print(f'  {i}',f'수량{dessert_dic[i]}개'.rjust(30-len(i),'ㅤ'),f'{dessert_dic[i] * dessert_price[i]}원'.rjust(10))
    for i in drink_dic:
        print(f'  {i}',f'수량{drink_dic[i]}개'.rjust(30-len(i),'ㅤ'),f'{drink_dic[i] * drink_price[i]}원'.rjust(10))
    print('└────────────────────────────────────────────────────────────────────────────┘')


