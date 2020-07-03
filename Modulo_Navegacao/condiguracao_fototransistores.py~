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
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_vl53l0x

# inicializacao do protocolo i2c
i2c = busio.I2C(board.SCL, board.SDA)


def aciona_buzina(ativa):
	if ativa is True:	
		GPIO.output(var.pin_BUZINA, ativa)
	else:
		GPIO.output(var.pin_BUZINA, ativa)
		

def fototransistores():
	ads_a = ADS.ADS1115(i2c, address=0x48)
	ads_b = ADS.ADS1115(i2c, address=0x49)

	a0 = AnalogIn(ads_a, ADS.P0)
	a1 = AnalogIn(ads_a, ADS.P1)
	a2 = AnalogIn(ads_a, ADS.P2)
	a3 = AnalogIn(ads_a, ADS.P3)

	b0 = AnalogIn(ads_b, ADS.P0)
	b1 = AnalogIn(ads_b, ADS.P1)
	b2 = AnalogIn(ads_b, ADS.P2)
	b3 = AnalogIn(ads_b, ADS.P3)

	return a0.value, a1.value, a2.value, a3.value, b0.value, b1.value, b2.value, b3.value


def vl530x():
	vl53 = adafruit_vl53l0x.VL53L0X(i2c)

	return vl53.range


	
	
	
