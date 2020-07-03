#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:26:24 2020

@author: estanislau
"""


import cv2 


video = cv2.VideoCapture("/home/estanislau/Projetos/Atena/Videos/video.mp4")

n_placa_1, c_placa_1 = "Pare", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_pare.xml')
n_placa_2, c_placa_2 = "Pedestre", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_pedestre.xml')
n_placa_3, c_placa_3 = "Desvio", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_desvio.xml')


classificadores = [(n_placa_1, c_placa_1), (n_placa_2, c_placa_2), (n_placa_3, c_placa_3)]

def detecta_Placas(img, nome, classificador):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_placa = classificador.detectMultiScale(img_gray, scaleFactor = 1.1, minNeighbors = 15)
    
    for (x,y,w,h) in img_placa:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    
    return img



while(True):
    status, frame = video.read()
    
    # Redimensionamento da imagem
    imagem = cv2.resize(frame, (680, 420))
    
    for n, c in classificadores: 
        imagem_placas = detecta_Placas(imagem, n, c)

    # Apresenta Imagens
    cv2.imshow("Imagem Placas", imagem_placas)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()