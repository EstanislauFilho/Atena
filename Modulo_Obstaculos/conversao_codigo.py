#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:38:13 2020

@author: estanislau
"""

import cv2

imagem =  cv2.imread("/home/estanislau/Projetos/Atena/Videos/Frames_Video/248.jpg")

def gerar_matriz (n_linhas, n_colunas):
    return [[0]*n_colunas for _ in range(n_linhas)]

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
  
    '''
     matriz_contagem: primeira linha (0) contem codigo da regiao
     1 - Black (desconhecido)
     2 - Red (região livre, na verdade cinza)
     3 - White (faixa)
    
     Segunda linha (1) contem o numero de pixels seguidos da regiao em determinado perfil da imagem.
     Terceira linha (2) contem o ponto medio da regiao (coordenada x)
     Quarta linha (3) contem 1 se regiao for candidata a pertencer a faixa de pedestre BR
     Quinta linha (4) contem 1 se regiao for candidata a pertencer a faixa de pedestre BW
     Sexta linha (5) contem 1 se regiao for candidata a pertencer a faixa de pedestre WR
    '''  
  
    matriz_perfis = gerar_matriz(num_perfis, 6)
    '''
    matriz_perfis: resultados da analise de cada perfil
    (uma linha por perfil)
    Colunas: y, classificacao, numero de regioes R validas, ponto medio R1, ponto medio R2
    
    Classificacao:
    1- livre
    2- obstaculo
    3- faixa
    '''


    # int i, j;
    
    perfil_atual = 0
    
    # zera matriz perfis
    for i in range(num_perfis):
        for j in range(6):
            matriz_perfis[i][j] = 0;



    return matriz_contagem, matriz_perfis



  
  
# ------------------------- Main ------------------------- 
matriz_contagem, matriz_perfis = DetectaObstaculos(imagem, None)  
cv2.imshow("Imagem Pista", imagem)  
cv2.waitKey(0)    
cv2.destroyAllWindows() 