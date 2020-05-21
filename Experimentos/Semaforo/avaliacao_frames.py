#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:14:59 2020

@author: estanislau
"""

import cv2
import glob
import numpy as np


caminho_pasta = '/home/estanislau/Projetos/Atena/Experimentos/Semaforo/vermelho/*.jpg'


min_H_sem_vermelho = 102
max_H_sem_vermelho = 174

min_S_sem_vermelho = 162
max_S_sem_vermelho = 255

min_V_sem_vermelho = 123
max_V_sem_vermelho = 255

semaforo_vermelho = [min_H_sem_vermelho, max_H_sem_vermelho, min_S_sem_vermelho, max_S_sem_vermelho, min_V_sem_vermelho, max_V_sem_vermelho]




min_H_sem_verde = 65
max_H_sem_verde = 94

min_S_sem_verde = 46
max_S_sem_verde = 255

min_V_sem_verde = 0
max_V_sem_verde = 255

semaforo_verde = [min_H_sem_verde, max_H_sem_verde, min_S_sem_verde, max_S_sem_verde, min_V_sem_verde, max_V_sem_verde]




acertos = 0

def hsv_semaforo_vermelho(img, valores_semaforo):
    status_vermelho = False
    qte_min_contornos_vermelho = 160

    #global acertos_vermelho, acertos_verde
	
    min_H, max_H, min_S, max_S, min_V, max_V = valores_semaforo
	
    hsv_min = np.array([min_H, min_S, min_V])
    hsv_max = np.array([max_H, max_S, max_V])
  
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			
    mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

    contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    	
    for c in contours:
        if (cv2.contourArea(c) > qte_min_contornos_vermelho):			
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Sinal Vermelho", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            status_vermelho = True
            #acertos_vermelho += 1
 		
    return  status_vermelho



def hsv_semaforo_verde(img, valores_semaforo):
    status_verde = False
    qte_min_contornos_verde = 265
    #global acertos_vermelho, acertos_verde
	
    min_H, max_H, min_S, max_S, min_V, max_V = valores_semaforo
	
    hsv_min = np.array([min_H, min_S, min_V])
    hsv_max = np.array([max_H, max_S, max_V])
  
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			
    mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

    contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    	
    for c in contours:                  
        if (cv2.contourArea(c) > qte_min_contornos_verde):			
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Sinal Verde", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            status_verde = True
            #acertos_verde += 1
		
    return  status_verde




cont_imagem = 1000
quantidade_imagens = len((glob.glob(caminho_pasta)))



try:     
    status_vermelho, status_verde = False, False
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        
        
        status_vermelho = hsv_semaforo_vermelho(imagem, semaforo_vermelho)
        status_verde = hsv_semaforo_verde(imagem, semaforo_verde)
        
        print("Sem. Vermelho: {0} | Sem. Verde: {1} | Frame: {2}".format(status_vermelho, status_verde, cont_imagem))
        
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