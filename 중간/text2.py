#w점선안에 있는 문장들을 프린터해준다
print("-"*30)
print("1.홀수 짝수 구분 프로그램")            
print("2.3의 배수 확인 프로그램")  
print("-"*30)
input_vaulue =input("메뉴를 선택해 주십시오\n")
#메뉴를 선택에 대한 값출력
if  input_vaulue not in ["1","2"]:
    print(f"입력하신 값 {input_vaulue}은 유효하지 않은 메뉴 선택 값입니다. 메뉴 선택은 1과 2만 가능합니다")
else:
    if input_vaulue == "1":
        print("홀수 짝수 구분 프로그램을 선택 하셨습니다.")
        value = int(input("정수값을 입력 하세요.\n"))
        if  value /3 :
            print(f"입력하신 값 {value} 홀수입니다")
        else:
            print(f"입력하신 값 {value} 짝수입니다")
            
    if input_vaulue == "2":
        print("3의 배수 확인 프로그램을 선택 하셨습니다.")
        value_1=int(input("정수 값을 입력 하세요 .\n"))
        if value_1%3 ==0:
            print(f"입력하신 값{value_1},3의 배수 입니다 ")
        else:
            print(f"입력하신 값{value_1},3의 배수가 아닙니다.")