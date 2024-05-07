while True:
    #메뉴 출력
    print("-"*10)
    print("1.구구단 출력 ")
    print("2.프로그램 종료")
    print("-"*10)
    #메뉴 값 입력
    seelect = input("메뉴 값을 입력하세요!:")
    
    #메뉴 값 =1 
    if seelect =="1":
        #구구단 입력 
        while True:
            dam = int(input("단을 입력하세요:"))
         #해당 단의 구구단 출력
        if 2 <= dam <= 9:
            for num in range(1,10):
                print(dam,"x",num,"=",dam * num)
                break
            print("단은 2~9 사이 오네가이")
        
           
    #메뉴 값 = 2
    elif seelect == "2":
        #프로그램 종료
        print("프로그램 종료")
        break
    #메뉴값이 != 1 and 메뉴 값이 != 2
    #에러 메세지 출력
    else:
        print("메뉴 값은 1또는 2만 입력")
        
        
        
while True:             #예외가 발생하지 않았을때 멈춤  while계속도는건 예외가 생기는거임 
    input_value = int(input(""))
    if input_value >0 :
        print("입력 값은 :" , input_value)
        break
    print("양의 정수를 입력하세요 ")       # IF문은 break가 필요 , while  = true 이기때문에 ELSE은 필요없음 