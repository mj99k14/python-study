
    
user_list = []

for i in range(1, 4):
    input_str = input(f"시도 {i}: 입력한 숫자(): ")
    user_list_split = input_str.split(" ")
    for num in user_list_split:  # user_list_split의 각 문자열을 정수로 변환하여 user_list에 추가
        user_list.append(int(num))
    print(user_list)





count_game_trial = 0
count_strike_out = 0
count_strike = 0
count_ball = 0


com_list= getRandValue()
while True:
    #사용자 입력
     
    user_list = []

    for i in range(1, 4):
        input_str = input(f"시도 {i}: 입력한 숫자(): ")
        user_list_split = input_str.split(" ")
        for num in user_list_split:  # user_list_split의 각 문자열을 정수로 변환하여 user_list에 추가
            user_list.append(int(num))
    

    com_list = getRandValue()
    if count_game_trial ==input_str:
        if count_game_trial >=5 :
            print(f"게임 종료: 패배(시도 횟수{count_game_trial})")
            print(f"정답{com_list}")
    if com_list == input_str:
        count_strike+=3
        msg =(f"{count_strike}strike")
        break
    elif com_list in input_str:
        msg=(f"{count_ball}ball,{count_strike_out}out")
    else:
        msg=(f"{count_strike}strike,{count_ball}ball,{count_strike_out}out")

    #종료 조건:패배
    if count_game_trial >=5 or count_strike_out >=2:
        break
 
    #종료 조건:승리
    if  count_strike_out >=3:
        break

    
   print(f"게임 종료: 패배(시도 횟수{count_game_trial}회 초과)")
    print(f"정답{com_list}")