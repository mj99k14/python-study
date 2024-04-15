import random
def rock(user):
    
    choices = ['가위','바위','보']
    computer_choice = random.choice(choices)
    print(computer_choice)
    if user=='가위':
        if computer_choice =='보':
            msg = "당신이 이겼습니다!"
        elif computer_choice =='바위':
            msg = "당신이 졌습니다!"
        else:
            msg = "무승부입니다!"
    
    if user == '바위':
        if computer_choice =='가위':
            msg = "당신이 이겼습니다!"
        elif computer_choice == '보':
            msg = "당신이 졌습니다!"
        else:
            msg = "무승부입니다!"
    
    if user == '보':
        if computer_choice =='바위':
            msg = "당신이 이겼습니다!"
        elif computer_choice =='가위':
            msg ='당신이 졌습니다!'
        else:
            msg ='무승부입니다'
    return msg

user = input("가위, 바위, 보 중 하나를 선택하세요:")
result = rock(user)
print(result)