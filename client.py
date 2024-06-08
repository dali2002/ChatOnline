import socket
import threading


nickname = input("Choose your nickname: ")
server_ip = input("Enter your ip bjeh rabi")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

