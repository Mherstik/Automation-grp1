
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 52700))
while True:
    d2send = input("What to say: ")
    s.sendall(d2send.encode())
    data = s.recv(1024)
    print('Received', repr(data))
