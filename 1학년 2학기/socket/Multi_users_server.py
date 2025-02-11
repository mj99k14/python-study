import socket
import threading
HOST = "127.0.0.1 "
PROT = 12345

client_list = []                       #연결된 클라이언트목록
client_list_lock = threading.Lock()    #쓰레드  동기화를 위한 lock

def handler_client(client_socket:socket.socket,client_addr):
    try:
        while True:
            rcvd_msg = client_socket.recv(1024).decode('uft-8')

            if not rcvd_msg:          #클라이언트가 연결을 종료한 경우
                break
            rcvd_msg = f"{client_addr}:{rcvd_msg}"
            while client_list_lock:   #멀티스레드 환경에서 리스트 동기화
                for socket_item in client_list:
                    if socket_item != client_socket:
                        try:
                            socket_item.sendall(rcvd_msg.encode("utf-8"))
                        except:       #비정상 종료된 클라이언트 제거
                            client_list.remove(socket_item)
                            socket_item.close()
    except Exception as e:
        print(f"[ERROR] client {client_addr} error:{e}")
    

    finally:
        with client_list_lock:       #클라이언트 연결 종료시 목록에서 제거
            if client_socket in client_list:
                client_list.remove(client_socket)

        client_socket.close()
        print(f"client{client_addr} disconnected")


#서버 소켓생성 및 설정
server_socket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PROT))
server_socket.listen(5)

print(f"Server listening on{HOST}:{PROT}")

try:
    while True:
        print(f"Connected client: {len(client_list)}")

        client_socket, client_addr = server_socket.accept()
        print(f"Client connencted: {client_addr}")
        with client_list_lock:      #클라이언트 목록에 추가
            client_list.append(client_socket)
                                    #클라이언트 전용 스레드 실행
            client_thread =  threading.Thread(target=handler_client,args=(client_socket,client_addr),daemon=True)
            client_thread.start()
except KeyboardInterrupt:
    print("\n[INFO]server shutting down...")
finally:
    with client_list_lock:         # 서버 종료 시 모든 클라이언트 연결 종료
        for client_socket in client_list:
            client_socket.close()
    server_socket.close()
    print("[INFO] server closed")



