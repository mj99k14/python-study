import pygame

#pygame 초기화
pygame.init()

#화면 설정
screen = pygame.display.set_mode((640, 480)) # 640 X 480 크기의 창을
pygame.display.set_caption("Rectangle collision Example")

#색상 정의
black = (0, 0, 0)
blue =(0 ,0, 255)
red = (255, 0, 0)

#사각형 초기화(x, y, width ,height)
rect1 = pygame.Rect(300, 220 ,60 ,60 )
rect2 = pygame.Rect(100, 100, 60, 60)
rect1_speed = [10, 10]
rect2_speed = [5,5]

#fps 설정
fps = 30
clock = pygame.time.Clock()

#게임 루프
running =True
while  running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창을 닫는 이벤트가 발생하면
            running =False# 루프 종료

    clock.tick(fps)

    #사각형 움직임
    rect1 = rect1.move(rect1_speed)
    rect2 = rect2.move(rect2_speed)

    #화면 경계에 충돌 처리
    if rect1.left < 0 or rect1.right > 640:
        rect1_speed[0] = -rect1_speed[0]
    if rect1.top < 0 or rect1.bottom > 480:
        rect1_speed[1] = -rect1_speed[1]
    if rect2.left < 0 or rect2.right > 640:
        rect2_speed[0] = -rect2_speed[0]
    if rect2.top < 0 or rect2.bottom > 480:
        rect2_speed[1] = -rect2_speed[1]


    if rect1.colliderect(rect2):
        print("Collision Detected!")

    #화면그리기
    screen.fill(black)
    pygame.draw.rect(screen, blue ,rect1)
    pygame.draw.rect(screen , red , rect2)
    pygame.display.flip()#화면 업데이트

pygame.quit()