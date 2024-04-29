import socket
import time

startTime = time.time()

def isPronic(i):
    for num in range(i):
        if num * (num + 1) == i:
            return True
    return False


targetIP = input("Which IP would you like to scan against: ")
print("Establishing connection to: ", targetIP)

for i in range(4000, 5000):
    if isPronic(i):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = scanner.connect_ex((targetIP, i))
        if conn == 0:
            print("Port %d: Pronic and OPEN." %(i))
        scanner.close()

endTime = time.time()

totalTime = endTime - startTime

print("Time taken: ", totalTime)




