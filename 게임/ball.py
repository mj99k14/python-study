import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("벽돌꺠기")
#색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# 공 설정
ball_radius = 10
ball_speed = [5, -5]
ball = pygame.Rect(400, 300, ball_radius * 2, ball_radius * 2)
# 게임 속도 설정
clock = pygame.time.Clock()
fps = 60

# 초기 공 위치
ball = pygame.Rect(400, 300, ball_radius * 2, ball_radius * 2)

# 공 속도 (x 방향 속도, y 방향 속도)
ball_speed = [5, -5]

# 메인 루프
running = True
while running:
    dt = clock.tick(fps) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 공 이동 (현재 위치에 속도를 더해 새로운 위치를 계산)
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 충돌 처리 및 화면 업데이트 (생략된 부분)
    # 공과 벽 충돌
    if ball.left <= 0 or ball.right >= screen.get_width():
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()

pygame.quit()
