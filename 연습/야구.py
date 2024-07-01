import random
#컴터 난수 생성, 중복값나오면 안됨
def getrandomvalue(getvalue,valuestart,valueend):
    com_list  = []
    while len(com_list) < getvalue:
        randomvalue = random.randint(valuestart,valueend)
        if randomvalue not in com_list:
            com_list.append(randomvalue)
    
    return com_list

com_random = getrandomvalue(3,0,9)
print(com_random)
#플레이어 입력 
count = 0 
out = 0
while True:
    strike = 0
    ball = 0
    print("사용자 입력하세요 : ")
    input_user = list[map(int,input().split()) ]
    for a in range(3):
        for i in range(3):
                if input_user[a] == com_list[i]:
                        if a == i :
                            strike +=1
                            print(f"스트라이크 횟수:{strike} ")
                        else:
                            ball +=1
                            print(f"ball 입니다 횟수: {ball}")
                            break

    if strike == 0 and ball ==0:
        out +=1
        print(f"out 횟수: {out}")
    count +=1
    if strike <= 3:
        print(f"stirke입니다 승리~")
        break

    if count <=5 or out <=2:
        print("count가 5회이상입니다 "if count<=5 else "out이 2번입니다")