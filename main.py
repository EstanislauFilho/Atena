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
import glob
import Motores as motor
import Variaveis as var
import RPi.GPIO as GPIO
import Sensores as sensor
import Tratamento as trata
import Interface as interface
from picamera import PiCamera
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
'''
while(inicializacao is False):
	opcao_destino = interface.menu_texto()	
	resposta_autorizacao, ck1, ck2, ck3 = trata.interface_menu(opcao_destino)
	inicializacao = resposta_autorizacao
'''


# 138 frames em 1 minuto
cont_frames = 0

class main:
	try:
		for frame in frames.capture_continuous(capturaFrames, format="bgr", use_video_port=True):

			ck1, ck2, ck3 = False, False, False

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

			imagem_sinalizacao_dir = imagem.copy()
			imagem_sinalizacao_esq = imagem.copy()

			imagem_obstaculo = imagem.copy()

			imagem_sinalizacao_dir = imagem_sinalizacao_dir[var.y1_img_sinalizacao_dir:var.y2_img_sinalizacao_dir, var.x1_img_sinalizacao_dir:var.x2_img_sinalizacao_dir]
			imagem_sinalizacao_esq = imagem_sinalizacao_esq[var.y1_img_sinalizacao_esq:var.y2_img_sinalizacao_esq, var.x1_img_sinalizacao_esq:var.x2_img_sinalizacao_esq]

			
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

		
			# Deteccao de obstaculos na pista
			(
				imagem_obstaculos,
				status_obstaculo_visao, 
				status_obstaculo_vl53x, 
			) = trata.deteccao_obstaculo(imagem_obstaculo, 0)					
			
			status_obstaculo_vl53x = False

			'''
			# Deteccao de placas na pista
			(
				status_placa_pare, 
				status_placa_pedestre, 
				status_placa_desvio, 
				status_placa_60, 
				status_placa_proib_virar,
				status_semaforo_vermelho,  
				status_semaforo_verde
			) = trata.sinalizacao_direita(imagem_sinalizacao_dir)
			
			
			# Deteccao de checkpoints na pista
			(
				status_ck_1, 
				status_ck_2, 
				status_ck_3,
			) = trata.sinalizacao_esquerda(imagem_sinalizacao_esq)

			# --------------------------------------------------------------------------------


			
			# -------------------------- Condicionais Placas---------------------------------
			if(status_placa_pare is True):
				gerencia.placa_pare(ctr_vel_motor_dir, ctr_vel_motor_esq)
			elif(status_placa_pedestre is True):
				gerencia.placa_pedestre(ctr_vel_motor_dir, ctr_vel_motor_esq)
			elif(status_placa_desvio is True):
				gerencia.placa_desvio(ctr_vel_motor_dir, ctr_vel_motor_esq)
								
					
			# -------------------------------------------------------------------------------

		
			# ------------------------ Condicionais Checkpoints -----------------------------
			if((ck1 is True) and (status_ck_1 is True)):
				print("Você chegou no destino {0}. Desligando...".format(var.nome_check_1))			
				break
			elif((ck2 is True) and (status_ck_2 is True)):  
				print("Você chegou no destino {0}. Desligando...".format(var.nome_check_2))
				break
			elif((ck3 is True) and (status_ck_3 is True)):
				print("Você chegou no destino {0}. Desligando...".format(var.nome_check_3))
				break

			# -------------------------------------------------------------------------------
			'''



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
			'''	
			DETECCAO_OBSTACULOS_VISAO = False

			CORRECAO_MOTOR_DIR_VISAO = False
			CORRECAO_MOTOR_ESQ_VISAO = False

			
			
			print(status_semaforo_vermelho, status_semaforo_verde)				
			
			if(status_semaforo_vermelho is True):
				SAIR_FAIXA_CONTENCAO = False
				
				print("Sinal vermelho!!!")
				SINAL_VERMELHO = True
				while(SINAL_VERMELHO is True):
					_, _, _, a3, _, _, _, b3 = sensor.fototransistores()
					print("Indo ate a faixa de conteção para aguardar...")
					gerencia.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
					if((a3 <= var.CONST_A3) and (b3 <= var.CONST_B3)):
						print("Faixa de contenão")
						motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)	
						SINAL_VERMELHO = False

				print("Aguardando abrir sinal verde!")
				if(status_semaforo_verde is False):
					print("Sinal verde esta fechado!")
					motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)		
					status_semaforo_vermelho = True
			'''	


			SINAL_VERDE, SINAL_VERMELHO, DETECCAO_OBSTACULOS_SENSOR = True, False, False
			
			# Tratamento especifico para faixa de contencao
			if(FAIXA_CONTENCAO_VISAO is True):
				print("faixa de contencao visao")
				CORRECAO_MOTOR_DIR_VISAO = False
				CORRECAO_MOTOR_ESQ_VISAO = False
				gerencia.interrupcao_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)

				if((SINAL_VERDE is True) and (SINAL_VERMELHO is False) and (DETECCAO_OBSTACULOS_SENSOR is False)):
					print("Prosseguir ate faixa de pedestre.")
					while(FAIXA_CONTENCAO_FOTO is False):
						a0, a1, _, a3, b0, b1, _, b3 = sensor.fototransistores()
						gerencia.movimento_frente(var.velReacao, ctr_vel_motor_dir, ctr_vel_motor_esq)
						print("...")
						if(((a0 <= var.CONST_A0) and (b0 <= var.CONST_B0)) or ((a1 <= var.CONST_A1) and (b1 <= var.CONST_B1)) or (a3 <= var.CONST_A3) and (b3 <= var.CONST_B3)):
							FAIXA_CONTENCAO_FOTO = True
					print("Chegou na faixa pedestre. Prosseguir cuidadosamente...")
					while(FAIXA_CONTENCAO_FOTO is True):
						a0, a1, _, a3, b0, b1, _, b3 = sensor.fototransistores()
						gerencia.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)
						print("...")
						if(((a0 >= var.CONST_A0) and (b0 >= var.CONST_B0)) and ((a1 >= var.CONST_A1) and (b1 >= var.CONST_B1)) and (a3 >= var.CONST_A3) and (b3 >= var.CONST_B3)):
							FAIXA_CONTENCAO_FOTO = False
					print("Saiu da faixa de pedestre. Continuar percurso.")
					break
			
				
				print("Sinal Verde: {0}\tSinal Vermelho: {1}\tObstaculo: {2}".format(SINAL_VERDE, SINAL_VERMELHO, DETECCAO_OBSTACULOS_SENSOR))
			

			

			# ------------------ *** Condicionais De Movimentacao *** -----------------------
			
			# ------------------ Seguir em frente ou manter robô parado  -------------------- 	
			if(MOVIMENTO_FRENTE is True):
				print("Seguindo em frente...")
				gerencia.movimento_frente(var.velNormal, ctr_vel_motor_dir, ctr_vel_motor_esq)					
			# -------------------------------------------------------------------------------

			# ---------------- Correcao do motor da direita com Visao Comp  -----------------
			elif (CORRECAO_MOTOR_DIR_VISAO is True):
				while(CORRECAO_MOTOR_DIR_VISAO is True):
					print("Virar Esquerda com Visao") 
					gerencia.correcao_motor_dir(var.velVisao, ctr_vel_motor_dir, ctr_vel_motor_esq)
					CORRECAO_MOTOR_DIR_VISAO = False
				if(CORRECAO_MOTOR_DIR_VISAO is True):
					CORRECAO_MOTOR_DIR_VISAO = True	
			# -------------------------------------------------------------------------------


			# --------------- Correcao do motor da esquerda com Visao Comp  ----------------- 
			elif (CORRECAO_MOTOR_ESQ_VISAO is True):
				while(CORRECAO_MOTOR_ESQ_VISAO is True):
					print("Virar Direita com Visao")
					gerencia.correcao_motor_esq(var.velVisao, ctr_vel_motor_dir, ctr_vel_motor_esq)
					CORRECAO_MOTOR_ESQ_VISAO = False
				if(CORRECAO_MOTOR_ESQ_VISAO is True):
					CORRECAO_MOTOR_ESQ_VISAO = True	
			# -------------------------------------------------------------------------------
	

			# --------- Metodo para fazer correcao de extrema emergencia (DIREITA) ----------
			elif((a3 <= var.CONST_A3) and (b3 >= var.CONST_B3)):
				CORRECAO_NIVEL_3 = True
				print("ALERTA MAXIMO!!! O robo esta saindo da faixa Direita... ")
				while(CORRECAO_NIVEL_3 is True):		
					a0, a1, _, a3, _, _, _, _ = sensor.fototransistores()
					motor.movimento_esquerda(var.velEmergencia , ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(((a3 >= var.CONST_A3) and ((a0 <= var.CONST_A0) or (a1 <= var.CONST_A1) or (b0 <= var.CONST_B0) or (b1 <= var.CONST_B1)))):
						print("Correcao estabelecida!")	 
						CORRECAO_NIVEL_3 = False
			# -------------------------------------------------------------------------------			
	
		

			# -------- Metodo para fazer correcao de extrema emergencia (ESQUERDA) ---------
			elif((a3 >= var.CONST_A3) and (b3 <= var.CONST_B3)):
				CORRECAO_NIVEL_3 = True
				print("ALERTA MAXIMO!!! O robo esta saindo da faixa Esquerda... ")
				while(CORRECAO_NIVEL_3 is True):		
					_, _, _, _, b0, b1, _, b3 = sensor.fototransistores()
					motor.movimento_direita(var.velEmergencia , ctr_vel_motor_dir, ctr_vel_motor_esq)
					if(((b3 >= var.CONST_B3) and ((b0 <= var.CONST_B0) or (b1 <= var.CONST_B1) or (a0 <= var.CONST_A0) or (a1 <= var.CONST_A1)))):
						print("Correcao estabelecida!")	 
						CORRECAO_NIVEL_3 = False
			# -------------------------------------------------------------------------------



			# ---------------------- Detccao faixa direita Fototransitor -------------------
			elif (status_a0 is True):
				if(CORRECAO_MOTOR_DIR_VISAO is True):
					CORRECAO_NIVEL_2 = True
					while(CORRECAO_NIVEL_2 is True):
						print("Virar Esquerda A0")
						a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores() 
						motor.movimento_esquerda(var.velCorrecaoN2, ctr_vel_motor_dir, ctr_vel_motor_esq)
						if(((a0 >= var.CONST_A0) and (a1 >= var.CONST_A1))  or (b0 <= var.CONST_B0) or (b1 <= var.CONST_B1)): 
							CORRECAO_NIVEL_2 = False
				else:
					status_a0 = False

			elif (status_a1 is True):
				if(CORRECAO_MOTOR_DIR_VISAO is True):
					CORRECAO_NIVEL_1 = True
					while(CORRECAO_NIVEL_1 is True):
						print("Virar Esquerda A1")
						a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores() 
						motor.movimento_esquerda(var.velCorrecaoN1, ctr_vel_motor_dir, ctr_vel_motor_esq)
						if(((a0 >= var.CONST_A0) and (a1 >= var.CONST_A1))  or (b0 <= var.CONST_B0) or (b1 <= var.CONST_B1)): 
							CORRECAO_NIVEL_1 = False
				else:
					status_a1 = False
			# -------------------------------------------------------------------------------


			
			# ---------------------- Detccao faixa esquerda Fototransitor -------------------
			elif (status_b0 is True):
				if(CORRECAO_MOTOR_ESQ_VISAO is True):
					CORRECAO_NIVEL_2 = True
					while(CORRECAO_NIVEL_2 is True):
						print("Virar Direita B0")
						a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores()  
						motor.movimento_direita(var.velCorrecaoN2, ctr_vel_motor_dir, ctr_vel_motor_esq)
						if(((b0 >= var.CONST_B0) and (b1 >= var.CONST_B1)) or (a0 <= var.CONST_A0) or (a1<= var.CONST_A1)): 
							CORRECAO_NIVEL_2 = False
				else:
					status_b0 = False

			elif (status_b1 is True):
				if(CORRECAO_MOTOR_ESQ_VISAO is True):
					CORRECAO_NIVEL_1 = True	
					while(CORRECAO_NIVEL_1 is True):
						print("Virar Direita B1")
						a0, a1, _, _, b0, b1, _, _ = sensor.fototransistores()  
						motor.movimento_direita(var.velCorrecaoN1, ctr_vel_motor_dir, ctr_vel_motor_esq)
						if(((b0 >= var.CONST_B0) and (b1 >= var.CONST_B1)) or (a0 <= var.CONST_A0) or (a1<= var.CONST_A1)): 
							CORRECAO_NIVEL_1 = False
				else:
					status_b1 = False
			# ------------------------------------------------------------------------------



			# -------------- Manter robô parado caso não atenda as condições  ---------------
			else:
				#print("O Sistema apresentou uma anomalia! Aguardando...")
				motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
			# -------------------------------------------------------------------------------
			
			

			
			# -------------------------- Apresentacao Telas ---------------------------------
			interface.apresenta_tela("Sinalizacoes da Esquerda", imagem_sinalizacao_esq, 80, 10)
			interface.apresenta_tela("Imagem Original", imagem, 580, 10)
			interface.apresenta_tela("Sinalizacoes da Direita", imagem_sinalizacao_dir, 1080, 10)
		
			interface.apresenta_tela("Imagem Faixa Esquerda", imagem_faixa_esq, 80, 355)
			interface.apresenta_tela("Imagem Perspetiva Pista", imagem_perspectiva_pista, 580, 355)
			interface.apresenta_tela("Imagem Faixa Direita", imagem_faixa_dir, 1080, 355)

			interface.apresenta_tela("Imagem obstaculos", imagem_obstaculos, 580, 705)

			# -------------------------------------------------------------------------------
			




			'''		
			# ----------------- Apresentacao Telas Monitor Pequeno ---------------------------
			#cv2.imshow("Imagem Placas",imagem)
			interface.apresenta_tela("Imagem Original", imagem, 10, 10)
			#interface.apresenta_tela("Imagem Checkpoints", imagem_deteccao_checkpoints, 10, 10)
			#interface.apresenta_tela("Imagem Placas", imagem_detecao_placa, 500, 10)
			#interface.apresenta_tela("Imagem obstaculos", imagem_obstaculos, 500, 10)
			#interface.apresenta_tela("Imagem Perspe", imagem_perspectiva_pista, 500, 10)
			interface.apresenta_tela("Imagem Faixa Esquerda", imagem_faixa_esq, 10, 400)
			interface.apresenta_tela("Imagem Faixa Direita", imagem_faixa_dir, 500, 400)
			# -------------------------------------------------------------------------------
			'''
			
			
			cont_frames += 1
			#print(status_a0, status_a1, status_a2, status_a3, status_b0, status_b1, status_b2, status_b3, status_visao_faixa_dir, status_visao_faixa_esq, status_obstaculo_vl53x)
			#print("A0:{:>5} A1:{:>5} A2:{:>5} A3:{:>5} \tB0:{:>5} B1:{:>5} B2:{:>5} B3:{:>5}".format(a0, a1, a2, a3, b0, b1, b2, b3))
			#print(DETECCAO_OBSTACULOS_VISAO)
			#print(status_visao_faixa_dir, status_visao_faixa_esq, status_normalidade_faixa_dir, status_normalidade_faixa_esq, DETECCAO_OBSTACULOS_VISAO)
			#print("\nDetectou Obstaculo: {0} \tValor: {1}".format(status_obstaculo_visao, 0))
			#print(status_placa_pare, status_placa_pedestre, status_placa_desvio, status_placa_60, status_placa_proib_virar, status_semaforo_vermelho, status_semaforo_verde)
	
			capturaFrames.truncate(0)
			
			if cv2.waitKey(1) & 0xFF == 27:
				motor.parar_movimento(ctr_vel_motor_dir, ctr_vel_motor_esq)
				cv2.destroyAllWindows()
				GPIO.cleanup()
				break
	finally:
		print("bye bye...")	
		cv2.destroyAllWindows()
		GPIO.cleanup()
