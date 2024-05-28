import random
count =0 
input_list =[]
num =["하나","둘","셋"]
while count <=2:
    while True:
        input_value = input(f"{num[count]}번쨰 입력하세요 :")
    # 글자범위 5<= =>20 else 범위 재요구
        if 3 <=len(input_value) <=20:
            input_list.append(input_value) 
            count+=1
            break
        else:
            print("재입력 구다사이")
            break

com_random = random.choice(input_list)     
print(f"단어 선택 완료게임을 시작합니다: {com_random}") 
num = 0
    #랜덤값을 반올림 and 반 
if len(com_random) % 2 == 0 :
    num+=len(com_random) // 2 
else:
    num+=len(com_random) // 2 + 1

#랜덤 글자 분열 
asap = []
b = 0
for i in com_random:
    asap += i
print(asap)
# asap = 단어 쪼갠거

#랜덤숫자를 담아줌
a=[]#랜덤 숫자
while b < num:
    randomhaha=random.randint(0,len(com_random)-1)
    if randomhaha not in a:
        a.append(randomhaha)
        b += 1
print(a)

blind_list_under  = asap
#-추가
for q in a: # a = 1 2 3
    blind_list_under[q] = "_" # =오른쪽의 값을 왼쪽에 대입하겠다


#list에있는값을 뽑아주기
blind_word = ""
for i in blind_list_under:
    
    blind_word+=i

count=1


while True:
    dano = 0
    
    print(f"{count}번쨰 시도, 아래 단어를 구성하는 알파벳 하나 입력하시던지 ")
    print(blind_word)
    input_user =input("입력오네가이 :")

 
    #혹시포함하면 포함하는숫자 알려줌 그리고blind_word추가 
    for index in a:
        if  com_random[index] == input_user:
            blind_list_under[index] = input_user
            blind_word=""
            for i in blind_list_under:
                blind_word+=i 
                
                dano+=1
                
                   
    if input_user not in com_random:
        count += 1
        print("노포함")
            
            
            
    if dano >1:
        count +=1
        
    elif dano == 1:
        count +=1
            
    if blind_word == com_random:
        print(f"clear 선택 ")
        break
        
                   
               
               
            
            
                
            
      
                
                
                
                
                        
    # if blind_word == com_random:
    #     print("clear -선택")
    #     break
                    
    # #포함하는 글자가 포함 횟수랑 그만큼 추가  ,ㅡ.
    #다맞추면 선택단어 총 시도 횟수 나와야함 
    

    



                