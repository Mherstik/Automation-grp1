'''
Name: Simple Socket Server
Description: Echo back the input the connection provided
Author: Marcus (+ ChatGPT)
Version: 0.1
Date: 20230329
'''
import socket 

## IP and PORT
HostIP= ''
Port = 52700

## create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Open port and listen
s.bind((HostIP,Port))
s.listen()
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
# reply back with what we heard
    while True:
        data = conn.recv(1024)
        #if not data: break
        if data == b'Hello, world':
             conn.sendall(b"Hello back")
        elif not data: break 
        else:
            conn.sendall(data)
        print("Received", data)
        #conn.sendall(data)
s.close()
print("Finished")
