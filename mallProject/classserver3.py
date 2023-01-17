import socketserver
import threading
import datetime
import time
import pymysql
import pickle
#import chromedriver_autoinstaller # chrome driver 자동 설치 라이브러리
from selenium import webdriver
from selenium.webdriver.common.by import By

HOST = '172.30.1.34' # 서버의 ip를 열음. (이 서버의 ip로 클라이언트가 접속을 해야 한다), 그전에 ping을 먼저 확인하도록.
PORT = 9900			 # 포트번호 (같아야 함)
lock = threading.Lock()  # syncronized 동기화 진행하는 스레드 생성

#chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions() # Browser 세팅하기
options.add_argument('lang=ko_KR') # 사용언어 한국어
options.add_argument('disable-gpu') # 하드웨어 가속 안함

driver = webdriver.Chrome(options=options)
driver2 = webdriver.Chrome(options=options)
driver3 = webdriver.Chrome(options=options)
driver4 = webdriver.Chrome(options=options)
driver5 = webdriver.Chrome(options=options)
driver.get('https://search.shopping.naver.com/search/all?query=%EB%82%A8%EC%84%B1%EC%83%81%EC%9D%98') # 상의
driver2.get('https://search.shopping.naver.com/search/all?query=%EB%82%A8%EC%84%B1%ED%95%98%EC%9D%98') # 하의
driver3.get('https://search.shopping.naver.com/search/all?query=%EB%82%A8%EC%84%B1%EB%AA%A8%EC%9E%90') # 모자
driver4.get('https://search.shopping.naver.com/search/all?query=%EB%82%A8%EC%84%B1%EC%95%84%EC%9A%B0%ED%84%B0') #아우터
driver5.get('https://search.shopping.naver.com/search/all?query=%EB%82%A8%EC%84%B1%EC%8B%A0%EB%B0%9C') # 신발
driver.implicitly_wait(0.5)

#t:상의 p:하의 c:모자 o:아우터 s:신발
Tprice = driver.find_elements(By.CLASS_NAME, value='price_num__S2p_v')
Tname = driver.find_elements(By.CLASS_NAME, value='basicList_link__JLQJf')
Pprice = driver2.find_elements(By.CLASS_NAME,value='price_num__S2p_v')
Pname =  driver2.find_elements(By.CLASS_NAME, value='basicList_link__JLQJf')
Cprice = driver3.find_elements(By.CLASS_NAME,value='price_num__S2p_v')
Cname =  driver3.find_elements(By.CLASS_NAME, value='basicList_link__JLQJf')
Oprice = driver4.find_elements(By.CLASS_NAME,value='price_num__S2p_v')
Oname =  driver4.find_elements(By.CLASS_NAME, value='basicList_link__JLQJf')
Sprice = driver5.find_elements(By.CLASS_NAME,value='price_num__S2p_v')
Sname =  driver5.find_elements(By.CLASS_NAME, value='basicList_link__JLQJf')
# print(len(Tprice))
TOP10Tprice = []
TOP10Tname = []
TOP10Pprice = []
TOP10Pname = []
TOP10Cprice = []
TOP10Cname = []
TOP10Oprice = []
TOP10Oname = []
TOP10Sprice = []
TOP10Sname = []

for i in Tprice:
    TOP10Tprice.append(i.text)
for j in Tname:
    TOP10Tname.append(j.text)
for i in Pprice:
    TOP10Pprice.append(i.text)
for j in Pname:
    TOP10Pname.append(j.text)
for i in Cprice:
    TOP10Cprice.append(i.text)
for j in Cname:
    TOP10Cname.append(j.text)
for i in Oprice:
    TOP10Oprice.append(i.text)
for j in Oname:
    TOP10Oname.append(j.text)
for i in Sprice:
    TOP10Sprice.append(i.text)
for j in Sname:
    TOP10Sname.append(j.text)



con = pymysql.connect(host='localhost', port=3306, user='root', passwd='7539518642a', db='mall_db', charset='utf8')
cur = con.cursor()
#
# sql2 = "INSERT INTO goods (goods_name, goods_code, goods_num, goods_price, goods_size) VALUES(%s, %s, %s, %s, %s)"
# val = [
# (f'{TOP10Tname[0]}', 'T', None, f'{TOP10Tprice[0]}', None),
# (f'{TOP10Tname[1]}', 'T', None, f'{TOP10Tprice[1]}', None),
# (f'{TOP10Tname[2]}', 'T', None, f'{TOP10Tprice[2]}', None),
# (f'{TOP10Tname[3]}', 'T', None, f'{TOP10Tprice[3]}', None),
# (f'{TOP10Tname[4]}', 'T', None, f'{TOP10Tprice[4]}', None),
# (f'{TOP10Pname[0]}', 'P', None, f'{TOP10Pprice[0]}', None),
# (f'{TOP10Pname[1]}', 'P', None, f'{TOP10Pprice[1]}', None),
# (f'{TOP10Pname[2]}', 'P', None, f'{TOP10Pprice[2]}', None),
# (f'{TOP10Pname[3]}', 'P', None, f'{TOP10Pprice[3]}', None),
# (f'{TOP10Pname[4]}', 'P', None, f'{TOP10Pprice[4]}', None),
# (f'{TOP10Oname[0]}', 'O', None, f'{TOP10Oprice[0]}', None),
# (f'{TOP10Oname[1]}', 'O', None, f'{TOP10Oprice[1]}', None),
# (f'{TOP10Oname[2]}', 'O', None, f'{TOP10Oprice[2]}', None),
# (f'{TOP10Oname[3]}', 'O', None, f'{TOP10Oprice[3]}', None),
# (f'{TOP10Oname[4]}', 'O', None, f'{TOP10Oprice[4]}', None),
# (f'{TOP10Cname[0]}', 'C', None, f'{TOP10Cprice[0]}', None),
# (f'{TOP10Cname[1]}', 'C', None, f'{TOP10Cprice[1]}', None),
# (f'{TOP10Cname[2]}', 'C', None, f'{TOP10Cprice[2]}', None),
# (f'{TOP10Cname[3]}', 'C', None, f'{TOP10Cprice[3]}', None),
# (f'{TOP10Cname[4]}', 'C', None, f'{TOP10Cprice[4]}', None),]
#
# cur.executemany(sql2, val)
# con.commit()
# con.close()


class UserManager:  # 사용자관리 및 채팅 메세지 전송을 담당하는 클래스
    # ① 채팅 서버로 입장한 사용자의 등록
    # ② 채팅을 종료하는 사용자의 퇴장 관리
    # ③ 사용자가 입장하고 퇴장하는 관리
    # ④ 사용자가 입력한 메세지를 채팅 서버에 접속한 모두에게 전송

    def __init__(self):
        self.users = {}  # 사용자의 등록 정보를 담을 사전 {사용자 이름:(소켓,주소),...}


    def addUser(self, username, userpw, name, conn, addr):  # 사용자 ID를 self.users에 추가하는 함수
        con = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='mall_db', charset='utf8')
        cur = con.cursor()
        sql = 'SELECT mem_id, mem_pw FROM mall_db.members'
        cur.execute(sql)
        data = cur.fetchall()
        print(data)
        for i in data:
            if username in i[0]:
                conn.send(conn.send('False').encode())
            else:
                sql2 = 'INSERT INTO members (mam_id, mem_pw, mem_name) VALUES (%s, %s, %s)'.format(username,userpw,name)
                cur.execute(sql2)
        con.commit()
        con.close()
        if username in self.users:  # 이미 등록된 사용자라면
            conn.send('이미 등록된 사용자입니다.'.encode())
            time.sleep(0.01)
            return '이미 등록된 사용자입니다'

        # 새로운 사용자를 등록함
        lock.acquire()  # 스레드 동기화를 막기위한 락
        self.users[username] = (conn, addr)

        lock.release()  # 업데이트 후 락 해제


        print('+++ 대화 참여자 수 [%d]' % len(self.users))

        return username

    def removeUser(self, username):  # 사용자를 제거하는 함수
        con = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='mall_db', charset='utf8')
        cur = con.cursor()
        sql = 'SELECT mem_id FROM mall_db.members'
        cur.execute(sql)
        data = cur.fetchall()
        print(data)
        for i in data:
            if i == username:
                sql2 = 'DELETE FROM members WHERE mem_id = username'
                cur.execute(sql2)
            else:
                pass
        con.commit()
        con.close()
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()


        print('--- 대화 참여자 수 [%d]' % len(self.users))


    def loginname(self, username, userpw, conn):
        con = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='mall_db', charset='utf8')
        cur = con.cursor()
        sql = 'SELECT mem_id, mem_pw FROM mall_db.members'
        cur.execute(sql)
        data = cur.fetchall()
        print(data)
        for i in data:
            if username in i[0] and userpw in i[1]:
                conn.send(conn.send('True').encode())
            else:
                conn.send(conn.send('False').encode())
        con.close()

    def messageHandler(self, username, msg):  # 전송한 msg를 처리하는 부분
        now = datetime.datetime.now()
        date = f"--{now.strftime('%H:%M:%S')}"
        if username in self.users:
            if msg[0] == '/':
                if msg.strip() == '/quit':  # 보낸 메세지가 'quit'이면
                    self.removeUser(username)
                    return -1
                #elif username in :
                 #   if msg[:3] == '/공지':
                  #      msg = "[전체공지]" + msg[4:] + date
                        #self.sendMessageToAll(msg)
                   #     return


                    # elif msg[:3] == '/강퇴':
                    #
                    #     if msg[4:] in self.users and msg[4:] != username:
                    #         print("강퇴 if문 진입")
                    #         msg2 = "아이디 : " + msg[4:] + "님를 강퇴 하였습니다." + date
                    #         self.users[msg[4:]][0].close()
                    #         self.removeUser(msg[4:])
                    #         return 0
                    #     else:
                    #         print("강퇴 else문 진입")
                    #         if msg[4:] == username:
                    #             print("강퇴자가 자기자신일때")
                    #             self.users[username][0].send(("자기자신을 강퇴 시킬 수 없습니다.").encode())
                    #             return 0
                    #         elif msg[4:] not in self.users:
                    #             print("강퇴자가 들어와있지 않은 사람일 때")
                    #             self.users[username][0].send((f"{msg[4:]}는 현재 접속중인 사람이 아닙니다.").encode())
                    #             return 0







class MyTcpHandler(socketserver.BaseRequestHandler): # socketserver의 BaseRequestHandler클래스를 상속받은 요청 처리기 객체
    userman = UserManager() # 유저의 사용자 관리및 체팅 을 관리하는 클래스를 인스턴스화 시킴
    # 클래스를 인스턴스화 시켰지만, 위에서 클래스가 선언됨과 동시에 users 클래스 변수, badcount 클래스변수가 메모리에 저장되기 때문에
    # 복제된 많은 인스턴스들도 같은 클래스변수users, badcount를 가르키고 있다.

    def handle(self):  # 클라이언트가 접속시 클라이언트 주소, 출력 요청을 처리하는 데 필요한 모든 작업을 수행
        # handle클래스는 BaseRequestHandler의 객체로 기본 구현은 아무것도 수행하지 않음.
        # 요청 : self.request로 할수 있음.
        # 클라이언트 주소 : self.client_address로 요청가능
        # 서버 주소 : self.server로 제공
        print('[%s] 연결됨' % self.client_address[0])

        try:
            # username = self.registerUsername() # registerUsername : 유저id를 만들고 체팅에 참여 할수 있도록 돕는 메서드.
            msg = pickle.loads(self.request.recv(1024))

            # msg = self.request.recv(1024)

            while msg:

                msg = self.request.recv(1024)

        except Exception as e:
            print(e , '<-- 에러메세지') # 감자

        # print('[%s] 접속종료' % self.client_address[0])
        # self.userman.removeUser(username)



class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # socketserver모듈의 TCPServer 클래스는 클라이언트와 서버와의 connect 기능을 하는 클래스
    # TCPServer 클래스는 두가지 매개변수가 필요 1. server_address 2. ResquestHandlerclass
    # ThreadingMixIn ????
    # soketserver모듈의 ThreadingMixIn 클래스는 서버가 동작하기 위한 요청의 내용을 비동기 동작화 하여 간단하게 요청처리를 하기 위한 클래스
    #
    # 서버만들기에 필요한 단계
    # 1. BaseRequestHandler클래스를 서브클래싱하여 handle()메서드를 사용하여 요청처리기 클래스를 만들어야 함. -- MyTcpHandler
    # 2. 서버주소와 핸들메서드를 사용한 요청처리기 클래스를 전달하여 인스턴스화를 함. -- server = ChatingServer((HOST, PORT), MyTcpHandler)
    # 3. 서버객체(server)의 server_forever()메서드를 호출하여 필요한 요청을 처리.
    pass


def runServer():
    print('+++ 채팅 서버를 시작합니다.')
    print('+++ 채텅 서버를 끝내려면 Ctrl-C를 누르세요.')

    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler) # server_address : (HOST, PORT), ResquestHandlerclass : MyTcpHandler(socketserver.BaseRequestHandler)
        # TypeError: TCPServer.__init__() missing 1 required positional argument: 'RequestHandlerClass' -- 에러 코드
        # 매개변수 하나를 빼고 실행했을때 나타나는 에러 : TCPServer클래스가 필요한 요소 RequestHandlerClass가 없다고 나옴.
        server.serve_forever() # 매개변수를 받은 ChatingServer 클래스를 server라는 변수에 인스턴스화 시킨후에
        # server라는 인스턴스에 클라이언트가 서버접속을 알 수 있도록 인터벌을 돌리는 기능.

    except KeyboardInterrupt:
        print('--- 채팅 서버를 종료합니다.')
        server.shutdown()
        # shutdown : serve_forever() 루프가 정지하도록 하고 정지할 때까지 기다립니다. serve_forever()가 다른 스레드에서 실행되는 동안 shutdown()을 호출해야 합니다. 그렇지 않으면 교착 상태가 됩니다.
        server.server_close()

runServer()

