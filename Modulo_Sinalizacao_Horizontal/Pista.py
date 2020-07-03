#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Pista

# --------------------------------------------------------

import time
import cv2
import numpy as np
import Variaveis as var


def perspectiva_pista(img):
	cv2.line(img, var.pt_pista_1, var.pt_pista_2, (0,0,255), 4)
	cv2.line(img, var.pt_pista_1, var.pt_pista_3, (0,0,255), 4)
	cv2.line(img, var.pt_pista_2, var.pt_pista_4, (0,0,255), 4)
	cv2.line(img, var.pt_pista_3, var.pt_pista_4, (0,0,255), 4)

	cv2.line(img, var.pt_destino_1, var.pt_destino_2, (0,255,0), 4)
	cv2.line(img, var.pt_destino_1, var.pt_destino_3, (0,255,0), 4)
	cv2.line(img, var.pt_destino_2, var.pt_destino_4, (0,255,0), 4)
	cv2.line(img, var.pt_destino_3, var.pt_destino_4, (0,255,0), 4)


	matriz = cv2.getPerspectiveTransform(var.pontos_pista, var.pontos_destino)
	img = cv2.warpPerspective(img, matriz, (var.tam_original_tela_x, var.tam_original_tela_y)) 
	return img
	


def filtros_faixas(img):
	img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_blur = cv2.GaussianBlur(img_cinza,(5,5),0)
	
	# Binariza a imagem, definindo regiões pretas e brancas. Para visualizar a imagem binarizada comentar linhas abaixo
	img_tresh = cv2.inRange(img_blur, var.tresh_min, var.tresh_max) 

	img_canny = cv2.Canny(img_tresh, var.canny_min, var.canny_max) # Cria contornos especificos nos elementos de cor mais clara. Detecção de bordas.

	img_final = cv2.add(img_tresh, img_canny) # Soma as duas imagens para maior confiabilidade na deteccao das linhas da pista

	img = img_final
	return img



def detecta_faixas(img):
	# Color thresholding
	ret,thresh = cv2.threshold(img,145,205,cv2.THRESH_BINARY_INV)
	
	# Find the contours of the frame
	_, contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
	
	if len(contours) > 0:
		c = max(contours, key=cv2.contourArea)
		
		M = cv2.moments(c)

		cx = int(M['m10']/M['m00'])

		cy = int(M['m01']/M['m00'])

		cv2.line(img,(cx,0),(cx,var.tam_original_tela_y),(255,0,0),1)

		cv2.line(img,(0,cy),(var.tam_original_tela_x,cy),(255,0,0),1)

		cv2.drawContours(img, contours, -1, (0,255,0), 1)

		return img, cx


