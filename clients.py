#!/usr/bin/python

import socket

probe_port = 5000

servers = {
    1: {"name": "LEGOLAS", "ip": "10.0.1.1"},
    2: {"name": "FRODO", "ip": "10.0.2.2"},
    3: {"name": "SAM", "ip": "11.0.3.1"},
}

server_num = 1
tempo_maximo_espera = 10  # Tempo máximo de espera em segundos
flag = 0

# Solicita a quantidade de sondas que devem ser propagadas
probe_qtd = int(input("Digite a quantidade de sondas a propagar: "))

for key, server in servers.items():
    server_info = servers[server_num]
    server_name = server_info["name"]
    server_ip = server_info["ip"]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

    print(f"Conectado ao servidor {server_name} (ip:{server_ip}, porta:{probe_port}).")

    for i in range(probe_qtd):

        # Lógica para enviar uma sonda
        message = f"Sonda {server_name}, Número {i + 1}"
        client_socket.sendto(message.encode(), (server_ip, probe_port))

        # Lógica para receber a resposta do servidor com timeout
        client_socket.settimeout(tempo_maximo_espera)

        try:
            response, _ = client_socket.recvfrom(1024)
            print(f"Resposta do servidor {server_name}: {response.decode()}")
            flag = key
        except socket.timeout:
            print(f"Tempo limite de {tempo_maximo_espera} segundos atingido para o servidor {server_name}")
            break

    if(flag != 0):

        break

    server_num += 1

if(flag != 0):
    print(f"\n------ Iniciando o chat com o servidor {server_name} ------\n")

    server_info = servers[flag]
    server_name = server_info["name"]
    server_ip = server_info["ip"]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

    flag_begin_chat = "1"
    client_socket.sendto(flag_begin_chat.encode(), (server_ip, probe_port))

    while True:
        message = input("Insira a sua mensagem: ")
        client_socket.sendto(message.encode(), (server_ip, probe_port))

        response, _ = client_socket.recvfrom(1024)
        print(f"{response.decode()}")
              
else:
    print("Não foi encontrado nenhum servidor")
    client_socket.close()


client_socket.close()
