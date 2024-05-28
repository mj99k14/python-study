import random
count = 0
user_list = []
while count <=2:
    #영어 3개 단어를 입력하셈
    num = ["첫","둘","셋"]

    input_user =input(f"{num[count]}번째 단어를 입력하세요")
    #단어는 #3이상 20이하 제한
    if  3 <= len(input_user) <= 20:
        user_list.append(input_user)
        count+=1
        
    else:
        print("범위 안에 입력하라옹~!")
    #3개중에 하나 임의 선택           
    random_word = random.choice(user_list)
  
print(f"게임을 시작하지!{random_word}")


    
hinum = 0

if len(random_word) % 2 ==0:
    hinum+=len(random_word) // 2
    #홀수인경우 +1
else:
    hinum+=len(random_word) // 2 + 1
        
#랜덤 글자분열
words= []
b = 0
for i in random_word:
    words+=i
print(words)
#비교할 랜덤 숫자를 받아줌
a = []
while b < hinum:
    random_number = random.randint(0,len(random_word)-1)  
    if random_number not in a:
        a.append(random_number)
        b += 1
print(a)

#대입
blind_list_num = words
 
 
          
#선택한 글자 반은 블라인드처리
for i in a:
    blind_list_num[i] = "_"


#블라인드 처리된 리스트안에 글자뽑아주기
blind_list_ma = ""
for  o in blind_list_num:
    blind_list_ma+=o
print(blind_list_ma)
count+=1

#사용자로부터 글자한개 입력받음
input_user1 =input("입력하시요~ ")
#입력받은 글자가 블라인드처리된 안에있으면 블라인드해제

#존재하지않은 경우 없음
#단어 모든글자 맞추면 종료