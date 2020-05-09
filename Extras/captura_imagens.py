#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Interface HSV

# --------------------------------------------------------

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# Inicializacao da camera e parâmetros de resolucao e quadros por segundo capturado
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

cont_imagem = 1




for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array

	#if cv2.waitKey(1) & 0xFF == ord('c'):
	cv2.imwrite("4/" + str(cont_imagem) + ".jpg",imagem)
	print(str(cont_imagem)+"º imagem capturada com sucesso! Pressione 'ESC' para encerrar...")
	cont_imagem += 1    
	
	
	cv2.imshow("Streaming Camera Atena", imagem)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	if cv2.waitKey(1) & 0xFF == 27 or cont_imagem > 3000:
		break

cv2.destroyAllWindows()

