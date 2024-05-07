




while True:
    #메뉴를 출력한다
    print("-"*20)
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("-"*20) 
    
#메뉴 선택
    input_value = int(input(""))
    if input_value == 1 :
        print("출력할 구구단의 단을 입력하세요. 구구단의 2~9 사이 입력 ")
        #1를 선택하면 사용자가 입력한 구구단을 입력받는다
        while True:
            input_value1 = int(input(""))
            if 2<= input_value1 <=9:
                for i in range(1,10):
                    print(f"{input_value1} * {i} =  {input_value1 * i}")
                break #2~9 탈출
            else:
                print("2~9사이 정수를 입력해주세요")
       
#2 구구단 종료            
    elif input_value == 2:
        print("종료")
        break
        
    else:
        print("잘못 입력하셨습니다.다시 입력하세요.")
    






















