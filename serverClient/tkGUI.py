# tk interface
# tkinter
# pyQT
import tkinter

tkinter.Button

window = tkinter.Tk()

# 메인 프레임 생성
window.title("python server")
# 프로그램 명 지정
window.geometry("700x700")
# 프레임 사이즈 설정
window.resizable(False,False)
# 프레임의 사이즈 변경 불가 처리

label = tkinter.Label(window, text="텍스트")
# label컨트롤 객체 생성
label.pack()
# 위에서 생성한 label을 배치

label2 = tkinter.Label(window, text="두번째 텍스트", width=10, height=5, relief='sunken', fg='red',justify='left',padx=20)
# label2컨드롤 생성
label2.pack()
# label2를 배치한다
label3 = tkinter.Label(window,text="0")
label3.pack()
# 텍스트 0을 띄우고 있는 label3 생성 및 배치


count = 0 # 전역변수 count 0
def func(): # 버튼에서 호출하려는 함수 func 선언
    global  count # 전역 global 선언
    count += 1 # 함수 호출마다 카운트 수 증가
    label.config(text=str(count)) # 전역에 있는 label3객체의 text속성을 수정

button = tkinter.Button(window,width=15, command=func, repeatdelay=100, repeatinterval=100)
# 버튼 객체 생성
button.pack()
# 버튼 객체 배치

label4 = tkinter.Label(window)
label4.pack()
def calc(event):
    label4.config(text="결과: " + str(eval(entry.get())))

entry = tkinter.Entry(window)
# 입력폼 객체 생성

entry.bind("<Return>", calc)

entry.pack()
# 엔트리 입력폼 객체 배치

listbox = tkinter.Listbox(window)
listbox.insert(0,"0")
listbox.insert(1,"1")
listbox.insert(2,"1")
listbox.insert(3,"1")
listbox.insert(4,"1")
listbox.insert(5,"1")
listbox.pack()
window.mainloop()

# 메인 프레임 window를 실행하는 mainloop 함수

