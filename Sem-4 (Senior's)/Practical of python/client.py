import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
localhost = "127.0.0.1" 
port = 80
c.connect((localhost, port))
while True: 
    in_data = c.recv(1024)
    print("From Server :", in_data.decode())
    out_data = input()
    c.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'Bye':
        break
    c.close()