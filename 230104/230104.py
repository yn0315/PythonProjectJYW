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
sql = "SELECT * FROM "
x = 'market_db.xxx'

# 커서를 통해 sql문 실행
cur.execute(sql + x)

# 데이터 가져오기
data = cur.fetchall()

# 출력
print(data)

#connection 해제
#con.close()

# fetchall : 모든 데이터를 한번에 가져온다
# fetchone : 데이터 1개를 가져온다(하나의 행)
# execute : sql 문법을 실행

print(type(data))

# root계정으로 접근해서 select조회
# 변경, 저장 execute(sql query)

# 20명의 회원목록 테이블을 생성

# 20명의 정보 삽입
# 테이블명 : xxx
# col : 아이디 이름 나이 성별 주소 전화번호

sql2 = '''
        CREATE TABLE xxx
        (member_id char(8) not null,
        member_name char(20) not null,
        member_age int not null,
        member_gender char(2) not null, 
        member_addr varchar(20),
        member_phone_number char(10) not null
        );
        '''
sql3 = []
id = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj','kkk','lll','mmm','nnn','ooo','ppp','qqq','rrr','sss','ttt']
name = ['김김김','이이이','박박박','최최최','정정정','김김김','이이이','박박박','최최최','정정정','김김김','이이이','박박박','최최최','정정정','김김김','이이이','박박박','최최최','정정정',]
age = 20
gender = ['M','F']
addr = '서울'
phone_number = 11112222
#for i in range(20):
#   sql3.append('INSERT INTO xxx VALUES(' +"'"+ id[i] +"'"+',' +"'" + name[i]+ "'"+',' +str(age)+',' +"'" + gender[0] +"'" +','+"'"+addr+"'" + ',' + str(phone_number) + ');')


#for i in range(20):
#    cur.execute(sql3[i])
#cur.execute('commit')
sql4 = 'INSERT INTO xxx VALUES(%s,%s,%s,%s,%s,%s)'
val = [('aaa','김김김',20,'F','서울',1112223),
       ('bbb','이이이',20,'M','서울',1112223),
       ('ccc','박박박',20,'F','서울',1112223),
        ('ddd','석석석',20,'M','서울',1112223)
       ]
cur.executemany(sql4,val)
cur.execute('commit')





cur.close()





