# msg = ""
# value = 1
# if value ==1:
#     msg ="안녕"
# else:
#     msg ="hello"
    
# #삼항 연산자 -> "안녕" value == 1 else "hello" 
# msg = "안녕"if value ==1 else "hello"






# stikre_out = True

# print("패배"if stikre_out else "승리")

# if stikre_out:
# #     print("패배")
# # else:
# #     print("승리")
    
    
    
    
# 알고리즘?
# 명령어

# value_1 = int(input("1st 값: "))
# value_2 = int(input("2st 값: "))

# sum = value_1 + value_2


# print(sum)

import turtle
#화면을 생성하여 거북이가 그릴 수 있는 캔버스를 만듦
# screen = turtle.Screen()  #종이   #screen 과 t는 참조변수 = screnn object

# #그림을 그릴 거북이 객체를 생성함
# t = turtle.Turtle() # 팬 
# #거북이의 이동속도를 설정함 (1이 가장 느림 ,10이 가장 빠름)
# t.speed(1)
# #거북이를 앞으로 100만큼 이동
# t.forward(100)
# #거북아를 오른쪽으로 90도 회전
# t.right(90)
# #거북이를 뒤로 200만큼 이동시킴
# t.backward(200)
# #거북이를 왼쪽으로 270도 회전시킴
# t.left(270)
# #팬을 들어서 그림을 그리지않도록 함
# t.penup()
# #거북이를 초기 위치로 이동시킴
# t.home()
# #펜을 내려서 그림을 그리도록 함
# t.pendown()
# #거북이를 왼쪽으로 90도 회전 시킴
# t.left(90)
# #거북이를 앞으로 100만큼 이동시킴
# t.forward(100)
# #터틀 그래픽 창이 닫히지 않고 유지하도록 함 
# turtle.done()




# #
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(1)
# #북이 100전진
# t.forward(100)
# #꺽으세요
# t.left(120)
# #돌아요 다시
# t.forward(100)
# #돌아요
# t.left(120)
# t.forward(100)

# turtle.done()


# screen = turtle.Screen()
# t = turtle.Turtle()
# t.circle(150)
# t.circle(100)
# t.circle(50)
# turtle.done()


screen = turtle.Screen()
t = turtle.Turtle()
# t.speed(90)
# # for _ in  range(2):
# #     t.forward(300)
# #     t.right(90)
# #     t.forward(300)
# #     t.right(90)
# # turtle.done()


# for _ in range(3):
#     t.forward(100)
#     t.left(120)
# turtle.done()


import turtle

def draw_heart():
    t = turtle.Turtle()
    t.speed(1)  # 거북이 속도를 설정합니다. (1이 가장 느리고 10이 가장 빠릅니다)

    t.begin_fill()  # 하트 내부를 색칠하기 시작합니다
    t.color("red")  # 하트 색깔을 빨간색으로 설정합니다

    t.left(50)  # 왼쪽으로 50도 회전합니다
    t.forward(133)  # 앞으로 133 단위만큼 이동합니다

    # 오른쪽 곡선 그리기
    t.circle(50, 200)  # 반지름이 50인 원을 200도 그립니다

    # 왼쪽 곡선 그리기
    t.right(140)  # 오른쪽으로 140도 회전합니다
    t.circle(50, 200)  # 반지름이 50인 원을 200도 그립니다

    t.forward(133)  # 앞으로 133 단위만큼 이동합니다
    t.end_fill()  # 하트 내부 색칠을 마칩니다

    turtle.done()  # 거북이 그래픽 창을 유지합니다

draw_heart()
