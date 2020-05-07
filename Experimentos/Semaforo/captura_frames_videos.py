#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:22:38 2020

@author: estanislau
"""

import cv2

#video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/Videos/video_calibracao_semaforo.mp4")
video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/Videos/video_avaliacao_semaforo.mp4")

#caminho_pasta = "frames_video_calibracao/"
caminho_pasta = "frames_video_avaliacao/"

cont_imagem = 1000
cont_execucao = 1

while(True):
    
    verif, frame = video.read()
    
    if verif is True:
        imagem = cv2.resize(frame, (680, 420))
    
        if cont_execucao % 10 == 0:
            cv2.imwrite(caminho_pasta + str(cont_imagem) + ".jpg",imagem)
            print(str(cont_imagem)+"º imagem capturada com sucesso...")
            cont_imagem += 1
        cont_execucao += 1 
    else:
        print("Todas as imagens gravadas com sucesso!")
        break