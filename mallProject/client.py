import tkinter
from tkinter import *
from tkinter import ttk

# tkinter 객체 생성
window = Tk()
window.title("Frmae_change")
window.geometry("600x600+200+200")

frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)
frame3 = tkinter.Frame(window)

frame1.grid(row=0,column=0,sticky= "nsew")
frame2.grid(row=0,column=0,sticky= "nsew")
frame3.grid(row=0,column=0,sticky= "nsew")
# 사용자 id와 password를 저장하는 변수 생성
user_id, password = StringVar(), StringVar()

def openFrame(frame):
    frame.tkrase()
    btnToFrame1 = tkinter.Button(frame3, text="change to frame1", padx=10,pady=10, command= lambda :[openFrame(frame2)])
    btnToFrame1.pack()

def openFrame2(frame):
    frame.tkrase()
    btnToFrame2 = tkinter.Button(frame3, text="change to frame1", padx=10,pady=10, command= lambda :[openFrame(frame1)])
    btnToFrame2.pack()
# 사용자 id와 password를 비교하는 함수
def check_data():
    if user_id.get() == "admin" and password.get() == "1234":
        print("Logged IN Successfully")
        f = ttk.Frame(window, width=200, height= 100, relief='solid')
        f.pack()
        openFrame(frame1)


    else:
        print("Check your Usernam/Password")
        f = ttk.Frame(window, width=200, height=100, relief='solid')
        f.pack()
        openFrame(frame1)


# id와 password, 그리고 확인 버튼의 UI를 만드는 부분
ttk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = password).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Button(window, text = "Login", command = openFrame(frame1)).grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()