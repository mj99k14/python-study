import socket
import threading
import time
import random

# 서버 설정
SERVER_IP = "127.0.0.1"
PORT = 12345
BUFFER_SIZE = 1024

# 게임 설정
WIDTH, HEIGHT = 800, 600
NUM_ITEMS = 10  # 아이템 개수

# UDP 소켓 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, PORT))

print(f"🎮 UDP 먹이 먹기 게임 서버 실행 중... {SERVER_IP}:{PORT}")

# 플레이어 데이터 저장
clients = {}
player_positions = {}
player_scores = {"P1": 0, "P2": 0}
items = [(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(NUM_ITEMS)]

start_time = None  # 게임 시작 시간

def game_loop():
    """서버에서 지속적으로 플레이어 상태를 업데이트하고 클라이언트에 전송"""
    global start_time

    while len(clients) < 2:  # 2명이 연결될 때까지 대기
        time.sleep(0.1)

    start_time = time.time()  # 게임 시작 시간 기록
    print("✅ 게임 시작!")

    while True:
        time.sleep(1 / 60)  # 60FPS로 상태 업데이트

        # 클라이언트에게 게임 상태 전송
        game_state = f"{player_positions.get('P1', (0, 0))},{player_positions.get('P2', (0, 0))}|{player_scores['P1']},{player_scores['P2']}|{items}"
        
        for addr in clients.keys():
            server_socket.sendto(game_state.encode(), addr)

        # 모든 아이템이 사라지면 게임 종료
        if not items:
            elapsed_time = time.time() - start_time
            print(f"🎉 게임 종료! 걸린 시간: {elapsed_time:.2f}초 🎉")
            break

def handle_clients():
    """클라이언트에서 위치 데이터를 받아와 업데이트"""
    global player_positions, items

    while True:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        if addr not in clients:
            if len(clients) == 0:
                clients[addr] = "P1"
            elif len(clients) == 1:
                clients[addr] = "P2"
            else:
                continue  # 최대 2명만 가능

        player_id = clients[addr]
        x, y = map(int, data.decode().split(","))
        player_positions[player_id] = (x, y)

        # 아이템 충돌 감지
        for item in items[:]:
            if abs(x - item[0]) < 20 and abs(y - item[1]) < 20:
                player_scores[player_id] += 1  # 점수 증가
                items.remove(item)  # 아이템 삭제

# 스레드 실행
threading.Thread(target=game_loop, daemon=True).start()
threading.Thread(target=handle_clients, daemon=True).start()

while True:
    time.sleep(1)  # 메인 스레드 유지
