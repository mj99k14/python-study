import socket
import threading

HOST = '127.0.0.1'
PROT = 12345

is_active = [True]

#소켓 생성 및서버연결
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PROT))

#전송 쓰레드
def handeler_tx(client_socket:socket.socket):
    while is_active[0]:
        send_msg = input("text: ")

        if send_msg.lower() == "exit":
            client_socket.close()
            is_active[0] = False
            break

        client_socket.sendall(send_msg.encode('utf-8'))


#수신 쓰레드
def handler_rx(client_socket:socket.socket):
    while is_active[0]:
        rcvd_msg = client_socket.recv(1024).decode('utf-8')

        if not rcvd_msg:
            break
        print(f"Received msg:{rcvd_msg}")
    is_active[0] = False

#멀티쓰레딩 송수신 동시처리
thread_tx = threading.Thread(target=handeler_tx,args=(client_socket,))
thread_rx = threading.Thread(target=handler_rx, args=(client_socket,))

#쓰레드 실행
thread_rx.start()
thread_tx.start()
#쓰레드 끝날떄까지 기다림
thread_tx.join()
thread_rx.join()