import socket
host='127.0.0.1'
port=9000
#server side
s=socket.socket()
s.bind((host,port))
s.listen(1)
#wait till the client connects
c,addr=s.accept()
print("A client connected")
while True:
    data=c.recv(1024)
    if not data:
        break
    print("From client: "+str(data.decode()))
    #enter response data from server
    data1=input("Enter response: ")
    c.send(data1.encode())
#close connection
c.close()    

    
