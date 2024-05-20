import random
# 입력자 입력받음
win,lose,draw = 0,0,0

#3전2선
while True:
    if win >=2 or lose>=2:
        if win >=2:
            print("내가이김/n최종 승자: 나")
        else:
            print("컴터이김/n 최종 승자:컴터")
            
        break
    
    #가위,바위,보 승패
    while True:
        input_user = input("가위,바위,보 중 하나를 입력하세요:")
        if input_user == "가위" or input_user =="바위" or input_user =="보":
            break
        print("가위,바위,보  중에 고르삼 ")
        rsp =["가위",'바위',"보"]
        input_computer =rsp[random.randint(0,2)]
        msg_1 =""
        if input_user == input_computer :
            msg_1="무승부"
            draw+=1
        elif input_user =="가위" and input_computer =="보" or\
            input_user =="보" and input_computer =="바위" or\
            input_user =="바위" and input_computer =="가위":
            msg_1="이김"
            win +=1
        else:
            msg_1="짐"
            lose+=1
        print(input_user)
        print(f"컴퓨터:{input_computer}")
        print(f"결과{msg_1}")
        print(f"전적:{win}승{lose}패{draw}무")
    