#난수
import random
random_list =[v for v in range(0,10)]
for i in range(7):
    del random_list[random.randint(0,len(random_list)-1)]
print(random_list)
out = 0
while True:
    input_user =list(map(int,input("입력하라닝겐").split()))
    ball = 0
  
    strike = 0 
    for i in range(3):
        for s in range(3):
            if random_list[i] == input_user[s]:
                if i == s :
                    strike +=1
                else:
                    ball += 1
    print(f"스트라이크 횟수: {strike} , 볼 횟수{ball}")
    if strike == 0 and ball ==0 :
        out +=1
        print(f"아웃 횟수{out}")

    if strike == 3: 
        print(f"전부 다  스트라이크!{strike}")
        break


    

    

