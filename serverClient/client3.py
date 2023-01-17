import datetime
import socket, threading

import socket
from _thread import *
import threading
from tkinter import *
from time import sleep
import tkinter.font as tkFont


# 서버 사이드 공통 구현기능

# 메시지 전송자 id, 시간표시
# 로그인 권한(우리반 학생만 접속 가능)
# 관리자 id 따로 지정
# 관리자 권한 공지
# 관리자 권한 로그인 차단
# 관리자 권한 퇴장시키기
# 비속어 필터

idList = ['관리자', '조윤우'] # 아이디 리스트
admin = False # 관리자 권한 부여시 필요한 변수
class Room:  # 채팅방 클래스.
    def __init__(self):
        self.clients = [] # 클라이 언트 들어오는 곳
        self.allChat=None

    def addClient(self, c):  # c: 텔레마케터 . 클라이언트 1명씩 전담하는 쓰레드
        self.clients.append(c)

    def delClient(self, c):
        self.clients.remove(c)

    def sendMsgAll(self, msg):  # 채팅방에 있는 모든 사람한테 메시지 전송
        for i in self.clients:
            print(i)
            i.sendMsg(msg)

    def sendNotice(self, msg):
        for i in self.clients:
            print(i)
            i.sendMsg(msg)





class ChatClient:  # 텔레마케터
    def __init__(self, r, soc):
        self.room = r  # 채팅방. Room 객체
        self.id = None  # 사용자 id
        self.soc = soc  # 사용자와 1:1 통신할 소켓

    def readMsg(self):

        for i in range(len(idList)):
            if self.soc.recv(1024).decode() == idList[i]:
                self.id = self.soc.recv(1024).decode()
            else:
                self.room.sendMsgAll('다시 입력해주세요.')
                continue


        if self.id == '관리자':
            global admin
            admin = True


        msg = self.id + '님이 입장하셨습니다' + '\t' + str(datetime.datetime.now().hour) + ":"+ str(datetime.datetime.now().minute)
        self.room.sendMsgAll(msg)

        while True:

            msg = self.soc.recv(1024).decode()  # 사용자가 전송한 메시지 읽음
            if msg == '/stop':  # 종료 메시지이면 루프 종료
                self.soc.sendall(msg + '\t' + str(datetime.datetime.now().hour) + ":"+ str(datetime.datetime.now().minute))  # 이 메시지를 보낸 한명에게만 전송
                self.room.delClient(self)
                break
            msg = self.id+': '+ msg
            self.room.sendMsgAll(msg)  # 모든 사용자에 메시지 전송
        self.room.sendMsgAll(self.id + '님이 퇴장하셨습니다.\t' + str(datetime.datetime.now().hour) + ":"+ str(datetime.datetime.now().minute))

    def sendMsg(self, msg):
        print(type(msg))
        self.soc.sendall(msg.encode(encoding='utf-8') + '\t'+ str(datetime.datetime.now().hour) + ":"+ str(datetime.datetime.now().minute))



class ChatServer:
    ip = '172.20.10.2'  # or 본인 ip or 127.0.0.1
    port = 9999

    def __init__(self):
        self.server_soc = None  # 서버 소켓(대문)
        self.room = Room()

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((ChatServer.ip, ChatServer.port))
        self.server_soc.listen()

    def run(self):
        self.open()
        print('서버 시작11')

        while True:
            client_soc, addr = self.server_soc.accept()
            print(addr, '접속')
            c = ChatClient(self.room, client_soc)
            self.room.addClient(c)
            print('클라:',self.room.clients)
            th = threading.Thread(target=c.readMsg)
            th.start()

        self.server_soc.close()


def main():
    cs = ChatServer()
    cs.run()


main()