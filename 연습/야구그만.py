import random
#컴터 난수생성
def getrandlist(argnumrandvalues,argstart,argend):
    random_list =  []

    rand_count = 0

    while rand_count < argnumrandvalues:

        rand_value =  random.randint(argstart,argend)
        
        found_dup_value = False

        for i in range(rand_count):
            if random_list[i] == rand_value:
                found_dup_value = True
                break

        if not found_dup_value:
            random_list.append(rand_value)
            rand_count +=1

    return random_list
    

com_random = getrandlist(3,0,9)
print(com_random)
count = 0
out = 0
#플레이어 입력 
#게임조건 
#자리값 숫자 같으면 strike
while True: 

    strike = 0
    ball = 0
    
    user_input = [int(input("입력하셈")) for _ in range(3)]
   
       
#숫자만 같으면 ball
    for s in range(3):
        for f in range(3):
            if com_random[s] == user_input[f]:
                if s == f :
                    strike +=1
                    print("stike 입니다")
                else:
                    ball +=1
                    print("ball입니다")
                    break

    if strike  == 0 and ball == 0:
        out +=1
    print("안맞음")
#안맞으면 ball
#승리 strike 되면 끝

    if count >=5 or out >= 2:
        print("5회 이상실행"if count >=5 else" out 횟수가 2번이상")
        break
#시도가 5회이상 ,out 2번이상
    if strike >=3:
        print("승리임")
        break