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

com_list = getRandValue()

while True:
    count_strike = 0
    count_ball = 0

    # 사용자 입력
    input_str = input(f"시도 {count_game_trial}: 입력한 숫자: ")
    user_list_split = input_str.split(" ")
    input_user = [int(num) for num in user_list_split]

    for i in range(3):
        if input_user[i] == com_list[i]:
            count_strike += 1
        elif input_user[i] in com_list:
            count_ball += 1

    if count_strike == 0 and count_ball == 0:
        count_strike_out += 1

    if count_strike_out >= 1:
        print(f"결과: {count_strike} strike, {count_ball} ball, {count_strike_out} out")
    else:
        print(f"{count_strike} strike, {count_ball} ball")

    if count_game_trial >= 5:
        print(f"게임 종료: (시도 횟수 {count_game_trial}회 초과)")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break

    elif count_strike_out >= 2:
        print(f"게임 종료: (아웃 횟수 {count_strike_out}회 초과)")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break

    elif count_strike == 3:
        print("게임 종료: 승리")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break

    count_game_trial += 1
