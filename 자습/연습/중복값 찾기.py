#5번 반복하고 싶어
# for count in range(0,5):
#     print(count)
    
    
# #while 조건식:
# # pass

# count_w = 0 
# while count_w < 5 :
#     print(count_w)
#     count_w += 1 #ount_w = count_w + 1 
        
import  random
    
#유효값: 1<= trial_num <= 100
#유효범위 이외 값인 경우 에러메세지 출력후 재입력
#무한루프
while True: # 계속반복하기위해서 
    #n 값 입력 
    trail_num = int(input("N값: "))
    
    #입력 받은 n값이 유효범위
    if 1 <= trail_num <= 100:
        #무한루프 탈출
        break
    
    print("에러: 1이상 100이하 값 입력")
    
#중복 값이 없는 정수의 개수    
trail_num = 5
#중복 값이 없는 정수를 저장할 list
made_list =[] 
#trail_num 개수 만큼 중복값이 없는 정수 생성 후 리스트에 저장  
for trial_count in range(0,trail_num): 
    #중복 값 검사를 위해서 
    while True:
        random_num = random.randint(1,100)
        
        found_duplication = False   #
        for made_index in range(0,trial_count):
            #중복값이 있으면 
            if made_list[made_index] == random_num:
                found_duplication = True             #값은 값을 다시뽑기위해서 
                break
        if not found_duplication:   
            made_list.append(random_num)    # 중복되지않는 값만 받아주기위해서
            break
print(made_list)

while True:
    input_index = int(input("index:"))
    if 0 <= input_index < len(made_list): # 리스트 길이를 알기 위해서 
        print(f"원소 값:{made_list[made_index]}")
        break
    print("에러")
    
    
    
    