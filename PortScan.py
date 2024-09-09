import socket
import threading
from queue import Queue
from rich.console import Console
from rich.progress import track

# Inicializa o console do Rich
console = Console()

# Fila para armazenar as portas que serão escaneadas
queue = Queue()

# Lista de portas abertas
open_ports = []

# Função para verificar portas
def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            console.print(f"[bold green]Port {port} is open[/bold green]")
        sock.close()
    except socket.error as err:
        console.print(f"[bold red]Error connecting to port {port}: {err}[/bold red]")

# Função para gerenciar o escaneamento
def threader():
    while not queue.empty():
        port = queue.get()
        port_scan(port)
        queue.task_done()

# Validação da entrada do alvo
while True:
    target = input("Enter the target IP address or domain: ")
    try:
        socket.gethostbyname(target)
        break
    except socket.error:
        console.print("[bold red]Invalid target. Please enter a valid IP address or domain.[/bold red]")

# Input de range de portas
while True:
    try:
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
        break
    except ValueError:
        console.print("[bold red]Please enter valid port numbers between 1 and 65535.[/bold red]")

# Preenche a fila de portas para escanear
for port in range(start_port, end_port + 1):
    queue.put(port)

console.print(f"[cyan]Starting scan on {target} from port {start_port} to {end_port}[/cyan]")

# Cria threads para o escaneamento
for i in track(range(100), description="Scanning ports..."):
    thread = threading.Thread(target=threader)
    thread.daemon = True
    thread.start()

queue.join()

# Resultados do escaneamento
if open_ports:
    console.print("\n[bold green]Scan completed. Open ports:[/bold green]")
    for port in open_ports:
        console.print(f" - [bold yellow]{port}[/bold yellow]")
else:
    console.print("\n[bold red]No open ports found.[/bold red]")
