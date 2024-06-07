import random 
name = ["첫","두","세"]
list_word = []
#3개단어 리스트 범위,3이상 20이하
for i in name:
    while True:
        input_value1 = input(f"{i}번쨰 단어를 입력하세여")
        if  3 <= len(input_value1) <=  20:
            list_word.append(input_value1)
            break
        else:
            while  not 3 <= len(input_value1) <=  20:
                print("다시 입력하셈!")
                break




#단어랜덤
random_word = list_word[random.randint(0,2)]
print(list(random_word))
#같은 리스트 만들어주기 
same_list = list(random_word)[:]
print(same_list)
same1_list = list(random_word)
print(same1_list)
#블라인드 글자수 
random_count = len(random_word)
r = random_count // 2
if random_count % 2 != 0 :
    r += 1 
print(r)

#블라인처리 하자!
for i in range(r):
    i = random.choice(range(len(same_list)))
    same_list[i] = "_"
print(same_list)
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어 :{random_word}")   
#단어 선택 
count = 1
while True:
    input_value  = input(f"{count}번째 시도 , 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    print(same1_list)

    if input_value  in random_word :
        for i in range(len(random_word)):
            if random_word[i] == input_value:
                same_list[i] = input_value      
        print(same_list)

    else:   
        print("뿌뿌 안들어가있음!")
       
    count+=1
  
    if not "_" in same_list:
        print(f"전부 정답 {random_word}, 도전횟수:{count}")
        break

    

