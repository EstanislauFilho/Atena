# -*- coding: utf-8 -*-

import socket
from random import *

# Seleciona e retorna o dado requisitado
def selecionaDado(dadoRequisitado):
    if(dadoRequisitado == "cor"):
        cores = ['branco', 'azul']
        idx = randint(0,1)
        cor = cores[idx]
        return cor

    elif(dadoRequisitado == "distancia"):
        distancia = randint(0.0, 29.0)
        return distancia

    elif(dadoRequisitado == "altura"):
        altura = randint(0.0, 5.0)
        return altura

    elif(dadoRequisitado == "mobilidade"):
        estados = ['movel', 'estatico']
        idx = randint(0,1)
        mobilidade = estados[idx]
        return mobilidade

HOST = ''              # Endereco IP do Servidor
PORT = 9101            # Porta que o Servidor esta
orig = (HOST, PORT)

# Criando o socket TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(orig)   # Enderecamento
tcp.listen(1)    # Modo Passivo de escuta

con, cliente = tcp.accept()	# inicio da conexão com cliente
print('Conectado pelo IP ' + str(cliente[0]) + ' através da porta ' + str(cliente[1]))

while True:
    solicitacaoCliente = con.recv(1024)
    if not solicitacaoCliente: break
    msgInput = con.recv(1024)
    print('Mensagem recebida ' + msgInput)
    parametroSolicitado = solicitacaoCliente.decode()
    print('Parametro solicitado ' + parametroSolicitado)
    parametroRetornado = selecionaDado(parametroSolicitado)
    print('Parametro retornado ' + str(parametroRetornado))
    parametroRetornadoStr = str(parametroRetornado)
    con.sendto(parametroRetornadoStr.encode(), ('192.168.0.102', 8000))

print('Finalizando conexao do cliente ', cliente)
con.close()