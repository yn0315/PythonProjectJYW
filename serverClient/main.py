import socket
from _thread import *

import threaded as threaded

import client
import client2

client_sockets = [] # 서버에 접속한 클라이언트 목록

# 서버 IP 및 열어줄 포트
HOST = '172.20.10.2'
PORT = 9999

# 서버 소켓 생성
print('>> Server Start')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

# 서버 사이드 공통 구현기능

# 메시지 전송자 id, 시간표시
# 로그인 권한(우리반 학생만 접속 가틍)
# 관리자 id 따로 지정
# 관리자 권한 공지
# 관리자 권한 로그인 차단
# 관리자 권한 퇴장시키기
# 비속어 필터


try:
    while True:
        print('>> Wait')

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수 : ", len(client_sockets))

except Exception as e:
    print('에러는? : ', e)

finally:
    server_socket.close()


    # 쓰레드에서 실행되는 코드입니다.
    # 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
    def threaded(client_socket, addr):
        print('>> Connected by :', addr[0], ':', addr[1])

        # 클라이언트가 접속을 끊을 때 까지 반복합니다.
        while True:

            try:

                # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
                data = client_socket.recv(1024)

                if not data:
                    print('>> Disconnected by ' + addr[0], ':', addr[1])
                    break

                print('>> Received from ' + addr[0], ':', addr[1], data.decode())


                # 서버에 접속한 클라이언트들에게 채팅 보내기
                # 메세지를 보낸 본인을 제외한 서버에 접속한 클라이언트에게 메세지 보내기
                # for client in client_sockets:
                #     if client != client_socket: # 본인 글 못 보게 막혀있는 코드 주석처리하면 보임
                #         client.send(data)




            except ConnectionResetError as e:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

        if client_socket in client_sockets:
            client_sockets.remove(client_socket)
            print('remove client list : ', len(client_sockets))

        client_socket.close()


