import pygame
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('몬스터 먹이주기 게임')

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# 배경 음악
background_music = pygame.mixer.music.load("C:/Users/USER/Desktop/pythonmj/python/tfile.mp3")
pygame.mixer.music.play(-1)

# 장애물 생성 함수
def create_obstacles(num_obstacles, size, screen_width, screen_height):
    obstacles = []
    for _ in range(num_obstacles):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size),
                               random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(o) for o in obstacles):
                obstacles.append(rect)
                break
    return obstacles

# 아이템 생성 함수
def create_items(num_items, size, screen_width, screen_height, obstacles):
    items = []
    for _ in range(num_items):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size),
                               random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(o) for o in obstacles) and \
               not any(rect.colliderect(i) for i in items):
                items.append(rect)
                break
    return items

# 장애물 및 아이템 생성
obstacles = create_obstacles(5, 50, screen_width, screen_height)
items = create_items(10, 20, screen_width, screen_height, obstacles)

# 이미지 불러오기 및 크기 조정
monster = pygame.image.load("C:/Users/USER/Desktop/pythonmj/python/sa.png")
monster = pygame.transform.scale(monster, (30, 30))
monster_rect = monster.get_rect()

monster_rect_width, monster_rect_height = monster_rect.width, monster_rect.height
print(f"화면 너비: {screen_width}, 몬스터 너비: {monster_rect_width}")

# 몬스터 랜덤 위치 설정
while True:
    random_x = random.randint(0, screen_width - monster_rect_width)
    random_y = random.randint(0, screen_height - monster_rect_height)
    temp_rect = pygame.Rect(random_x, random_y, monster_rect_width, monster_rect_height)

    # 장애물 및 아이템과 겹치지 않는 위치 찾기
    if temp_rect.collidelist(obstacles) == -1 and temp_rect.collidelist(items) == -1:
        monster_rect.topleft = (random_x, random_y)
        break

# 이동 속도 설정
velocity = 300

# FPS 제어를 위한 clock 객체 생성
clock = pygame.time.Clock()

# 폰트 설정
font = pygame.font.Font(None, 36)  # 기본 폰트 크기 36
start_time = pygame.time.get_ticks()  # 게임 시작 시간 기록

# 게임 시작
running = True
scale_factor = 1.0  # 이미지 크기 증가율

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    previous_position = monster_rect.topleft
    dt = clock.tick(60) / 1000.0  # Delta Time 계산 (초 단위)

    # 키 입력에 따른 이동 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        monster_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        monster_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        monster_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        monster_rect.y += velocity * dt

    # 장애물 충돌 처리
    collision_index = monster_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"장애물 {collision_index}와 충돌! 몬스터가 아파요!!")
        monster_rect.topleft = previous_position
        screen.fill(BLUE)
        pygame.display.flip()
        running = False

    # 아이템 충돌 처리
    item_index = monster_rect.collidelist(items)
    if item_index != -1:
        print(f"몬스터터 먹이 나머지: {len(items) - 1}")
        del items[item_index]
        scale_factor += 0.1  # 크기 증가

        # 이미지 크기 증가
        monster = pygame.transform.scale(monster,
                                         (int(monster_rect_width * scale_factor),
                                          int(monster_rect_height * scale_factor)))
        monster_rect = monster.get_rect(center=monster_rect.center)

    # 모든 아이템을 다 먹었을 때
    if not items:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # 초 단위 변환
        print(f"🎉 몬스터터 다 먹음! 걸린 시간: {elapsed_time:.2f}초 🎉")
        running = False

    # 화면 업데이트
    screen.fill(WHITE)

    # 장애물 그리기
    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, obs)

    # 아이템 그리기
    for item in items:
        pygame.draw.rect(screen, YELLOW, item)

    # 몬스터 그리기
    screen.blit(monster, monster_rect)

    # ⏳ **타이머 표시 (오른쪽 상단)**
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # 초 단위 변환
    timer_text = font.render(f"Time: {elapsed_time:.2f}s", True, RED)
    screen.blit(timer_text, (screen_width - 150, 10))  # 오른쪽 상단에 표시

    pygame.display.flip()

pygame.quit()
