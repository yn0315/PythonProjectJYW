import socket
import time
import tkinter
from _thread import *
import threading
from tkinter import *
from tkinter import ttk
from time import sleep
import pymysql
import tkinter.font as tkFont
import json
import tkinter.messagebox

HOST = '192.168.0.5'
PORT =9900

#sql을 파이썬에서 활용하기 위해 pymysql 라이브러리 설치 import

con = pymysql.connect(host='localhost', user='root', password='7539518642a', db='news_db', charset='utf8')
#user,pw,host,db,charset 등 매개변수 설정 후 connect 한 객체 : con

# con 객체에서 cursor 만들기

cur = con.cursor()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))


def exit_window():
    window.destroy()
def news_exit():
    global news
    news.pack_forget()
    back_button.pack_forget()
    client_socket.sendall(bytes('main'.encode('utf-8')))
    id_input.delete(0, len(id_input.get()))
    password_input.delete(0, len(password_input.get()))
    login_button['state'] = 'normal'


def login():
    values = json.dumps({
        "userId" : id_input.get(),
        "userPw" : password_input.get()

    }).encode('utf-8')
    # 서버로 id,pw값 전송
    client_socket.sendall(bytes('login'.encode('utf-8')))
    client_socket.sendall(bytes(values))


    data = json.loads(client_socket.recv(16184))
    print(data , "data!!!!!!!!!!!!")


    if data["logIn"] == "1":
        news.pack(side='left', fill='both', expand=True)
        news.pack()
        print(data)
    elif data["logIn"] == "0":
        tkinter.messagebox.showinfo("메세지", "정보가 맞지 않습니다.")

    # 검색.......검색.......검색..............



def sign_member():
    signFrame.pack(side='left', fill='both', expand=True)
    signFrame.pack()
    client_socket.sendall(bytes("sign".encode('utf-8')))

    return

def sign():
    print(sign_id_input.get())
    print(sign_password_input.get())
    print(sign_name_input.get())


    # 헤드리스 찾아보기

    values = json.dumps({

        "userId": sign_id_input.get(),
        "userPw": sign_password_input.get(),
        "userName": sign_name_input.get(),
        "userAddr": addr_combobox.get(),
        "userGender": sign_gender_input.get(),
        "userAge": sign_age_input.get()

    }).encode('utf-8')

    #print(type(values))
    #json_string = json.dumps(values)
    #print(type(json_string))

    try:
        client_socket.sendall(bytes(values))

    except Exception as ex:
        print(type(ex), ex)


    data = client_socket.recv(16184)
    if bytes(data).decode() == "1":
        tkinter.messagebox.showinfo("메시지","존재하는 아이디입니다.")
    elif bytes(data).decode() == "0":
        tkinter.messagebox.showinfo("메시지","가입이 완료되었습니다.")


def exit_signFrame():
    signFrame.pack_forget()


window = Tk()
window.geometry('1200x800')
window.title('NewsWindow')

window.configure(bg='ivory')
window.resizable(False, False)


frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)
frame3 = tkinter.Frame(window)

# frame1.grid(row=0, column=0, sticky="nsew")
# frame2.grid(row=0, column=0, sticky="nsew")
# frame3.grid(row=0, column=0, sticky="nsew")
frame1.pack()

# photo = PhotoImage(file = 'C:\\Users\\202-uil\\Desktop\\KCY\\musinsa.jpg')
# musin = Label(window, image=photo, width=464, height=350)
# musin.pack(expand=1, anchor=CENTER)


# photo = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\mu2.png")

#logo = Label(window, image=photo)
#logo.place(x=160, y=100)

id_input = Entry(window, bg='white', font=22)
id_input.place(width=300, height=40, x=600, y=450)

password_input = Entry(window, bg='white', font=22,show='*')
password_input.place(width=300, height=40, x=600, y=530)

login_button = Button(window, text='로그인', command =login, width=12, height=2, bg='antiquewhite')
fontExample = tkFont.Font(family="굴림체", size=9)
login_button.configure(font=fontExample,borderwidth= 0)
login_button.place(x=950, y=455)

make_id = Button(window, text='회원 가입',  command= sign_member , width=12, height=2, bg='antiquewhite')
make_id.configure(font=fontExample,borderwidth= 0)
make_id.place(x=950, y=535)

#############################################뉴스 프레임##############################################################
news = Frame(window, relief='solid', bd=2,background='ivory')
back_button = Button(news, text= '뒤로가기', command = news_exit, bg='antiquewhite',width=12, height=2)
back_button.configure(font=fontExample,borderwidth=0)
back_button.place(x= 30,y = 25)

sign_id_input = Entry(news, bg='white', font=22)
sign_id_input.place(width=300, height=40, x=700, y=20)

search_button = Button(news, text= '검색', command = exit_signFrame, bg='antiquewhite',width=12, height=2)
search_button.configure(font=fontExample,borderwidth=0)
search_button.place(x= 1050,y = 25)

titleLabel = tkinter.Label(news, text='rkrkrk',background='ivory')
titleLabel.place(x=30,y=100)


###################################################################################################################

signFrame = Frame(window, relief='solid', bd=2,background='ivory')
sign_button = Button(signFrame, text= '가입', command = sign,bg='antiquewhite',width=12, height=2)
sign_button.configure(font= fontExample,borderwidth=0)
sign_button.place(x= 440,y = 700)

back_button = Button(signFrame, text= '뒤로가기', command = exit_signFrame, bg='antiquewhite',width=12, height=2)
back_button.configure(font=fontExample,borderwidth=0)
back_button.place(x= 300,y = 700)

sign_id_label = Label(signFrame, text="아이디",background='ivory')
sign_id_label.place(x= 150,y= 170)

sign_id_input = Entry(signFrame, bg='white', font=22)
sign_id_input.place(width=300, height=40, x=220, y=170)

sign_pw_label = Label(signFrame, text="비밀번호",background='ivory')
sign_pw_label.place(x= 150,y= 250)

sign_password_input = Entry(signFrame, bg='white', font=22,show='*')
sign_password_input.place(width=300, height=40, x=220, y=250)

sign_name_label = Label(signFrame, text="이름",background='ivory')
sign_name_label.place(x= 150,y= 330)

sign_name_input = Entry(signFrame, bg='white', font=22)
sign_name_input.place(width=300, height=40, x=220, y=330)

sign_gender_input = Entry(signFrame, bg='white', font=22)
sign_gender_input.place(width=300, height=40, x=220, y=410)

sign_gender_label = Label(signFrame, text="성별",background='ivory')
sign_gender_label.place(x= 150,y= 410)

sign_age_input = Entry(signFrame, bg='white', font=22)
sign_age_input.place(width=300, height=40, x=220, y=490)

sign_age_label = Label(signFrame, text="나이",background='ivory')
sign_age_label.place(x= 150,y= 490)

#sign_addr_input = Entry(signFrame, bg='white', font=22)
#sign_addr_input.place(width=300, height=40, x=220, y=570)

sign_addr_label = Label(signFrame, text="주소",background='ivory')
sign_addr_label.place(x= 150,y= 570)

a=["서울", "경기", "강원", "충북", "충남", "대전","세종", "경북", "경남", "전북", "전남", "제주"]           # 콤보 박스에 나타낼 항목 리스트
addr_combobox = tkinter.ttk.Combobox(signFrame)    # root라는 창에 콤보박스 생성
addr_combobox.config(height=40,width=40)           # 높이 설정
addr_combobox.config(values=a)           # 나타낼 항목 리스트(a) 설정
addr_combobox.config(state="readonly")   # 콤보 박스에 사용자가 직접 입력 불가
addr_combobox.set("서울")           # 맨 처음 나타낼 값 설정
addr_combobox.place(x= 220,y= 570)


window.protocol('WM_DELETE_WINDOW',exit_window)

window.mainloop()