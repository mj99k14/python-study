# 사용자로부터"left", "right", "up", "down" 중 하나의 단어를 입력받습니다. 

location=input("방향을 입력하세요(left, right, up, down):" )

# • 입력받은문자열에따라"왼쪽으로이동합니다", "오른쪽으로이동합니다", "위로
# 이동합니다", "아래로 이동합니다"를 출력하는프로그램을작성하세요. 
if location=="left":
    print("왼쪽으로 이동합니다.")
elif location=="right":
    print("오른쪽으로 이동합니다.")
elif location=="up":
    print("위로 이동합니다.")
elif location=="down":
    print("아래로 이동합니다.")
else:
    print("알 수 없는 명령입니다.")
# • 만약다른단어가입력되면"알수없는명령입니다"를출력하세요. 
#  – 사용자에게방향을입력받습니다.
#  – 입력받은방향에따른메시지를결정합니다.