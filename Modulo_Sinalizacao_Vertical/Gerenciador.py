#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Gerenciador

# --------------------------------------------------------

import cv2
import time
import numpy as np
import Pista as pista
import Variaveis as var
import Motores as motor
import RPi.GPIO as GPIO
import Sensores as sensor
import Sinalizacoes as sinalizacao


# ##################### FUNCAO PARA DEFINICAO DOS COMANDOS DO ROBO ##############################
def definicao_de_comandos(status_a0, status_a1, status_a2, status_a3, status_b0, status_b1, status_b2, status_b3, status_visao_faixa_dir, status_visao_faixa_esq, status_faixa_contencao_visao, status_obstaculo_vl53x):
	MOVIMENTO_FRENTE = False

	CORRECAO_MOTOR_DIR_VISAO = False
	CORRECAO_MOTOR_ESQ_VISAO = False

	DETECCAO_OBSTACULOS_VISAO = False

	FAIXA_CONTENCAO = False

	FAIXA_CONTENCAO_VISAO = False
	FAIXA_CONTENCAO_FOTO = False

	# Condicao para o robo ter movimento liberado
	if(
		  
		  (status_a3 is False) and
		  (status_b3 is False) and  
		  (status_visao_faixa_dir is False) and 
		  (status_visao_faixa_esq is False) and
		  (status_obstaculo_vl53x is False)
	  ):
		MOVIMENTO_FRENTE = True	
	 
	# Condicao para o robo fazer a correcao para a direita a partir da visao
	if(status_visao_faixa_dir is True):
		CORRECAO_MOTOR_DIR_VISAO = True

	# Condicao para o robo fazer a correcao para a esquerda a partir da visao
	if(status_visao_faixa_esq is True):
		CORRECAO_MOTOR_ESQ_VISAO = True

	if(((status_visao_faixa_dir is True) and (status_visao_faixa_esq is True)) or (status_faixa_contencao_visao is True)):	
		FAIXA_CONTENCAO_VISAO = True

	if(
			((status_a0 is True) and (status_b0 is True)) or 
			((status_a1 is True) and (status_b1 is True)) or 
			((status_a3 is True) and (status_b3 is True))  
	  ):
		FAIXA_CONTENCAO_FOTO = True


	COMANDOS = [
					MOVIMENTO_FRENTE,
					CORRECAO_MOTOR_DIR_VISAO,
					CORRECAO_MOTOR_ESQ_VISAO,
					DETECCAO_OBSTACULOS_VISAO,
					FAIXA_CONTENCAO_VISAO,
					FAIXA_CONTENCAO_FOTO
			   ]

	return COMANDOS

# ###############################################################################################



# ##################### FUNCAO PARA GERENCIAR MOVIMENTO E CORRECAO ##############################
def movimento_frente(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq):
	motor.movimento_frente(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq)

def correcao_motor_esq(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq):
	motor.movimento_direita(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq)

def correcao_motor_dir(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq):
	motor.movimento_esquerda(velocidade, ctr_vel_motor_dir, ctr_vel_motor_esq)

def interrupcao_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq):
	motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
# ###############################################################################################




def seta_para_direita():
	GPIO.output(var.pin_SETA_FRENTE_DIR, False)
	GPIO.output(var.pin_SETA_TRAS_DIR, False)
	GPIO.output(var.pin_SETA_TRAS_ESQ, False)
	GPIO.output(var.pin_SETA_FRENTE_ESQ, False)
	time.sleep(0.2)
	GPIO.output(var.pin_SETA_FRENTE_DIR, True)
	GPIO.output(var.pin_SETA_TRAS_DIR, True)
	GPIO.output(var.pin_SETA_TRAS_ESQ, False)
	GPIO.output(var.pin_SETA_FRENTE_ESQ, False)
	time.sleep(0.2)

	

def seta_para_esquerda():
	GPIO.output(var.pin_SETA_FRENTE_DIR, False)
	GPIO.output(var.pin_SETA_TRAS_DIR, False)
	GPIO.output(var.pin_SETA_TRAS_ESQ, True)
	GPIO.output(var.pin_SETA_FRENTE_ESQ, True)
	time.sleep(0.2)
	GPIO.output(var.pin_SETA_FRENTE_DIR, False)
	GPIO.output(var.pin_SETA_TRAS_DIR, False)
	GPIO.output(var.pin_SETA_TRAS_ESQ, False)
	GPIO.output(var.pin_SETA_FRENTE_ESQ, False)
	time.sleep(0.2)


def luz_de_freio():
	GPIO.output(var.pin_LUZ_FREIO_DIR, True)
	GPIO.output(var.pin_LUZ_FREIO_ESQ, True)
	GPIO.output(var.pin_SETA_FRENTE_ESQ, False)
	GPIO.output(var.pin_SETA_TRAS_ESQ, False)


def desliga_luzes():
	GPIO.output(var.pin_SETA_FRENTE_DIR, False)
	GPIO.output(var.pin_SETA_TRAS_DIR, False)
	GPIO.output(var.pin_SETA_TRAS_ESQ, False)
	GPIO.output(var.pin_SETA_FRENTE_ESQ, False)
	GPIO.output(var.pin_LUZ_FREIO_DIR, False)
	GPIO.output(var.pin_LUZ_FREIO_ESQ, False)
	time.sleep(0.2)


# ########################## FUNCAO PARA GERENCIAR ACAO PLACA PARE ##############################
def placa_pare(ctr_vel_motor_dir, ctr_vel_motor_esq):
	print()
# ###############################################################################################



# ###################### FUNCAO PARA GERENCIAR ACAO PLACA PEDESTRE ##############################
def placa_pedestre(ctr_vel_motor_dir, ctr_vel_motor_esq):
	print()
# ###############################################################################################


# ######################## FUNCAO PARA GERENCIAR ACAO PLACA DESVIO ##############################
def placa_desvio(ctr_vel_motor_dir, ctr_vel_motor_esq):
	print()
# ###############################################################################################





