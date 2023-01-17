import tkinter
import threading
import socket
import sys

win_connect = tkinter.Tk()
win_connect.title("접속대상")

tkinter.Label(win_connect, text="접속대상").grid(row=0, column=0)
input_addr_string = tkinter.StringVar(value="172.20.10.2:9999")
input_addr = tkinter.Entry(win_connect, textvariable=input_addr_string, width=20)
input_addr.grid(row=0, column=1, padx=5, pady=5)
connect_button = tkinter.Button(win_connect, text="접속하기")
connect_button.grid(row=0, column=2, padx=5, pady=5)

width = 280
height = 40

screen_width = win_connect.winfo_screenwidth()
screen_height = win_connect.winfo_screenheight()

x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))
win_connect.geometry('%dx%d+%d+%d' % (width, height, x, y))
input_addr.focus()
win_connect.mainloop()
