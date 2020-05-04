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

imagem = cv2.imread("/home/estanislau/Projetos/Atena/Videos/Placas/frames_video_teste_1/1000.jpg")





cv2.imshow("Apresenta Imagens", imagem)
cv2.waitKey(0)

cv2.destroyAllWindows()	