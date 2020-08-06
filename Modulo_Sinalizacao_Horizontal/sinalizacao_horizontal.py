#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import glob
import numpy as np

################################ Para Testes ################################ 
numero_pasta = 1

caminho_pasta = '/home/estanislau/Projetos/Atena/frames_video_obs_'+str(numero_pasta)+'/*.jpg'
#############################################################################


pt_pista_1, pt_pista_2, pt_pista_3, pt_pista_4 = (105,380), (567,380), (80,410), (592,410)
pt_destino_1, pt_destino_2, pt_destino_3, pt_destino_4 = (190,0), (490,0), (190,420), (490,420)

pontos_pista = np.float32([[pt_pista_1], [pt_pista_2], [pt_pista_3], [pt_pista_4]])
pontos_destino = np.float32([[pt_destino_1], [pt_destino_2], [pt_destino_3], [pt_destino_4]])


def filtros(img):
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_cinza,(5,5),0)
    img_tresh = cv2.inRange(img_blur,  185, 255) 
    return img_tresh

def get_perspectiva_pista(img):
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


def calcula_centro_de_massa_imagem(img):
    ret,thresh = cv2.threshold(img,145,250,cv2.THRESH_BINARY_INV)
	
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


def detecta_borda_esquerda(img):
    img_borda_esq = img[0:420, 170:360]
    img_borda_esq, cx_esq = calcula_centro_de_massa_imagem(img_borda_esq.copy())
    return img_borda_esq, cx_esq


def detecta_borda_direita(img):
    img_borda_dir = img[0:420, 300:490] 
    img_borda_dir, cx_dir = calcula_centro_de_massa_imagem(img_borda_dir.copy())
    return img_borda_dir, cx_dir


def detecta_faixa_pedestre(img):
    return img


def sinalizacao_horizontal(img):
    status_fxa_pedestre, status_correc_motor_dir, status_correc_motor_esq = False, False, False
    img = cv2.imread(img)
    img_pista = get_perspectiva_pista(img)
    img_filtro = filtros(img_pista)
    detecta_faixa_pedestre(img_filtro)
    img_borda_esq, cx_esq = detecta_borda_esquerda(img_filtro)
    img_borda_dir, cx_dir = detecta_borda_direita(img_filtro)
    return img_filtro, img_borda_esq, img_borda_dir, status_fxa_pedestre, status_correc_motor_dir, status_correc_motor_esq
           
        
  

############################ Teste chamada do main ############################ 
quantidade_imagens = len((glob.glob(caminho_pasta)))
try:    
    
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem, img_borda_esq, img_borda_dir, status_fxa_pedestre, status_correc_motor_dir, status_correc_motor_esq = sinalizacao_horizontal(i)
         
        quantidade_imagens -= 1
        
        cv2.imshow("Apresenta Imagem", imagem)
        cv2.imshow("Faixa esq", img_borda_esq)
        cv2.imshow("Faixa dir", img_borda_dir)
        cv2.waitKey(0)
        
        if quantidade_imagens == 0:
            print("Todas as imagens analisadas com sucesso!")
            cv2.destroyAllWindows()
            break
        
        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()	
         
    
except KeyboardInterrupt:
    cv2.destroyAllWindows()
    print('Encerrar execução...') 
    
finally:
    cv2.destroyAllWindows()
###############################################################################