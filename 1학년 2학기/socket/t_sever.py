import socket
import threading

#서버 주소
HOST = '127.0.0.1'
PORT = 12345

is_active = [True]

#데이터 전송
def handler_tx(client_socket:socket.socket):
    while is_active[0]:
        send_msg = input("text: ")
        if send_msg.lower() == "exit":
            client_socket.close()
            is_active[0] = False
            break
        client_socket.sendall(send_msg.encode('uft-8'))

#데이터 수신
def handler_rx(client_socket:socket.socket):
    while is_active[0]:
        rcvd_msg = client_socket.recv(1024).decode('uft-8')

        if not rcvd_msg:
            break
        print(f"Received msg:{rcvd_msg}")
    is_active[0] = False
#SOCKET 생성
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind
server_socket.bind((HOST,PORT))
#listen
server_socket.listen(1)

print(f"[Listen] {HOST},{PORT}")

client_socket,client_add = server_socket.accept()
#멀티쓰레딩 송수신 동시처리
thread_tx = threading.Thread(target=handler_tx,args=(client_socket,))
thread_rx = threading.Thread(target=handler_rx,args=(client_socket,))
#쓰레드 실행
thread_rx.start()
thread_tx.start()
#쓰레드 기다림
thread_tx.join()
thread_rx.join()