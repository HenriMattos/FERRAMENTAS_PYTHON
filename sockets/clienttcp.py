import socket

username = input("Digite seu nome de usuário: ")

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = input(f"{username}: ") + "\n"
        client.sendto(message.encode(), ("127.0.0.1", 666)) #o localhost e a porta é só um exemplo.
        msg, friend = client.recvfrom(1024)
        print(f"{friend[0]}: {msg.decode()}")

except ConnectionError:
    print("Erro ao conectar ao servidor.")
except TimeoutError:
    print("Tempo limite de espera esgotado.")
except ValueError:
    print("Mensagem inválida.")
except PermissionError:
    print("Acesso não autorizado.")
except Exception as error:
    print("Erro inesperado:", error)

finally:
    client.close()

