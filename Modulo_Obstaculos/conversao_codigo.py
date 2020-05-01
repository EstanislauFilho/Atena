#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:38:13 2020

@author: estanislau
"""

import cv2

imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/248.jpg")

def gerar_matriz (n_linhas, n_colunas):
    return [[" "]*n_colunas for _ in range(n_linhas)]

def DetectaObstaculos(imgBin, vet):

  # Variáveis e limiares
  minimo_livre_inf = 200 # na parte de baixo da imagem
  minimo_livre_sup = 110 # na parte de cima da imagem
  num_perfis = 15 # quantidade de perfis a serem analisados na imagem

  largura, altura, _ = imgBin.shape

  print("Largura = {0} Altura = {1}".format(largura, altura))

  passo_vertical = altura/num_perfis

  linhas, colunas = 6, 50
  matriz_contagem = gerar_matriz(linhas, 50)
  
  
  
  
  
  
# ------------------------- Main ------------------------- 
DetectaObstaculos(imagem, None)  
cv2.imshow("Imagem Pista", imagem)  
cv2.waitKey(0)    
cv2.destroyAllWindows() 