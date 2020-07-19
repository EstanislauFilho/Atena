#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:06:43 2020

@author: estanislau
"""


import cv2
import glob

largura_imagem, altura_imagem = 50, 35

caminho_pasta_original = "/home/estanislau/Projetos/Atena/Base_Dados/desvio/plc_desvio_original/*.jpg"
caminho_pasta_destino = "/home/estanislau/Projetos/Atena/Base_Dados/desvio/plc_desvio/"

cont_imagem = 10000




print("Iniciando transformação das imagens...")

for i in sorted(glob.glob(caminho_pasta_original)):
    imagem = cv2.imread(i)
    
    try:
        imagem_red = cv2.resize(imagem, (largura_imagem, altura_imagem))
    
        imagem_cinza = cv2.cvtColor(imagem_red, cv2.COLOR_BGR2GRAY)
    except:
        print("Imagem {0} com problema!".format(cont_imagem))
    
    try:
        cv2.imwrite(caminho_pasta_destino+str(cont_imagem)+".jpg", imagem_cinza)
    except ValueError:
        print("Falha no salvamento das imagens.")
        
    print("Recortando imagem {0}".format(cont_imagem))    
    cont_imagem += 1

print("Fim da seleção e recorte das imagens!")