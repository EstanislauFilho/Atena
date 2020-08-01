# DataServer1.py

from threading import Thread
import socket
import time
import RPi.GPIO as GPIO

VERBOSE = True
IP_PORT = 22000
P_BUTTON = 3  # GPIO 2 pino 3

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP) # cfg GPIO 2 port com resistor de pull down (press = GND)

def debug(text):
    if VERBOSE:
        print ("Debug:---", text)

# ------------------------- classe SocketHandler -------------------------
class SocketHandler(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):
        global isConnected
        debug("SocketHandler started")
        while True:
            cmd = ""
            try:
                debug("Calling blocking conn.recv()")
                cmd = self.conn.recv(1024)
            except:
                debug("exception in conn.recv()") 
                # happens when connection is reset from the peer
                break
            debug("Received cmd: " + cmd + " len: " + str(len(cmd)))
            if len(cmd) == 0:
                break
            self.executeCommand(cmd)
        conn.close()
        print ("cliente desconectado, aguardando nova solicitação...")
        isConnected = False
        debug("SocketHandler terminated")

    def executeCommand(self, cmd):
        debug("Calling executeCommand() with  cmd: " + cmd)
        if cmd[:-1] == "go":  # remove trailing "\0"
            if GPIO.input(P_BUTTON) == GPIO.LOW:
                state = "push button ativo"
            else:
                state = "push button inativo"
            print ("estado atual:", state)
            self.conn.sendall(state + "\0")

# ------------------------- Servidor TCP -------------------------

setup()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket de servidor criado
# close port when process exits:
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
debug("Socket created")
HOSTNAME = "" # Symbolic name meaning all available interfaces

try:
    serverSocket.bind((HOSTNAME, IP_PORT)) # endereçamento no socket
except socket.error as msg:
    print ("Bind failed", msg[0], msg[1])
    sys.exit()
    
serverSocket.listen(1)	# servidor em modo passivo, aguardando solicitação do cliente

print ("aguardando cliente...")
isConnected = False
while True:
    debug("aceitar bloqueio de chamadas()...")
    conn, addr = serverSocket.accept()	# aceita a conexão com o cliente
    print ("conectado com o cliente em " + addr[0])
    isConnected = True
    socketHandler = SocketHandler(conn)
    
    socketHandler.setDaemon(True)  
    socketHandler.start()
    t = 0
    while isConnected:
        print ("servidor conectado em", t, "s") # se necessário aumentar a constante de tempo
        time.sleep(1)
        t += 1