import random
#컴퓨터1~100까지 숫자중하나 고름
count =4
com_random =random.randint(1,101)
print(com_random)
num_start = 0
num_last = 100
while count  < 5:
#기회는 5번
#사용자 숫자입력
    user_input = int(input(f"횟수:{count} 사용자 입력한 숫자:   "))
#힌트제공: 사용자가 고른숫자보다 컴터 숫자가 작으면 작습니다
    if user_input != com_random:
        if user_input < com_random:
            num_start = user_input +1
            print(f"{user_input}보다 더 큽니다{num_start} - {num_last}")
        elif user_input >  com_random:
            num_last = user_input -1
            print(f"{user_input}보다 작습니다{num_start} - {num_last}")
        count-=1
    else:
        print(f"よし！正解！{com_random}")
        break

    if count <= -1:
        print(f"おなたのチャンス終わりだよ～正解はこれだよ{com_random}だよ")
        break