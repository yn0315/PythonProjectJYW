import pymysql
#sql을 파이썬에서 활용하기 위해 pymysql 라이브러리 설치 import

# mysql workbench
# id root
# pw 내꺼...753...
# connection
# 192.168.0.2
# localhost 내 컴퓨터

con = pymysql.connect(host='localhost', user='root', password='7539518642a', db='market_db', charset='utf8')
#user,pw,host,db,charset 등 매개변수 설정 후 connect 한 객체 : con

# con 객체에서 cursor 만들기

cur = con.cursor()

#sql변수에 sql문법 작성
sql = '''SELECT *
    FROM member
	INNER JOIN buy
    ON member.mem_id = buy.mem_id; '''


# 커서를 통해 sql문 실행
cur.execute(sql)

# 데이터 가져오기
data = cur.fetchall()
print(data)
