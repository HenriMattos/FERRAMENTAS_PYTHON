import socket
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def criar_cliente_socket():
    """
    Cria e retorna um socket UDP para comunicação.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)  # timeout de 5 segundos
    return client

def enviar_mensagem(client, username, server_address):
    """
    Envia a mensagem do cliente para o servidor.
    """
    try:
        while True:
            message = Prompt.ask(f"[bold cyan]{username}[/bold cyan]")  # interface para entrada do usuário
            if not message.strip():
                console.print("[bold red]A mensagem não pode estar vazia![/bold red]")
                continue
            
            client.sendto(message.encode(), server_address)

            try:
                msg, friend = client.recvfrom(1024)
                console.print(f"[bold green]{friend[0]}[/bold green]: {msg.decode()}")
            except socket.timeout:
                console.print("[bold yellow]Servidor não respondeu dentro do tempo limite.[/bold yellow]")
    except ConnectionError:
        console.print("[bold red]Erro ao conectar ao servidor.[/bold red]")
    except TimeoutError:
        console.print("[bold red]Tempo limite de espera esgotado.[/bold red]")
    except ValueError:
        console.print("[bold red]Mensagem inválida.[/bold red]")
    except PermissionError:
        console.print("[bold red]Acesso não autorizado.[/bold red]")
    except Exception as error:
        console.print(f"[bold red]Erro inesperado: {error}[/bold red]")
    finally:
        client.close()

def main():
    username = input("Digite seu nome de usuário: ").strip()
    if not username:
        console.print("[bold red]O nome de usuário não pode estar vazio.[/bold red]")
        return

    server_address = ("127.0.0.1", 666)  # Endereço do servidor
    
    client = criar_cliente_socket()
    enviar_mensagem(client, username, server_address)

if __name__ == "__main__":
    main()
