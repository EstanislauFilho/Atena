#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Main

# --------------------------------------------------------

import time
import RPi.GPIO as GPIO
from motores import Motores
from configuracoes import Configuracoes


import pygame, sys
from pygame.locals import *

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

pygame.init()

screen = pygame.display.set_mode((400,200))
clock = pygame.time.Clock()

class Controle_Remoto():

	def __init__(self):
		self.configura = Configuracoes()
		self.movimento = Motores()
		
	def incializacao(self):
		self.configura.pinos_MOTORES()
		self.configura.pinos_VELOCIDADE()

	def main(self):
		self.incializacao()
	
		try:
			while (True):
				clock.tick(30)
				key=pygame.key.get_pressed()
				self.movimento.parar(0, self.configura.controle_motor_dir, self.configura.controle_motor_esq)

				if key[pygame.K_UP]:
					self.movimento.frente(40, self.configura.controle_motor_dir, self.configura.controle_motor_esq)
				if key[pygame.K_RIGHT]:
					self.movimento.direita(40, self.configura.controle_motor_dir, self.configura.controle_motor_esq)
				if key[pygame.K_LEFT]:
					self.movimento.esquerda(40, self.configura.controle_motor_dir, self.configura.controle_motor_esq)
				if key[pygame.K_DOWN]:
					self.movimento.tras(40, self.configura.controle_motor_dir, self.configura.controle_motor_esq)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						GPIO.cleanup()
						sys.exit()
					elif event.type == KEYDOWN and event.key == K_ESCAPE:
						GPIO.cleanup()
						sys.exit()			
				
		finally:
			print("Cleaning up")
			GPIO.cleanup()


if __name__ == '__main__':
	execute_app = Controle_Remoto()
	execute_app.main()

