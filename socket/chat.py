import socket
import threading

def receive_messages(client_socket):
    """서버로부터 메시지를 수신"""
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
    except:
        print("서버 연결 끊김.")
    finally:
        client_socket.close()

def run_client():
    host = '210.101.236.192'  # 서버 주소
    port = 8500        # 서버 포트

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # 닉네임 입력
    nickname = input("사용할 닉네임을 입력하세요: ")
    client_socket.send(nickname.encode('utf-8'))

    # 수신용 스레드 시작
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    print("채팅에 연결되었습니다. 메시지를 입력하세요. 종료하려면 'exit' 입력.")
    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                print("채팅을 종료합니다.")
                break
            client_socket.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        print("\n채팅 종료.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()
