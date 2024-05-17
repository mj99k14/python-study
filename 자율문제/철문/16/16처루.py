#컴퓨터가 1~10까지 3개 선택  중복x
#리스트로 만듬
#경우의수 
#컴퓨터의 값은 모름 결과값을 보고 예측 
#컴퓨터 난수를 맞춰야함




# #in ,not in ,list 내 중복되지않은 랜덤 정수 생성 함수 사용금지

#     #중복되지않은 1~10 사이 정수 3개 생성
# 3 7 4 :computer
# 2 3 4 :user
# result: 1 strike, 1ball
# import random
# com_list = list()
# for count in range(3):
#     while True:
#     #랜덤 값 생성: GR
#         rand_valie = random.randint(1,10)
     
    
#     #생성된 랜덤 값이 리스트 내 없을 경우 로직 종료
#         if rand_valie not in com_list:
#             com_list.append(rand_valie)
#             break




# import random
# com_list = list()
# count = 0
# def getrandvalue():
#     while count < 3:
#         rand_list = random.randint(1,10)
#         found_duplicated_value = False
#         for sub_count in range(count):
#             #중복 값이 있을 경우
#             if rand_valie == com_list[sub_count]:
#                 found_duplicated_value = True
#                 break
#         if not found_duplicated_value:
#             com_list.append(rand_valie)
#             count +=1
#     return rand_list   
# print(com_list)



# 중복되지 않은 1~10사이 정수 3개 생성
# in, not in, list 내 중복되지 않은 랜덤 정수 생성 함수 사용금지

# 3 7 4 : computer
# # 2 3 4 : user
# result : 1 strike, 1 ball

import random


def getRandValue():
    rand_list = list()

    count = 0

    while count < 3:
        rand_value = random.randint(1, 10)
        found_duplicated_value = False
        
        for sub_count in range(count):
            # 중복 값이 있을 경우
            if rand_value == rand_list[sub_count]:
                found_duplicated_value = True
                break
        
        if not found_duplicated_value:
            rand_list.append(rand_value)
            count += 1
            
    return rand_list






count_game_trial = 1
count_strike_out = 0
count_strike = 0
count_ball = 0

user_list = []
com_list= getRandValue()
while True:
    #사용자 입력
    if count_game_trial >= 6:
        break
    
    input_str = input(f"시도 {count_game_trial}: 입력한 숫자: ")
    user_list_split = input_str.split(" ")
    user_list.append(user_list_split)
 

    #변수 업데이트
   
    
    if user_list[0]==com_list[0] and\
        user_list[1]==com_list[1]and\
        user_list[2]==com_list[2]:
        count_strike+=3
        msg =(f"{count_strike}strike,{count_ball} ball")
        print(msg)
        print(f"게임 종료: 승리 ")
        print(f"정답{com_list}")
        break
    if  user_list[0]in com_list or\
        user_list[1]in com_list or\
        user_list[2]in com_list :
        count_ball+=1
        msg=(f"결과:{count_ball}ball,{count_strike_out}out")
    else:
        count_strike_out+=1
        msg=(f"결과:{count_strike}strike,{count_ball}ball,{count_strike_out}out")
    
        print(msg)
    #종료 조건:패배
        
        
    
    if count_strike_out >=2 or count_game_trial >6:
        print(f"게임 종료: 패배(시도 횟수{count_game_trial}초과)\n정답 {com_list}")
    
        break
   
    count_game_trial+=1

