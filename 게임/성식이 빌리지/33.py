import random
import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("하늘에서 성식이가 내려와요")

clock = pygame.time.Clock()
running = True

# 게임 변수
fall_rect_width = 25
fall_rect_height = 25

# 움직이는 성식이
s_i = pygame.image.load("ss.png")
s_rect = s_i.get_rect()
s_rect.topleft = (screen_width // 2 - s_rect.width, screen_height - s_rect.height)

# 보너스 아이템
b_i = pygame.image.load("s.png")
b_rect = b_i.get_rect()
b_width = 20
b_height = 20
b_rect.x= (random.randint(0, screen_width - b_width))
count_e = 0

# 떨어지는 사각형 -> 3개
fall_rect_list = []

def get():
    
    for _ in range(random.randint(4, 9)):
        while True:
            rect_x = random.randint(0, screen_width - fall_rect_width)  # 0 <= x <= 720
            rect = pygame.Rect(rect_x, 0, fall_rect_width, fall_rect_height)
            
            # 충돌이 발생하지 않았을 경우
            if rect.collidelist(fall_rect_list) == -1:
                # 사각형을 리스트에 추가
                fall_rect_list.append(rect)
                break

# 객체 이동 속도
speed = 100  # 300 pixel / second
s_speed = 150  # 성식이 스피드
count = 0

# 사용자 정의 이벤트 생성
MY_EVENT = pygame.USEREVENT + 1

# 타이머 설정: 2초마다 MY_EVENT는 이벤트가 발생하도록 설정
pygame.time.set_timer(MY_EVENT, 2000)  # 2000밀리초(2초)마다 이벤트 발생

font = pygame.font.Font(None, 36)
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MY_EVENT:
            get()
            # 보너스 아이템의 위치를 무작위로 변경
            b_rect.x = random.randint(0, screen_width - b_width)
            b_rect.y = 0

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, (0, 0, 0))
    b_text = font.render(f"뽀너스:{count_e}",True,(0,0,0))

    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        s_rect.x -= s_speed * dt
    if keys[pygame.K_RIGHT]:
        s_rect.x += s_speed * dt

    # 사각형의 y축 좌표 증가 (위에서 아래로 이동)
    for rect in fall_rect_list:
        rect.y += speed * dt
    
    for s in range(random.randint(1,3)):
        b_rect.y += speed * dt

    if b_rect.colliderect(s_rect) == True:
        count_e += 1
        b_rect.x = -100
         

    if s_rect.collidelist(fall_rect_list) != -1:
        running = False

    count += 1
    if count % 3 == 0:
        speed += 2
    
    s_speed = 300 + count_e * 50

    # 경계 처리
    s_rect.x = max(0, min(s_rect.x, screen_width - s_rect.width))
    s_rect.y = max(0, min(s_rect.y, screen_height - s_rect.height))

    # 화면 그리기
    screen.fill((255, 255, 255))
    screen.blit(s_i, s_rect)
    screen.blit(timer_text, (10, 10))
    screen.blit(b_text,(100,100))
    screen.blit(b_i, b_rect)

    for rect in fall_rect_list:
        pygame.draw.rect(screen, (0, 0, 255), rect)

    pygame.display.flip()

pygame.quit()
