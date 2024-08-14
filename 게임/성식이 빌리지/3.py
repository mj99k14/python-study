import random
import pygame
import json
import os

pygame.init()

screen_width = 1280
screen_height = 720
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
b_width = b_rect.width
b_height = b_rect.height

count_e = 0

fall_rect_list = []

def geta():
    for _ in range(random.randint(6, 15)):
        while True:
            rect_x = random.randint(0, screen_width - fall_rect_width)
            rect = pygame.Rect(rect_x, 0, fall_rect_width, fall_rect_height)
            if rect.collidelist(fall_rect_list) == -1:
                fall_rect_list.append(rect)
                break

# 객체 이동 속도
speed = 100  # 300 pixel / second
s_speed = 200  # 성식이 스피드
count = 0

# 배경음악 파일 로드
background_music = pygame.mixer.music.load("tfile.mp3")
sound_fire = pygame.mixer.Sound("fire.mp3")
the_end = pygame.mixer.Sound("loser.mp3")
# 배경음악 무한 반복 재생 시작(-1은 무한 반복을 의미)
pygame.mixer.music.play(-1)

# 기록 파일 이름
record_file = "records.json"

# 기록 파일을 로드하는 함수
def load_records():
    if os.path.exists(record_file):
        with open(record_file, "r") as file:
            return json.load(file)
    return []

# 기록을 저장하는 함수
def save_records(records):
    with open(record_file, "w") as file:
        json.dump(records, file)

# 현재 게임의 기록을 추가하고 등수를 계산하는 함수
def add_record(elapsed_time):
    records = load_records()
    records.append(elapsed_time)
    records.sort()  # 시간 순으로 정렬 (작은 값이 높은 등수)
    save_records(records)
    return records.index(elapsed_time) + 1  # 0-based index이므로 1을 더해줌

# 사용자 정의 이벤트 생성
MY_EVENT = pygame.USEREVENT + 1


# 타이머 설정: 2초마다 MY_EVENT는 이벤트가 발생하도록 설정
pygame.time.set_timer(MY_EVENT, 3000)  # 2000밀리초(2초)마다 이벤트 발생

font = pygame.font.Font(None, 36)
start_time = pygame.time.get_ticks()

# 보너스 아이템 초기 위치 설정
b_rect.x = random.randint(0, screen_width - b_width)
b_rect.y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MY_EVENT:
            geta()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("음악 정지")
            elif event.key == pygame.K_p:
                pygame.mixer.music.play()
                print("음악 재생")
            elif event.key == pygame.K_i:
                pygame.mixer.music.play(fade_ms= 3000)
                print("음악 재생 - fade-in mode")
            elif event.key == pygame.K_o:
                pygame.mixer.music.fadeout(3000)
                print("음악 종료 -fade - out mode")
            elif event.key == pygame.K_u:
                current_vol = pygame.mixer.music.get_volume()
                current_vol += 0.1
                pygame.mixer.music.set_volume(current_vol)
                print(f"볼륨 증가:{current_vol}")
            elif event.key == pygame.K_d:
                current_vol = pygame.mixer.music.get_volume()
                current_vol = max(0.0, current_vol - 0.1)
                pygame.mixer.music.set_volume(current_vol)
                print(f"볼륨 감소: {current_vol}")

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, (0, 0, 0))
    b_text = font.render(f"count: {count_e}", True, (0, 0, 0))

    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        s_rect.x -= s_speed * dt
    if keys[pygame.K_RIGHT]:
        s_rect.x += s_speed * dt

    # 사각형의 y축 좌표 증가 (위에서 아래로 이동)
    for rect in fall_rect_list:
        rect.y += speed * dt
    
    # 보너스 아이템의 y축 좌표 증가
    b_rect.y += speed * dt

    # 보너스 아이템이 화면 아래로 벗어나면 다시 위에서 생성
    if b_rect.y > screen_height:
        b_rect.x = random.randint(0, screen_width - b_width)
        b_rect.y = 0

    # 성식이와 보너스 아이템 충돌 처리
    if b_rect.colliderect(s_rect):
        count_e += 1
        b_rect.x = random.randint(0, screen_width - b_width)
        b_rect.y = 0
        sound_fire.play()
              
    if s_rect.collidelist(fall_rect_list) != -1:
        the_end.play()
        pygame.time.wait(2000)  

        # 현재 게임 시간을 등수에 추가
        rank = add_record(elapsed_time)
        print(f"게임 종료! 당신의 등수는 {rank}위입니다.")
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
    screen.blit(b_text, (100, 100))
    screen.blit(b_i, b_rect)

    for rect in fall_rect_list:
        pygame.draw.rect(screen, (0, 0, 255), rect)

    pygame.display.flip()

pygame.quit()
