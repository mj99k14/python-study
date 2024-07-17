import pygame
import random

pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movement and Click Example")

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 사각형 설정
rect_width, rect_height = 50, 50
rect = pygame.Rect(400, 300, rect_width, rect_height)
speed = 5

# 게임 루프 설정
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                random_x = random.randint(0, screen.get_width() - rect_width)
                random_y = random.randint(0, screen.get_height() - rect_height)
                rect.topleft = (random_x, random_y)

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.x -= speed
    if keys[pygame.K_RIGHT]:
        rect.x += speed
    if keys[pygame.K_UP]:
        rect.y -= speed
    if keys[pygame.K_DOWN]:
        rect.y += speed

    # 화면을 흰색으로 채움
    screen.fill(WHITE)
    
    # 검은색 사각형을 그리기
    pygame.draw.rect(screen, BLACK, rect)
    
    # 화면 업데이트
    pygame.display.flip()
    
    # 초당 60 프레임 설정
    clock.tick(60)

pygame.quit()
