#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:14:59 2020

@author: estanislau
"""

import cv2
import glob
import numpy as np



numero_pasta = 1

caminho_pasta = '/home/estanislau/Projetos/Atena/frames_video_fxa_'+str(numero_pasta)+'/*.jpg'

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



def filtros_faixas(img):
	img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_blur = cv2.GaussianBlur(img_cinza,(5,5),0)
	
	# Binariza a imagem, definindo regiões pretas e brancas. Para visualizar a imagem binarizada comentar linhas abaixo
	img_tresh = cv2.inRange(img_blur,  240, 255) 

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

cont_imagem = 1000

quantidade_imagens = len((glob.glob(caminho_pasta)))

try:    
    
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
           
        quantidade_imagens -= 1
        
        # Imagens da perspectiva da pista sem filtros aplicados
        imagem_pista = perspectiva_pista(imagem)
        
        # Imagem da perspectiva da pista pista com aplicação dos filtros 
        imagem_pista_filtrada = filtros_faixas(imagem_pista)
        
        # Imagem da faixa da esquerda
        imagem_faixa_esq = imagem_pista_filtrada[0:420, 100:360]
        imagem_faixa_esq, cx_esq = detecta_faixas(imagem_faixa_esq.copy())
        
        # Imagem da faixa da direta
        imagem_faixa_dir = imagem_pista_filtrada[0:420, 300:560]    
        imagem_faixa_dir, cx_dir = detecta_faixas(imagem_faixa_dir.copy())
        
        correcao_esq, correcao_dir =  False, False
        
        if cx_esq >= 59 and cx_esq <= 105:
            correcao_esq = True
        elif cx_dir >= 154 and cx_dir <= 198:
            correcao_dir = True
        
        print("Corrigir_MT_Esq: {0} | Corrigir_MT_Dir: {1} | Frame: {2}\n".format(correcao_esq, correcao_dir, cont_imagem))
        
        cv2.imshow("Img", imagem)
        cv2.imshow("Perspectiva Pista Filtrada", imagem_pista_filtrada)
        cv2.imshow("Faixa Esquerda", imagem_faixa_esq)
        cv2.imshow("Faixa Direita", imagem_faixa_dir)
        cv2.waitKey(0)
        
        if quantidade_imagens == 0:
            print("Todas as imagens analisadas com sucesso!")
            cv2.destroyAllWindows()
            break
        
        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()	
         
        cont_imagem += 1
    
    
except KeyboardInterrupt:
    cv2.destroyAllWindows()
    print('Encerrar execução...') 
    
finally:
    cv2.destroyAllWindows()
