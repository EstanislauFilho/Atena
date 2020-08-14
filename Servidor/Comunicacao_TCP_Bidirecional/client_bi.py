# -*- coding: utf-8 -*-
import socket

# Tamanho dos bytes a receber
lenBytes = 1024

# Criação do socket TCP
destino = ('192.168.0.102', 9101)
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect(destino)

opcao = 1

while int(opcao) == 1:
    print('Qual parametro deseja solicitar?')
    print('0 - Cor')
    print('1 - Distancia')
    print('2 - Altura')
    print('3 - Mobilidade')

    idxRequisicao = input()

    # Exemplo de parâmetros a solicitar
    requisicoes = ['cor', 'distancia', 'altura', 'mobilidade']

    # Enviando a requisição
    envioRequisicao = tcpClient.sendto(requisicoes[int(idxRequisicao)].encode(), destino)

    # Mensagem enviada para fins de testagem
    msg = input('Digite aqui a mensagem para enviar ao servidor: ')
    tcpClient.sendto(msg.encode(),(destino))

    # Recebendo dados do servidor
    dadosRecebidos = tcpClient.recv(lenBytes)

    # Print the quote
    print('Os dados recebidos foram: ' + str(dadosRecebidos.decode()))

    print('Deseja se manter conectado no servidor? 1 - Sim   0 - Não')
    opcao = input()

tcpClient.close()