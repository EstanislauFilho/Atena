#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:46:04 2020

@author: estanislau
"""


import cv2 
import numpy as np
#import glob


imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/248.jpg")
#imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/272.jpg")
#imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/287.jpg")
#imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/309.jpg") 


# Imagem da faixa da esquerda
#imagem_obstaculos = imagem_c[210:420, 0:680]

largura, altura = 340, 210

# Redimensionamento da imagem
imagem = cv2.resize(imagem, (largura, altura))
largura, altura, _ = imagem.shape
print(largura, altura)

  
imagem_c = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
semente = (180, 205)
    
'''
ini_eixo_x = 0
mei_eixo_x = int(largura/2)
fim_eixo_x = largura

ini_eixo_y = (altura-1)
fim_eixo_y = int(altura/2)    
'''


cont_elementos = 0 


for y in range(209, 105,-1):
    for x in range(170, 340):
        #cv2.floodFill(imagem, None, imagem_c[209,170],(0, 0, 255))
        cv2.floodFill(imagem, None, semente, (0, 0, 255), (5, 5, 5, 5), (15, 15, 15, 15)) 
     
'''
for y in range(209, 105,-1):
    for x in range(170, 340):
        if imagem_c[y,x] <= 127:
            cv2.floodFill(imagem, None, (x, y),(0, 0, 255))
            cont_elementos += 1
        else:
            break
        
    for x in range(169, 0, -1):
        if imagem_c[y,x]  <= 127:
            cv2.floodFill(imagem, None, (x, y),(0, 0, 255))
            cont_elementos += 1
        else:
            break
''' 
 
   
print(cont_elementos)


cv2.imshow("Imagem Pista", imagem)  
cv2.waitKey(0)    
cv2.destroyAllWindows() 



'''
cont_imagem = 100
for i in sorted(glob.glob('/home/estanislau/Projetos/Atena/Videos/Frames_Semaforo/*.jpg')):  

    imagem = cv2.imread(i)
    
    cv2.imshow("Apresenta Imagem", imagem)
    cv2.waitKey(1000)
    
    print("Frame: {0}".format(cont_imagem))
    cont_imagem += 1
'''  
    
    
    
