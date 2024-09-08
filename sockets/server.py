import socket

# Inicializa o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "0.0.0.0"
port = 8888

try:
    with open("shell.php", 'wb') as file:
        try:
            # Vincula o servidor ao IP e porta
            server.bind((ip, port))

            # Define o servidor para ouvir até 5 conexões simultâneas
            server.listen(5)
            print(f"Listening on {ip}:{port}")

            # Aceita a conexão do cliente
            client_socket, address = server.accept()
            with client_socket:
                print(f"Received connection from: {address[0]}")

                # Loop para receber dados do cliente
                while True:
                    data = client_socket.recv(1024)
                    
                    # Se não houver mais dados, encerra o loop
                    if not data:
                        print(f"Connection closed by {address[0]}")
                        break

                    # Escreve os dados recebidos no arquivo
                    file.write(data)

                print("Data has been written to shell.php.")

        except Exception as error:
            print(f"Server error: {error}")
finally:
    # Fecha o servidor
    server.close()
    print("Server closed.")
