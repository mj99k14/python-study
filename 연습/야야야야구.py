import random
r_list  = [value for value in range(0,10)]
for i in range(7):
    del r_list[random.randint(0,len(r_list)-1)]


print(r_list)

out = 0
while True:
    strike = 0
    ball = 0 
    input_user = input("")
    user_list = [int(value) for value in input_user.split()]

    for i in range(3):
        for j in range(3):
            if user_list[i] == r_list[j]:
                if i == j:
                    strike += 1 
                else:
                    ball += 1 
    print(f"스트라이크 {strike}  볼 { ball } 아웃 {out}")
                    
                    
                    

    if strike == 0 and ball == 0:
        out += 1
        print("아웃입니다")

    if strike  == 3:
        print(f"{strike}다 채우 ")
        break

    



