#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Configurações

# --------------------------------------------------------

import RPi.GPIO as GPIO
import Variaveis as var


def configuracoes():
	GPIO.setup(var.pin_ENA, GPIO.OUT)
	GPIO.setup(var.pin_IN1, GPIO.OUT)	
	GPIO.setup(var.pin_IN2, GPIO.OUT)

	GPIO.setup(var.pin_ENB, GPIO.OUT)
	GPIO.setup(var.pin_IN3, GPIO.OUT)	
	GPIO.setup(var.pin_IN4, GPIO.OUT)

	GPIO.setup(var.pin_BUZINA, GPIO.OUT)



