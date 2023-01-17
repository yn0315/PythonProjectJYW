import socketserver
import threading
import datetime
import json
import pymysql

HOST = '192.168.0.5' # 서버의 ip를 열음. (이 서버의 ip로 클라이언트가 접속을 해야 한다), 그전에 ping을 먼저 확인하도록.
PORT = 9900       # 포트번호 (같아야 함)
lock = threading.Lock()  # syncronized 동기화 진행하는 스레드 생성

# sql에 insert into

con = pymysql.connect(host='localhost', user='root', password='7539518642a', db='news_db', charset='utf8')
# user,pw,host,db,charset 등 매개변수 설정 후 connect 한 객체 : con

# con 객체에서 cursor 만들기

cur = con.cursor()


class User:  # 사용자관리 및 채팅 메세지 전송을 담당하는 클래스

    userList = ['aa']

    def __init__(self):
        self.users = {}  # 사용자의 등록 정보를 담을 사전 {사용자 이름:(소켓,주소),...}
        # 사용자 리스트

    def addUser(self, userId, userPw, userName, userAddr, userAge, userGender):  # 사용자 ID를 self.users에 추가하는 함수

        sql = 'SELECT id FROM member'
        cur.execute(sql)
        data = cur.fetchall()

        for k in data:
            for i in range(len(k)):
                if userId == k[i]:
                    return "1"

                else:
                    User.userList = userId

                    # sql변수에 sql문법 작성
                    sql4 = 'INSERT INTO member VALUES(%s,%s,%s,%s,%s)'
                    val = [(userId, userPw, userAge, userGender, userAddr)]

                    # sql변수에 sql문법 작성
                    sql = '''SELECT *
                              FROM members; '''
                    # 커서를 통해 sql문 실행
                    try:
                        cur.executemany(sql4, val)
                        con.commit()
                    except Exception as ex:
                        print(type(ex),ex)

                    print(User.userList)
                    return "0" # 없으면 0

    def loginUser(self, userId, userPw):
        sql = 'SELECT id,pw FROM member'
        cur.execute(sql)
        data = cur.fetchall()
        print(data[0][0],"튜플 0,0", data[0][1],"튜플 0,1")

        for i in range(len(data)):
            if userId == data[i][0]:
                if userPw == data[i][1]:
                    return "0"

                else:
                    return "1"
            else:
                return "1"

class MyTcpHandler(socketserver.BaseRequestHandler):
    user = User()

    def handle(self):  # 클라이언트가 접속시 클라이언트 주소 출력
        # 클라이언트의 접속요청이 수락된 후 호출됨
        # 서버와 클라이언트가  데이터를 주고 받는 메소드로 재정의해서 사용,
        # BaseRequestHandler클래스 안에 속해있는 메소드

        try:
            while True:
                # json데이터의 내용에 따라 실행하는 함수가 갈라져야 함
                data = self.request.recv(16184)
                print(data)
                if bytes(data).decode() == 'sign': # 회원가입
                    print("if문 안쪽")
                    json_dict = json.loads(self.request.recv(16184))
                    print(json_dict)
                    result = self.user.addUser(json_dict["userId"], json_dict["userPw"], json_dict["userName"],
                                               json_dict["userAddr"], json_dict["userAge"], json_dict["userGender"])
                    self.request.send(result.encode())

                else: # 로그인

                    json_dict = json.loads(self.request.recv(16184))
                    print(11111111111111111111111111111111111111111)
                    print(json_dict)
                    print(222222222222222222222222222222222222)
                    result = self.user.loginUser(json_dict["userId"], json_dict["userPw"])
                    print(result)
                    self.request.send(result.encode())

                    print("else")

        except Exception as e:
            print(e)




class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
   # ThreadingMixIn 클래스는 서버가 스레드 종료를 기다려야하는지를 가리키는 daemon_threads 어트리뷰트를 정의

   # TCPServer 클래스 안의 serve_forever()메소드 : 클라이언트의 접속 요청을 수신대기. 접속 요청이 있을 경우 수락하고 BaseRequestHandler의 handle() 메소드를 호출
   # TCPServer 클래스가 serve_forever() 메소드를 통해 클라이언트의 연결 요청을 기다리다가 클라이언트에게서 접속요청이 오면 이를 수락한 뒤 BaseRequestHandler
   # 객체의 handle() 메소드를 호출.서버 애플리케이션은 이 handler()메소드를 재정의해서 클라이언트와 데이터를 주고받는 일을 수행.

   # 서버가 클라이언트의 연결 요청을 수락해서 TCP 커넥션이 만들어지고 나면 그 다음부터는 서버 측의 socket 객체와 클라이언트 측의 socket 객체가
   # socket.send() 메소드와 socket.recv() 메소드를 통해 데이터를 주고 받을 수 있다. 서버 애플리케이션에서는
   # BaseRequestHandler의 request 데이터 속성이 바로 socket 객체. 데이터를 주고받는 일을 마치고 나서 서버와 클라이언트의 연결을 종료할 때는
   # socket의 close() 메소드를 호출하면 됨.

   # BaseRequestHandler 클래스 안의 handle() 메소드 : 클라이언트 접속 요청을 처리.
   # socket : 논리적인 의미로 컴퓨터 네트워크를 경유하는 프로세스 간 통신(Inter-Process Communication, IPC)의 종착점(end-point)
   # bind(): 사용할 IP address와 Port number 등록(각 소켓에 할당)
   # connect(): Client에서 Server와 연결하기 위해 소켓과 목적지 IP address, Port number 지정 (Block 상태)
   # send(), recv(): Client는 처음에 생성한 소켓으로, Server는 새로 반환(생성)된 소켓으로 client와 server간에 데이터 송수신

    pass



def runServer():
    print('+++ 채팅 서버를 시작합니다.')
    print('+++ 채텅 서버를 끝내려면 Ctrl-C를 누르세요.')

    try:

        server = ChatingServer((HOST, PORT), MyTcpHandler)# 서버 객체 생성
        # 인스턴스 = 클래스명(생성자)
        server.serve_forever() # 클라이언트의 접속요청 수락 및 handle() 메소드 호출하는 역할
    except KeyboardInterrupt:
        print('--- 채팅 서버를 종료합니다.')
        server.shutdown()
        server.server_close()

runServer()