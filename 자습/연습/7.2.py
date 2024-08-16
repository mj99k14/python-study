
import random
n =100


random_count = [0,0,0,0,0,0]
for i in range(n):
    random_value = random.randint(1,6)
    random_count[random_value -1] += 1

max = 0
for i in range(6):
    max < random_count[i]
    max = random_count[i]
#확률 , 별
for i in range(6):
    print("*" * int(random_count[i] / max *10),end="")
    print(random_count[i]/n *100)







