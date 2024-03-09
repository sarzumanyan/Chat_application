import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7976))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception as e:
            print("An error occurred:", e)
            client.close()
            break

def write():
    while True:
        try:
            message = f'{nickname}: {input("")}'
            client.send(message.encode('ascii'))
        except Exception as e:
            print("An error occurred:", e)
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()