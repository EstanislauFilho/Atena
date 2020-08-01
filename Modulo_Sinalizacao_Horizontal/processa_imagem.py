#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2
import numpy as np

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
    #cv2.imshow("Imga", img)
    return img



def aplica_filtros(img):
	img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_blur = cv2.GaussianBlur(img_cinza,(5,5),0)
	
	# Binariza a imagem, definindo regiões pretas e brancas. Para visualizar a imagem binarizada comentar linhas abaixo
	img_tresh = cv2.inRange(img_blur,  240, 255) 

	return img_tresh