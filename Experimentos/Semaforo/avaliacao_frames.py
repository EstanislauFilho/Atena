#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:14:59 2020

@author: estanislau
"""

import cv2
import glob
import numpy as np


caminho_pasta = '/home/estanislau/Projetos/Atena/Experimentos/Semaforo/frames_video_avaliacao/*.jpg'


min_H_sem_vermelho = 132
max_H_sem_vermelho = 179

min_S_sem_vermelho = 173
max_S_sem_vermelho = 255

min_V_sem_vermelho = 172
max_V_sem_vermelho = 255

semaforo_vermelho = [min_H_sem_vermelho, max_H_sem_vermelho, min_S_sem_vermelho, max_S_sem_vermelho, min_V_sem_vermelho, max_V_sem_vermelho]


def hsv_semaforo_vermelho(img, semaforo_vermelho):
    status_vermelho = False
	
    min_H, max_H, min_S, max_S, min_V, max_V = semaforo_vermelho
	
    hsv_min = np.array([min_H, min_S, min_V])
    hsv_max = np.array([max_H, max_S, max_V])
  
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			
    mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

    contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    	
    for c in contours:
        if (cv2.contourArea(c) > 400):			
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Sinal Vermelho", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            status_vermelho = True
		
    return  status_vermelho


cont_imagem = 1000
quantidade_imagens = len((glob.glob(caminho_pasta)))

try:     
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        
        status = hsv_semaforo_vermelho(imagem, semaforo_vermelho)
        print("Status Semáforo Vermelho: {0} | Frame: {1}".format(status, cont_imagem))
        
        cv2.imshow("Apresaenta Imagem", imagem)
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