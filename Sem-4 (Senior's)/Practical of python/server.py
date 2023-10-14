import socket
s = socket.socket(socket.AF_INET,
socket.SOCK_STREAM) 
localhost = "127.0.0.1" 
port = 80
s.bind((localhost, port))
s.listen(1)
print("Server is Ready Now :")
print("Waiting for Client :")
cc, address = s.accept() 
msg =''
while True: 
    in_data =cc.recv(1024) 
    msg =in_data.decode() 
    if msg== 'Bye':
        break   
    print("From Client:",msg) 
    out_data = input()
    cc.send(bytes(out_data, 'UTF-8'))
    print("!!! Connection Terminated !!!")