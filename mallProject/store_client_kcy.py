import socket
import tkinter.ttk
from _thread import *
import threading
from tkinter import *
from time import sleep

def sign_member():
    signFrame.pack(side='left', fill='both', expand=True)
    signFrame.pack()

    return

def exit_signFrame():
    signFrame.pack_forget()


def Lonin(evevt):
    if id_input.get() == '111':
        if password_input.get() == '111':
            shopping.pack(side="left", fill="both", expand=True)
            exit_button.place(x=730, y=18)
            cate1_button.place(x=0, y= 100)
            cate2_button.place(x=0, y= 200)
            cate3_button.place(x=0, y= 300)
            cate4_button.place(x=0, y= 400)
            cate5_button.place(x=0, y= 500)
            cate6_button.place(x=0, y=600)



            login_button['state'] = 'disabled'
            make_id['state'] = 'disabled'


def Shopping_Exit():
    global shopping
    shopping.pack_forget()
    login_button['state'] = 'normal'
    make_id['state'] = 'normal'
    id_input.delete(0, len(id_input.get()))
    password_input.delete(0, len(password_input.get()))

def Goods_T():
    GT.place(x=200, y=100)




def new_window():
    global membership
    global window

    membership = Toplevel()
    membership.title('회원가입')
    make_id['state'] = 'disabled'
    #login_button['state'] = 'disabled'



window = Tk()
window.geometry('800x800')
window.title('MUSINSA')
window.configure(bg='white')
window.resizable(False, False)






photo = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\mu2.png")
category1 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\t-shirt.png")
category2 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\pants.png")
category3 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\dress.png")
category4 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\shoes1.png")
category5 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\shoes2.png")
category6 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\cap.png")

logo = Label(window, image=photo)
logo.place(x=160, y=100)

id_input = Entry(window, bg='gray80', font=22)
id_input.place(width=300, height=40, x=180, y=450)

password_input = Entry(window, bg='gray80', font=22)
password_input.place(width=300, height=40, x=180, y=530)

login_button = Button(window, text='Log In', width=12, height=7, bg='gray80', font=22)
login_button.bind('<Return>', Lonin)
login_button.place(x=510, y=445)

make_id = Button(window, text='회원 가입',  command = new_window, width=12, height=2, bg='white', font=22)
make_id.place(x=510, y=580)

shopping = Frame(window, relief="solid", bd=2, bg='white')
exit_button = Button(shopping, text='X', font=20, command=Shopping_Exit, width=4, height=2, bg='red2')
cate1_button = Button(shopping, image=category1, command=Goods_T)
cate2_button = Button(shopping, image=category2)
cate3_button = Button(shopping, image=category3)
cate4_button = Button(shopping, image=category4)
cate5_button = Button(shopping, image=category5)
cate6_button = Button(shopping, image=category6)

GT = tkinter.ttk.Treeview(shopping, height=10, columns=["one", "two","three"], displaycolumns=["one","two","three"])
GT.column("#0", width=100,)
GT.heading("#0", text="제품코드")

GT.column("#1", width=100, anchor="center")
GT.heading("one", text="제품이름", anchor="center")

GT.column("#2", width=100, anchor="center")
GT.heading("two", text="제품가격", anchor="center")

GT.column("#3", width=100, anchor="center")
GT.heading("three", text="제품사이즈", anchor="center")

signFrame = Frame(window, relief='solid', bd=2)
sign_button = Button(signFrame, text= '가입', command = exit_signFrame)
sign_button.place(x= 500,y = 700)

id_label = Label(signFrame, text="아이디")
id_label.place(x= 150,y= 450)

id_input = Entry(signFrame, bg='gray80', font=22)
id_input.place(width=300, height=40, x=220, y=450)

pw_label = Label(signFrame, text="비밀번호")
pw_label.place(x= 150,y= 530)

password_input = Entry(signFrame, bg='gray80', font=22)
password_input.place(width=300, height=40, x=220, y=530)

name_label = Label(signFrame, text="이름")
name_label.place(x= 150,y= 610)


name_input = Entry(signFrame, bg='gray80', font=22)
name_input.place(width=300, height=40, x=220, y=610)



window.mainloop()