import socket

dest = "192.168.186.68"
port = 2002

for i in range(10):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((dest, port))
    while True:
        message = client.recv(1024)
        print(message)
        if not message:
            break
    client.close()

    