#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:40:46 2020

@author: estanislau
"""


import cv2

n_placa_1, c_placa_1 = "Pare", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_pare.xml')
n_placa_2, c_placa_2 = "Pedestre", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_pedestre.xml')

classificadores = [(n_placa_1, c_placa_1), (n_placa_2, c_placa_2)]

numero_imagem = 1200

imagem = cv2.imread("/home/estanislau/Projetos/Atena/Videos/Placas/frames_video_teste_1/"+str(numero_imagem)+".jpg")

imagem = cv2.resize(imagem, (680, 420))

def detecta_Placas(img, nome, classificador):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_placa = classificador.detectMultiScale(img_gray, scaleFactor = 1.1, minNeighbors = 15)
    
    for (x,y,w,h) in img_placa:       
        cv2.rectangle(img, (x, y), (x + w, y + h), ((0, 220, 220)), 2)
        cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 220, 220), 2)
        
    return img

for n, c in classificadores: 
    imagem_placas = detecta_Placas(imagem, n, c)

cv2.imshow("Apresenta Imagens", imagem_placas)
cv2.waitKey(0)

cv2.destroyAllWindows()	