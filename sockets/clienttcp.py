import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = input("você: ") + "\n"
        client.sendto(message.encode(), ("127.0.0.1", 666))
        msg, friend = client.recvfrom(1024)
        print(f"{friend[0]}: {msg.decode()}")

except Exception as error:
    print("conexão falhou")
    print(error)

finally:
    client.close()
