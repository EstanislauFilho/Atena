#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Main

# --------------------------------------------------------


import cv2
import time
import Motores as motor
import Variaveis as var
import RPi.GPIO as GPIO
import Sensores as sensor
import Configuracoes as definir


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

ctr_vel_motor_esq, ctr_vel_motor_dir = GPIO.PWM(var.pin_ENB, 500), GPIO.PWM(var.pin_ENA, 500)
ctr_vel_motor_esq.start(0)
ctr_vel_motor_dir.start(0)

time.sleep(1)


A0_ATIVADO, A1_ATIVADO, A3_ATIVADO = False, False, False

FAIXA_CONTENCAO = False

desligar = False


tempoCorrecao = 0

# 138 frames em 1 minuto
cont_frames = 0
obstaculo = False

try:
	while(True):

		a0, a1, _, a3, b0, b1, _, b3 = sensor.fototransistores()

		print("A0:{:>5} A1:{:>5} A2:{:>5} A3:{:>5} \tB0:{:>5} B1:{:>5} B2:{:>5} B3:{:>5}".format(a0, a1, _, a3, b0, b1, _, b3))

		
		if(((a0 <= var.CONST_A0) and (b0 <= var.CONST_B0)) or ((a1 <= var.CONST_A1) and (b1 <= var.CONST_B1)) or (a3 <= var.CONST_A3) and (b3 <= var.CONST_B3)):
			print("Chegou na faixa de contencao...")
			FAIXA_CONTENCAO = True
			while(FAIXA_CONTENCAO is True):	
				a0, a1, _, a3, b0, b1, _, b3  = sensor.fototransistores()
				print("Faixa de contenção \tA3:{:>5} B3:{:>5}".format(a0, a1, _, a3, b0, b1, _, b3))
				motor.movimento_frente(var.velCautela, ctr_vel_motor_dir, ctr_vel_motor_esq)

				if(((a0 >= var.CONST_A0) and (b0 >= var.CONST_B0)) and ((a1 >= var.CONST_A1) and (b1 >= var.CONST_B1)) and (a3 >= var.CONST_A3) and (b3 >= var.CONST_B3)):
					print("Saiu da faixa de contenção...")
					FAIXA_CONTENCAO = False
					#break

				
		# ---------- Metodo para fazer correcao de extrema emergencia (DIREITA) -----------
		elif((a3 <= var.CONST_A3) and (a0 >= var.CONST_A0) and (a1 >= var.CONST_A1) and (b3 >= var.CONST_B3) and (b0 >= var.CONST_B0) and (b1 >= var.CONST_B1)):
			A3_ATIVADO = True
			print("ALERTA MAXIMO!!! O robo esta saindo da faixa Direita... ")
			while(A3_ATIVADO is True):
				if(tempoCorrecao < 30):			
					a0, a1, _, a3, _, _, _, _ = sensor.fototransistores()
					motor.movimento_tras(var.velEmergencia, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if((a3 >= var.CONST_A3) and (a1 <= var.CONST_A1)):
						A3_ATIVADO = False
				else:
					print("Não foi possivel corrigir o percurso! Desligando por segurança...")
					desligar = True
					break
				print("Tempo para corrigir: {0}".format((30-tempoCorrecao))) 
				tempoCorrecao += 1
			tempoCorrecao = 0
		# -------------------------------------------------------------------------------			
		

		# ---------- Metodo para fazer correcao de extrema emergencia (ESQUERDA) -----------
		elif((b3 <= var.CONST_B3) and (b0 >= var.CONST_B0) and (b1 >= var.CONST_B1) and (a0 >= var.CONST_A0) and (a1 >= var.CONST_A1) and (a3 >= var.CONST_A3)):
			B3_ATIVADO = True
			print("ALERTA MAXIMO!!! O robo esta saindo da faixa Esquerda... ")
			while(B3_ATIVADO is True):
				if(tempoCorrecao < 30):		
					_, _, _, _, b0, b1, _, b3 = sensor.fototransistores()
					motor.movimento_tras(var.velEmergencia, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if((b3 >= var.CONST_B3) and (b1 <= var.CONST_B1)):
						B3_ATIVADO = False
				else:
					print("Não foi possivel corrigir o percurso! Desligando por segurança...")
					desligar = True
					break
				print("Tempo para corrigir: {0}".format((30-tempoCorrecao))) 
				tempoCorrecao += 1
			tempoCorrecao = 0
		# -------------------------------------------------------------------------------


		elif(desligar is True):
			break
		
		# --------------------------- Detccao faixa direita -----------------------------
		elif (a0 <= var.CONST_A0):
			while(a0 <= var.CONST_A0):
				print("Vira direita A0")
				a0, _, _, _, _, _, _, _ = sensor.fototransistores()
				motor.movimento_esquerda(var.velCorrecaoN2 , ctr_vel_motor_dir, ctr_vel_motor_esq)
				if(a0 >= var.CONST_A0): 
					break

		# Detccao faixa direita
		elif (a1 <= var.CONST_A1):
			while(a1 <= var.CONST_A1):
				print("Vira direita A1")
				_, a1, _, _, _, _, _, _ = sensor.fototransistores()
				motor.movimento_esquerda(var.velCorrecaoN1, ctr_vel_motor_dir, ctr_vel_motor_esq)
				if(a1 >= var.CONST_A1): 
					break
		# -------------------------------------------------------------------------------

		# -------------------------- Detccao faixa esquerda -----------------------------
		elif (b0 <= var.CONST_B0):
			while(b0 <= var.CONST_B0):
				print("Vira direita B0")
				_, _, _, _, b0, _, _, _ = sensor.fototransistores()
				motor.movimento_direita(var.velCorrecaoN2 , ctr_vel_motor_dir, ctr_vel_motor_esq)
				if(b0 >= var.CONST_B0): 
					break
		
		elif (b1 <= var.CONST_B1):
			while(b1 <= var.CONST_B1):
				print("Vira direita B1")
				_, _, _, _, _, b1, _, _ = sensor.fototransistores()
				motor.movimento_direita(var.velCorrecaoN1, ctr_vel_motor_dir, ctr_vel_motor_esq)
				if(b1 >= var.CONST_B1): 
					break


		else:
			# Seguir em frente
			motor.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)			


		# -------------------------------------------------------------------------------
		

		
		if cv2.waitKey(1) & 0xFF == 27:
			motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
			GPIO.cleanup()
			break
			
finally:
	print("bye bye...")	
	motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
	GPIO.cleanup()

