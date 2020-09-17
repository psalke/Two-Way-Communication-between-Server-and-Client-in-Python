import socket
host='127.0.0.1'
port=9000
#server side
s=socket.socket()
s.connect((host,port))
str=input("Enter data: ")
while str!='exit':
    s.send(str.encode())
    data=c.recv(1024)
    data=data.decode()
    print("From server: "+data)
    str=input("Enter data: ")
c.close()  
