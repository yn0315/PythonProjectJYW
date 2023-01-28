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
import os
import threading
import PyInstaller




HOST = '172.30.1.46'
PORT =9900

current_working_directory = os.getcwd()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))


loginId = ''
loginPw = ''
searchTitle = ''

g_age = 0
g_gen = ''
g_replyList = []

g_labelX = 100
g_labelY = 100
g_titleLabelX = 100
g_titleLabelY = 100
g_replyInput = ''
# 터미널에 명령어 pyinstaller -w -F 클라이언트 파일명.py
# 콘솔 나타내지 않는 옵션
# -F 단일파일 exe로 묶는 옵션
# 터미널 경로를 클라이언트 py를 포함하고 있는 경로로 설정
# exe결과물은 해당 폴더 아래 dist폴더에 생성됨


class replyBox():
    def __init__(self, textContent, id):
        global g_labelX
        global g_labelY
        global g_titleLabelX
        global g_titleLabelY
        replyLabel = tkinter.Label(FF, background='white', justify="left", anchor="n", wraplength=980, pady=20, text='"' + textContent + '"')
        titleLabel1 = tkinter.Label(FF, background='ivory', text=id)  # 아이보리
        titleFont = tkFont.Font(weight='bold', size=10)
        titleLabel1.configure(font=titleFont)

        if g_labelY == 100:
            replyLabel.place(x=g_labelX, y=g_labelY, width=1000, height=100)
            titleLabel1.place(x=g_titleLabelX, y=g_titleLabelY)
            g_labelY = 210
            g_titleLabelY = 220



        elif g_labelY != 100:
            replyLabel.place(x=g_labelX, y=g_labelY, width=1000, height=100)
            g_labelY = g_labelY + 110
            print(g_labelY)
            titleLabel1.place(x=g_titleLabelX, y=g_titleLabelY)
            g_titleLabelY = g_titleLabelY + 110

class Reply:
    replyList = []

    def __init__(self, newsNum,newsLength):

        tempNews = list(0 for i in range(newsLength))
        Reply.replyList = tempNews


    # def createReply(self):
        tempNews[newsNum] = {"writer": "", "reply": ""}
        for i in range(len(Reply.replyList)):
            Reply.replyList[i] = tempNews[i]

def registerComment():
    global g_replyInput
    g_replyInput = FF_input.get()
    replyBox(FF_input.get(), loginId)
    FF_input.delete(0, len(FF_input.get()))
    client_socket.sendall(bytes('replyContent'.encode('utf-8')))
    client_socket.sendall(bytes(g_replyInput.encode('utf-8')))



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

    contentLabel1.configure(text=str(data["content"][0]).strip())
    contentLabel2.configure(text=str(data["content"][1]).strip())
    contentLabel3.configure(text=str(data["content"][2]).strip())
    contentLabel4.configure(text=str(data["content"][3]).strip())
    contentLabel5.configure(text=str(data["content"][4]).strip())

def updateInputBox(title):
    if g_age != '나이순' and g_gen != '성별순':
        mainLabel.configure(text='"' + g_age+'대", ' +'"'+ g_gen+'성"의 키워드 '+ '"'+title+'"')
    elif g_age =='나이순' and g_gen != '성별순':
        mainLabel.configure(text='"' + g_gen + '성"의 키워드 ' + '"' + title + '"')
    elif g_age != '나이순' and g_gen =='성별순':
        mainLabel.configure(text='"' + g_age + '대"의 키워드 ' + '"' + title + '"')
    elif g_age == '나이순' and g_gen == '성별순':
        mainLabel.configure(text='"'+ loginId + '"님의 키워드' +'"'+title+'"')

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

    data = json.loads(client_socket.recv(92236))
    searchTitle = data["title"]


    if data["logIn"] == "1":
        # container.pack(side='left', fill='both', expand=True)
        news.pack(side='left', fill='both', expand=True)
        #news.pack()
        # scrollbar.pack(side="right", fill="y")

        json_data = json.loads(client_socket.recv(92236))

        #upd(json_data["g_title"])

        titleLabel1.configure(text=json_data["title"][0])
        titleLabel2.configure(text=json_data["title"][1])
        titleLabel3.configure(text=json_data["title"][2])
        titleLabel4.configure(text=json_data["title"][3])
        titleLabel5.configure(text=json_data["title"][4])


        contentLabel1.configure(text=str(json_data["content"][0]).strip())
        contentLabel2.configure(text=str(json_data["content"][1]).strip())
        contentLabel3.configure(text=str(json_data["content"][2]).strip())
        contentLabel4.configure(text=str(json_data["content"][3]).strip())
        contentLabel5.configure(text=str(json_data["content"][4]).strip())

    elif data["logIn"] == "0":
        tkinter.messagebox.showinfo("메세지", "정보가 맞지 않습니다.")



def search_news():
    global searchTitle
    client_socket.sendall(bytes('search'.encode('utf-8')))

    searchTitle = search_input.get()
    print(searchTitle,"검색어")
    client_socket.sendall(bytes(searchTitle.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))
    print(json_data["title"][0])

    titleLabel1.configure(text=json_data["title"][0])
    titleLabel2.configure(text=json_data["title"][1])
    titleLabel3.configure(text=json_data["title"][2])
    titleLabel4.configure(text=json_data["title"][3])
    titleLabel5.configure(text=json_data["title"][4])


    contentLabel1.configure(text=str(json_data["content"][0]).strip())
    contentLabel2.configure(text=str(json_data["content"][1]).strip())
    contentLabel3.configure(text=str(json_data["content"][2]).strip())
    contentLabel4.configure(text=str(json_data["content"][3]).strip())
    contentLabel5.configure(text=str(json_data["content"][4]).strip())


def ageGen_news():
    global g_age
    global g_gen

    client_socket.sendall(bytes('select'.encode('utf-8')))

    g_age = age_combobox.get()
    g_gen = gen_combobox.get()

    values = json.dumps({
        "userAge" : g_age,
        "userGen" : g_gen

    }).encode('utf-8')

    client_socket.sendall(bytes(values))

    json_data = json.loads(client_socket.recv(92236))
    print(json_data["content"])

    updateInputBox(json_data["selectTitle"])


    titleLabel1.configure(text=json_data["title"][0])
    titleLabel2.configure(text=json_data["title"][1])
    titleLabel3.configure(text=json_data["title"][2])
    titleLabel4.configure(text=json_data["title"][3])
    titleLabel5.configure(text=json_data["title"][4])

    contentLabel1.configure(text=str(json_data["content"][0]).strip())
    contentLabel2.configure(text=str(json_data["content"][1]).strip())
    contentLabel3.configure(text=str(json_data["content"][2]).strip())
    contentLabel4.configure(text=str(json_data["content"][3]).strip())
    contentLabel5.configure(text=str(json_data["content"][4]).strip())


def readNews1():
    global conc
    global concArr
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    #newsContent.pack()

    client_socket.sendall(bytes('read1'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))


    conc = ''

    concArr = []

    Reply(json_data["newsNum"], json_data["newsLength"])
    # client_socket.sendall(bytes('replyContent'.encode('utf-8')))
    # client_socket.sendall(bytes(FF_input.get().encode('utf-8')))
    # print(bytes(FF_input.get().encode('utf-8')))


    for i in range(len(json_data["content"]) -1):
        concArr.append(json_data["content"][i])

    for j in range(len(concArr)):
        if j == 0:
            conc += concArr[j] + '\n\n\n'
        else:
            conc += concArr[j] + '\n\n'

    news_contentLabel1.configure(text=conc)
    conc = ''

def readNews2():
    global conc1
    global concArr1
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    #newsContent.pack()

    client_socket.sendall(bytes('read2'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))
    client_socket.sendall(bytes('replyContent'.encode('utf-8')))
    client_socket.sendall(bytes(FF_input.get().encode('utf-8')))

    conc1 = ''
    concArr1 = []
    Reply(json_data["newsNum"], json_data["newsLength"])
    for i in range(len(json_data["content"]) - 1):
        concArr1.append(json_data["content"][i])

    for j in range(len(concArr1)):
        if j == 0:
            conc1 += concArr1[j] + '\n\n\n'
        else:
            conc1 += concArr1[j] + '\n\n'
    news_contentLabel1.configure(text=conc1)

    del conc1


def readNews3():
    global conc2
    global concArr2
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    #newsContent.pack()
    client_socket.sendall(bytes('read3'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))
    client_socket.sendall(bytes('replyContent'.encode('utf-8')))
    client_socket.sendall(bytes(FF_input.get().encode('utf-8')))

    conc2 = ''

    concArr2 = []
    Reply(json_data["newsNum"], json_data["newsLength"])
    for i in range(len(json_data["content"]) - 1):
        concArr2.append(json_data["content"][i])

    for j in range(len(concArr2)):
        if j == 0:
            conc2 += concArr2[j] + '\n\n\n'
        else:
            conc2 += concArr2[j] + '\n\n'
    news_contentLabel1.configure(text=conc2)

    del conc2

def readNews4():
    global conc3
    global concArr3
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    #newsContent.pack()

    client_socket.sendall(bytes('read4'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))

    conc3 = ''

    concArr3 = []
    Reply(json_data["newsNum"], json_data["newsLength"])
    client_socket.sendall(bytes('replyContent'.encode('utf-8')))
    client_socket.sendall(bytes(FF_input.get().encode('utf-8')))

    for i in range(len(json_data["content"]) - 1):
        concArr3.append(json_data["content"][i])

    for j in range(len(concArr3)):
        if j == 0:
            conc3 += concArr3[j] + '\n\n\n'
        else:
            conc3 += concArr3[j] + '\n\n'
    news_contentLabel1.configure(text=conc3)

    del conc3


def readNews5():
    global conc4
    global concArr4
    news.pack_forget()
    newsContent.pack(side='left', fill='both', expand=True)
    #newsContent.pack()
    client_socket.sendall(bytes('read5'.encode('utf-8')))

    json_data = json.loads(client_socket.recv(92236))

    conc4 = ''
    concArr4 = []
    Reply(json_data["newsNum"], json_data["newsLength"])
    client_socket.sendall(bytes('replyContent'.encode('utf-8')))
    client_socket.sendall(bytes(FF_input.get().encode('utf-8')))

    for i in range(len(json_data["content"]) - 1):

        concArr4.append(json_data["content"][i])

    for j in range(len(concArr4)):
        if j == 0:
            conc4 += concArr4[j] + '\n\n\n'
        else:
            conc4 += concArr4[j] + '\n\n'
    news_contentLabel1.configure(text=conc4)

    del conc4

def readReply():
    newsContent.pack_forget()
    FF.pack(side='left', fill='both', expand=True)

    pass


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

photo = PhotoImage(file = 'newsImg.png')
logo = Label(window, image=photo)
logo.pack(expand=1, anchor=CENTER)
logo.place(x=250, y=250)

id_input = Entry(window, bg='white', font=22)
id_input.place(width=300, height=40, x=700, y=450)

password_input = Entry(window, bg='white', font=22,show='*')
password_input.place(width=300, height=40, x=700, y=530)

login_button = Button(window, text='로그인', command =login, width=12, height=2, bg='antiquewhite')
fontExample = tkFont.Font(family="굴림체", size=9)
login_button.configure(font=fontExample,borderwidth= 0)
login_button.place(x=1020, y=455)

make_id = Button(window, text='회원 가입',  command= sign_member , width=12, height=2, bg='antiquewhite')
make_id.configure(font=fontExample,borderwidth= 0)
make_id.place(x=1020, y=535)

#############################################뉴스 프레임##############################################################

#####################################################

news = Frame(window, relief='solid',background='ivory')
# scrollbar = ttk.Scrollbar(news,orient='vertical',command=news.yview)
# scrollable_frame = ttk.Frame(news)
#
# scrollbar.bind('<Configure>', lambda e: news.configure(scrollregion=news.bbox("all")))
#
# news.create_window((0,0),window=scrollable_frame,anchor='nw')
# news.configure(yscrollcommand=scrollbar.set)

#####################################################

back_button = Button(news, text= '뒤로가기', command = news_exit, bg='antiquewhite',width=12, height=2)
back_button.configure(font=fontExample,borderwidth=0)
back_button.place(x= 100,y = 25)

######################################################################################################

age=["10", "20", "30", "40", "50", "60"]           # 콤보 박스에 나타낼 항목 리스트
age_combobox = tkinter.ttk.Combobox(news)    # root라는 창에 콤보박스 생성
age_combobox.config(height=40,width=10)           # 높이 설정
age_combobox.config(values=age)           # 나타낼 항목 리스트(a) 설정
age_combobox.config(state="readonly")   # 콤보 박스에 사용자가 직접 입력 불가
age_combobox.set("나이순")           # 맨 처음 나타낼 값 설정
age_combobox.place(x= 200,y= 25)


gen=["남", "여"]           # 콤보 박스에 나타낼 항목 리스트
gen_combobox = tkinter.ttk.Combobox(news)    # root라는 창에 콤보박스 생성
gen_combobox.config(height=40,width=10)           # 높이 설정
gen_combobox.config(values=gen)           # 나타낼 항목 리스트(a) 설정
gen_combobox.config(state="readonly")   # 콤보 박스에 사용자가 직접 입력 불가
gen_combobox.set("성별순")           # 맨 처음 나타낼 값 설정
gen_combobox.place(x= 300,y= 25)

ageGen_button = Button(news, text= '조회', command = ageGen_news, bg='antiquewhite',width=12, height=2)
ageGen_button.configure(font=fontExample,borderwidth=0)
ageGen_button.place(x= 410,y = 25)

mainLabel = tkinter.Label(news, background='white',justify="left",anchor="n",wraplength=980,pady=10)
mainLabel.place(x= 200, y=70, width=290, height= 30)

######################################################################################################
search_input = Entry(news, bg='white', font=22)
search_input.place(width=300, height=40, x=650, y=20)

search_button = Button(news, text= '검색', command = search_news, bg='antiquewhite',width=12, height=2)
search_button.configure(font=fontExample,borderwidth=0)
search_button.place(x= 1020,y = 25)

titleLabel1 = tkinter.Label(news, background='ivory') # 아이보리
titleFont= tkFont.Font(weight='bold',size=10)
titleLabel1.configure(font=titleFont)
titleLabel1.place(x=100,y=110)

contentLabel1 = tkinter.Label(news, background='white',justify="left",anchor="n",wraplength=980,pady=10)
contentLabel1.place(x= 100, y=140, width=1000, height= 100)

button1 = Button(news, text= '이동', command = readNews1, bg='antiquewhite',width=12, height=2)
button1.configure(font=fontExample,borderwidth=0)
button1.place(x= 1020,y = 110)


titleLabel2 = tkinter.Label(news, background='ivory',justify="left",anchor="n") # 아이보리
titleLabel2.configure(font=titleFont)
titleLabel2.place(x=100,y=260)

contentLabel2 = tkinter.Label(news, background='white',justify="left",anchor="n",wraplength=980,pady=10)
contentLabel2.place(x= 100, y=290, width=1000, height= 100)

button2 = Button(news, text= '이동', command = readNews2, bg='antiquewhite',width=12, height=2)
button2.configure(font=fontExample,borderwidth=0)
button2.place(x= 1020,y = 260)

titleLabel3 = tkinter.Label(news, background='ivory',justify="left",anchor="n") # 아이보리
titleLabel3.configure(font=titleFont)
titleLabel3.place(x=100,y=410)

contentLabel3 = tkinter.Label(news, background='white',justify="left",anchor="n",wraplength=980,pady=10)
contentLabel3.place(x= 100, y=440, width=1000, height= 100)

button3 = Button(news, text= '이동', command = readNews3, bg='antiquewhite',width=12, height=2)
button3.configure(font=fontExample,borderwidth=0)
button3.place(x= 1020,y = 410)

titleLabel4 = tkinter.Label(news, background='ivory',justify="left",anchor="n") # 아이보리
titleLabel4.configure(font=titleFont)
titleLabel4.place(x=100,y=560)

contentLabel4 = tkinter.Label(news, background='white',justify="left",anchor="n",wraplength=980,pady=10)
contentLabel4.place(x= 100, y=590, width=1000, height= 100)

button4 = Button(news, text= '이동', command = readNews4, bg='antiquewhite',width=12, height=2)
button4.configure(font=fontExample,borderwidth=0)
button4.place(x= 1020,y = 560)

titleLabel5 = tkinter.Label(news, background='ivory',justify="left",anchor="n") # 아이보리
titleLabel5.configure(font=titleFont)
titleLabel5.place(x=100,y=710)

contentLabel5 = tkinter.Label(news, background='white',justify="left",anchor="n",wraplength=980,pady=10)
contentLabel5.place(x= 100, y=740, width=1000, height= 100)

button5 = Button(news, text= '이동', command = readNews5, bg='antiquewhite',width=12, height=2)
button5.configure(font=fontExample,borderwidth=0)
button5.place(x= 1020,y = 710)


#################################################본문 프레임#########################################################

newsContent = Frame(window, relief='solid',background='ivory')
content_back_button = Button(newsContent, text= '뒤로가기', command = newsContent_exit, bg='antiquewhite',width=12, height=2)
content_back_button.configure(font=fontExample,borderwidth=0)
content_back_button.place(x= 100,y = 25)

news_contentLabel1 = tkinter.Label(newsContent, background='white',justify="left",anchor="n",wraplength=980,pady=10)
news_contentLabel1.place(x= 100, y=130, width=1000, height= 700)

button4 = Button(newsContent, text= '댓글', command = readReply, bg='antiquewhite',width=12, height=2)
button4.configure(font=fontExample,borderwidth=0)
button4.place(x= 1020,y = 110)

###
FF= Frame(window, relief='solid',background='ivory')
FF_button = Button(FF, text= '등록', bg='antiquewhite',width=12, height=2, command= registerComment)
FF_button.configure(font=fontExample,borderwidth=0)
FF_button.place(x= 420,y = 30)

FF_input = Entry(FF, bg='white', font=22)
FF_input.place(width=300, height=40, x=100, y=25)


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