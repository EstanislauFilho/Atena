#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:06:43 2020

@author: estanislau
"""


import cv2
import glob



caminho_pasta_original = "/home/estanislau/Projetos/Atena/Base_Dados/obras/i/*.jpg"
caminho_pasta_destino = "/home/estanislau/Projetos/Atena/Base_Dados/obras/plc_obras_original/"

cont_imagem = 11098


min_H = 0
min_S = 64
min_V = 166

max_H = 80
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
	if(areaMaxima > 2000.0):
		imagem = imagem[y-10:y+h+10, x-10:x+w+10]
	return imagem
	


print("Iniciando seleção e recorte das imagens...")

for i in sorted(glob.glob(caminho_pasta_original)):
    imagem = cv2.imread(i)
    
    try:
        imagem_hsv = seleciona_regiao_HSV(imagem)

    except:
        print("Imagem {0} com problema!".format(cont_imagem))
    
    try:
        cv2.imwrite(caminho_pasta_destino+str(cont_imagem)+".jpg", imagem_hsv)
    except ValueError:
        print("Falha no salvamento das imagens.")
        
    print("Recortando imagem {0}".format(cont_imagem))    
    cont_imagem += 1

print("Fim da seleção e recorte das imagens!")