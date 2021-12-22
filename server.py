import socket
import threading

host = '127.0.0.1'
port = 5181

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients   = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(clients)
            clients.remove(index)
            client.close()
            broadcast(f"{nicknames[index]} left the chat".encode('ascii'))
            nicknames.remove(index)
            break

def receive():
    while True:
        client , address = server.accept()
        print(f'client with address {address} has been connected')
        client.send("Nick?".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        clients.append(client)
        nicknames.append(nicknames)
        print(f"nickname of the client is {nickname}")
        broadcast(f"{nickname} has been connected".encode("ascii"))
        client.send("connected to the server".encode("ascii"))
        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print("server is running at",host ,port )
receive()