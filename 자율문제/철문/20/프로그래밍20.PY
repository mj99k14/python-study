import random
while True:
    print("-"*20)
    print("1.구구단 출력")
    print("2.랜덤값 삼각형 출력")
    print("3.종료")
    print("-"*20)
# 1구구단 출력 
    user_input = int(input("원하는 메뉴 번호를 입력하세요: "))
    if user_input > 4:
        print("1~3  사이의 값을 입력하세요")
        break
    else:
        if user_input == 1:
    
            # while True:
            #     user_input1 = input("출력할 구구단을 아래 형식으로 입력하세요")
            # #나눠주기
            #     user_num = list(map(int, user_input1.split("~")))
            #     user_input11 = [int(v) for v in range(user_num[0],user_num[1]+1)]
            #     for i in user_input11:            
            #         if 1 >= i or 9 <= i:
            #             print("2~9 사이의 값으로 입력하세요")   

            #     else:
            #         for i in user_input11:
            #             for s in range (1 , 10):

            #                 print(f"{i} * {s} = {i * s} ")
            #             print()
                        
            #             break
            import random
while True:
    print("-"*20)
    print("1.구구단 출력")
    print("2.랜덤값 삼각형 출력")
    print("3.종료")
    print("-"*20)
# 1구구단 출력 
    user_input = int(input("원하는 메뉴 번호를 입력하세요: "))
    if user_input > 4:
        print("1~3  사이의 값을 입력하세요")
        break
    else:
        if user_input == 1:
    
            while True:
                user_input1 = input("출력할 구구단을 아래 형식으로 입력하세요")
                #나눠주기
                user_num = list(map(int, user_input1.split("~")))
                if len(user_num) >= 2:
                    user_input11 = [int(v) for v in range(user_num[0],user_num[1]+1)]
                    for i in user_input11:            
                        if 1 >= i or 9 <= i:
                            print("2~9 사이의 값으로 입력하세요")   
                        print()
                        break
                else:
                    user_input11 = []
                    for i in user_num:
                        user_input11.append(int(i))

                for i in user_input11:
                    for s in range (1 , 10):
                        print(f"{i} * {s} = {i * s} ")
                    print()

        
    if user_input == 2:
        while True:
            user_input2 =int(input("삼각형의 높이 줄 수를 입력하세요(2이상  3이하)"))
            if user_input2 != 2 and  user_input2 !=3:
                print("삼각형의 높이는 2이상 3이하입니다")
                
                
            else:
                if user_input2 == 2:
                    n = [s for s in range(0,10)]
                    for _ in range(user_input2):
                        del n[random.randint(0,len(n)-1)]
                    #삼각형을빈칸 3 랜덤숫자
                    #빈칸 2 랜덤숫자
                    #랜덤숫자 
              
                    n = [s for s in range(0,10)]
                    for _ in range(7):
                        del n[random.randint(0,len(n)-1)]
                    print(" " ,n[0])
                    print(n[1], n[2])

                elif user_input2 == 3:
                    n = [s for s in range(0,10)]
                    for _ in range(user_input2):
                        del n[random.randint(0,len(n)-1)]
                    #삼각형을빈칸 3 랜덤숫자
                    #빈칸 2 랜덤숫자
                    #랜덤숫자 
                   
                    n = [s for s in range(0,10)]
                    for _ in range(4):
                        del n[random.randint(0,len(n)-1)]
                    print(" "*2,    n[0])
                    print(" ", n[1],n[2])
                    print(n[3],n[4],n[5])
        



    if user_input == 3:
        print("프로그램을 종료합니다.")
        break


#2랜덤값 삼각형출력
#3종료
# 시용자로 부터 입력 
# 1번을 출력하면 구구단 형식 범위는 (2~9)이외는 안됨
#2번을 선택하면 높이를 줄수있는 범위
# (2 이상 3이하)

