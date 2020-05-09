#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste Sensor Obstaculo

# --------------------------------------------------------


import RPi.GPIO as GPIO
import time
import board
import busio

import adafruit_vl53l0x

# inicializacao do protocolo i2c
i2c = busio.I2C(board.SCL, board.SDA)

# Ativacao do sensor
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    print('Distancia: {0}mm'.format(vl53.range))
    time.sleep(1.0)
