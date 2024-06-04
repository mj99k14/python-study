import random
import turtle

#화면을 설정합니다
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")
#거북이를 생성합니다
width =screen.window_width()//2 #가로 860
height =screen.window_height() //2 #세로 540
print("원도우 가로x세로",width,height)
t =turtle.Turtle() 

#거북이가 움직이는 함수를 정의합니다
def move_forward():
    t.forward(100)
    
    x,y = t.position()
    print(x,y)
    if x >= width :
        t.right(180)
    elif x <= -width:
        t.right(180)
    elif y >= height:
        t.right(180)
    elif y <= -height:
        t.right(180)
def move_backward():
    t.backward(100)
    
def turn_left():
    t.left(15)

def turn_right():
    t.right(15)
#펜 색깔을 검은색으로 변경


#펜 색깔 변경 함수를 정의
def move_random():
    colors = ["red","green","blue","yellow","purple","orange"]
    t.pencolor(random.choice(colors))
    
#키보드 이벤트를 설정랍니다
screen.listen()
screen.onkey(move_forward,"Up")#위쪽 화살표 키를 누르면 앞으로 이동
screen.onkey(move_backward,"Down")#아래쪽 화살표 키를 누르면 뒤로 이동
screen.onkey(turn_left,"Left")#왼쪽 화살표 키를 누르면 왼쪽으로 회전
screen.onkey(turn_right,"Right")
screen.onkey(move_random,"c")
# screen.onkey(change_color_to_black,"b")
# screen.onkey(change_color_to_red,"r")

# curent_color = t.pencolor()

#i를 누르면 색깔빨간색 _>검은색  검은색->빨간색
# def change_color_to_black():
#     if curent_color == t.pencolor("i"):
#         print(t.pencolor("black"))
        
# def change_color_to_red():
#     t.pencolor("red")  
#     if curent_color == t.pencolor("i"):
#         print(t.pencolor("red"))

# def change_color():
#     if t.pencolor =="black":
#         t.pencolor =="red"
#     else:
        
        
# def inverse_color():
#     current_pen_color = t.pencolor()
    
#     if current_pen_color =="red":
#         t.pencolor("black")
#     elif current_pen_color =="black":
#         t.pencolor("red")
    
# screen.onkey(change_color_to_black,"i")
# screen.onkey(change_color_to_red,"i")
# #이벤트 루프를 시작합니다



# def change_color():
#    while  True:
#         print("색깔 선택: ")
#         print("1.파란색 ")
#         print("2.검정색 ")
#         print("3.노란색 ")
        
#         input_value = int(input("숫자 입력 :"))
        
#         # if input_value == 1:
#         #     t.pencolor("blue")
#         #     break
#         # elif input_value == 2:
#         #     t.pencolor("black")
#         #     break
#         # elif input_value == 3:
#         #     t.pencolor("yellow")
#         #     break
#         # else:
#         #     print("재입력 구다사이")
            
            
            
            
#         if  1 <= input_value <=3:
#             if input_value == 1:
#                 t.pencolor("blue")
    
#             elif input_value == 2:
#                 t.pencolor("black")
          
#             elif input_value == 3:
#                 t.pencolor("yellow")
#             break
#         else:
#             print("다시입력하셈 ")
        
        
        
        
        
# while not ( 1 <= input_value <=3):
#     input_value = int(input("숫자 입력 :"))
#     if input_value == 1:
#         t.pencolor("blue")

#     elif input_value == 2:
#         t.pencolor("black")

#     elif input_value == 3:
#         t.pencolor("yellow")

# screen.onkey(change_color,"t")







screen.mainloop()







