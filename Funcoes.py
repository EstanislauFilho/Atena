#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Funcoes

# --------------------------------------------------------

import RPi.GPIO as GPIO
import Variaveis as var
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# inicializacao do protocolo i2c
i2c = busio.I2C(board.SCL, board.SDA)

def buzina(ativa_bozina):
	if ativa_bozina == True:	
		GPIO.output(var.pin_BOZINA, True)
	else:
		GPIO.output(var.pin_BOZINA, False)
		

def detecta_faixas_pista():
	# Criando um objeto ADC com a interface i2c
	ads = ADS.ADS1115(i2c)

	# Criando entradas para leitura dos canais A0, A1, A2, e A3 do conversor AD
	ft_dir_extrem = AnalogIn(ads, ADS.P0)
	ft_dir_centro = AnalogIn(ads, ADS.P1)
	ft_esq_centro = AnalogIn(ads, ADS.P2)
	ft_esq_extrem = AnalogIn(ads, ADS.P3)

	return ft_dir_extrem.value, ft_dir_centro.value, ft_esq_centro.value, ft_esq_extrem.value


def detect_obstaculo():
	# Ativacao do sensor
	vl53 = adafruit_vl53l0x.VL53L0X(i2c)

	return vl53.range

	
	
