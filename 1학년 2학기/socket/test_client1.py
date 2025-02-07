import socket

HOST="127.0.0.1"
PORT =12345

#SOCKET생성
client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#CONNENT
client_socket.connect((HOST,PORT))

#사용자로 부터 데이터 입력
#blocking mode ->input
send_msg = input("input text: ")

#입력된 데이터를 서버로 전송
# sendall ->블락킹 
client_socket.sendall(send_msg.encode("utf-8"))

#서버로부터 수신한 데이터를 출력 
rcvd_msg = client_socket.recv(1024).decode('utf-8')

print(f"[Client_rcvd data]:{rcvd_msg}")


print("클라이언트 종료료")