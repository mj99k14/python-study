import pygame
import random

pygame.init()

screen_width,screen_height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Collect Items Game")

WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
YELLOW = (255,255,0)
num_obs = 5
rect1_width = 200
rect1_height = 300
obs_width = 150
obs_height = 150
moving_width = 100
moving_height = 100
# 1. 사각형 1개 그리기


rect_list = []




# 2. 사각형 랜덤하게 화면에 그리기
while True:
    for _ in range(num_obs):
        rect_x = random.randint(0,screen_width - rect1_width)
        rect_y = random.randint(0,screen_height - rect1_height)
        rect1 =( rect_x,rect_y,rect1_width,rect1_height)
# 3. 랜덤하게 그리는데 경계를 벗어나지 않게 그리기

# 4. 경계를 벗어나지 않으면서 사각형 여러 개 그리기

# 5. 충돌이 일어나지 않게 사각형 그리기
# - 충돌이 일어나지 않으면 obs_list에 추가
    if rect1.collidelist(rect_list) != -1:
        rect_list.append(rect1)
    break

# - 충돌이 일어나면 다시 반복

# 6. 아이템 1개 그리기
obs_list = []
# 7. 아이템 랜덤하게 화면에 그리기
while True:
    for _ in range(num_obs):
        obs_x = random.randint(0, screen_width - obs_width)
        obs_y = random.randint(0,screen_height - obs_height)
        obs = (obs_x, obs_y, obs_width, obs_height)

# 8. 랜덤하게 그리는데 경계를 벗어나지 않게 그리기

# 9. 경계를 벗어나지 않으면서 사각형 여러 개 그리기

# 10. 아이템과 장애물에 충돌이 일어나지 않게 사각형 그리기
    if obs.collidelist(rect1) != -1:
        obs_list.append(obs)
    break
    
# - 충돌이 일어나지 않으면 item_list에 추가
# - 충돌이 일어나면 다시 반복
moving_list = []
# 11. moving_rect를 랜덤하게 1개 그리면서 경계를 벗어나지 않게 그리기
while True:
    m_x = random.randint(0, screen_width - moving_width )
    m_y = random.randint(0, screen_height - moving_height)
    moving_rect = (m_x , m_y ,moving_width, moving_height)
    if moving_rect.collidelist(obs_list) == -1 and moving_rect.collidelist(rect_list) == -1:
        break
velocity = 300
clock = pygame.time.Clock()
# 12. moving_rect가 장애물과 아이템과 충돌이 일어나지 않게 그리기
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    previous_position = moving_rect.topleft
    dt = clock.tick(60)/1000.0

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += velocity * dt

    if moving_rect.collidelist(rect_list) != -1 :
        print(f"{rect_list}충돌충돌발생")
        moving_rect.topleft = previous_position

    col = moving_rect.collidelist(obs_list) 
    if col != -1:
        del obs_list[col]
        print(f"남은 개수: {len(obs_list)} 입니다 ")


    if not obs_list:
        running = False
        screen.fill(255,255,255)
    
    for  s in rect_list:
        pygame.draw.

# 13. 움직이는 사각형과 장애물 간에 충돌이 있을 경우, 이전 좌표를 복원
# 키보드 입력 전 이전 좌표를 저장한 후, 움직이는 사각형과 장애물과 충돌이 일어났을 경우,
# 움직이는 사각형의 topleft의 좌표를 이전에 저장한 좌표로 복원한다.

# 14. 움직이는 사각형과 아이템 간의 충돌이 있을 경우, 해당 아이템을 리스트에서 삭제
# - 움직이는 사각형과 아이템 간에 충돌이 있는지 없는지 검사
# - 아이템을 없어지게 한다는 것은 아이템을 그려주지 않는다는 것을 의미 => 리스트에서 빼면 됨

# 15. 아이템 리스트가 없으면 프로그램 종료
# - if not item_list:
#    running = False
# --
    pygame.draw.rect(screen, RED, rect1)
    pygame.display.flip()

pygame.quit() 