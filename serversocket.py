import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.0.20"
port = 8080

server.bind((host, port)) #binds address and port to the server

server.listen(2) #wait for client connection, only 2 clients can connect to the server

print("Server is listening to incoming connections.") #prints this when run

while True:
    conn, address = server.accept() #established connection with client
    print("connection received from %s" %str(address) )
    message = "Connection established"
    conn.send(message.encode('ascii'))
    received = conn.recv(1024)
    print(received.decode())
    conn.close()