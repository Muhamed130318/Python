import socket
import telnetlib

def interact(s):
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = socket.gethostname()
port = 8080


client.connect((dest, port))
message = client.recv(1024)
print(message.decode('ascii'))
interact(client)
client.close()