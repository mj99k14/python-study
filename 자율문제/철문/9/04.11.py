# import random
# 사용자입력은input() 함수를 통해 받으세요.
# 컴퓨터의선택은난수발생을이용해결정하세요. random 모듈의choice() 함수를 사용할 수있습니다.
# 사용자와컴퓨터의선택을비교하여승리, 패배, 또는무승부를결정하고결과를출력하세요.
# 사용자가잘못된입력을한경우, 적절한에러메시지를출력하고프로그램을종료하세요
# use=input("가위, 바위, 보 중 하나를 선택하세요: ")
# choices = ['가위','바위','보']
# computer_choice = random.choice(choices)
# print("컴퓨터의 선택:",computer_choice)
# if computer_choice == use:
#     print("결과: 무승부입니다!")
# if computer_choice=='바위' and use =='보':
#     print("결과: 당신이 이겼습니다!")
# if computer_choice=='보'and use =='가위':
#     print("결과: 당신이 이겼습니다!")
# if computer_choice=='가위' and use =='바위':
#     print("결과: 당신이 이겼습니다!")
# elif computer_choice =='바위' and use =='가위':
#     print("결과: 당신이 졌습니다!")
# elif computer_choice =='가위' and use =='보':
#     print("결과: 당신이 졌습니다!")
# elif computer_choice =='보' and use =='바위':
#     print("결과: 당신이 졌습니다!")        
# else:
#     print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요")
    
    
    



# use=input("가위, 바위, 보 중 하나를 선택하세요: ")
# choices = ['가위','바위','보']
# computer_choice = random.choice(choices)
# print("컴퓨터의 선택:",computer_choice)

 
# if use == computer_choice:
#     print("결과: 무승부 입니다!")
# if(computer_choice=='바위' and use =='보') or(computer_choice=='보'and use =='가위')or(computer_choice=='가위' and use =='바위'):
#     print("결과: 당신이 이겼습니다!")
# elif(computer_choice =='바위' and use =='가위')or (computer_choice =='가위' and use =='보') or (computer_choice =='보' and use =='바위'):
#     print("결과: 당신이 졌습니다!")   
# else:
#     print("잘못된 입력입니다.가위,바위,보 중에서 선택해주세요")




        
        




import random

def usein(usein1):
    choices = ['가위','바위','보']
    computer_choice = random.choice(choices)
    print("컴퓨터의 선택:",computer_choice)

 
    if usein1 == '가위':
        if computer_choice=='보':
            return"결과:이겼습니다!"
        elif computer_choice == '바위':
            return "결과:졌습니다!"
        else:
            return "비겼습니다" 
        
    elif usein1 == '보':
        if computer_choice=='보':
            msg= "비겼습니다"
        elif computer_choice == '바위':
            msg = "결과:졌습니다!"
        else:
            msg = "비겼습니다"
    elif usein1 == '바위':
        if computer_choice=='보':
            msg= "결과:졌습니다!"
        elif computer_choice == '가위':
            msg = "결과:이겼습니다!"
        else:
            msg = "비겼습니다" 
        return msg
    