import random
while True:
    n = int(input("100에서 1000000까지만 입력하셈"))
    if  100 <= n <=100000:
        break
    #카운트해주기
random_value_list= [0, 0, 0, 0, 0, 0]
for i in range(n):
    random_value = random.randint(1, 6)
    random_value_list[random_value - 1] +=1 #주사위의 위치만큼 더해주기위해서 +=1
#큰수 찾기
max = 0
for i in range(6):
    if random_value_list[i] > max:
        max = random_value_list[i]
#확률, 별
for i in range(6):
    print("*"*int(random_value_list[i] / max * 10), end ="")
    print(random_value_list[i] / n * 100)

