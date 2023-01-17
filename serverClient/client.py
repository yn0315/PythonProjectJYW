import socket
from _thread import *
import threading
from tkinter import *
from time import sleep
import tkinter.font as tkFont
import datetime


def send(socket):
    global go_send
    while True:
        if go_send:
            message = (message_input.get(1.0,"end")).rstrip()
            socket.send(message.encode())
            message_input.delete(1.0, "end")
            go_send = False
        else:
            if go_out:
                socket.close()
                exit()
            sleep(0.1)

def receive(socket):
    first = True
    while True:
        try:
            data = socket.recv(1024)
            chat_log['state'] = 'normal'
            if first: # 이걸 처음 체크 이후 의미없이 매번 체크하므로 이렇게 하는 건 효율적이지 않음.
                chat_log.insert("end",str(data.decode( )))
                first = False
            else:
                chat_log.insert("end",'\n' + str(data.decode()))
                chat_log.see('end')
            chat_log['state'] = 'disabled'
        except ConnectionAbortedError as e:
            chat_log['state'] = 'normal'
            chat_log.insert("end", '\n[System] 접속을 종료합니다.\t' + str(datetime.datetime.now().hour) + ":"+ str(datetime.datetime.now().minute))
            chat_log['state'] = 'disabled'
            exit()

def login():
    # 서버의 ip주소 및 포트
    HOST = ip_entry.get()
    PORT = int(port_entry.get())
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    threading.Thread(target=send, args= (client_socket,)).start()
    threading.Thread(target=receive, args= (client_socket,)).start()

    exit()

def try_login():
    global go_out
    start_new_thread(login,())
    login_button['state'] = 'disabled'
    logout_button['state'] = 'active'
    ip_entry['state'] = 'readonly'
    port_entry['state'] = 'readonly'
    go_out = False

def try_logout():
    global go_out
    login_button['state'] = 'active'
    logout_button['state'] = 'disabled'
    ip_entry['state'] = 'normal'
    port_entry['state'] = 'normal'
    go_out = True

def set_go_send(event):
    global go_send
    go_send = True

go_out, go_send = False, False
window = Tk()
window.geometry('500x500')
window.configure(background='lightsteelblue')
window.title('Messenger')
window.resizable(False, False)

''' Top Menu '''
Label(window, text = 'Server IP : ',background='lightsteelblue')
Label(window, text = 'Port : ',background='lightsteelblue')
ip_entry = Entry(window, width=14)
ip_entry.insert(0,'172.20.10.2')
port_entry = Entry(window, width=5)
port_entry.insert(0,'9999')
login_button = Button(window,text='로그인', command=try_login, background='lightsteelblue', borderwidth=0,foreground='midnightblue'); login_button.place(x=350, y=18)
logout_button = Button(window,text='로그아웃',state = 'disabled', command = try_logout, background='lightsteelblue', borderwidth=0,foreground='midnightblue')
logout_button.place(x=420, y=18)

''' Middle Menu '''
chat_frame = Frame(window)
scrollbar = Scrollbar(chat_frame) ; scrollbar.pack(side='right',fill='y')
chat_log = Text(chat_frame, width = 62, height = 24, state = 'disabled', yscrollcommand = scrollbar.set)
fontExample = tkFont.Font(family="돋움체", size=8)
chat_log.configure(font=fontExample)
chat_log.pack(side='left')#place(x=20, y=60)
scrollbar['command'] = chat_log.yview # xview는 가로 스크롤 yview는 세로 스크롤
chat_frame.place(x=20, y=60)
message_input = Text(window, width = 65, height = 4)
message_input.place(x=20,y = 390)
message_input.configure(font=fontExample)

send_button = Button(window, text = '보내기', command = lambda: set_go_send(None),background='lightsteelblue',borderwidth=0,foreground='midnightblue')
send_button.place(x=430, y=405)
message_input.bind("<Return>",set_go_send)



window.mainloop()
