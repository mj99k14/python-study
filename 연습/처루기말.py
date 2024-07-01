import random

random_list =[value for value in range(0,10)]
for _ in range(7):
    del random_list[random.randint(0,len(random_list)-1)]
print(random_list)

count = 0
strike = 0
ball = 0
out = 0
while True:
    ball = 0 
    user_input = input()
    user = [int(f) for f in user_input.split()]

    for i in random_list:
        for s in user:
            if random_list[i] == user[s]:
                if i == s:
                    strike += 1
        else:
            ball += 1

    

