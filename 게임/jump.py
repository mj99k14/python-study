import pygame
import sys

pygame.init()
#화면 크기 설정
screen_width =800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("점프하는 사각형")
#색상
WHITE = (255,255,255)
BLUE = (0,0,255)
#사각형설정
rect_width = 50
rect_height = 50
rect_x =100
rect_y = screen_height - rect_height
rect_speed_y = 0 # 사각형 세로방향
rect_speed_x = 10# 사각형 가로
jump_speed = -15 # 초기 속도
gravity = 1 #가속도

#게임 루프 
running =True
jumping = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                rect_speed_y = jump_speed
                jumping = True
            if event.key == pygame.K_LEFT:
               rect_x -=rect_speed_x
            elif event.key == pygame.K_RIGHT:
                rect_x +=rect_speed_x
                
    #사각형의 위치업데이트
    rect_speed_y += gravity
    rect_y += rect_speed_y
    #바닥에 닿으면 멈추고 점프 가능
    if rect_y >=screen_height - rect_height:
        rect_y = screen_height - rect_height
        rect_speed_y = 0
        jumping = False
    
    #화면 경계
    if rect_x < 0:
        rect_x = 0
    elif rect_x >  screen_width - rect_width:
        rect_x =  screen_width - rect_width 

    #화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen,BLUE,(rect_x,rect_y,rect_width,rect_height))
    pygame.display.flip()
    #프레임 설정

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()