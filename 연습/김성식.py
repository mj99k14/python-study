import random
r_list =[value for value in range(0,10)]
for i in range(7):
    del r_list[random.randint(0,len(r_list)-1)]

print(r_list)

strike  = 0
out = 0
while True:
  
    ball = 0 
    input_user = input()
    u_list = [int(value) for value in input_user.split() ]

    for i in range(3):
        for a in range(3):
            if r_list[i] == u_list[a]:
                if i == a:
                    strike += 1
                   
                else:
                    ball += 1
    print(f"볼: {ball} 스트라이크:{strike}   아웃:{out}입니다")
                    

    if strike == 0 and ball == 0:
        out += 1
        print("아웃입니다")

    if strike == 3:
        print(f"{strike}정답 입니다~~~")
        break

    if ball > 2 or out > 5:
        print("기회 박탈~~")
        break




