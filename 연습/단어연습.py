import random

count1= ["첫","두","세"]
user_words = []
#단어 입력
for i in count1:
   
    while True:
        user = input(f"{i}번쨰 단어를 입력하세요")
        if 3 <= len(user) <=20:
            user_words.append(user)
            break
        else:
            print("범위내를 입력하세요")
          
    


#단어임의 선택
user_random_word1 = random.choice(user_words)
user_random_word = [i for i in user_random_word1]
print(user_random_word)
smae_list = user_random_word[:]

#블라인드해줄글자 수 구하기
count_words = len(user_random_word)
half_word = count_words // 2
if count_words % 2 !=0:
    half_word +=1
print(half_word)
#블라인드 처리해주기
#half_word만큼 랜덤으로 블라인드처리해주기 
count = 0
index_list = []
while count < half_word:
    random_num = random.randint(0,count_words-1)
    if smae_list[random_num] != "_":
        smae_list[random_num] = "_"
        index_list.append(random_num)
        count += 1
print(smae_list)


c = 1
while True:
    count = 0
    user_input = input(f"{c}번째 시도 ,아래 단어를 구성하는 알파벳 한 개 입력하세요")
    print(smae_list)
    #user_input이 user_random_word 안에들어가면 user_random_word같은 자리
    for i in index_list:
        if user_input == user_random_word[i]:
            smae_list[i] = user_input
            count +=1
    
    if count == 0:
        print("더머리를 굴려봐라이 자식아") 

    c+=1   
   
    
    if "_"not in smae_list:
        print(f"오메데토~~~~ 전부다 맞췄어~~~{user_random_word1}")
        break

            

