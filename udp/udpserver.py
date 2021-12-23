import cv2,imutils,socket
import numpy as py
import time
import base64

BUFF_SIZE = 65536

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_ip)
port = 9999
socket_address =(host_ip,port)
server_socket.bind(socket_address)
print('listening at',socket_address)

vid = cv2.VideoCapture('Gedamay.mp4')
fps,st,frames_to_count,cnt = (0,0,20,0)

while True:
    msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
    print('GOT connection from ',client_addr)
    WIDTH = 400
    while(vid.isOpened()):
        _,frame =vid.read()
        frame = imutils.resize(frame,width=WIDTH)
        encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
        message = base64.b64encode(buffer)
        server_socket.sendto(message,client_addr)
        cv2.imshow('TRANSMITING VIDEO',frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            server_socket.close()
            break

        