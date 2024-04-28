import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = "192.168.0.20"
port = 8080


client.connect((dest, port))
message = client.recv(1024)
print(message.decode('ascii'))
#interact(client)
client.close()