import socket
#소켓생성(tcp or udp,ip주소 버전 :v4 or v6)
#TCP:socket.SOCK_STREAM
#UDP:socket.SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind(ip주소,port주소)
server_socket.bind(("127.0.0.1",5500))

#listen(큐의 개수)
server_socket.listen(5)

print(f"listen on 127.0.0.0.1:5500")

#accept(), ->사용자로 부터 연결 요청을 받았을떄 ->새로운 소켓 생성
#클라이언트 ->connect()
server_socket.accept()

print("hello~~")

