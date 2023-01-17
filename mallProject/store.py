import socket
import tkinter
from _thread import *
import threading
from tkinter import *
from time import sleep
import pymysql
#sql을 파이썬에서 활용하기 위해 pymysql 라이브러리 설치 import

con = pymysql.connect(host='localhost', user='root', password='7539518642a', db='mall_db', charset='utf8')
#user,pw,host,db,charset 등 매개변수 설정 후 connect 한 객체 : con

# con 객체에서 cursor 만들기

cur = con.cursor()





def shopping_exit():
    global shopping
    shopping.pack_forget()
    exit_button.pack_forget()
    id_input.delete(0, len(id_input.get()))
    password_input.delete(0, len(password_input.get()))
    login_button['state'] = 'normal'


def lonin():
    if id_input.get() == '111':
        if password_input.get() == '222':
            shopping.pack(side='left', fill='both', expand=True)
            shopping.pack()
            exit_button.pack()
            login_button['state'] = 'disabled'

def sign_member():
    signFrame.pack(side='left', fill='both', expand=True)
    signFrame.pack()



    return

def sign():
    print(sign_id_input.get())
    print(sign_password_input.get())
    print(sign_name_input.get())
    # sqlInsert = '''insert into members values('admin', '1234','관리자','null','F','null','2023-01-13');'''
    #sqlInsert = 'insert into members values(' + f'{sign_id_input.get()},{sign_password_input.get()}, {sign_name_input.get()},"'"+ 'null'+ "'" + ,'F',"'" +'null',"'"+'2023-01-13'+"'"+'');'
    # sqlInsert = f"insert into members values("'" + {sign_id_input.get()} + "'","'"+{sign_password_input.get()}+"'","'"+{sign_name_input.get()}+"'",'null','F','null','2023-01-13');"

    sql4 = 'INSERT INTO members VALUES(%s,%s,%s,%s,%s,%s,%s)'
    #val = [(sign_id_input.get(), sign_password_input.get(), sign_name_input.get(), 'null', 'F', 'null', '2023-01-13')]

    # cur.executemany( "INSERT INTO members (mem_id, mem_pw, mem_name, mem_addr, mem_gender, mem_phone, sign_date) VALUES('" + sign_id_input.get() + "','" + sign_password_input.get() + "','" + sign_name_input.get() + "'," + 'Null' + "," + 'Null' + "," + 'Null' + "," + '2023-01-13' + ")")
    # cur.execute('commit')

    # sql변수에 sql문법 작성
    sql = '''SELECT *
           FROM members; '''
    # 커서를 통해 sql문 실행
    # cur.execute(sqlInsert)
    #cur.execute(sql)
    cur.execute('commit')

    # 데이터 가져오기
    data = cur.fetchall()
    print(data)
    sign_member()

    # socket.socket.send(socketList)


def exit_signFrame():
    signFrame.pack_forget()



def new_window():
    # global membership    # membership = Toplevel()    # membership.geometry("300x300")
    # id_input = Entry(membership, bg='gray80', font=22)
    # id_input.place(width=300, height=40, x=180, y=450)
    # pw_input = Entry(membership, bg='gray80', font=22)
    # pw_input.place(width=300, height=40, x=180, y=450)
    # name_input = Entry(membership, bg='gray80', font=22)
    # name_input.place(width=300, height=40, x=180, y=450)
    # btn = Button(membership, text= "가입")
    # btn.pack()
    # btn2 = Button(membership, text="돌아가기", command='back')
    # btn2.pack()
    # make_id['state'] = 'disabled'
    return



def openFrame(Frame):
    Frame.tkraise()
    btnToFrame1 = tkinter.Button(window, text="change to frame1", padx=10,pady=10, command= lambda :[openFrame(frame1)])
    btnToFrame1.pack()

def openFrame2(Frame):
    Frame.tkraise()
    btnToFrame2 = tkinter.Button(window, text="change to frame1", padx=10,pady=10, command= lambda :[openFrame(frame1)])
    btnToFrame2.pack()


window = Tk()
window.geometry('800x800')
window.title('MUSINSA')
window.configure(bg='white')
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


photo = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\mu2.png")

logo = Label(window, image=photo)
logo.place(x=160, y=100)

id_input = Entry(window, bg='gray80', font=22)
id_input.place(width=300, height=40, x=180, y=450)

password_input = Entry(window, bg='gray80', font=22)
password_input.place(width=300, height=40, x=180, y=530)

login_button = Button(window, text='Log In', command =lonin, width=12, height=7, bg='gray80', font=22)
login_button.place(x=510, y=445)

make_id = Button(window, text='회원 가입',  command= sign_member , width=12, height=2, bg='white', font=22)
make_id.place(x=510, y=580)


shopping = Frame(window, relief='solid', bd=2)
exit_button = Button(shopping, text= 'EXIT', command = shopping_exit)


signFrame = Frame(window, relief='solid', bd=2)
sign_button = Button(signFrame, text= '가입', command = sign)
sign_button.place(x= 500,y = 700)

back_button = Button(signFrame, text= '뒤로가기', command = exit_signFrame)
back_button.place(x= 300,y = 700)

sign_id_label = Label(signFrame, text="아이디")
sign_id_label.place(x= 150,y= 450)

sign_id_input = Entry(signFrame, bg='gray80', font=22)
sign_id_input.place(width=300, height=40, x=220, y=450)

sign_pw_label = Label(signFrame, text="비밀번호")
sign_pw_label.place(x= 150,y= 530)

sign_password_input = Entry(signFrame, bg='gray80', font=22)
sign_password_input.place(width=300, height=40, x=220, y=530)

sign_name_label = Label(signFrame, text="이름")
sign_name_label.place(x= 150,y= 610)


sign_name_input = Entry(signFrame, bg='gray80', font=22)
sign_name_input.place(width=300, height=40, x=220, y=610)







window.mainloop()