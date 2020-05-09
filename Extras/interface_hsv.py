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
camera.resolution = (480, 320)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(480, 320))
time.sleep(0.1)

def nada(x): pass

def rotaciona_imagem(img):
	# Armazenamento das dimensoes dos frames e criacao do vetor com referencia aos pixels do centro da imagem
	(h, w) = img.shape[:2]
	centro_imagem = (w / 2, h / 2)

	# Utilizacao da funcao RotationMatrix2D para realizar a rotacao da imagem a partir do ponto central
	M = cv2.getRotationMatrix2D(centro_imagem, 180, 1.0)

	# Realiza a rotacao da imagem a partir das funcoes determinadas acima
	img_rotacionada = cv2.warpAffine(img, M, (w, h))

	return img_rotacionada


# -------------------------- Interface HSV ------------------------------------
cv2.namedWindow("Interface_HSV")

cv2.createTrackbar("Valor Minimo - H", "Interface_HSV", 0, 179, nada) #Hue
cv2.createTrackbar("Valor Minimo - S", "Interface_HSV", 0, 255, nada) #Saturation
cv2.createTrackbar("Valor Minimo - V", "Interface_HSV", 0, 255, nada) #Value

cv2.createTrackbar("Valor Maximo - H", "Interface_HSV", 179, 179, nada) #Hue
cv2.createTrackbar("Valor Maximo - S", "Interface_HSV", 255, 255, nada) #Saturation
cv2.createTrackbar("Valor Maximo - V", "Interface_HSV", 255, 255, nada) #Value
# -----------------------------------------------------------------------------


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	imagem = frame.array

	# Conversao da imagem para HSV
	imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

	# Obtencao dos valores maximos e minimos dos parametros do HSV definidos pelas barras na interface
	val_minimo_H = cv2.getTrackbarPos("Valor Minimo - H", "Interface_HSV")
	val_minimo_S = cv2.getTrackbarPos("Valor Minimo - S", "Interface_HSV")
	val_minimo_V = cv2.getTrackbarPos("Valor Minimo - V", "Interface_HSV")

	val_maximo_H = cv2.getTrackbarPos("Valor Maximo - H", "Interface_HSV")
	val_maximo_S = cv2.getTrackbarPos("Valor Maximo - S", "Interface_HSV")
	val_maximo_V = cv2.getTrackbarPos("Valor Maximo - V", "Interface_HSV")


	valores_maximos_hsv = np.array([val_maximo_H, val_maximo_S, val_maximo_V])
	valores_minimos_hsv = np.array([val_minimo_H, val_minimo_S, val_minimo_V])
	mascara = cv2.inRange(imagem_hsv, valores_minimos_hsv, valores_maximos_hsv)
	imagem_hsv = cv2.bitwise_and(imagem, imagem, mask=mascara)



	# Apresentacao dos frames em tempo real
	cv2.imshow("Streaming Camera Atena", imagem)

	cv2.imshow('Interface HSV Atena', imagem_hsv)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Metodo para abortar execucao
	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()



