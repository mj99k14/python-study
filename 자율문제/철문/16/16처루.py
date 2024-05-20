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
        rand_value = random.randint(1, 9)
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
    #strike 충족
    user_list1,user_list2,user_list3=map(int,input(f"시도 {count_game_trial}: 입력한 숫자: ").split())    
    if user_list1==com_list[0]:
        count_strike+=1
    if user_list2==com_list[1]:
        count_strike+=1
    if user_list3==com_list[2]:
        count_strike+=1
    #ball   
    if user_list1==com_list[1]or user_list1==com_list[2]:
        count_ball+=1
    if user_list2==com_list[2]or user_list2==com_list[0]:
        count_ball+=1
    if user_list3==com_list[1]or user_list3==com_list[0]: 
        count_ball+=1
     #out   
    if  user_list1!=com_list[0]and user_list1!=com_list[1]and  user_list1!=com_list[2]:
        if user_list2!=com_list[0]and user_list2!=com_list[1]and  user_list2!=com_list[2]:
            if user_list3!=com_list[0]and  user_list3!=com_list[1]and user_list3!=com_list[2]:
                count_strike_out+=1
       #out 은 1이상 부터 표시한다해
    if count_strike_out >= 1 :
        print(f"{count_strike}strike,{count_ball}ball,{count_strike_out}out")
    else:
        print(f"{count_strike}strike,{count_ball}ball")
    #패~배
    if  count_game_trial >= 5:
            print(f"게임종료 : (시도횟수({count_game_trial}회 초과))")
            print(f"{com_list[0]} {com_list[1]} {com_list[2]}")
            break
    elif  count_strike_out >= 2:
        print(f"게임종료 : (시도횟수({count_strike_out}회 초과))")
    #승~리
    elif count_strike == 3:
        print(f"게임 종료: 승리 ")
        print(f"{com_list[0]} {com_list[1]} {com_list[2]}")
        break

    count_game_trial+=1        
    #리셋
    count_strike = 0
    count_ball = 0



