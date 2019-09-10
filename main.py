#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Main

# --------------------------------------------------------
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import RPi.GPIO as GPIO
import Configuracoes as definir
import Motores as motor
import Sensores as sensor
import Tratamento as trata
import Variaveis as var
import Tela as tela
import time


frames = PiCamera()
frames.resolution = (var.tam_original_tela_x, var.tam_original_tela_y)
frames.framerate = var.taxa_quadros
capturaFrames = PiRGBArray(frames, size=(var.tam_original_tela_x, var.tam_original_tela_y))

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

definir.configuracoes()

controle_velocidade_direita = GPIO.PWM(var.pin_ENA, 500)
controle_velocidade_direita.start(0)

controle_velocidade_esquerda = GPIO.PWM(var.pin_ENB, 500)
controle_velocidade_esquerda.start(0)

print("Inicializando Sistema...")
time.sleep(0.5)
print("Pronto!")

cont_imagem = 1

class main:
	try:
		for frame in frames.capture_continuous(capturaFrames, format="bgr", use_video_port=True):
			imagem = frame.array

			# Obtendo valores brutos dos sensores
			ft_dir_ex, ft_dir_ce, ft_esq_ce, ft_esq_ex = sensor.fototransistores()

			print(ft_dir_ex, ft_dir_ce, ft_esq_ce, ft_esq_ex)
			distancia_obstaculo = sensor.vl530x()	

			#tela.apresenta("Imagem Original", imagem, 20, 20)

			# Deteccao das faixas na pista
			deteccao_faixa_dir, deteccao_faixa_centro, deteccao_faixa_esq = trata.deteccao_faixas_pista(ft_dir_ex, ft_dir_ce, ft_esq_ce, ft_esq_ex)
			#deteccao_faixa_dir, deteccao_faixa_centro, deteccao_faixa_esq = trata.deteccao_faixas_pista(imagem)
			#print(deteccao_faixa_dir, deteccao_faixa_centro, deteccao_faixa_esq)	
			# Deteccao de obstaculos na pista
			deteccao_obstaculo = trata.deteccao_obstaculo(distancia_obstaculo)


			if (deteccao_faixa_dir ==  True):
				print("Virar Esquerda") 
				motor.movimento_esquerda(controle_velocidade_direita, controle_velocidade_esquerda)
				time.sleep(1.4)
			elif (deteccao_faixa_esq  ==  True):
				#print("Virar Direita")				
				motor.movimento_direita(controle_velocidade_direita, controle_velocidade_esquerda)
				time.sleep(1.4)
			#elif ((deteccao_faixa_centro  ==  True) or (deteccao_obstaculo  ==  True)):
				#print("Parar movimento")				
				#motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
			else:
				#print("Seguir em frente")
				motor.movimento_frente(controle_velocidade_direita, controle_velocidade_esquerda) 

			capturaFrames.truncate(0)
			
			if cv2.waitKey(1) & 0xFF == 27:
				motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)
				cv2.destroyAllWindows()
				GPIO.cleanup()
				break
	finally:
		print("Cleaning up")
		motor.parar_movimento(controle_velocidade_direita, controle_velocidade_esquerda)		
		cv2.destroyAllWindows()
		GPIO.cleanup()
