#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Motores

# --------------------------------------------------------

import RPi.GPIO as GPIO
import Variaveis as var

def movimento_frente(velocidade, controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, True)
	GPIO.output(var.pin_IN2, False)
	controle_velocidade_direita.ChangeDutyCycle(velocidade)

	GPIO.output(var.pin_IN3, True)
	GPIO.output(var.pin_IN4, False)
	controle_velocidade_esquerda.ChangeDutyCycle(velocidade)


def movimento_tras(velocidade, controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, False)
	GPIO.output(var.pin_IN2, True)
	controle_velocidade_direita.ChangeDutyCycle(velocidade)

	GPIO.output(var.pin_IN3, False)
	GPIO.output(var.pin_IN4, True)
	controle_velocidade_esquerda.ChangeDutyCycle(velocidade)


def parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, False)
	GPIO.output(var.pin_IN2, False)
	controle_velocidade_direita.ChangeDutyCycle(0)

	GPIO.output(var.pin_IN3, False)
	GPIO.output(var.pin_IN4, False)
	controle_velocidade_esquerda.ChangeDutyCycle(0)


def movimento_direita(velocidade, controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, True)
	GPIO.output(var.pin_IN2, False)
	controle_velocidade_direita.ChangeDutyCycle((velocidade * var.CONST_CORREC_INV))

	GPIO.output(var.pin_IN3, False)
	GPIO.output(var.pin_IN4, True)
	controle_velocidade_esquerda.ChangeDutyCycle((velocidade * var.CONST_CORREC_REF))


def movimento_esquerda(velocidade, controle_velocidade_direita, controle_velocidade_esquerda):
	GPIO.output(var.pin_IN1, False)
	GPIO.output(var.pin_IN2, True)
	controle_velocidade_direita.ChangeDutyCycle((velocidade * var.CONST_CORREC_REF))
	GPIO.output(var.pin_IN3, True)
	GPIO.output(var.pin_IN4, False)
	controle_velocidade_esquerda.ChangeDutyCycle((velocidade * var.CONST_CORREC_INV))


