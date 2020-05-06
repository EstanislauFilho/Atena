#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:22:38 2020

@author: estanislau
"""


import cv2

video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/Videos/video_calibracao_placas_1.mp4")
#video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/Videos/video_calibracao_placas_2.mp4")

cont_imagem = 1000
cont_execucao = 1


while(True):
    
    verif, frame = video.read()
    
    imagem = cv2.resize(frame, (680, 420))
    
    if cont_execucao % 10 == 0:
        cv2.imwrite("frames_calibracao_1/" + str(cont_imagem) + ".jpg",imagem)
        print(str(cont_imagem)+"º imagem capturada com sucesso...")
        cont_imagem += 1
    cont_execucao += 1 
    
    cv2.imshow("Apresenta Imagem", imagem)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()