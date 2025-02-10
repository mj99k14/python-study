import socket
import threading

HOST='127.0.0.1'
PORT=12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

is_active = [True]
#데이터 전송
def handler_tx():
    while True:
        send_msg = input("TEXT: ")

        if send_msg.lower() =="exit":
            client_socket.close()
            is_active[0] = False
            break

        client_socket.sendall(send_msg.encode('utf-8'))



#데이터 수신
def handler_rx():
      while is_active[0]:
        rcvd_msg = client_socket.recv(1024).decode('utf-8')

        if not  rcvd_msg:
            break

        print(f"Received msg:{rcvd_msg}")
        


is_active[0] =False

thread_tx = threading.Thread(target=handler_tx)
thread_rx = threading.Thread(target=handler_rx)


thread_tx.start()
thread_rx.start()

thread_rx.join()
thread_tx.join()

print("hello")