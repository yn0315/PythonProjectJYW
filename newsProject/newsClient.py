import socket
import tkinter
from _thread import *
import threading
from tkinter import *
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

def shopping_exit():
    global shopping
    shopping.pack_forget()
    exit_button.pack_forget()
    id_input.delete(0, len(id_input.get()))
    password_input.delete(0, len(password_input.get()))
    login_button['state'] = 'normal'


def lonin():
    values = json.dumps({
        "userId" : id_input.get(),
        "userPw" : password_input.get()

    }).encode('utf-8')
    client_socket.sendall(bytes('login'.encode('utf-8')))
    client_socket.sendall(bytes(values))

    data = client_socket.recv(16184)
    if bytes(data).decode() == "0":

        shopping.pack(side='left', fill='both', expand=True)
        shopping.pack()
        exit_button.pack()
        login_button['state'] = 'disabled'
    elif bytes(data).decode() == "1":
        tkinter.messagebox.showinfo("메세지","정보가 맞지 않습니다.")

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
        "userAddr": sign_addr_input.get(),
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
    else:
        tkinter.messagebox.showinfo("메시지","가입이 완료되었습니다.")
        sign_member()





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

password_input = Entry(window, bg='white', font=22)
password_input.place(width=300, height=40, x=600, y=530)

login_button = Button(window, text='로그인', command =lonin, width=12, height=2, bg='antiquewhite')
fontExample = tkFont.Font(family="굴림체", size=9)
login_button.configure(font=fontExample,borderwidth= 0)
login_button.place(x=950, y=455)

make_id = Button(window, text='회원 가입',  command= sign_member , width=12, height=2, bg='antiquewhite')
make_id.configure(font=fontExample,borderwidth= 0)
make_id.place(x=950, y=535)


shopping = Frame(window, relief='solid', bd=2)
exit_button = Button(shopping, text= 'EXIT', command = shopping_exit)


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

sign_password_input = Entry(signFrame, bg='white', font=22)
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

sign_addr_input = Entry(signFrame, bg='white', font=22)
sign_addr_input.place(width=300, height=40, x=220, y=570)

sign_addr_label = Label(signFrame, text="주소",background='ivory')
sign_addr_label.place(x= 150,y= 570)




window.mainloop()