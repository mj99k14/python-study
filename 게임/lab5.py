import pygame
import random
#초기화
pygame.init()
#화면 크기설정
screen_width = 800
screen_height = 600
screen =pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('동그라미 이동 및 색상 변경 프로그램')
#색상 정의
colors = [(255 , 0, 0),(0, 0, 0),(255, 255 , 0),(0, 255, 0),(0, 0, 255)]
current_color =random.choice(colors)
circle_radius = 40
#동그라미 초기위치
circle_x = screen_width // 2
circle_y = screen_height // 2
#프레임 레이트 설정
clock = pygame.time.Clock()
fps = 30
#이동속도 (픽셀/초)
speed = 300
#메인루프
running =True
while running:
    #델타 타임 계산
    delta_time = clock.tick(fps) /1000.0
    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_color = random.choice(colors)
                while new_color == current_color:
                    new_color =random.choice(colors)
                current_color = new_color
    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -=speed * delta_time
    if keys[pygame.K_RIGHT]:
         circle_x += speed * delta_time
    if keys[pygame.K_UP]:
        circle_y -= speed * delta_time
    if keys[pygame.K_DOWN]:
        circle_y += speed * delta_time
    #대각선

    if keys[pygame.K_UP]and keys[pygame.K_RIGHT]:
         circle_y -=speed * delta_time
         circle_x += speed * delta_time

     

    if keys[pygame.K_LEFT]and keys[pygame.K_UP]:
        circle_y -=speed * delta_time
        circle_x -=speed * delta_time
    if keys[pygame.K_LEFT]and keys[pygame.K_DOWN]:
        circle_x -=speed * delta_time
        circle_y += speed * delta_time
    if keys[pygame.K_RIGHT]and keys[pygame.K_DOWN]:
        circle_x += speed * delta_time
        circle_y += speed * delta_time

    if keys[pygame.K_r]:
        circle_x = screen_width //2
        circle_y = screen_height //2


    #화면 경계체크
    if circle_x - circle_radius < 0:
        circle_x = circle_radius
    if circle_x + circle_radius > screen_width:
        circle_x = screen_width - circle_radius
    if circle_y - circle_radius < 0:
        circle_y = circle_radius
    if circle_y + circle_radius > screen_height:
        circle_y = screen_height - circle_radius

    #화면 그리기
    screen.fill((255,255,255))
    pygame.draw.circle(screen,current_color,(int(circle_x),int(circle_y)),circle_radius)
    #화면업데이트
    pygame.display.flip()
#파이게임 종료
pygame.quit()   