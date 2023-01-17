import socketserver
import threading
import datetime

HOST = '192.168.0.5' # 서버의 ip를 열음. (이 서버의 ip로 클라이언트가 접속을 해야 한다), 그전에 ping을 먼저 확인하도록.
PORT = 9999          # 포트번호 (같아야 함)
lock = threading.Lock()  # syncronized 동기화 진행하는 스레드 생성




class UserManager:  # 사용자관리 및 채팅 메세지 전송을 담당하는 클래스
    # ① 채팅 서버로 입장한 사용자의 등록
    # ② 채팅을 종료하는 사용자의 퇴장 관리
    # ③ 사용자가 입장하고 퇴장하는 관리
    # ④ 사용자가 입력한 메세지를 채팅 서버에 접속한 모두에게 전송

    # 서버 사이드 공통 구현기능

    # 메시지 전송자 id, 시간표시 o
    # 로그인 권한(우리반 학생만 접속 가틍) o
    # 관리자 id 따로 지정
    # 관리자 권한 공지
    # 관리자 권한 로그인 차단 o
    # 관리자 권한 퇴장시키기
    # 비속어 필터


    def __init__(self):
        self.users = {}  # 사용자의 등록 정보를 담을 사전 {사용자 이름:(소켓,주소),...}
        self.admin = '관리자'
        self.usersList = ['조윤우','김근영','강철순','김채연','이한영','김연경','박희재','조웅희','강명구']
        self.blackList = []

    # 아이디 차단권한
    def idBlock(self, username):
        self.blackList = username

    # 강퇴
    def outOfChat(self, username):
        # 주소값 가져와서 끊어버리면............................하면 될 거 같은데...........
        self.users[username][1].close()
        return




    def addUser(self, username, conn, addr):  # 사용자 ID를 self.users에 추가하는 함수

        if username == '조윤우':
            conn.send(username.encode() + '님 로그인'.encode())
            self.users[username] = conn,addr[0]
            self.outOfChat('조윤우')



            #conn.send('[%s]'.encode() % self.users)

            conn.send('+++ 대화 참여자 수 [%d]'.encode() % len(self.users))

            #print('[%s]' % self.users)
            #conn.send('[%s]'.encode() % self.users)

            # print('+++ 대화 참여자 수 [%d]' % len(self.users))

            return username

        elif username in self.usersList and username not in self.blackList:  # 이미 등록된 사용자라면
            conn.send(username.encode() + '님 로그인'.encode())
            # conn.send('이미 등록된 사용자입니다.\n'.encode())
            return username
        elif username in self.blackList:
            conn.send('차단된 사용자입니다.\n'.encode())
            return


        # 새로운 사용자를 등록함
        lock.acquire()  # 스레드 동기화를 막기위한 락
        #        self.users[username] = (conn, addr)
        lock.release()  # 업데이트 후 락 해제

        self.sendMessageToAll('[%s]님이 입장했습니다.' % username)
        conn.send('[%s]님이 입장했습니다.' % username)
        print('+++ 대화 참여자 수 [%d]' % len(self.users))

        return username


    def removeUser(self, username):  # 사용자를 제거하는 함수
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        self.sendMessageToAll('[%s]님이 퇴장했습니다.' % username)
        print('--- 대화 참여자 수 [%d]' % len(self.users))

    def messageHandler(self, username, msg):  # 전송한 msg를 처리하는 부분
        if msg[0] != '/':  # 보낸 메세지의 첫문자가 '/'가 아니면
            self.sendMessageToAll('[%s] %s' % (username, msg) + '\t' + str(datetime.datetime.now().hour) + ":"+ str(datetime.datetime.now().minute))
            return

        if msg.strip() == '/quit':  # 보낸 메세지가 'quit'이면
            self.removeUser(username)
            return -1
        if msg.strip() == '/강퇴': # 보낸 메세지가 '/강퇴'면
            return



    def sendMessageToAll(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())


class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()

    def handle(self):  # 클라이언트가 접속시 클라이언트 주소 출력
        # 클라이언트의 접속요청이 수락된 후 호출됨
        # 서버와 클라이언트가  데이터를 주고 받는 메소드로 재정의해서 사용,
        # BaseRequestHandler클래스 안에 속해있는 메소드

        print('[%s] 연결됨' % self.client_address[0])


        try:
            username = self.registerUsername()
            msg = self.request.recv(1024)
            while msg:
                print(msg.decode())
                if self.userman.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)

        except Exception as e:
            print(e)

        print('[%s] 접속종료' % self.client_address[0])
        self.userman.removeUser(username)

    def registerUsername(self):

        while True:
            self.request.send('로그인ID:'.encode())

            username = self.request.recv(1024)
            username = username.decode().strip()
            #return self.userman.addUser(username,self.request,self.client_address)

            if self.userman.addUser(username, self.request, self.client_address):
                 return username



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