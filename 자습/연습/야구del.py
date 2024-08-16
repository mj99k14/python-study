import random
random_num = [value for value in range(0,10)]
for i in range(7):
    del random_num[random.randint(0,len(random_num)-1)]

print(random_num)
rand_list = random_num

count_strike_out =0
count_trial = 0
while True:
    count_strike = 0
    count_ball = 0
    
    # 사용자로부터 정수 3개 입력
    input_values = input()
    
    input_list = [int(value) for value in input_values.split()]

    # strike, ball 판별
    for i in range(3):
        for j in range(3):
            if rand_list[i] == input_list[j]:
                if i == j:
                    count_strike += 1
                else:
                    count_ball += 1

    print(f"스트라이크ㅋ : {count_strike}, 볼ㅋ: {count_ball}")
    
    # strike out 판별
    if count_strike == 0 and count_ball == 0:
        count_strike_out += 1
        print(f"스트라이크 아웃ㅋ: {count_strike_out}")

    # 게임종료 조건
    #  - strike 3개
    if count_strike >= 3:
        print(f"사용자 승리!")
        break
    
    #  - strike out 2번
    #  - 시도 회수 5번 이상
    if count_strike_out >= 2 or count_trial >= 5:
        print(f"사용자 패배")
        break
    
    count_trial += 1
