#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:06:43 2020

@author: estanislau
"""


import cv2
import glob

largura_imagem, altura_imagem = 50, 50

caminho_pasta_original = "/home/estanislau/Projetos/Atena/Mistura/Machine_Learning/ori_plc_velocidade/*.jpg"
caminho_pasta_destino = "/home/estanislau/Projetos/Atena/Mistura/Machine_Learning/rec_plc_velocidade/"

cont_imagem = 10000


min_H = 0
min_S = 0
min_V = 142

max_H = 179
max_S = 255
max_V = 255


def seleciona_regiao_HSV(imagem):
	min_HSV = (min_H, min_S, min_V)
	max_HSV = (max_H, max_S, max_V)

	imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

	mascara = cv2.inRange(imagem_hsv, min_HSV, max_HSV)

	contours, hierarchy = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	if contours:
		areaMaxima = cv2.contourArea(contours[0])
		idContorno = 0
		i = 0
		for cnt in contours:
			if areaMaxima < cv2.contourArea(cnt):
				areaMaxima = cv2.contourArea(cnt)
				idContorno = i
			i += 1
		cnt = contours[idContorno]
		x,y,w,h = cv2.boundingRect(cnt)	
	if(areaMaxima > 500.0):
		imagem = imagem[y-2:y+h+2, x-2:x+w+2]
	return imagem
	


print("Iniciando seleção e recorte das imagens...")

for i in sorted(glob.glob(caminho_pasta_original)):
    imagem = cv2.imread(i)
    
    try:
        quadros = cv2.resize(imagem, (480,270))
    
        imagem_hsv = seleciona_regiao_HSV(quadros)
    
        imagem_red = cv2.resize(imagem_hsv, (50,50))
    
        imagem_cinza = cv2.cvtColor(imagem_red, cv2.COLOR_BGR2GRAY)
        
        print("Recortando imagem {0}".format(cont_imagem)) 
    except:
        print("Imagem {0} com problema!".format(cont_imagem))
    
    try:
        cv2.imwrite(caminho_pasta_destino+str(cont_imagem)+".jpg", imagem_cinza)
    except ValueError:
        print("Falha no salvamento das imagens.")
        
       
    cont_imagem += 1

print("Fim da seleção e recorte das imagens!")