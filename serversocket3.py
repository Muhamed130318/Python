import socket

dest = socket.gethostname()
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((dest, port))

server.listen(20)
print("listening for connections")
while True:
    conn, address = server.accept()
    print("connection received from %s" %str(address))
    message = "connection established."
    conn.send(message.encode('ascii'))
    conn.close()