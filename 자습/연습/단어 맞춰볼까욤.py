import random
count = ["첫","두","세"]
user_list = []
for i in count:
    while True:

        user =input(f"{i}번쨰 단어를 입력 하세요")
        if 3 <= len(user) <= 20:
            user_list.append(user)
            break
        else:
            print("재입력원츄")
            

user_c = [random.choice(user_list)]
print(user_c)
user_c1 = [i for i in user_c[0]]
same_list = user_c1[:]


user_num = len(user_c1)
print(user_num)
half_num = user_num //2
if user_num %2 !=0:
    half_num +=1


# 블라인드 리스트 만들어주기
count = 0
random_list = []
while count< half_num:
    random_blind = random.randint(0,half_num-1)
    if same_list[random_blind] != "_":
        same_list[random_blind] = "_"
        count += 1
        random_list.append(random_blind)

            
        
print(same_list)

count = 1
while True:
 
    input_user = input(f"{count}번째 시도,아래 단어를 구성하는 알파벳 한 개를 입력하세요: ")
  
    # 사용자 입력이 맞으면 블라인드해제
    if input_user in user_c1:
        for i in random_list:
            if user_c1[i] == input_user:
                same_list[i] = input_user
        print(f"입력한 알파벳 단어 내 포함: {count}")
        print(f"{same_list}")
    else:
        print("포함 안되는 글자입니다~")

    count+=1
    if "_" not in same_list:
        print(f" 총시도 횟수: {count},  선택된 단어 :{user_c}")
        break
    #사용자입력이 트리면 입력하지않음 
        
