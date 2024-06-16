import random



random_num = [value for value in range(0,10)]
for i in range(7):
    del random_num[random.randint(0,len(random_num)-1)]

print(random_num)
strike = 0 
out = 0
while True:
    ball = 0
    
    user_input = input()
    user = [i for i in user_input.split()]

    for i in random_num:
        for j in user:
            if random_num[i] == user[j]:
                if i == j:
                    strike +=1

                else:
                    ball += 1

    if strike == 0 or ball == 0:
        out += 1
        print(f"아웃입니다!ㅋ{out}")
    else:
        print(f"{ball}{strike}")

        


    
    