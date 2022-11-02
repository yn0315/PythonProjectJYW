# 221102
# 파일 입출력



# 데이터 입력
# 메뉴 정보? 외 모든 입력을 사용자 입력을 통해 전달 받았다.

# 파일 내부 내용을 불러오는 방법

# 파일 생성 방법

# 파일에 원하는 데이터를 쓰는 방법
x = 1;

# 파일 생성방법
x6 = id(x)
print(x6)

f=open("creat.txt", 'w')

# 첫번째 매개변수 : 파일명(확장자포함)
# 두번째 매개변수 : 모드

# 모드의 종류
# r(ead) : 읽기모드 파일을 읽기만 할 때
# w(rite): 쓰기모드 파일에 내용을 (새로쓰기)쓸 때
# a(dd): 추가모드 파일의 마지막 내용에 추가 내용을 넣을 때(이어쓰기)


print(f)
f.close()
file = open("basic.txt","w")
file.write("hello")
# file.write("hello python programming...!")
for i in range(1,11):
    data= "%d번째 줄\n" % i
    file.write(data)
file.close()


# 파일을 open하면 close는 필수로 수행

# with 키워드
# close하지 않는 실수방지
# with open("create.txt","w") as f :
#   수행문

with open("basic2.txt","w") as file:
    file.write("hello python programming .....!")

with open("doc1.txt","r" ,encoding = 'UTF-8') as mydoc:
    contents = mydoc.read() # 텍스트파일 내부 컨텐츠를 한 덩어리로 다 가져옴
print(contents)

# 한글 인코딩 방식
# UTF-8, EUC-KR

# 윈도우는 CP949방식 사용

# readline()
# read와 다르게 한 줄 씩 읽어온다.

ff = open("doc1.txt", 'r', encoding = 'UTF-8')
line = ff.readline()
print(line)
ff.close()

ff = open("doc1.txt", 'r', encoding = 'UTF-8')
while True:
    line = ff.readline()
    if not line:
        break
    print(line)
ff.close()

ff = open("doc1.txt", 'r', encoding = 'UTF-8')
line = ff.readline()
print(line)
line = ff.readline()
print(line)
ff.close()

# readline함수는 더 이상 읽을 라인이 없을 경우 ""빈문자열을 리턴한다.

# read,readline,readlines
# readlines : 모든 줄을 읽어서 각각의 줄을 요소로 리스트화하여 반환한다.

fff = open("doc1.txt",'r', encoding="UTF-8")
lines = fff.readlines()
print(type(lines))
print(lines)
for line in lines:
    print(line)
fff.close()

#a모드
# 추가모드
# 파일을 열 때 이미 존재하는 파일 열면 그 파일의 내용이 사라진다.
