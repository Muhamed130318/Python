import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = "192.168.45.202"
port = 4444

server.bind((dest, port))

server.listen(4)
print("server is listening to incoming connections.")

while True:
    conn, address = server.accept() #conn creates a socket for the connection, addres is address of client that is connecting
    print("connection received from %s" % str(address))
    message = conn.recv(1024) #conn is used to receive and send data, NOT the server socket created at the beginning
    print(message)
    conn.close() #We close conn when ending the connection, NOT the server socket, because we want to be able to receive other connections.