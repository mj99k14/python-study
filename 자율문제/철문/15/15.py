# 사용자로부터 가위, 바위, 보 중 하나를 입력받고 컴퓨터가 선택한 값과 대결하여 승, 패, 무를
# 판단하고 결과를 출력
import random
win = 0
lose = 0
draw = 0
while True:
    user = input("가위, 바위, 보 중 하나를 입력하세요: ")
    choices = ["가위", "바위", "보"]
    computer = random.choice(choices)
    print(f"컴퓨터: {computer}")
   
    if user == "가위"and computer =="보" or user == "바위"and computer =="가위" or user == "보"and computer =="묵":
        win += 1
        print(f"승리! 현재 전적:{win}승{lose}패{draw}무")
    elif user == "가위"and computer =="바위" or user == "바위" and computer =="보" or user == "보" and computer =="가위":
        lose += 1
        print(f"승리! 현재 전적:{win}승{lose}패{draw}무")
    elif user == computer  or user ==  computer or user == computer:
        draw += 1
        print(f"무승부! 현재 전적 :승리! 현재 전적:{win}승{lose}패{draw}무")
        break
    else :
        print("가위,바위,보 중에서 선택하셈")
        continue  
    
    

# • 게임은 3판 2선승제로 진행
    if win ==2 :
        print(f"전적:{win}승{lose}패{draw}무\n최종 승자:사용자")
    elif lose ==2:
        print(f"전적:{win}승{lose}패{draw}무\n최종 승자:컴퓨터")
        break
        
# • 매 게임마다 승, 패, 무의 결과가 출력


# • 사용자가 입력하는 값은 "가위", "바위", "보" 중 하나여야 하며,이외의 값이 입력되면 다시 입력