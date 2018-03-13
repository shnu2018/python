from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b"server data...", ("localhost", 8885))
data = s.recvfrom(4096)
print(data.decode("utf-8"))