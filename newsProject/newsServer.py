import socketserver
import threading
import datetime
import json
import pymysql
from selenium import webdriver

from selenium.webdriver.common.by import By
from urllib import parse
import requests
from bs4 import BeautifulSoup


HOST = '172.30.1.46'  # 서버의 ip를 열음. (이 서버의 ip로 클라이언트가 접속을 해야 한다), 그전에 ping을 먼저 확인하도록.
PORT = 9900  # 포트번호 (같아야 함)
lock = threading.Lock()  # syncronized 동기화 진행하는 스레드 생성

# sql에 insert into

con = pymysql.connect(host='localhost', user='root', password='7539518642a', db='news_db', charset='utf8')
# user,pw,host,db,charset 등 매개변수 설정 후 connect 한 객체 : con

# con 객체에서 cursor 만들기

cur = con.cursor()

# driver = webdriver.Chrome()
WEBDRIVER_OPTIONS = webdriver.ChromeOptions()
# WEBDRIVER_OPTIONS.add_argument("headless")

WEBDRIVER_OPTIONS.add_argument('--headless')
WEBDRIVER_OPTIONS.add_argument('window-size=1920x1080')
WEBDRIVER_OPTIONS.add_argument("disable-gpu")

url = ''
g_searchTitle = '' # 검색어
g_title = [] # 기사 제목
g_content = [] # 기사 요약문
a_link = [] # 기사본문으로 가는 링크 리스트

g_content1 = [] # 기사 본문

g_loginId = '' # 로그인한 회원 아이디
g_loginPw = '' # 로그인한 회원 비밀번호

g_newsDict = {}
g_newsDict_length = 0
g_newsList = []

g_newsTitleList = [] # 뉴스 제목 리스트
newsId= '' # 뉴스 고유번호
g_selectTitle = '' # 성별, 나이 조회할 때 나오는 검색어 변수
def insertNews(newsList):
    global g_newsTitleList
    sql = 'SELECT news_title FROM news_info'
    cur.execute(sql)
    data = cur.fetchall()

    for d in range(len(data)):
        if len(data) != 0:
            g_newsTitleList.append(data[d][0])

    # 커서를 통해 sql문 실행
    try:
        for i in range(len(newsList)):

            if len(data) == 0:
                sql1 = 'INSERT INTO news_info VALUES(%s,%s,%s,%s)'
                val2 = [(None, newsList[i][0], newsList[i][1], newsList[i][2])]

                cur.executemany(sql1, val2)
                con.commit()
            else:

                if newsList[i][1] in g_newsTitleList:
                    continue
                else:
                    sql5 = 'INSERT INTO news_info VALUES(%s,%s,%s,%s)'
                    val3 = [(None, newsList[i][0], newsList[i][1], newsList[i][2])]

                    cur.executemany(sql5, val3)
                    con.commit()

    except Exception as e:
        print(type(e),e)



def newsUrl(keyword):
    global g_title
    global g_content
    global a_link
    global l
    global g_selectTitle
    l = []
    g_selectTitle = keyword
    keywordIn = parse.quote(keyword)
    print(keyword, "키워드!!!!!!!!!!!!!!!!!!!")
    base_url = f"https://search.hankookilbo.com/Search?tab=NEWS&sort=relation&searchText={keywordIn}&searchTypeSet=TITLE,CONTENTS&selectedPeriod=%EC%A0%84%EC%B2%B4&filter=head"
    # 검색어 위 url에 추가해서 검색 후 띄워주기
    # print(base_url)
    response = requests.get(base_url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one(('ul.board-list'))
        title1 = ul.select('li > div > h3 > a')
        news_content1 = ul.select('li > div > div > a')
        news_content2 = ul.select('li > div > div')

        a = []
        a_link = []

        for con in news_content2:
            a.append(con.find("a")["href"])

        for j in range(len(a)):
            if j % 2 == 0:
                a_link.append(a[j])

        for k in range(len(title1)):
            if k % 2 == 0:
                g_title.append(title1[k].get_text())

        ##################################################
        NewsDict(g_searchTitle, g_title)
        ##################################################

        # # 해당하는 딕셔너리 불러오기
        # for m in range(len(NewsDict.newsList)):
        #     if NewsDict.newsList[m]["newsNum"] == 2:
        #         print(NewsDict.newsList[m],"NewsDict!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        g_content.append(news_content1[0].get_text())
        g_content.append(news_content1[2].get_text())
        g_content.append(news_content1[4].get_text())
        g_content.append(news_content1[6].get_text())
        g_content.append(news_content1[8].get_text())

    else:
        print(response.status_code)

    return g_title, g_content

def readNews(url):

    global g_content1
    g_content1 = []

    # keywordIn = parse.quote(keyword)
    base_url = url
    # 검색어 위 url에 추가해서 검색 후 띄워주기
    # print(base_url)
    response = requests.get(base_url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        content1 = soup.select_one(
            'body > div.wrap.imp-end > div.container.end-uni > div.end-body > div > div.col-main')
        c = content1.find_all('p')

        for i in c:
            g_content1.append(i.get_text())
        # print(c)

    else:
        print(response.status_code)

    return g_content1


class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # ThreadingMixIn 클래스는 서버가 스레드 종료를 기다려야하는지를 가리키는 daemon_threads 어트리뷰트를 정의

    # TCPServer 클래스 안의 serve_forever()메소드 : 클라이언트의 접속 요청을 수신대기. 접속 요청이 있을 경우 수락하고 BaseRequestHandler의 handle() 메소드를 호출
    # TCPServer 클래스가 serve_forever() 메소드를 통해 클라이언트의 연결 요청을 기다리다가 클라이언트에게서 접속요청이 오면 이를 수락한 뒤 BaseRequestHandler
    # 객체의 handle() 메소드를 호출.서버 애플리케이션은 이 handler()메소드를 재정의해서 클라이언트와 데이터를 주고받는 일을 수행.

    # 서버가 클라이언트의 연결 요청을 수락해서 TCP 커넥션이 만들어지고 나면 그 다음부터는 서버 측의 socket 객체와 클라이언트 측의 socket 객체가
    # socket.send() 메소드와 socket.recv() 메소드를 통해 데이터를 주고 받을 수 있다. 서버 애플리케이션에서는
    # BaseRequestHandler의 request 데이터 속성이 바로 socket 객체. 데이터를 주고받는 일을 마치고 나서 서버와 클라이언트의 연결을 종료할 때는
    # socket의 close() 메소드를 호출하면 됨.

    # BaseRequestHandler 클래스 안의 handle() 메소드 : 클라이언트 접속 요청을 처리.
    # socket : 논리적인 의미로 컴퓨터 네트워크를 경유하는 프로세스 간 통신(Inter-Process Communication, IPC)의 종착점(end-point)
    # bind(): 사용할 IP address와 Port number 등록(각 소켓에 할당)
    # connect(): Client에서 Server와 연결하기 위해 소켓과 목적지 IP address, Port number 지정 (Block 상태)
    # send(), recv(): Client는 처음에 생성한 소켓으로, Server는 새로 반환(생성)된 소켓으로 client와 server간에 데이터 송수신

    pass

class NewsDict: # 댓글 기능을 위한 뉴스 정보 클래스

    newsList = []
    newsNum = 1
    def __init__(self, searchTitle, title):
        global g_newsDict_length
        for i in range(5):
            NewsDict.newsList.append({"search": searchTitle, "newsNum": NewsDict.newsNum, "title": title[i]})
            NewsDict.newsNum += 1
        g_newsDict_length = NewsDict.newsNum - 1


class News:

    def __init__(self,searchTitle, n_title, newsContent):
        global g_newsList
        for i in range(5):
            self.newsSearchTitle = searchTitle
            self.newsTitle = n_title[i]
            self.newsContent = newsContent[i]
            self.newsReply = []

            g_newsList.append([self.newsSearchTitle, n_title[i], newsContent[i]])

    def comment(self, writer, replyContent):
        self.newsReply = {"writer": writer, "reply": replyContent}

class User:  # 사용자관리 및 채팅 메세지 전송을 담당하는 클래스

    userList = []

    def __init__(self):
        self.users = {}  # 사용자의 등록 정보를 담을 사전 {사용자 이름:(소켓,주소),...}
        # 사용자 리스트

    def addUser(self, userId, userPw, userName, userAddr, userAge, userGender):  # 사용자 ID를 self.users에 추가하는 함수

        sql = 'SELECT mem_id FROM member'
        cur.execute(sql)
        data = cur.fetchall()

        if len(data) == 0:  # 회원이 한명도 없는 경우

            User.userList = userId

            # sql변수에 sql문법 작성
            sql2 = 'INSERT INTO member VALUES(%s,%s,%s,%s,%s,%s)'
            val = [(userId, userPw, userName, userAge, userGender, userAddr)]

            # sql변수에 sql문법 작성

            cur.executemany(sql2, val)
            con.commit()

            sql4 = 'SELECT * FROM member WHERE mem_id =' + f'"{userId}"'
            cur.execute(sql4)
            data = cur.fetchall()

            # sql변수에 sql문법 작성

            sql5 = 'INSERT INTO waching_data VALUES(%s,%s,%s,%s,%s)'
            val3 = [(data[0][0], data[0][3], data[0][4], data[0][5], "1")]
            # 커서를 통해 sql문 실행
            cur.executemany(sql5, val3)
            con.commit()

            return "0"  # 없으면 0

        for k in data:  # sql 데이터를 가져와 하나씩 뽑은후
            for i in range(len(k)):
                if userId == k[i]:  # 아이디가 있으면

                    return "1"

                else:
                    User.userList = userId

                    # sql변수에 sql문법 작성
                    sql3 = 'INSERT INTO member VALUES(%s,%s,%s,%s,%s,%s)'
                    val2 = [(userId, userPw, userName, userAge, userGender, userAddr)]

                    cur.executemany(sql3, val2)
                    con.commit()
                    ###########################################################################################
                    sql4 = 'SELECT * FROM member WHERE mem_id =' + f'"{userId}"'
                    cur.execute(sql4)
                    data = cur.fetchall()

                    # sql변수에 sql문법 작성

                    sql5 = 'INSERT INTO waching_data VALUES(%s,%s,%s,%s,%s)'
                    val3 = [(data[0][0], data[0][3], data[0][4], data[0][5], "1")]
                    # 커서를 통해 sql문 실행
                    cur.executemany(sql5, val3)
                    con.commit()

                    return "0"  # 없으면 0

    def loginUser(self, userId, userPw):
        global g_searchTitle
        ###################################
        sql1 = 'SELECT mem_id,mem_pw FROM member'
        cur.execute(sql1)
        data1 = cur.fetchall()

        # sql에 검색정보 있는지 확인
        sql2 = 'SELECT title FROM waching_data WHERE mem_id =' + f'"{userId}"'
        cur.execute(sql2)
        data2 = cur.fetchall()

        values = {

            "logIn": '',
            "title": '',
        }

        # 최근 검색어로 추천기사 띄워주기위해
        for i in range(len(data2)):
            values["title"] = str(data2[0][i])
        ###################################
        g_searchTitle = str(data2[0][i])

        for i in range(len(data1)):
            if userId == data1[i][0]:
                if userPw == data1[i][1]:
                    # return "1"
                    values["logIn"] = "1"
                elif userPw != data1[i][1]:
                    # return "0"
                    values["logIn"] = "0"

        return values

    def addTitle(self, userId, title):
        # 회원 아이디로 waching_data찾아서 읽어옴
        global g_searchTitle
        g_searchTitle = title
        print(userId, "userId!!!")
        sql4 = 'SELECT * FROM waching_data WHERE mem_id =' + f'"{userId}"'
        cur.execute(sql4)
        data1 = cur.fetchall()

        # sql변수에 sql문법 작성

        sql = '''UPDATE waching_data SET title =''' + f'"{title}"' + ''' WHERE title =''' + f'"{data1[0][4]}" AND mem_id = ''' + f'"{userId}"'
        cur.execute(sql)
        print(sql)

        cur.fetchall()
        con.commit()
        print("commit!!!!!!!")


    def selectAgeGenSearch(self, userAge, userGen):
        # 회원 나이와 성별순으로 뉴스조회
        global tempGen
        global limitTempAge
        global key
        global g_searchTitle
        key = ''
        print(userGen)
        tempGen = ''
        if userAge !='나이순':
            limitTempAge = str(int(userAge) + 9)
            print(limitTempAge, "나이!!!!!!!!!!!!!!!!!!")

            if userGen == '성별순' and userAge != '나이순':
                sql5 = 'SELECT MAX(distinct title) FROM waching_data WHERE mem_age BETWEEN '+ f'{userAge} AND {limitTempAge}'
                cur.execute(sql5)
                print(sql5)
                con.commit()
                data2 = cur.fetchall()
                print(sql5, "sql!!!!!!!!!!!!!!!!!!!")
                key = data2[0][0]
                print(key, "key!!!!!!!")
                return newsUrl(key)

            elif userGen == '남' and userAge != '나이순':
                tempGen = 'm'
                sql5 = 'SELECT MAX(distinct title) FROM waching_data WHERE mem_gender =' + f'"{tempGen}" AND mem_age between "{userAge}" and "{limitTempAge}"'

                cur.execute(sql5)
                print(sql5)
                con.commit()
                data2 = cur.fetchall()
                key = data2[0][0]
                print(data2, "key!!!!!!!")
                return newsUrl(key)

            elif userGen == '여' and userAge != '나이순':
                tempGen = 'f'
                sql5 = 'SELECT MAX(distinct title) FROM waching_data WHERE mem_gender =' + f'"{tempGen}" AND mem_age between "{userAge}" and "{limitTempAge}"'

                cur.execute(sql5)
                print(sql5)
                con.commit()
                data2 = cur.fetchall()
                key = data2[0][0]
                print(key, "key!!!!!!!")
                return newsUrl(key)

        elif userAge == '나이순' and userGen != '성별순':
            sql5 = 'SELECT MAX(distinct title) FROM waching_data WHERE mem_gender =' + f'"{tempGen}"'

            cur.execute(sql5)
            print(sql5)
            con.commit()
            data2 = cur.fetchall()
            key = data2[0][0]
            print(key, "key!!!!!!!")
            return newsUrl(key)

        else:
            return newsUrl(g_searchTitle)

        # return newsUrl(key)

    def getNumber(self, newsTi):
        print(newsTi, "newsTi########################################################################")
        global g_newsTitleList
        sql = 'SELECT news_title FROM news_info'
        cur.execute(sql)
        data = cur.fetchall()

        for d in range(len(data)):
            if len(data) != 0:
                g_newsTitleList.append(data[d][0])
        try:
            if newsTi in g_newsTitleList:
                sql1 = f'SELECT news_id FROM news_info WHERE news_title = "{newsTi}"'
                cur.execute(sql1)
                data1 = cur.fetchall()
                print(data1[0][0], "newsNumber!!!!!!!!!!!!!!!!!!!!!!")
                return data1[0][0]

        except Exception as e:
            print("getNumber", type(e), e)

    def makeReply(self, newsId, replyContent):
        try:
            print(newsId,"뉴스아이디!!!!!!!!!!!!!!!!!!!!!")
            sql2 = f'INSERT INTO news_reply VALUES ("{newsId}", "{g_loginId}","{replyContent}")'

            cur.execute(sql2)
            con.commit()
            data1 = cur.fetchall()

        except Exception as e:
            print("makeReply", type(e), e)



class MyTcpHandler(socketserver.BaseRequestHandler):
    user = User()

    def handle(self):  # 클라이언트가 접속시 클라이언트 주소 출력
        # 클라이언트의 접속요청이 수락된 후 호출됨
        # 서버와 클라이언트가  데이터를 주고 받는 메소드로 재정의해서 사용,
        # BaseRequestHandler클래스 안에 속해있는 메소드

        try:
            while True:
                # json데이터의 내용에 따라 실행하는 함수가 갈라져야 함
                data = self.request.recv(16184)

                if bytes(data).decode() == '':
                    break

                elif bytes(data).decode() == 'sign':  # 회원가입
                    print(bytes(data).decode())
                    json_dict = json.loads(self.request.recv(16184))

                    result = self.user.addUser(json_dict["userId"], json_dict["userPw"], json_dict["userName"],
                                               json_dict["userAddr"], json_dict["userAge"], json_dict["userGender"])

                    self.request.send(result.encode())

                elif bytes(data).decode() == 'login2':  # 본문에서 뒤로가기 실행시
                    global g_searchTitle
                    global g_title
                    global g_content
                    global a_link
                    global g_loginId
                    global g_loginPw
                    global g_newsDict
                    global g_newsDict_length
                    global g_newsList
                    global newsId
                    global g_selectTitle


                    # 클라이언트로부터 로그인정보 id,pw받아옴
                    result = self.user.loginUser(g_loginId, g_loginPw)

                    title0, cont0 = newsUrl(result["title"])
                    g_searchTitle = result["title"]

                    values0 = json.dumps({

                        "title": title0,
                        "content": cont0,

                    }).encode('utf-8')

                    # 회원정보 저장

                    self.request.sendall(bytes(values0))

                    News(g_searchTitle, g_title, g_content)

                    insertNews(g_newsList)

                    g_title = []
                    g_content = []

                    while True:

                        result2 = self.request.recv(16184)
                        if bytes(result2).decode() == '':
                            break

                        elif bytes(result2).decode() == 'select':
                            print(bytes(result2).decode())
                            json_age_gen = json.loads(self.request.recv(16184))

                            selectTitle, selectContent = self.user.selectAgeGenSearch(json_age_gen["userAge"], json_age_gen["userGen"])
                            selectValues = json.dumps({

                                "title": selectTitle,
                                "content": selectContent,
                                "selectTitle": g_selectTitle

                            }).encode('utf-8')

                            # 회원정보 저장

                            self.request.sendall(bytes(selectValues))
                            g_title = []
                            g_content = []

                        elif bytes(result2).decode() == 'search':

                            # 검색어
                            result3 = self.request.recv(16184)
                            print(bytes(result3).decode())
                            # 검색어 저장
                            self.user.addTitle(g_loginId, bytes(result3).decode())

                            # driver.get(newsUrl(bytes(result3).decode()))

                            title1, content1 = newsUrl(bytes(result3).decode())

                            g_searchTitle = bytes(result3).decode()
                            News(g_searchTitle, g_title, g_content)
                            insertNews(g_newsList)

                            values1 = json.dumps({

                                "title": title1,
                                "content": content1,

                            }).encode('utf-8')

                            print(bytes(values1).decode())
                            self.request.sendall(bytes(values1))
                            # 검색 및 출력

                        elif bytes(result2).decode() == 'main':
                            g_loginId = []
                            g_loginPw = []
                            break

                        elif bytes(result2).decode() == 'read1':
                            print(bytes(result2).decode())
                            try:
                                # 본문내용 보내기
                                con1 = readNews(a_link[0])
                                for m in range(len(NewsDict.newsList)):
                                    if NewsDict.newsList[m]["newsNum"] == 1:
                                        g_newsDict = NewsDict.newsList[m]
                                        newsId = self.user.getNumber(newsTi)

                                values2 = json.dumps({

                                    "content": con1,
                                    "newsNum": g_newsDict["newsNum"],
                                    "newsLength": g_newsDict_length,


                                }).encode('utf-8')

                                self.request.sendall(bytes(values2))

                                result4 = self.request.recv(16184)

                                if bytes(result4).decode() == 'back':
                                    break
                                elif bytes(result4).decode() == 'replyContent':
                                    result5 = self.request.recv(92236)
                                    self.user.makeReply(newsId, bytes(result5).decode())

                            except Exception as e:
                                print(type(e), e)

                        elif bytes(result2).decode() == 'read2':

                            # 본문내용 보내기
                            con2 = readNews(a_link[1])
                            for m in range(len(NewsDict.newsList)):
                                if NewsDict.newsList[m]["newsNum"] == 2:
                                    g_newsDict = NewsDict.newsList[m]
                                    newsId = self.user.getNumber(newsTi)


                            values3 = json.dumps({

                                "content": con2,
                                "newsNum": g_newsDict["newsNum"],


                            }).encode('utf-8')

                            self.request.sendall(bytes(values3))
                            result4 = self.request.recv(16184)
                            if bytes(result4).decode() == 'back':
                                break
                            elif bytes(result4).decode() == 'replyContent':
                                result5 = self.request.recv(92236)
                                self.user.makeReply(newsId, bytes(result5).decode())

                        elif bytes(result2).decode() == 'read3':

                            # 본문내용 보내기
                            con3 = readNews(a_link[2])
                            for m in range(len(NewsDict.newsList)):
                                if NewsDict.newsList[m]["newsNum"] == 3:
                                    g_newsDict = NewsDict.newsList[m]
                                    newsId = self.user.getNumber(newsTi)

                            values4 = json.dumps({

                                "content": con3,
                                "newsNum": g_newsDict["newsNum"],
                                "newsLength": g_newsDict_length,


                            }).encode('utf-8')

                            self.request.sendall(bytes(values4))
                            result4 = self.request.recv(16184)
                            if bytes(result4).decode() == 'back':
                                break
                            elif bytes(result4).decode() == 'replyContent':
                                result5 = self.request.recv(92236)
                                self.user.makeReply(newsId, bytes(result5).decode())

                        elif bytes(result2).decode() == 'read4':

                            # 본문내용 보내기
                            con4 = readNews(a_link[3])
                            for m in range(len(NewsDict.newsList)):
                                if NewsDict.newsList[m]["newsNum"] == 4:
                                    g_newsDict = NewsDict.newsList[m]
                                    newsId = self.user.getNumber(newsTi)

                            values5 = json.dumps({

                                "content": con4,
                                "newsNum": g_newsDict["newsNum"],
                                "newsLength": g_newsDict_length,


                            }).encode('utf-8')

                            self.request.sendall(bytes(values5))
                            result4 = self.request.recv(16184)
                            if bytes(result4).decode() == 'back':
                                break
                            elif bytes(result4).decode() == 'replyContent':
                                result5 = self.request.recv(92236)
                                self.user.makeReply(newsId, bytes(result5).decode())

                        elif bytes(result2).decode() == 'read5':

                            # 본문내용 보내기
                            con5 = readNews(a_link[4])
                            for m in range(len(NewsDict.newsList)):
                                if NewsDict.newsList[m]["newsNum"] == 5:
                                    g_newsDict = NewsDict.newsList[m]
                                    newsId = self.user.getNumber(newsTi)

                            values6 = json.dumps({

                                "content": con5,
                                "newsNum": g_newsDict["newsNum"],
                                "newsLength": g_newsDict_length,


                            }).encode('utf-8')

                            self.request.sendall(bytes(values6))
                            result4 = self.request.recv(16184)
                            if bytes(result4).decode() == 'back':
                                break
                            elif bytes(result4).decode() == 'replyContent':
                                result5 = self.request.recv(92236)
                                self.user.makeReply(newsId, bytes(result5).decode())

                elif bytes(data).decode() == 'login':  # 로그인

                    # global g_searchTitle
                    # global g_title
                    # global g_content
                    # global a_link
                    # global g_loginId
                    # global g_loginPw
                    # global g_newsDict
                    # global g_newsDict_length
                    # global g_newsList
                    # 클라이언트로부터 로그인정보 id,pw받아옴

                    json_dict = json.loads(self.request.recv(16184))
                    g_loginId = json_dict["userId"]
                    g_loginPw = json_dict["userPw"]
                    result = self.user.loginUser(json_dict["userId"], json_dict["userPw"])
                    print(json_dict["userId"])

                    title, cont = newsUrl(result["title"])
                    g_searchTitle = result["title"]

                    values = json.dumps({

                        "title": title,
                        "content": cont,

                    }).encode('utf-8')
                    # 회원정보 저장
                    self.request.send(json.dumps(result).encode('utf-8'))

                    self.request.sendall(bytes(values))
                    print("###############################################")
                    print(g_title)
                    print(g_content)
                    News(g_searchTitle, g_title, g_content)
                    insertNews(g_newsList)

                    g_title = []
                    g_content = []

                    while True:

                        result2 = self.request.recv(16184)

                        if bytes(result2).decode() == '':
                            break

                        elif bytes(result2).decode() == 'select':
                            print(bytes(result2).decode())
                            json_age_gen = json.loads(self.request.recv(16184))

                            selectTitle, selectContent = self.user.selectAgeGenSearch(json_age_gen["userAge"], json_age_gen["userGen"])
                            selectValues = json.dumps({

                                "title": selectTitle,
                                "content": selectContent,
                                "selectTitle": g_selectTitle

                            }).encode('utf-8')

                            # 회원정보 저장

                            self.request.sendall(bytes(selectValues))
                            g_title = []
                            g_content = []


                        elif bytes(result2).decode() == 'search':

                            # 검색어
                            result3 = self.request.recv(16184)
                            print(bytes(result3).decode())
                            # 검색어 저장
                            self.user.addTitle(g_loginId, bytes(result3).decode())

                            # driver.get(newsUrl(bytes(result3).decode()))

                            g_searchTitle = bytes(result3).decode()

                            print(g_title,"타이틀!!!!!!!!!!!!!!")
                            print(g_content,"컨텐츠!!!!!!!!!!!!!!!")

                            ##################################################
                            # News(g_searchTitle, g_title, g_content)
                            # insertNews(g_newsList)
                            ##################################################
                            print("검색--------------------------------------")

                            title1, content1 = newsUrl(bytes(result3).decode())
                            print(bytes(result3).decode(), "받은 데이터--------------------")

                            values1 = json.dumps({

                                "title": title1,
                                "content": content1,

                            }).encode('utf-8')

                            print(bytes(values1).decode())

                            News(g_searchTitle, g_title, g_content)
                            insertNews(g_newsList)

                            self.request.sendall(bytes(values1))
                            print('데이터 보내기-------------------------------------------')
                            break

                            # 검색 및 출력

                        elif bytes(result2).decode() == 'main':
                            g_loginId = []
                            g_loginPw = []
                            break

                        elif bytes(result2).decode() == 'read1':
                            print(bytes(result2).decode())
                            try:
                                # 본문내용 보내기
                                con1 = readNews(a_link[0])
                                # 해당하는 딕셔너리 불러오기
                                for m in range(len(NewsDict.newsList)):
                                    if NewsDict.newsList[m]["newsNum"] == 1:
                                        g_newsDict = NewsDict.newsList[m]
                                        newsTi = NewsDict.newsList[m]["title"]
                                        newsId= self.user.getNumber(newsTi)
                                        print(newsTi,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

                                values2 = json.dumps({

                                    "content": con1,
                                    "newsNum": g_newsDict["newsNum"],
                                    "newsLength": g_newsDict_length,

                                }).encode('utf-8')

                                self.request.sendall(bytes(values2))
                                result4 = self.request.recv(16184)
                                if bytes(result4).decode() == 'back':
                                    break
                                elif bytes(result4).decode() == 'replyContent':
                                    print(bytes(result4).decode(), "받은 데이터!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    result5 = bytes(self.request.recv(92236)).decode()
                                    print(result5, "result5!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                    self.user.makeReply(newsId, result5)
                            except Exception as e:
                                print(type(e), e)

                        elif bytes(result2).decode() == 'read2':

                            # 본문내용 보내기
                            con2 = readNews(a_link[1])
                            for m in range(len(NewsDict.newsList)):
                                if NewsDict.newsList[m]["newsNum"] == 2:
                                    g_newsDict = NewsDict.newsList[m]
                                    newsTi = NewsDict.newsList[m]["title"]
                                    newsId= self.user.getNumber(newsTi)

                            values3 = json.dumps({

                                "content": con2,
                                "newsNum": g_newsDict["newsNum"],
                                "newsLength": g_newsDict_length,

                            }).encode('utf-8')

                            self.request.sendall(bytes(values3))
                            result4 = self.request.recv(16184)
                            if bytes(result4).decode() == 'back':
                                break
                            elif bytes(result4).decode() == 'replyContent':
                                result5 = self.request.recv(92236)
                                self.user.makeReply(newsId, bytes(result5).decode())

                        elif bytes(result2).decode() == 'read3':

                            # 본문내용 보내기
                            con3 = readNews(a_link[2])
                            for m in range(len(NewsDict.newsList)):
                                if NewsDict.newsList[m]["newsNum"] == 3:
                                    g_newsDict = NewsDict.newsList[m]
                                    newsId = self.user.getNumber(newsTi)

                            values4 = json.dumps({

                                "content": con3,
                                "newsNum": g_newsDict["newsNum"],
                                "newsLength": g_newsDict_length,

                            }).encode('utf-8')

                            self.request.sendall(bytes(values4))
                            result4 = self.request.recv(16184)
                            if bytes(result4).decode() == 'back':
                                break
                            elif bytes(result4).decode() == 'replyContent':
                                result5 = self.request.recv(92236)
                                self.user.makeReply(newsId, bytes(result5).decode())

                        elif bytes(result2).decode() == 'read4':

                            # 본문내용 보내기
                            con4 = readNews(a_link[3])
                            for m in range(len(NewsDict.newsList)):
                                if NewsDict.newsList[m]["newsNum"] == 4:
                                    g_newsDict = NewsDict.newsList[m]
                                    newsId = self.user.getNumber(newsTi)

                            values5 = json.dumps({

                                "content": con4,
                                "newsNum": g_newsDict["newsNum"],
                                "newsLength": g_newsDict_length,


                            }).encode('utf-8')

                            self.request.sendall(bytes(values5))
                            result4 = self.request.recv(16184)
                            if bytes(result4).decode() == 'back':
                                break
                            elif bytes(result4).decode() == 'replyContent':
                                result5 = self.request.recv(92236)
                                self.user.makeReply(newsId, bytes(result5).decode())

                        elif bytes(result2).decode() == 'read5':

                            # 본문내용 보내기
                            con5 = readNews(a_link[4])
                            for m in range(len(NewsDict.newsList)):
                                if NewsDict.newsList[m]["newsNum"] == 5:
                                    g_newsDict = NewsDict.newsList[m]
                                    newsId = self.user.getNumber(newsTi)

                            values6 = json.dumps({

                                "content": con5,
                                "newsNum": g_newsDict["newsNum"],
                                "newsLength": g_newsDict_length,


                            }).encode('utf-8')

                            self.request.sendall(bytes(values6))
                            result4 = self.request.recv(16184)
                            if bytes(result4).decode() == 'back':
                                break
                            elif bytes(result4).decode() == 'replyContent':
                                result5 = self.request.recv(92236)
                                self.user.makeReply(newsId, bytes(result5).decode())
        except Exception as e:
            print("handle", e)


def runServer():
    print('+++ 서버를 시작합니다.')

    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)  # 서버 객체 생성
        # 인스턴스 = 클래스명(생성자)
        server.serve_forever()  # 클라이언트의 접속요청 수락 및 handle() 메소드 호출하는 역할
    except KeyboardInterrupt:
        print('--- 서버를 종료합니다.')
        server.shutdown()
        server.server_close()


runServer()