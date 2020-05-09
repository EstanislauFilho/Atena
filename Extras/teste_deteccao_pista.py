#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste Detecção Pista

# --------------------------------------------------------

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


# Inicializacao da camera, definicao dos parametros de resolucao e dos quadros capturados por segundo capturado
camera = PiCamera()
camera.resolution = (1200, 900)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(1200, 900))
time.sleep(0.1)

tamanho_mini_tela_x, tamanho_mini_tela_y = 480, 320

ponto_pista_1, ponto_pista_2, ponto_pista_3, ponto_pista_4 = (31,160), (458,160), (2,205), (493,205), 
ponto_destino_1, ponto_destino_2, ponto_destino_3, ponto_destino_4 = (95,0), (220,0), (95,240), (220,240),

pontos_pista = np.float32([[ponto_pista_1], [ponto_pista_2], [ponto_pista_3], [ponto_pista_4]])
pontos_destino = np.float32([[ponto_destino_1], [ponto_destino_2], [ponto_destino_3], [ponto_destino_4]])

# Area para detecção das faixas
x1_faixa_esq, x2_faixa_esq = 95, 125
y1_faixa_esq, y2_faixa_esq = 100, 150

x1_faixa_dir, x2_faixa_dir = 190, 220 
y1_faixa_dir, y2_faixa_dir = 100, 150
	

def detecta_faixas(imagem):
	# Convert to grayscale
	imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

	# Gaussian blur
	imagem_blur = cv2.GaussianBlur(imagem_cinza,(5,5),0)

	img_final = limiarizacao(imagem_blur)

	# Color thresholding
	ret,thresh = cv2.threshold(img_final,200,255,cv2.THRESH_BINARY_INV)

	# Find the contours of the frame
	_, contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

	if len(contours) > 0:
		c = max(contours, key=cv2.contourArea)

		M = cv2.moments(c)

		cx = int(M['m10']/M['m00'])

		cy = int(M['m01']/M['m00'])

		cv2.line(imagem,(cx,0),(cx,720),(255,0,0),1)

		cv2.line(imagem,(0,cy),(1280,cy),(255,0,0),1)

		cv2.drawContours(imagem, contours, -1, (0,255,0), 1)

		return imagem, cx


def limiarizacao(img):
	# Valores para detectar somente as linhas na função inRange
	# tarde: (200, 240) 
	# noite: (145, 165)
	img_tresh = cv2.inRange(img, 200, 240) # Binariza a imagem, definindo regiões pretas e brancas
	img_canny = cv2.Canny(img, 900, 1000) # Cria contornos especificos nos elementos de cor mais clara	
	img_final = cv2.add(img_tresh, img_canny) # Soma as duas imagens para maior confiabilidade na deteccao das linhas da pista
	return img_final


# Funcao para regiao de interesse
def regiao_de_interesse(rg_imagem, pontos_pista, pontos_destino):
	cv2.line(rg_imagem, ponto_pista_1, ponto_pista_2, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_1, ponto_pista_3, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_2, ponto_pista_4, (0,0,255), 2)
	cv2.line(rg_imagem, ponto_pista_3, ponto_pista_4, (0,0,255), 2)

	# Cria uma matriz a partir dos pontos definidos
	matriz = cv2.getPerspectiveTransform(pontos_pista, pontos_destino)

	#Cria uma nova perspectiva de imagem atraves da definicao da matriz gerada pelos pontos que dermacaram a regiao de interesse
	rg_imagem = cv2.warpPerspective(rg_imagem, matriz, (360,280)) 
	return rg_imagem


# Funcao para rotacionar a imagem 180 graus
def rotaciona_imagem(imagem):
	(altura, largura) = imagem.shape[:2]
	centro_imagem = (largura / 2, altura / 2)
	matriz_imagem = cv2.getRotationMatrix2D(centro_imagem, 180, 1.0)
	imagem_rotacionada = cv2.warpAffine(imagem, matriz_imagem, (largura, altura))
	return imagem_rotacionada

# Funcao para apresentacao das telas
def apresenta_tela(nome, img, pos_x, pos_y):
	cv2.namedWindow(nome, cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow(nome, pos_x, pos_y);
	cv2.resizeWindow(nome, tamanho_mini_tela_x, tamanho_mini_tela_y)
	cv2.imshow(nome, img)


# Loop
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# O vetor com os frames capturados sao armazenados no vetor imagem	
	imagem = frame.array

	imagem_perspectiva = regiao_de_interesse(imagem, pontos_pista, pontos_destino)

	faixa_esquerda = imagem_perspectiva[y1_faixa_esq:y2_faixa_esq, x1_faixa_esq:x2_faixa_esq]
	faixa_esquerda, cx_esquerda = detecta_faixas(faixa_esquerda)

	faixa_direita = imagem_perspectiva[y1_faixa_dir:y2_faixa_dir, x1_faixa_dir:x2_faixa_dir]
	faixa_direita, cx_direita = detecta_faixas(faixa_direita)

	
	mensagem = ""
	
	if cx_esquerda > 10 and cx_direita <= 10:
		mensagem = str("Dentro da Faixa")	
	elif cx_esquerda <= 10:
		mensagem = str("Virar Direita")
	elif cx_direita > 10:
		mensagem = str("Virar Esquerda")
	else:
		mensagem = str("Não detectado faixas.")

	print ("CX Esquerda: {0}, CX Direita: {1}, Situração: {2}".format(cx_esquerda, cx_direita, mensagem))
	
	#cv2.imshow("dgsd", imagem)
	
	apresenta_tela("Imagem Original", imagem, 20, 20)
	#apresenta_tela("Imagem Perspectiva", imagem_perspectiva, 530, 20)

	# Faz a limpeza do stream e faz a preparacao para a captura dos proximos frames
	rawCapture.truncate(0)

	# Se prescionar a letra 'Esc' encerra execucao
	if cv2.waitKey(1) & 0xFF == 27:
		break
cv2.destroyAllWindows()
