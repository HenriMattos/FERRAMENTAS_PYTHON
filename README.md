Scanner de Portas em Python

Descrição:

Este script Python verifica um host especificado (endereço IP ou nome de domínio) em busca de portas abertas em um intervalo de 10 portas definidas pelo usuário. Ele utiliza programação de socket e o método connect_ex para verificar a disponibilidade da porta de forma eficiente.

Instalação:

Nenhuma instalação é necessária. Você pode salvar o script como um arquivo Python (por exemplo, port_scanner.py) e executá-lo diretamente.

Uso:

Salve o script como um arquivo Python.
Execute o script do seu terminal: python port_scanner.py
Digite o endereço IP ou nome de domínio do host de destino quando solicitado.
Digite os números das portas desejadas, um por linha, para um máximo de 10 portas. O script irá escanear essas portas sequencialmente.

Exemplo de Saída:

Digite o IP ou endereço: 192.168.1.100
Digite a porta: 22
22 -> Porta aberta
Digite a porta: 80
80 -> Porta aberta
Digite a porta: 443
443 -> Porta aberta
Digite a porta: 135
135 -> Porta aberta
Digite a porta: 445
445 -> Porta aberta
Digite a porta: 3389
3389 -> Porta fechada
Digite a porta: 8080
8080 -> Porta fechada
Digite a porta: 5900
5900 -> Porta fechada
Digite a porta: 21
21 -> Porta aberta
Scan Finalizado
