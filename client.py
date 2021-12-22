import socket
import threading

nickname=input("please inter  a nickname")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5181))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "Nick?":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("error occurred")
            client.close()
            break

def write():
    while True:
        message = input('')
        if len(message) !=0:
            client.send(f"{nickname}:- {message}".encode('ascii'))
thread1= threading.Thread(target=receive)
thread1.start()

thread2= threading.Thread(target=write)
thread2.start()