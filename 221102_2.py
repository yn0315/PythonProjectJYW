import random


f = open("new.txt",'w')
f.write("hello")
f.close()

m = open("new.txt",'w')
m.write("world") #월드로 덮어써짐
m.close()

# w모드는 새로 생성해서 작성하는 것
# a모드는 기존 파일 열어서 내용추가

f=open("new.txt",'a')
for i in range(2,10):
    data = "\nNo.%d" % i
    f.write(data)

f.close()


hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt","w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        file.write("{},{},{}\n".format(name,weight,height))


# 332페이지 예제
with open("info.txt","r") as file:
    for line in file:
        (name,weight,height) = line.strip().split(",")

        if(not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height) / 100) **2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5<= bmi:
            result = "정상체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name,weight,height,bmi,result))
        print()