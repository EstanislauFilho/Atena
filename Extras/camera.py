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
import time
import cv2

# Inicializacao da camera e parâmetros de resolucao e quadros por segundo capturado
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

cont_frames = 0
try:
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		# O vetor com os frames capturados sao armazenados no vetor image	
		image = frame.array

		# Apresenta as imagens capturas por meio dos frames
		cv2.imshow("Streaming Camera Atena", image)

		# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
		rawCapture.truncate(0)

	
		# Se prescionar a tecla Esc sai do programa
		if cv2.waitKey(1) & 0xFF == 27:
			break

finally:
	GPIO.cleanup()
	cv2.destroyAllWindows()



	
