

def insertData():
    con, cur = None, None
    data1, data2, data3, data3 = "", "", "", ""
    sql = ""

    con = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='practice_db', charset='utf8')
    cur = con.cursor()

    data1 = edit1.get()
    data2 = edit2.get()
    data3 = edit3.get()

    try:
        sql = "insert into userTable (id,userName,email) values ('" + data1 + "','" + data2 + "','" + data3 + ")"
        cur.execute(sql)
    except:
        messagebox.showerror('오류', '데이터 입력 오류가 발생하였습니다.')
    else:
        messagebox.showinfo('성공', '데이터 입력 성공')

    con.commit()
    con.close()

    # 기존에 입력한 입력박스값 내용삭제
    edit1.delete(0, END)
    edit2.delete(0, END)
    edit3.delete(0, END)
    edit4.delete(0, END)
    selectData()