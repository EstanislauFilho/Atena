#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:44:38 2020

@author: estanislau
"""


import cv2
import numpy as np
video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/Videos/video.mp4")

pt_pista_1, pt_pista_2, pt_pista_3, pt_pista_4 = (70,340), (570,340), (10,410), (620,410)
pt_destino_1, pt_destino_2, pt_destino_3, pt_destino_4 = (150,0), (480,0), (150,420), (480,420)

pontos_pista = np.float32([[pt_pista_1], [pt_pista_2], [pt_pista_3], [pt_pista_4]])
pontos_destino = np.float32([[pt_destino_1], [pt_destino_2], [pt_destino_3], [pt_destino_4]])


def perspectiva_pista(img):
    '''
    
	cv2.line(img, pt_pista_1, pt_pista_2, (0,0,255), 4)
	cv2.line(img, pt_pista_1, pt_pista_3, (0,0,255), 4)
	cv2.line(img, pt_pista_2, pt_pista_4, (0,0,255), 4)
	cv2.line(img, pt_pista_3, pt_pista_4, (0,0,255), 4)

	cv2.line(img, pt_destino_1, pt_destino_2, (0,255,0), 4)
	cv2.line(img, pt_destino_1, pt_destino_3, (0,255,0), 4)
	cv2.line(img, pt_destino_2, pt_destino_4, (0,255,0), 4)
	cv2.line(img, pt_destino_3, pt_destino_4, (0,255,0), 4)
    
    '''
    matriz = cv2.getPerspectiveTransform(pontos_pista, pontos_destino)
    img = cv2.warpPerspective(img, matriz, (680, 420)) 
    return img


def filtros_faixas(img):
	img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_blur = cv2.GaussianBlur(img_cinza,(5,5),0)
	
	# Binariza a imagem, definindo regiões pretas e brancas. Para visualizar a imagem binarizada comentar linhas abaixo
	img_tresh = cv2.inRange(img_blur,  240, 255) 

	#img_canny = cv2.Canny(img_tresh, 240, 250) # Cria contornos especificos nos elementos de cor mais clara. Detecção de bordas.

	#img_final = cv2.add(img_tresh, img_canny) # Soma as duas imagens para maior confiabilidade na deteccao das linhas da pista

	return img_tresh

def detecta_faixas(img):
	# Color thresholding
	ret,thresh = cv2.threshold(img,145,250,cv2.THRESH_BINARY_INV)
	
	# Find the contours of the frame
	contours, hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
	
	if len(contours) > 0:
		c = max(contours, key=cv2.contourArea)
		
		M = cv2.moments(c)

		cx = int(M['m10']/M['m00'])

		cy = int(M['m01']/M['m00'])

		cv2.line(img,(cx,0),(cx,420),(255,0,0),1)

		cv2.line(img,(0,cy),(680,cy),(255,0,0),1)

		cv2.drawContours(img, contours, -1, (0,255,0), 1)

		return img, cx


while(True):
    status, frame = video.read()
    
    # Redimensionamento da imagem
    imagem = cv2.resize(frame, (680, 420))
      
    # Imagens da perspectiva da pista sem filtros aplicados
    imagem_pista = perspectiva_pista(imagem.copy())
    
    # Imagem da perspectiva da pista pista com aplicação dos filtros 
    imagem_pista_filtrada = filtros_faixas(imagem_pista)
    
    # Imagem da faixa da esquerda
    imagem_faixa_esq = imagem_pista_filtrada[0:420, 100:360]
    imagem_faixa_esq, cx_esq = detecta_faixas(imagem_faixa_esq.copy())
    
    # Imagem da faixa da direta
    imagem_faixa_dir = imagem_pista_filtrada[0:420, 300:560]    
    imagem_faixa_dir, cx_dir = detecta_faixas(imagem_faixa_dir.copy())
    
    
    if cx_esq >= 70 and cx_esq <= 105:
        print("Fazer correção motores da esquerda! {0}".format(cx_esq))
    elif cx_dir >= 165 and cx_dir <= 195:
        print("Fazer correção motores da direita! {0}".format(cx_dir))
    else:
        print(cx_esq, cx_dir)
    
    # Apresentação Imagens
    #cv2.imshow("Imagem Original", imagem)  
    #cv2.imshow("Imagem Cinza", imagem_cinza)
    #cv2.imshow("Imagem Blur", imagem_blur)
    #cv2.imshow("Imagem Tresh", imagem_tresh)
    #cv2.imshow("Imagem Canny", imagem_canny)
    #cv2.imshow("Imagem Final", imagem_final)
    #cv2.imshow("Perspectiva Pista", imagem_perspectiva_pista)
    cv2.imshow("Perspectiva Pista Filtrada", imagem_pista_filtrada)
    cv2.imshow("Faixa Esquerda", imagem_faixa_esq)
    cv2.imshow("Faixa Direita", imagem_faixa_dir)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows() 