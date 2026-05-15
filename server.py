import socket
s=socket.socket()
s.connect(('localhost',4000))
while True:
    ip=input("Enter logical Address : ")
    s.send(ip.encode())
    print("MAC Address",s.recv(1024).decode())
    