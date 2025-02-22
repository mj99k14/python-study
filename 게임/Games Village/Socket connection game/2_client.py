import socket
import pygame
import threading

# 네트워크 설정
SERVER_IP = "127.0.0.1"
PORT = 12345
BUFFER_SIZE = 1024

# Pygame 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UDP 먹이 먹기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# 플레이어 설정
player_rect = pygame.Rect(100, 100, 30, 30)
enemy_rect = pygame.Rect(200, 200, 30, 30)
player_score, enemy_score = 0, 0
velocity = 300
clock = pygame.time.Clock()

# UDP 소켓 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 서버 연결
client_socket.sendto("JOIN".encode(), (SERVER_IP, PORT))

def receive_data():
    """서버에서 받은 데이터를 갱신"""
    global enemy_rect, player_score, enemy_score, items

    while True:
        try:
            data, _ = client_socket.recvfrom(BUFFER_SIZE)
            p1_data, p2_data, scores, items_data = data.decode().split("|")
            
            p1_x, p1_y = map(int, p1_data.strip("()").split(","))
            p2_x, p2_y = map(int, p2_data.strip("()").split(","))
            player_score, enemy_score = map(int, scores.split(","))
            items = eval(items_data)

            enemy_rect.topleft = (p2_x, p2_y)

        except:
            break

# 데이터 수신 스레드 시작
threading.Thread(target=receive_data, daemon=True).start()

# 게임 실행
running = True
while running:
    dt = clock.tick(60) / 1000.0  # Delta Time 계산

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        player_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        player_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        player_rect.y += velocity * dt

    # 내 좌표를 서버에 전송
    client_socket.sendto(f"{player_rect.x},{player_rect.y}".encode(), (SERVER_IP, PORT))

    # 화면 그리기
    screen.fill(WHITE)

    # 아이템 그리기
    for item in items:
        pygame.draw.circle(screen, YELLOW, item, 10)

    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    pygame.display.flip()

pygame.quit()
client_socket.close()
