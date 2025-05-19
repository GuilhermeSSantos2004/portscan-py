from socket import socket, AF_INET, SOCK_STREAM, gaierror

def conectar(ip):

    top_ports = [20,21,22,23,25,53,67,68,69,80,110,111,123,135,137,138,139,143,161,162,443,445,500,514,520,631,993,995,1434,1723,1900,3306,3389,4500,5900,8080,49152]

    for port in top_ports:
        print(f'Escaneando porta {port}', end='\r')
        scanner = socket(AF_INET, SOCK_STREAM)
        scanner.settimeout(0.2)
        response = scanner.connect_ex((ip, port))
        if response == 0:
            print(f'Porta {port} aberta!')

try:
    ip = input('Digite o alvo (IP):\n> ') 
    conectar(ip)

except KeyboardInterrupt:
    print('Programa finalizado')
except gaierror:
    print('Erro: Não foi possível encontrar o host')
