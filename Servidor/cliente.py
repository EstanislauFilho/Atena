import socket


HOST = '192.168.0.2'     # Endereco IP do Servidor
PORT = 8000           # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')

msg = input()

while msg != '\x18':
	#tcp.send (msg)
	tcp.sendto(msg.encode(),(HOST, PORT))
	msg = input()
tcp.close()