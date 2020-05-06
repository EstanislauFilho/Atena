#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:22:38 2020

@author: estanislau
"""


import cv2
import numpy as np

video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/Videos/video_calibracao_faixas.mp4")

cont_imagem = 1000
cont_execucao = 1


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

	return img_tresh


while(True):
    
    verif, frame = video.read()
    
    imagem = cv2.resize(frame, (680, 420))
    
    # Imagens da perspectiva da pista sem filtros aplicados
    imagem_pista = perspectiva_pista(imagem)
    
    # Imagem da perspectiva da pista pista com aplicação dos filtros 
    imagem_pista_filtrada = filtros_faixas(imagem_pista)
    
    if cont_execucao % 10 == 0:
        cv2.imwrite("frames_calibracao_faixas/" + str(cont_imagem) + ".jpg",imagem_pista_filtrada)
        print(str(cont_imagem)+"º imagem capturada com sucesso...")
        cont_imagem += 1
    cont_execucao += 1 
    
    cv2.imshow("Apresenta Imagem", imagem)
    cv2.imshow("Apresenta Faixas", imagem_pista_filtrada)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()