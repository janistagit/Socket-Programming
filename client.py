from socket import *
import sys

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

file = sys.argv[1]

clientSocket.send(file.encode())
message = clientSocket.recv(1024)

print("From Server: ", message.decode())

file.close()
clientSocket.close()