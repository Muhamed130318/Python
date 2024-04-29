import socket

dest = "www.megacorpone.com"
destPort = 80

request = "GET / HTTP/1.1\r\nHost: www.megacorpone.com\r\n\r\n"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((dest, destPort))
client.send(request.encode())

response = client.recv(1024)
print(response.decode())