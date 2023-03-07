from socket import *

serverName = "localhost"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print("The server is ready to receive.")

while True:
    connectionSocket, addr = serverSocket.accept()

    data = connectionSocket.recv(1024).decode()
    
    file = open(data, "rt")
    
    characters = 0
    words = 0
    lines = 0

    for line in file:
        wordSplit = line.split()
        lines = lines + 1
        words = words + len(wordSplit)
        characters += sum(len(word) for word in wordSplit)

    message = "\nNumber of characters: " + characters + "\nNumber of words: " + words + "\nNumber of lines: " + lines

    connectionSocket.send(message.encode())
    connectionSocket.close()