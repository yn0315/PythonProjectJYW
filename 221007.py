# 안녕하세요 : 주석처리
# 개념설명
# 실행할 수 있는 코드의 최소 단위를 문장 혹은 라인이라고 한다.
# 라인이 모여 문장이 모여 프로그램이 구성됨
# 프로그램 소스코드는 위에서 아래로 읽힌다.

# 표현식
# 어떤 값을 만들어 내는 코드를 표현식이라고 한다.
# 숫자, 수식, 문자열 등 의미한다.

# 키워드 : 특별한 기능을 지닌 파이썬 내에서 사용되는 단어

# 식별자 : 프로그래밍 언어에서 이름을 붙일 때 사용하는 단어
# 식별자 규칙
# 1. 키워드는 사용하지 않는다.
# 2. 특수문자는 언더바만 허용 _
# 3. 숫자로 시작 불가
# 4. 공백 넣을 수 없다.
# 5. 한국어 금지 경로도 영어로 해놔야 됨
# 5. 대소문자를 구분한다. A와 a는 다른 식별자이다.
# 7. 의미 있는 단어로 지정.
# 8. 함수 혹은 변수의 이름을 지어준다.

# 식별자 표현 형태 2가지
# 스네이크 케이스 : 단어 사이를 _ 로 연결 : item_list
# 캐멀 케이스 : 첫 글자를 대문자로 : itemList

# 캐멀 케이스는 클래스 명을 지정할 때
# 스네이크 케이스는 함수와 변수

# 연산자와 자료
# + - / *

# 출력
# print() 함수를 사용한다.
# print(출력하고자 하는 대상)
# print(출력대상1, 출력대상2)

print("Hello Python Programming...!")
print(52)
print(273)

# 파이참 IDE(통합개발환경)에서 자료형과 함수에 따라 다른 색상으로 표현됨
# "hello" 문자열 데이터
# 52 숫자데이터
# print()는 함수

print(52, 273, "Hello") # 쉼표는 띄어쓰기 적용

print("안녕하세요", "저의", "이름은", "ㅇㅇㅇ입니다.")

print("# 하나만 출력합니다.")
print("Hello Python Programming ...!")
print()

print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "ㅇㅇㅇ입니다.")
print()

print("# 아무것도 출력하지 않습니다.")
print("---확인 전용선---")
print()
print()
print("---확인 전용선---")

# 파이썬의 자료형
# 문자열 "안녕하세요", "py"
# 숫자 45, 33
# 불 True 1, False 0

print(type("안녕하세요")) #안쪽부터 해석
print(type(273))

# 문자열 만들기
# 문자열은 스트링 string 이라고 한다. 줄여서 str
# 문자열 데이터는 무조건 따옴표로 감싸줌

print("a") # 문자, 문자열 안나누고 다 문자열 취급
print(type("a"))
print(33)
print(type(33))
print(type("33")) # 따옴표로 감싸면 문자열 취급

# 문자열 작은따옴표 가능
print('aaa')

print('안녕하세요')
print('"안녕하세요"라고 말했습니다') # 따옴표 반대도 가능

# 신텍스 에러
# 문법오류
# 파이썬 문법에서 어긋난 문장임을 표현한다.

# 이스케이프 문자를 사용하여 문자열 만들기
# \', \"

print("\"안녕하세요\"라고 말했습니다")
print('\'배가 고픕니다\'라고 생각했습니다')

print("안녕하세요\n안녕하세요")
print("안녕하세요\t안녕하세요")

print("이름\t나이\t지역")
print("윤인성\t25\t\t강서구")
print("윤아린\t24\t\t강서구")
print("구름\t3\t\t강서구")

print("이름\t나이\\t지역") # 역슬래시 프린트하고 싶으면 한번더 써줌

# 여러 줄 띄어야 할때는 따옴표 세개를 쓰면 됨!!
print("""dkdjsdfjk
111111
222222
333333
55555
67677777""")

# 문자열 연산자
# 문자열 + 연산
# 문자열과 문자열을 더해주는 기능
print("안녕" + "하세요") # 데이터가 한 덩어리
print("안녕" , "하세요") # 데이터가 두 덩어리
print(type("안녕" + "하세요")) # 안쪽 연산 무조건 하고 나서 넘어감!!!!!

# print("안녕하세요" + 1) 문자열은 무조건 문자열끼리 연산가능

print("안녕하세요" + "1")

# 문자열의 * 연산 : 반복

print("hello" * 3)
print(3 *"hello")

# 사칙연산 중 문자열에 적용가능 : + , *

# 문자열의 인덱싱
# 인덱싱 방법 []
# 문자 선택 연산자

print("abcd"[1])

# 인덱싱 숫자는 0부터 시작, 0이 첫번째 자리
# 인덱싱 숫자를 음수로 표현도 가능( - 표기는 뒤에서부터 뜻, 여기는 1부터 카운팅!!!)

print("abcd"[-1])
print("abcd"[-2])
print("abcd"[-3])
print("abcd"[-4])

print("python is easy") # 공백도 문자로 셈, 14개짜리 문자열
# 위 문장만 이용하고 인덱싱 방법을 사용하여 this라는 단어를 표현하세요.

print("python is easy"[2] + "python is easy"[3]+ "python is easy"[7]+ "python is easy"[8])

# 문자열의 슬라이싱
# 문자열의 연속된 여러 요소(문자)를 한번에 인덱싱하는 느낌 : 어디서부터 어디까지의 의미
# 슬라이싱 문법 [시작:종료]
# 시작지점은 포함
# 종료지점은 비포함
# 시작 이상 ~ 종료 미만
# 시작<= , <종료  /시작   ~ /종료 전전
# 시작 빈칸 : 처음부터
# 종료 빈칸 : 끝까지(포함)
print("안녕하세요"[2:-1])
print("안녕하세요"[2:])

print("안녕하세요"[1])

print("python is easy")

# 문자열의 길이를 구하는 함수
# len(문자열)

print(type(len("python is easy")))

# 보통 5~6중첩까지 쓰임
























