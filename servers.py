#!/usr/bin/python

import socket

probe_port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", probe_port))
print(f"Servidor está escutando sondas na porta {probe_port}.")

# Lógica para receber sondas
while True:
    probe, address = server_socket.recvfrom(1024)
    print(f"Sonda recebida de {address}: {probe.decode()}")

    if (probe.decode() == "1"):
        break

    # Lógica para responder ao cliente
    response_message = "Sonda recebida com sucesso!"
    server_socket.sendto(response_message.encode(), address)

print(f"\n------ Iniciando o chat com o cliente {address} ------\n")

while True:
    reponse, address = server_socket.recvfrom(1024)
    print(f"{reponse.decode()}")

    message = input("Insira a sua mensagem: ")
    server_socket.sendto(message.encode(), address)

