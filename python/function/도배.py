import socket
import time

# 서버 정보
HOST = '172.28.16.94'  # 서버 IP 주소를 입력하세요
PORT = 5000       # 서버 포트를 입력하세요

# 메시지 설정
spam_message = "dpqpqfsdgs"  # 도배할 메시지
spam_count = 100                     # 보낼 메시지 수
delay = 2                      # 메시지 간 지연 시간 (초)

# 소켓 연결 설정
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))  # 서버에 연결
        print(f"Connected to server {HOST}:{PORT}")

        for i in range(spam_count):
            client_socket.sendall(spam_message.encode('utf-8'))  # 메시지 전송
            print(f"Sent: {spam_message} ({i + 1}/{spam_count})")
            time.sleep(delay)  # 지연 시간

        print("Spamming complete.")

except ConnectionRefusedError:
    print("Error: Unable to connect to the server. Check if the server is running and the HOST/PORT is correct.")
except Exception as e:
    print(f"An error occurred: {e}")
