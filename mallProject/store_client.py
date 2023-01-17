import socket
import tkinter.ttk
from _thread import *
import threading
from tkinter import *
from time import sleep
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from urllib import request
import tkinter.messagebox
import json

HOST ='172.30.1.34'
PORT = 9900

# img_folder = './img'
# if not os.path.isdir(img_folder) : # 없으면 새로 생성하는 조건문
#     os.mkdir(img_folder)
#
# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=option)
# driver.get("https://search.shopping.naver.com/search/all?query=%EB%82%A8%EC%84%B1%EC%83%81%EC%9D%98&cat_id=&frm=NVSHATC")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# driver.implicitly_wait(3)
# images = driver.find_elements(By.CLASS_NAME, value='list_basis')
# # for i in range(10):
# #     print(images[i].get_property(name='_blank'))
# img_url = []
# for image in images:
#     url = image.get_attribute('scr')
#     print(url)
#     img_url.append(url)
#
# for index, link in enumerate(img_url):
#     request.urlretrieve(link, f'./img/{index}.jpg')
# cnt = 0
# for index, img in enumerate(images):
#     try:
#         img.click()
#         time.sleep(2)
#         imgUrl = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[3]').get_attribute("src")
#         if '?' in imgUrl:
#             filetype = imgUrl[imgUrl.rfind('.'):imgUrl.rfind('?')]
#         elif '.' in imgUrl:
#             filetype = imgUrl[imgUrl.rfind('.'):]
#         urlretrieve(imgUrl, path + str(index) + filetype)
#         print('11')
#         cnt += 1
#     except:
#         pass
#
# driver.close()
# print("\nTotal CNT: {}, Success CNT: {}".format(index, cnt))


#lv-product-card__info-wrapper

con = pymysql.connect(host="localhost", user='root', password='7539518642a', db='mall_db', charset='utf8')
cur = con.cursor()
sql = "SELECT * FROM "
x = "mall_db.goods"
cur.execute(sql+x)
data = (cur.fetchall())
print(data)

def Lonin(evevt):
    if id_input.get() == '111':
        if password_input.get() == '111':
            shopping.pack(side="left", fill="both", expand=True)
            exit_button.place(x=730, y=18)
            t_button.place(x=0, y= 100)
            p_button.place(x=0, y= 200)
            o_button.place(x=0, y= 300)
            s_button.place(x=0, y= 400)
            c_button.place(x=0, y= 500)
            login_button['state'] = 'disabled'
            make_id['state'] = 'disabled'

############################################# 회원가입 ##################################################################3
def sign_member():
    signFrame.pack(side='left', fill='both', expand=True)
    signFrame.pack()
    return

def sign():
    print(sign_id_input.get())
    print(sign_password_input.get())
    print(sign_name_input.get())

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((HOST,PORT))

    values = json.dumps({
        "username": sign_id_input.get(),
        "userpw": sign_password_input.get(),
        "name": sign_name_input.get(),
    }).encode('utf8')

    client_socket.sendall((bytes(values)))

    data = client_socket.recv(1024)
    if data == "False":
       tkinter.messagebox.showinfo("메시지","존재하는 아이디입니다.")
    else:
        tkinter.messagebox.showinfo("메시지","가입이 완료되었습니다.")
    sign_member()



def exit_signFrame():
    signFrame.pack_forget()

################################################# end 회원가입 ############################################################################

def Shopping_Exit():
    global shopping
    global f2
    global TV
    shopping.pack_forget()
    TV.pack_forget()
    # f2.pack_forget()
    login_button['state'] = 'normal'
    make_id['state'] = 'normal'
    t_button['state'] = 'normal'
    p_button['state'] = 'normal'
    o_button['state'] = 'normal'
    s_button['state'] = 'normal'
    c_button['state'] = 'normal'
    id_input.delete(0, len(id_input.get()))
    password_input.delete(0, len(password_input.get()))


def Goods_T():
    global t_button
    global p_button
    global o_button
    global s_button
    global c_button
    global order_button
    t_button['state'] = 'disabled'
    p_button['state'] = 'normal'
    o_button['state'] = 'normal'
    s_button['state'] = 'normal'
    c_button['state'] = 'normal'
    TV.place(x=200, y=100)
    order_button.place(x=620, y=680)
    # for i in data:
    #     if i[1] == 't':
    #         if TV.exists(i[0]):
    #             pass
    #         else:
    #             TV.insert('', 'end', text=str(i), values=i)
    for i in TV.get_children():
        TV.delete(i)
    for i in data:
        if i[1] == 't':
            TV.insert('', 'end', text=str(i), values=i)


def Goods_P():
    global TV
    global t_button
    global p_button
    global o_button
    global s_button
    global c_button
    t_button['state'] = 'normal'
    p_button['state'] = 'disabled'
    o_button['state'] = 'normal'
    s_button['state'] = 'normal'
    c_button['state'] = 'normal'
    # if p_button['state'] == 'disabled':
    TV.place(x=200, y=100)
    for i in TV.get_children():
        TV.delete(i)
    for i in data:
        if i[1] == 'p':
            if TV.exists(i[0]):
                pass
            else:
                TV.insert('', 'end', text=str(i), values=i)

def Goods_O():
    global TV
    global t_button
    global p_button
    global o_button
    global s_button
    global c_button
    t_button['state'] = 'normal'
    p_button['state'] = 'normal'
    o_button['state'] = 'disabled'
    s_button['state'] = 'normal'
    c_button['state'] = 'normal'
    TV.place(x=200, y=100)
    for i in TV.get_children():
        TV.delete(i)
    for i in data:
        if i[1] == 'o':
            TV.insert('', 'end', text=str(i), values=i)

def Goods_S():
    global TV
    global t_button
    global p_button
    global o_button
    global s_button
    global c_button
    t_button['state'] = 'normal'
    p_button['state'] = 'normal'
    o_button['state'] = 'normal'
    s_button['state'] = 'disabled'
    c_button['state'] = 'normal'
    TV.place(x=200, y=100)
    for i in TV.get_children():
        TV.delete(i)
    for i in data:
        if i[1] == 's':
            TV.insert('', 'end', text=str(i), values=i)

def Goods_C():
    global TV
    global t_button
    global p_button
    global o_button
    global s_button
    global c_button
    t_button['state'] = 'normal'
    p_button['state'] = 'normal'
    o_button['state'] = 'normal'
    s_button['state'] = 'normal'
    c_button['state'] = 'disabled'
    TV.place(x=200, y=100)
    for i in TV.get_children():
        TV.delete(i)
    for i in data:
        if i[1] == 'c':
            TV.insert('', 'end', text=str(i), values=i)

def new_window(event):
    global membership
    global window
    membership = Toplevel()
    membership.title('회원가입')
    make_id['state'] = 'disabled'

def Goods_info(event):
    TV.place(x=900, y=100)
    # f2.config(width=400,height=400)
    # f2.place(x=200, y=200)
    t1_button.place(x=900,y=100)
    TV.tkraise()

getValue=[]
def click_item(event):
    global getValue
    selectedItem = TV.focus()
    getValue = TV.item(selectedItem).get('values')  # 딕셔너리의 값만 가져오기
    order_label.configure(text=getValue)
    print(getValue)
    print(getValue[1])


def Order():
    global getValue
    print(getValue)
    # order_frame.pack(side="left", fill="both", expand=True)
    # order_exit_button.place(x=730, y=18)
    # order_label.place(x=250, y=300)
    # pay_button.place(x=250, y=420)
    selectedItem = TV.focus()
    getValue = TV.item(selectedItem).get('values')
    sql = "INSERT INTO orders (mem_id, goods_code, goods_price, goods_size) VALUES (%s, %s, %s, %s)"
    val = [('111', getValue[1], getValue[3], getValue[4])]
    cur.executemany(sql, val)

def Oreder_Exit():
    global order_frame
    global TV
    TV.pack_forget()
    order_frame.pack_forget()
    # f2.pack_forget()
    login_button['state'] = 'normal'
    make_id['state'] = 'normal'
    t_button['state'] = 'normal'
    p_button['state'] = 'normal'
    o_button['state'] = 'normal'
    s_button['state'] = 'normal'
    c_button['state'] = 'normal'

def Pay():
    global order_label
    global TV
    val='4'
    # getValue = TV.item(selectedItem).get('values')
    # order_label.configure(text=getValue)
    # sql = "INSERT INTO orders (mem_id, goods_code, goods_price, goods_size) VALUES (%s, %s, %s, %s)"
    # val = [('111', getValue[1], getValue[3], getValue[5])]
    # cur.executemany(sql, val)
    print(val)



window = Tk()
window.geometry('800x800')
window.title('MUSINSA')
window.configure(bg='white')
window.resizable(False, False)

#####################################################################################
# photo = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\mu2.png")
# category1 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\t-shirt.png")
# category2 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\pants.png")
# category3 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\dress.png")
# category4 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\shoes1.png")
# category5 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\shoes2.png")
# category6 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\cap.png")

#################################<원래 내 자리>############################################
photo = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\mu2.png")
category1 = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\store_image\\t-shirt.png")
category2 = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\store_image\\pants.png")
category3 = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\store_image\\outer.png")
category4 = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\store_image\\shoes1.png")
category5 = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\store_image\\cap.png")
#########################################################################################




logo = Label(window, image=photo)
logo.place(x=160, y=100)

id_input = Entry(window, bg='gray80', font=22)
id_input.place(width=300, height=40, x=180, y=450)

password_input = Entry(window, bg='gray80', font=22)
password_input.place(width=300, height=40, x=180, y=530)

login_button = Button(window, text='Log In', width=12, height=7, bg='gray80', font=22)
login_button.bind('<Return>', Lonin)
login_button.place(x=510, y=445)

make_id = Button(window, text='회원 가입',  command = sign_member, width=12, height=2, bg='white', font=22)
make_id.place(x=510, y=580)

shopping = Frame(window, relief="solid", bd=2, bg='white')
exit_button = Button(shopping, text='X', font=20, command=Shopping_Exit, width=4, height=2, bg='red2')
t_button = Button(shopping, image=category1, command=Goods_T)
p_button = Button(shopping, image=category2, command=Goods_P)
o_button = Button(shopping, image=category3, command=Goods_O)
s_button = Button(shopping, image=category4, command=Goods_S)
c_button = Button(shopping, image=category5, command=Goods_C)

# t1 = PhotoImage(file = "C:\\Users\\202-uil\\Desktop\\KCY\\t1.png")

###############################<원래 내 자리>#################################
t1 = PhotoImage(file = "C:\\Users\\myosi\\OneDrive\\바탕 화면\\store_image\\t1.png")
t1_button = Button(shopping, image=t1)
t1_label = Label(shopping, text='t1 제품명', width=26, height=2)
#
# p1 = PhotoImage(file = "C:\\Users\\202-1\\Desktop\\KCY\\store_image\\p1.png")
# p1_button = Button(shopping, image=p1)
# p1_label = Label(shopping, text='p1 제품명', width=26, height=2)

TV = tkinter.ttk.Treeview(shopping, height=10, columns=["one", "two", "three", 'four', 'five'], displaycolumns=["one", "two", "three", 'four', 'five'])
TV.bind('<ButtonRelease-1>', click_item)
TV.bind("<Double-Button-1>", Goods_info)

TV.column("#0", width=0, anchor="center")
TV.heading("#0", text="비고")

TV.column("#1", width=100, anchor="center")
TV.heading("one", text='제품이름', anchor="center")

TV.column("#2", width=100, anchor="center")
TV.heading("two", text="제품종류", anchor="center")

TV.column("#3", width=100, anchor="center")
TV.heading("three", text="제품수량", anchor="center")

TV.column("#4", width=100, anchor="center")
TV.heading("four", text="제품가격", anchor="center")

TV.column("#5", width=100, anchor="center")
TV.heading("five", text="제품사이즈", anchor="center")

f2 = Frame(shopping)
f2.config(bg="gray90")

order_button = Button(shopping, text='주문하기', width=12, height=3, command=Order)
order_frame = Frame(shopping)
order_exit_button = Button(order_frame, text='X', font=20, command=Oreder_Exit, width=4, height=2, bg='red2')
order_label = Label(order_frame, width=26, height=3, font=30)
pay_button = Button(order_frame,width=26, height=4, text='결제하기', command=Pay)

############################################ 회원가입 #####################################################################


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