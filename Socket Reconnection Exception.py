import socket

def recon(dest, p):
    for i in range(30):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((dest, p))
        message = client.recv(1024)
        client.close()
        print(message.decode('ascii'))

dest = "192.168.186.68"
port = 2001

try:
    for i in range(15):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((dest, port))
        message = client.recv(1024)
        client.close()
        print(message.decode('ascii'))
        if not message:
            raise ConnectionRefusedError

except ConnectionRefusedError:
    recon(dest, port)