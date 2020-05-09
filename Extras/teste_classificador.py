#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste Classificadores

# --------------------------------------------------------

from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import cv2

# Inicializacao e configuracao da camera 
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

#classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_pare.xml')

#classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_desvio.xml')

#classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_pedestre.xml')

#classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_60.xml')

#classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_proibido_virar.xml')

#classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_virar.xml')


#classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_servicos.xml')


classificador = cv2.CascadeClassifier('/home/pi/Projetos/Atena/Classificadores/cascade_semaforo.xml')


# Captura dos quadros por segundo
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array

	# Conversão da imagem para escala de cinza
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	# Procurando caracteristicas semelhante na imagem capturada a partir do classificador
	faces = classificador.detectMultiScale(gray, 1.1, 10)

	for (x,y,w,h) in faces:
	    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
 
	# Apresenta imagem
	cv2.imshow("Frame", image)

	# limpa o buffer de quadros e prepara para receber o proximo
	rawCapture.truncate(0)

	if cv2.waitKey(1) & 0xFF == 27:
		break
	 
print("Cleaning up")
GPIO.cleanup()

