#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:44:38 2020

@author: estanislau
"""


import cv2
import numpy as np
video = cv2.VideoCapture("video.mp4")

pt_pista_1, pt_pista_2, pt_pista_3, pt_pista_4 = (50,445), (695,445), (0,510), (735,510)


pt_destino_1, pt_destino_2, pt_destino_3, pt_destino_4 = (150,0), (590,0), (150,680), (590,680)

pontos_pista = np.float32([[pt_pista_1], [pt_pista_2], [pt_pista_3], [pt_pista_4]])
pontos_destino = np.float32([[pt_destino_1], [pt_destino_2], [pt_destino_3], [pt_destino_4]])


def perspectiva_pista(img):
	cv2.line(img, pt_pista_1, pt_pista_2, (0,0,255), 4)
	cv2.line(img, pt_pista_1, pt_pista_3, (0,0,255), 4)
	cv2.line(img, pt_pista_2, pt_pista_4, (0,0,255), 4)
	cv2.line(img, pt_pista_3, pt_pista_4, (0,0,255), 4)

	cv2.line(img, pt_destino_1, pt_destino_2, (0,255,0), 4)
	cv2.line(img, pt_destino_1, pt_destino_3, (0,255,0), 4)
	cv2.line(img, pt_destino_2, pt_destino_4, (0,255,0), 4)
	cv2.line(img, pt_destino_3, pt_destino_4, (0,255,0), 4)

	#matriz = cv2.getPerspectiveTransform(var.pontos_pista, var.pontos_destino)
	#img = cv2.warpPerspective(img, matriz, (var.tam_original_tela_x, var.tam_original_tela_y)) 
	return img

while(True):
    status, frame = video.read()
    
    # Redimensionamento da imagem
    imagem = cv2.resize(frame, (780, 520))
      
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    imagem_blur = cv2.GaussianBlur(imagem_cinza,(5,5),0)
    
    imagem_tresh = cv2.inRange(imagem_blur, 240, 255) 
    
    imagem_canny = cv2.Canny(imagem_blur, 240, 250)
    
    imagem_final = cv2.add(imagem_tresh, imagem_canny)
    
    
    
    imagem = perspectiva_pista(imagem)
    
    
    
    cv2.imshow("Imagem Original", imagem)  
    #cv2.imshow("Imagem Cinza", imagem_cinza)
    #cv2.imshow("Imagem Blur", imagem_blur)
    #cv2.imshow("Imagem Tresh", imagem_tresh)
    #cv2.imshow("Imagem Canny", imagem_canny)
    #cv2.imshow("Imagem Final", imagem_final)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows() 