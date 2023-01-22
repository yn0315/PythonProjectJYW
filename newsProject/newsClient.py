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

HOST =  '172.30.1.46'
PORT =9900

#sql을 파이썬에서 활용하기 위해 pymysql 라이브러리 설치 import

con = pymysql.connect(host='localhost', user='root', password='7539518642a', db='news_db', charset='utf8')
#user,pw,host,db,charset 등 매개변수 설정 후 connect 한 객체 : con

# con 객체에서 cursor 만들기

cur = con.cursor()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

loginId = ''
loginPw = ''
searchTitle = ''
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

def newsContent_exit():
    global loginId
    global loginPw
    global newsContent
    global searchTitle
    newsContent.pack_forget()
    back_button.pack_forget()

    news.pack(side='left', fill='both', expand=True)
    news.pack()

    client_socket.sendall(bytes('back'.encode('utf-8')))

    client_socket.sendall(bytes('login2'.encode('utf-8')))

    data = json.loads(client_socket.recv(92236))
    print(data["title"][0])

    # searchTitle = data["title"]

    titleLabel1.configure(text=data["title"][0])
    titleLabel2.configure(text=data["title"][1])
    titleLabel3.configure(text=data["title"][2])
    titleLabel4.configure(text=data["title"][3])
    titleLabel5.configure(text=data["title"][4])

    contentLabel1.configure(text=data["content"][0])
    contentLabel2.configure(text=data["content"][1])
    contentLabel3.configure(text=data["content"][2])
    contentLabel4.configure(text=data["content"][3])
    contentLabel5.configure(text=data["content"][4])


def login():
    global loginId
    global searchTitle
    global loginPw

    search_input.delete(0, len(search_input.get()))

    values = json.dumps({
        "userId" : id_input.get(),
        "userPw" : password_input.get()

    }).encode('utf-8')
    # 서버로 id,pw값 전송
    loginId = id_input.get()
    loginPw = password_input.get()


    client_socket.sendall(bytes('login'.encode('utf-8')))
    client_socket.sendall(bytes(values))

    data = json.loads(client_socket.recv(16184))
    searchTitle = data["title"]




    if data["logIn"] == "1":
        news.pack(side='left', fill='both', expand=True)
        news.pack()

        json_data = json.loads(client_socket.recv(92236))

        titleLabel1.configure(text=json_data["title"][0])
        titleLabel2.configure(text=json_data["title"][1])
        titleLabel3.configure(text=json_data["title"][2])
        titleLabel4.configure(text=json_data["title"][3])
        titleLabel5.configure(text=json_data["title"][4])

        contentLabel1.configure(text=json_data["content"][0])
        contentLabel2.configure(text=json_data["content"][1])
        contentLabel3.configure(text=json_data["content"][2])
        contentLabel4.configure(text=json_data["content"][3])
        contentLabel5.configure(text=json_data["content"][4])

    elif data["logIn"] == "0":
        tkinter.messagebox.showinfo("메세지", "정보가 맞지 않습니다.")



def search_news():
    global searchTitle
    client_socket.sendall(bytes('search'.encode('utf-8')))

    searchTitle = search_input.get()
    client_socket.sendall(bytes(searchTitle.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))
    print(json_data["content"])

    titleLabel1.configure(text=json_data["title"][0])
    titleLabel2.configure(text=json_data["title"][1])
    titleLabel3.configure(text=json_data["title"][2])
    titleLabel4.configure(text=json_data["title"][3])
    titleLabel5.configure(text=json_data["title"][4])


    contentLabel1.configure(text=json_data["content"][0])
    contentLabel2.configure(text=json_data["content"][1])
    contentLabel3.configure(text=json_data["content"][2])
    contentLabel4.configure(text=json_data["content"][3])
    contentLabel5.configure(text=json_data["content"][4])


def readNews1():
    global conc
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    newsContent.pack()

    client_socket.sendall(bytes('read1'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))

    conc = ''
    for j in json_data["content"]:
        conc += j+'\n'

    news_contentLabel1.configure(text=conc)
    conc = ''

def readNews2():
    global conc1
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    newsContent.pack()

    client_socket.sendall(bytes('read2'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))

    conc1 = ''
    for j in json_data["content"]:
        conc1 += j + '\n'
    news_contentLabel1.configure(text=conc1)

    del conc1


def readNews3():
    global conc2
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    newsContent.pack()
    client_socket.sendall(bytes('read3'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))

    conc2 = ''
    for j in json_data["content"]:
        conc2 += j + '\n'
    news_contentLabel1.configure(text=conc2)

    del conc2

def readNews4():
    global conc3
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    newsContent.pack()

    client_socket.sendall(bytes('read4'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))

    conc3 = ''
    for j in json_data["content"]:
        conc3 += j + '\n'
    news_contentLabel1.configure(text=conc3)

    del conc3


def readNews5():
    global conc4
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    newsContent.pack()
    client_socket.sendall(bytes('read5'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))

    conc4 = ''
    for j in json_data["content"]:
        conc4 += j + '\n'
    news_contentLabel1.configure(text=conc4)

    del conc4


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
window.geometry('1200x900')
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
back_button.place(x= 100,y = 25)

search_input = Entry(news, bg='white', font=22)
search_input.place(width=300, height=40, x=650, y=20)

search_button = Button(news, text= '검색', command = search_news, bg='antiquewhite',width=12, height=2)
search_button.configure(font=fontExample,borderwidth=0)
search_button.place(x= 1020,y = 25)

titleLabel1 = tkinter.Label(news, background='ivory') # 아이보리
titleLabel1.place(x=100,y=100)

contentLabel1 = tkinter.Label(news, background='white',justify="left",anchor="n")
contentLabel1.place(x= 100, y=130, width=1000, height= 100)

button1 = Button(news, text= '이동', command = readNews1, bg='antiquewhite',width=12, height=2)
button1.configure(font=fontExample,borderwidth=0)
button1.place(x= 1020,y = 100)


titleLabel2 = tkinter.Label(news, background='ivory',justify="left",anchor="n") # 아이보리
titleLabel2.place(x=100,y=250)

contentLabel2 = tkinter.Label(news, background='white')
contentLabel2.place(x= 100, y=280, width=1000, height= 100)

button2 = Button(news, text= '이동', command = readNews2, bg='antiquewhite',width=12, height=2)
button2.configure(font=fontExample,borderwidth=0)
button2.place(x= 1020,y = 250)

titleLabel3 = tkinter.Label(news, background='ivory',justify="left",anchor="n") # 아이보리
titleLabel3.place(x=100,y=400)

contentLabel3 = tkinter.Label(news, background='white')
contentLabel3.place(x= 100, y=430, width=1000, height= 100)

button3 = Button(news, text= '이동', command = readNews3, bg='antiquewhite',width=12, height=2)
button3.configure(font=fontExample,borderwidth=0)
button3.place(x= 1020,y = 400)

titleLabel4 = tkinter.Label(news, background='ivory',justify="left",anchor="n") # 아이보리
titleLabel4.place(x=100,y=550)

contentLabel4 = tkinter.Label(news, background='white')
contentLabel4.place(x= 100, y=580, width=1000, height= 100)

button4 = Button(news, text= '이동', command = readNews4, bg='antiquewhite',width=12, height=2)
button4.configure(font=fontExample,borderwidth=0)
button4.place(x= 1020,y = 550)

titleLabel5 = tkinter.Label(news, background='ivory',justify="left",anchor="n") # 아이보리
titleLabel5.place(x=100,y=700)

contentLabel5 = tkinter.Label(news, background='white')
contentLabel5.place(x= 100, y=730, width=1000, height= 100)

button5 = Button(news, text= '이동', command = readNews5, bg='antiquewhite',width=12, height=2)
button5.configure(font=fontExample,borderwidth=0)
button5.place(x= 1020,y = 700)

# scrollbar = Scrollbar(news)
# scrollbar.pack(side="right", fill="y")

#################################################본문 프레임#########################################################

newsContent = Frame(window, relief='solid', bd=2,background='ivory')
content_back_button = Button(newsContent, text= '뒤로가기', command = newsContent_exit, bg='antiquewhite',width=12, height=2)
content_back_button.configure(font=fontExample,borderwidth=0)
content_back_button.place(x= 100,y = 25)

news_contentLabel1 = tkinter.Label(newsContent, background='white',justify="left",anchor="n")
news_contentLabel1.place(x= 100, y=130, width=1000, height= 800)





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