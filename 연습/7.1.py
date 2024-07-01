import random
n = 100

count_list = [0,0,0,0,0,0]
for i in range(n):
    random_value = random.randint(1,6)
    count_list[random_value-1]+=1

max = 0 
for i in range(6):
    if max < count_list[i]:
        max = count_list[i]
    

for i in range(6):
    print("*" * int((count_list[i])/max * 10))
    print(count_list[i] / n *100)
    
