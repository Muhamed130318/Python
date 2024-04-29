import socket
import time

startTime = time.time()

targetIP = input("which IP do you want to scan: ")
print("Initializing scan against ", targetIP)

for i in range(1000):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = scanner.connect_ex((targetIP, i))
    if (conn == 0):
        print("Port %d: OPEN" %(i))
    scanner.close()

endTime = time.time()

totalTime = endTime - startTime

print("Total time is: ", totalTime)