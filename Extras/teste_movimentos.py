#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste MOvimentos

# --------------------------------------------------------


import RPi.GPIO as GPIO
import Configuracoes as definir
import Motores as motor
import Variaveis as var
import time


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

controle_velocidade_direita = GPIO.PWM(var.pin_ENA, 500)
controle_velocidade_direita.start(0)

controle_velocidade_esquerda = GPIO.PWM(var.pin_ENB, 500)
controle_velocidade_esquerda.start(0)

try:
	while (True):
		motor.movimento_frente(var.velNormal, controle_velocidade_direita, controle_velocidade_esquerda)
		time.sleep(3)	
		motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
		time.sleep(0.8)

		'''
		motor.movimento_direita(var.velReacao, controle_velocidade_direita, controle_velocidade_esquerda)
		time.sleep(2)	
		motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
		time.sleep(0.8)


		motor.movimento_esquerda(var.velReacao, controle_velocidade_direita, controle_velocidade_esquerda)
		time.sleep(2)	
		motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
		time.sleep(0.8)
		'''


		motor.movimento_tras(var.velNormal, controle_velocidade_direita, controle_velocidade_esquerda)
		time.sleep(3)
		motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
		time.sleep(0.8)
finally:
	print("Cleaning up")
	GPIO.cleanup()

