import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

while True:
    msg_len = s.recv(HEADERSIZE)
    msg_len = int(msg_len)
    msg = s.recv(msg_len)
    print(msg.decode("utf-8"))