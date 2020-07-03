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
import Tratamento as trata
from picamera import PiCamera
import Interface as interface
import Gerenciador as gerencia
import Configuracoes as definir
from picamera.array import PiRGBArray


frames = PiCamera()
frames.framerate = var.taxa_quadros
frames.resolution = (var.tam_original_tela_x, var.tam_original_tela_y)
capturaFrames = PiRGBArray(frames, size=(var.tam_original_tela_x, var.tam_original_tela_y))

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

ctr_vel_motor_esq, ctr_vel_motor_dir = GPIO.PWM(var.pin_ENB, 500), GPIO.PWM(var.pin_ENA, 500)
ctr_vel_motor_esq.start(0)
ctr_vel_motor_dir.start(0)

time.sleep(1)

CORRECAO_NIVEL_1, CORRECAO_NIVEL_2, CORRECAO_NIVEL_3 = False, False, False

inicializacao = False
autorizado = False



# 138 frames em 1 minuto
cont_frames = 0
tempoDeteccao = 1


try:
	for frame in frames.capture_continuous(capturaFrames, format="bgr", use_video_port=True):

		

		# --------------------------- Obtencao valores sensores --------------------------
		# Obtendo quadros capturados pela camera
		imagem = frame.array

		# Obtendo valores brutos dos fototransistores
		a0, a1, a2, a3, b0, b1, b2, b3 = sensor.fototransistores()

		# Obtendo valores brutos sensor de obstaculo 
		#distancia_obstaculo = sensor.vl530x()	
		# --------------------------------------------------------------------------------


		# --------------------------- Definindo Imagens Filhas ---------------------------
		imagem_pista = imagem.copy()
	
		
		# --------------------- Obtentendo Respostas dos Tratamentos ---------------------
		# Deteccao das faixas na pista
		(
			imagem_perspectiva_pista,
			imagem_faixa_esq, 
   			imagem_faixa_dir,
			status_visao_faixa_dir, 
			status_visao_faixa_esq,
			status_faixa_contencao_visao
		) = trata.deteccao_faixas_visao(imagem_pista)
		# --------------------------------------------------------------------------------
		

		(
			status_a0, 
			status_a1, 
			status_a2, 
			status_a3, 
			status_b0, 
			status_b1, 
			status_b2, 
			status_b3
		) = trata.deteccao_faixas_fototransistores(a0, a1, a2, a3, b0, b1, b2, b3)
		# --------------------------------------------------------------------------------
		
		

		
		status_obstaculo_vl53x = False

		# ----------------------------- DEFININDO COMANDOS ------------------------------
		(
			MOVIMENTO_FRENTE,
			CORRECAO_MOTOR_DIR_VISAO,
			CORRECAO_MOTOR_ESQ_VISAO,
			DETECCAO_OBSTACULOS_VISAO,
			FAIXA_CONTENCAO_VISAO,
			FAIXA_CONTENCAO_FOTO
		) = gerencia.definicao_de_comandos(status_a0, status_a1, status_a2, status_a3, status_b0, status_b1, status_b2, status_b3, status_visao_faixa_dir, status_visao_faixa_esq, status_faixa_contencao_visao, status_obstaculo_vl53x)
		# -------------------------------------------------------------------------------

	
		if(FAIXA_CONTENCAO_VISAO is True):
			print("Faixa de pedestre a frente...")
			CORRECAO_MOTOR_DIR_VISAO = False	
			CORRECAO_MOTOR_ESQ_VISAO = False	
			DETECTAR_FAIXA_PEDESTRE = True
			while(DETECTAR_FAIXA_PEDESTRE is True):
				a0, a1, _, a3, b0, b1, _, b3 = sensor.fototransistores() 
				gerencia.movimento_frente(var.velCautela, ctr_vel_motor_dir, ctr_vel_motor_esq)
				if(((a0 <= var.CONST_A0) and (b0 <= var.CONST_B0)) or ((a1 <= var.CONST_A1) and (b1 <= var.CONST_B1)) or (a3 <= var.CONST_A3) and (b3 <= var.CONST_B3)):
					FAIXA_CONTENCAO_FOTO = True						
					DETECTAR_FAIXA_PEDESTRE = False	
		


		if(FAIXA_CONTENCAO_FOTO is True):		
			print("Chegou na Faixa de pedestre! Verificando presença de pedestre...")
			if(status_obstaculo_vl53x is True):
				print("Pedestres identificados! Aguarde liberação da via...")
				INDENTIFICADO_OBSTACULO = True
				while(INDENTIFICADO_OBSTACULO is True):
					status_obstaculo_vl53x = True
					gerencia.interrupcao_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
			else:
				print("Sem pedestres na faixa! Prosseguir ate sair da faixa...")
				DETECTOU_FAIXA_PEDESTRE = True
				while(DETECTOU_FAIXA_PEDESTRE is True):
					a0, a1, _, a3, b0, b1, _, b3 = sensor.fototransistores() 
					gerencia.movimento_frente(var.velCautela, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(((a0 >= var.CONST_A0) and (b0 >= var.CONST_B0)) and ((a1 >= var.CONST_A1) and (b1 >= var.CONST_B1)) and (a3 >= var.CONST_A3) and (b3 >= var.CONST_B3)):
						DETECTOU_FAIXA_PEDESTRE = False			
				print("Saiu da Faixa de pedestre! Prosseguir percurso...")
				

		
		# ------------------ *** Condicionais De Movimentacao *** -----------------------
		
		# ------------------ Seguir em frente ou manter robô parado  -------------------- 	
		if(MOVIMENTO_FRENTE is True):
			print("Seguindo em frente...")
			gerencia.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)					
		# -------------------------------------------------------------------------------

		# ---------------- Correcao do motor da direita com Visao Comp  -----------------
		elif (CORRECAO_MOTOR_DIR_VISAO is True):
			while(CORRECAO_MOTOR_DIR_VISAO is True):
				a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores() 
				if (status_a0 is True):
					CORRECAO_NIVEL_2 = True
					while(CORRECAO_NIVEL_2 is True):
						print("Virar Esquerda A0")
						a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores() 
						motor.movimento_esquerda(var.velCorrecaoN2, ctr_vel_motor_dir, ctr_vel_motor_esq)
						if(((a0 >= var.CONST_A0) and (a1 >= var.CONST_A1))  or (b0 <= var.CONST_B0) or (b1 <= var.CONST_B1)): 
							CORRECAO_NIVEL_2 = False
					status_a0 is False

				if (status_a1 is True):
					CORRECAO_NIVEL_1 = True
					while(CORRECAO_NIVEL_1 is True):
						print("Virar Esquerda A1")
						a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores() 
						motor.movimento_esquerda(var.velCorrecaoN1, ctr_vel_motor_dir, ctr_vel_motor_esq)
						if(((a0 >= var.CONST_A0) and (a1 >= var.CONST_A1))  or (b0 <= var.CONST_B0) or (b1 <= var.CONST_B1)): 
							CORRECAO_NIVEL_1 = False
					status_a1 is False

				if (status_b0 is True) or (status_b1 is True):
					break

							
				print("Virar Esquerda com Visao") 
				gerencia.correcao_motor_dir(var.velVisao, ctr_vel_motor_dir, ctr_vel_motor_esq)
				CORRECAO_MOTOR_DIR_VISAO = False
				if((CORRECAO_MOTOR_DIR_VISAO is True) or (b0 <= var.CONST_B0 or b1 <= var.CONST_B1)):
					CORRECAO_MOTOR_DIR_VISAO = True
			
		# -------------------------------------------------------------------------------


		# --------------- Correcao do motor da esquerda com Visao Comp  ----------------- 
		elif (CORRECAO_MOTOR_ESQ_VISAO is True):
			while(CORRECAO_MOTOR_ESQ_VISAO is True):
				a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores() 
				if (status_b0 is True):
					CORRECAO_NIVEL_2 = True
					while(CORRECAO_NIVEL_2 is True):
						print("Virar Direita B0")
						a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores()  
						motor.movimento_direita(var.velCorrecaoN2, ctr_vel_motor_dir, ctr_vel_motor_esq)
						if(((b0 >= var.CONST_B0) and (b1 >= var.CONST_B1)) or (a0 <= var.CONST_A0) or (a1<= var.CONST_A1)): 
							CORRECAO_NIVEL_2 = False
					status_b0 is False

				if (status_b1 is True):
					CORRECAO_NIVEL_1 = True	
					while(CORRECAO_NIVEL_1 is True):
						print("Virar Direita B1")
						a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores()  
						motor.movimento_direita(var.velCorrecaoN1, ctr_vel_motor_dir, ctr_vel_motor_esq)
						if(((b0 >= var.CONST_B0) and (b1 >= var.CONST_B1)) or (a0 <= var.CONST_A0) or (a1<= var.CONST_A1)): 
							CORRECAO_NIVEL_1 = False
					status_b1 is False

				if (status_a0 is True) or (status_a1 is True):
					break


				print("Virar Direita com Visao")
				gerencia.correcao_motor_esq(var.velVisao, ctr_vel_motor_dir, ctr_vel_motor_esq)
				CORRECAO_MOTOR_ESQ_VISAO = False
				if(CORRECAO_MOTOR_ESQ_VISAO is True or ((a0 <= var.CONST_A0 or a1 <= var.CONST_A1))):
					CORRECAO_MOTOR_ESQ_VISAO = True
		# -------------------------------------------------------------------------------


		# ---------- Metodo para fazer correcao de extrema emergencia (DIREITA) -----------
		elif((a3 <= var.CONST_A3) and (a0 >= var.CONST_A0) and (a1 >= var.CONST_A1) and (b3 >= var.CONST_B3) and (b0 >= var.CONST_B0) and (b1 >= var.CONST_B1)):
			A3_ATIVADO = True
			print("ALERTA MAXIMO!!! O robo esta saindo da faixa Direita... ")
			while(A3_ATIVADO is True):		
				a0, a1, _, a3, _, _, _, _ = sensor.fototransistores()
				motor.movimento_tras(var.velEmergencia, ctr_vel_motor_dir, ctr_vel_motor_esq)
				if((a3 >= var.CONST_A3) and (a1 <= var.CONST_A1)):
					print("Correcao estabelecida!")	 
					A3_ATIVADO = False
		# -------------------------------------------------------------------------------			
		

		# ---------- Metodo para fazer correcao de extrema emergencia (ESQUERDA) -----------
		elif((b3 <= var.CONST_B3) and (b0 >= var.CONST_B0) and (b1 >= var.CONST_B1) and (a0 >= var.CONST_A0) and (a1 >= var.CONST_A1) and (a3 >= var.CONST_A3)):
			B3_ATIVADO = True
			print("ALERTA MAXIMO!!! O robo esta saindo da faixa Esquerda... ")
			while(B3_ATIVADO is True):		
				_, _, _, _, b0, b1, _, b3 = sensor.fototransistores()
				motor.movimento_tras(var.velEmergencia, ctr_vel_motor_dir, ctr_vel_motor_esq)
				if((b3 >= var.CONST_B3) and (b1 <= var.CONST_B1)):
					print("Correcao estabelecida!")	 
					B3_ATIVADO = False
		# -------------------------------------------------------------------------------



		elif((a0 <= var.CONST_A3) or (a1 <= var.CONST_A1) and (a3 >= var.CONST_A1) and (b0 >= var.CONST_B0) and (b1 >= var.CONST_B1) and (b3 >= var.CONST_B3)):
			A3_ATIVADO = True
			while(A3_ATIVADO is True):		
				a0, a1, _, a3, b0, b1, _, b3 = sensor.fototransistores()
				motor.movimento_esquerda(var.velCorrecaoN2, ctr_vel_motor_dir, ctr_vel_motor_esq)
				if((a0 >= var.CONST_A3) and (a1 >= var.CONST_A1)): 
					A3_ATIVADO = False


		elif((b0 <= var.CONST_B0) or (b1 <= var.CONST_B1) and (b3 >= var.CONST_B3) and (a0 >= var.CONST_A0) and (a1 >= var.CONST_A1) and (a3 >= var.CONST_A3)):
			A3_ATIVADO = True
			while(A3_ATIVADO is True):		
				a0, a1, _, a3, b0, b1, _, b3 = sensor.fototransistores()
				motor.movimento_direita(var.velCorrecaoN2, ctr_vel_motor_dir, ctr_vel_motor_esq)
				if((b0 >= var.CONST_B0) and (b1 >= var.CONST_B1)): 
					A3_ATIVADO = False

		
		# -------------- Manter robô parado caso não atenda as condições  ---------------
		else:
			#print("O Sistema apresentou uma anomalia! Aguardando...")
			motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
		# -------------------------------------------------------------------------------
		


		# -------------------------- Apresentacao Telas ---------------------------------
		#interface.apresenta_tela("Imagem Original", imagem, 580, 10)
	
	
		#interface.apresenta_tela("Imagem Faixa Esquerda", imagem_faixa_esq, 80, 355)
		#interface.apresenta_tela("Imagem Perspetiva Pista", imagem_perspectiva_pista, 580, 355)
		#interface.apresenta_tela("Imagem Faixa Direita", imagem_faixa_dir, 1080, 355)

	
		# -------------------------------------------------------------------------------
		

		capturaFrames.truncate(0)
		
		if cv2.waitKey(1) & 0xFF == 27:
			motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
			cv2.destroyAllWindows()
			GPIO.cleanup()
			break
finally:
	print("bye bye...")	
	motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
	cv2.destroyAllWindows()
	GPIO.cleanup()
