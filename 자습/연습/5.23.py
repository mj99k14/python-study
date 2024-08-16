#영어단어 3개 입력 리스트저장
import random
count = 1

my_list = []
while count <= 3 :
    while True:
        input_value = input(f"{count}번쨰 입력하세요 :")
    # 글자범위 5<= =>20 else 범위 재요구
        if 3 <=len(input_value) <=20:
            my_list.append(input_value) 
            count+=1
            break
        else:
            print("재입력 구다사이")
            break
    #랜덤 값      
    com_random = random.choice(my_list)       
    num =0
    #랜덤값을 반올림 and 반 
    if len(com_random) % 2==0:
        num+=len(com_random) //2
    else:
        num+=len(com_random) // 2 +1
        print(num)
    
    #num값을 LIST로 바꿔줌
    count = 0
    num_list =[]
    for i in my_list:
        num_list.append(num)

    
    #리스트로 바꿔준 NUM에 _을 추가
    com_random=random.randint(1,9)
        
    if com_random< len(num_list) and num_list[com_random] != "-":
        print(num_list.insert(com_random, "-"))
       