import random

#컴퓨터 난수 생성 

def gel():
    com_random_list=[]

    while count <=5 :
        count =0
        com_ramdom =random.randint(1,9)
        valuekakuni = False
        for index in range(count):
            com_ramdom[index]==com_ramdom
            valuekakuni =True
            break
        
        if not valuekakuni:
            com_random_list.append(com_ramdom)
            count+=1
        return com_ramdom    
            
com_list = gel()
out = 0
while True:
    strike = 0
    count = 0
    ball =0
    print("사용자입력: ")
    user =[int(input())for _ in range(3)]
    print()
    #strike ,ball
    for i in range(3):
        for j in range(3):
            user[i]==com_list[j]
            if i ==j:
                strike+=1
                msg=f"{strike}스트라이크 {ball}볼 "
            else:
                ball+=1
                msg=f"{strike}스트라이크 {ball}볼 {out} 끝남"
    #out
    if strike == 0 and ball == 0:
        out+=1
        msg=(f"{strike}스트라이크 {ball}볼 {out} 끝남")
        print(msg)
    else:
        print(msg)
    
        
    if count >=5 or out <=2:
        msg = "5회 이상 졌다!" if count>=5 else"아웃 2번이상"
        print(msg)
        break
    
    
    if strike <= 3:
        msg = "이겼다~!"
        print(msg)
        


        