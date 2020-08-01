#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import socket
HOST = ''              # Endereco IP do Servidor
PORT = 8000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket server criado
orig = (HOST, PORT)
tcp.bind(orig)	# endereçamento
tcp.listen(1)	# modo passivo
while True:
    con, cliente = tcp.accept()	# inicio da conexão com cliente
    print('Conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print (cliente, msg)
    print('Finalizando conexao do cliente', cliente)
    con.close()