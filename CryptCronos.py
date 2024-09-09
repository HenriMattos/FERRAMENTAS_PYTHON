from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Inicializa o colorama

def gerar_chave_aes(bits=256):
    """Gera uma chave AES com o comprimento especificado em bits."""
    tamanho_chave = bits // 8
    return get_random_bytes(tamanho_chave)

def criptografar_arquivo_aes(arquivo_entrada, arquivo_saida, chave):
    cipher = AES.new(chave, AES.MODE_CBC)
    with open(arquivo_entrada, 'rb') as f:
        texto_plano = f.read()
    
    texto_cifrado = cipher.encrypt(pad(texto_plano, AES.block_size))
    with open(arquivo_saida, 'wb') as f:
        f.write(cipher.iv + texto_cifrado)  # Salva o IV junto com o texto cifrado

def descriptografar_arquivo_aes(arquivo_entrada, arquivo_saida, chave):
    with open(arquivo_entrada, 'rb') as f:
        iv = f.read(16)  # Extrai o IV
        texto_cifrado = f.read()

    cipher = AES.new(chave, AES.MODE_CBC, iv=iv)
    texto_plano = unpad(cipher.decrypt(texto_cifrado), AES.block_size)
    with open(arquivo_saida, 'wb') as f:
        f.write(texto_plano)

def gerar_pares_chaves_rsa():
    chave = RSA.generate(2048)
    chave_privada = chave.export_key()
    chave_publica = chave.publickey().export_key()
    with open('private.pem', 'wb') as f:
        f.write(chave_privada)
    with open('public.pem', 'wb') as f:
        f.write(chave_publica)

def criptografar_arquivo_rsa(arquivo_entrada, arquivo_saida, arquivo_chave_publica):
    with open(arquivo_chave_publica, 'rb') as f:
        chave_publica = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(chave_publica)
    with open(arquivo_entrada, 'rb') as f:
        texto_plano = f.read()
    texto_cifrado = cipher_rsa.encrypt(texto_plano)
    with open(arquivo_saida, 'wb') as f:
        f.write(texto_cifrado)

def descriptografar_arquivo_rsa(arquivo_entrada, arquivo_saida, arquivo_chave_privada):
    with open(arquivo_chave_privada, 'rb') as f:
        chave_privada = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(chave_privada)
    with open(arquivo_entrada, 'rb') as f:
        texto_cifrado = f.read()
    texto_plano = cipher_rsa.decrypt(texto_cifrado)
    with open(arquivo_saida, 'wb') as f:
        f.write(texto_plano)

def imprimir_menu():
    print(Fore.RED + Style.BRIGHT + "\nBem-vindo ao CryptCronos!")
    print(Fore.RED + Style.BRIGHT + "Opções:")
    print(Fore.YELLOW + "1. Criptografar Arquivo (AES)")
    print(Fore.YELLOW + "2. Descriptografar Arquivo (AES)")
    print(Fore.YELLOW + "3. Criptografar Arquivo (RSA)")
    print(Fore.YELLOW + "4. Descriptografar Arquivo (RSA)")
    print(Fore.YELLOW + "5. Info")
    print(Fore.RED + "q. Sair")

def obter_caminho_arquivo(prompt):
    caminho_arquivo = input(prompt)
    while not os.path.isfile(caminho_arquivo):
        print(Fore.RED + "Arquivo não encontrado. Por favor, tente novamente.")
        caminho_arquivo = input(prompt)
    return caminho_arquivo

def obter_caminho_chave(prompt):
    caminho_chave = input(prompt)
    while not os.path.isfile(caminho_chave):
        print(Fore.RED + "Arquivo da chave não encontrado. Por favor, tente novamente.")
        caminho_chave = input(prompt)
    return caminho_chave

def mostrar_info(opcao):
    if opcao == '1':
        print(Fore.GREEN + "\nCriptografar Arquivo (AES)")
        print("Esta opção criptografa um arquivo usando o algoritmo de criptografia AES.")
        print("Você precisará fornecer o caminho para o arquivo a ser criptografado e para salvar o arquivo criptografado.")
        print("A chave AES será gerada automaticamente e usada para criptografia.")
    elif opcao == '2':
        print(Fore.GREEN + "\nDescriptografar Arquivo (AES)")
        print("Esta opção descriptografa um arquivo criptografado usando o algoritmo de criptografia AES.")
        print("Você precisará fornecer o caminho para o arquivo criptografado, o caminho para salvar o arquivo descriptografado e o arquivo da chave.")
    elif opcao == '3':
        print(Fore.GREEN + "\nCriptografar Arquivo (RSA)")
        print("Esta opção criptografa um arquivo usando o algoritmo de criptografia RSA.")
        print("Você precisará fornecer o caminho para o arquivo a ser criptografado, o caminho para salvar o arquivo criptografado e o arquivo da chave pública RSA.")
    elif opcao == '4':
        print(Fore.GREEN + "\nDescriptografar Arquivo (RSA)")
        print("Esta opção descriptografa um arquivo criptografado usando o algoritmo de criptografia RSA.")
        print("Você precisará fornecer o caminho para o arquivo criptografado, o caminho para salvar o arquivo descriptografado e o arquivo da chave privada RSA.")
    else:
        print(Fore.RED + "Opção inválida.")

def main():
    print(Fore.RED + Style.BRIGHT + "Bem-vindo ao CryptCronos!")
    while True:
        imprimir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            print(Fore.YELLOW + "Criptografando arquivo com AES...")
            arquivo_entrada = obter_caminho_arquivo("Digite o nome do arquivo a ser criptografado: ")
            arquivo_saida = input("Digite o nome para salvar o arquivo criptografado: ")
            chave = gerar_chave_aes()
            criptografar_arquivo_aes(arquivo_entrada, arquivo_saida, chave)
            print(Fore.GREEN + "Arquivo criptografado com sucesso.")
        
        elif escolha == '2':
            print(Fore.YELLOW + "Descriptografando arquivo com AES...")
            arquivo_entrada = obter_caminho_arquivo("Digite o nome do arquivo a ser descriptografado: ")
            arquivo_saida = input("Digite o nome para salvar o arquivo descriptografado: ")
            arquivo_chave = obter_caminho_chave("Digite o nome do arquivo da chave: ")
            chave = open(arquivo_chave, 'rb').read()  # Lê a chave do arquivo
            descriptografar_arquivo_aes(arquivo_entrada, arquivo_saida, chave)
            print(Fore.GREEN + "Arquivo descriptografado com sucesso.")
        
        elif escolha == '3':
            print(Fore.YELLOW + "Criptografando arquivo com RSA...")
            arquivo_entrada = obter_caminho_arquivo("Digite o nome do arquivo a ser criptografado: ")
            arquivo_saida = input("Digite o nome para salvar o arquivo criptografado: ")
            arquivo_chave = obter_caminho_chave("Digite o nome do arquivo da chave pública: ")
            criptografar_arquivo_rsa(arquivo_entrada, arquivo_saida, arquivo_chave)
            print(Fore.GREEN + "Arquivo criptografado com sucesso.")
        
        elif escolha == '4':
            print(Fore.YELLOW + "Descriptografando arquivo com RSA...")
            arquivo_entrada = obter_caminho_arquivo("Digite o nome do arquivo a ser descriptografado: ")
            arquivo_saida = input("Digite o nome para salvar o arquivo descriptografado: ")
            arquivo_chave = obter_caminho_chave("Digite o nome do arquivo da chave privada: ")
            descriptografar_arquivo_rsa(arquivo_entrada, arquivo_saida, arquivo_chave)
            print(Fore.GREEN + "Arquivo descriptografado com sucesso.")
        
        elif escolha == '5':
            info_opcao = input("Digite o número da opção para obter informações (1-4): ")
            mostrar_info(info_opcao)
        
        elif escolha == 'q':
            print(Fore.RED + "Saindo...")
            break
        
        else:
            print(Fore.RED + "Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
