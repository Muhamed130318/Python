import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.186.61"
port = 2000

client.connect((host, port))

i = 0

while i <= 10:
    message = client.recv(1024)
    print(message.decode())
    client.send(message)
    i += 1

client.close()