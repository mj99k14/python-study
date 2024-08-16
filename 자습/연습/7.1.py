import random
n = 100
#카운트해주기위해서
count_list = [0, 0, 0, 0, 0, 0]
for i in range(n):
    random_value = random.randint(1,6)
    #랜덤 값만큼 카운트 해줌 
    count_list[random_value - 1]+=1
#최대 별찾기
max = 0 
for i in range(6):
    if max < count_list[i]:
        max = count_list[i]
    
#히스토그램 나타내기
for i in range(6):
    print("*" * int((count_list[i])/ max * 10))
    print(count_list[i] / n * 100)
    
