import random


random_num = ["kakao","mamak","asdaa"]

random_num = random.choice(random_num)
random_list = [value for value in random_num]
print(random_list)
s_list = random_list[:]

blind_num = len(random_list) 
half_num = blind_num // 2
if blind_num %2 != 0 :
    half_num += 1 
print(half_num)
left =[]
for _ in range(half_num):
    while True:
        rand_index = random.randint(0,len(s_list)-1)
        if s_list[rand_index] != "_":
            s_list[rand_index] = "_"
            left.append(rand_index)

            break



while True:
    input_user = input()


    if input_user in random_list:
        for i in left:
            if  random_list[i] == input_user:
                 s_list[i] = input_user
        print("들어가있질롱")
    
    else:
        print("존재하지않음")
    

    if "_" not in s_list:
        print("성공~")
        break