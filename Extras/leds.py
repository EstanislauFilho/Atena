

import time
import Variaveis as var
import RPi.GPIO as GPIO
import Sensores as sensor
import Configuracoes as definir

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

pin_SETA_FRENTE_DIR = 21
pin_SETA_FRENTE_ESQ = 18

pin_LUZ_FREIO_ESQ = 26
pin_SETA_TRAS_ESQ = 19

pin_LUZ_FREIO_DIR = 17
pin_SETA_TRAS_DIR = 27	

pin_BUZINA = 22


GPIO.setup(pin_LUZ_FREIO_DIR, GPIO.OUT)
GPIO.setup(pin_LUZ_FREIO_ESQ, GPIO.OUT)

GPIO.setup(pin_SETA_FRENTE_DIR, GPIO.OUT)
GPIO.setup(pin_SETA_FRENTE_ESQ, GPIO.OUT)

GPIO.setup(pin_SETA_TRAS_DIR, GPIO.OUT)
GPIO.setup(pin_SETA_TRAS_ESQ, GPIO.OUT)

GPIO.setup(pin_BUZINA, GPIO.OUT)

try:
	while(True):
		GPIO.output(var.pin_BUZINA, True)
		time.sleep(0.3)
		GPIO.output(var.pin_BUZINA, False)
		time.sleep(0.3)
finally:
	print("bye bye...")	
	GPIO.cleanup()
