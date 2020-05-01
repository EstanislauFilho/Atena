#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:38:13 2020

@author: estanislau
"""


def DetectaObstaculos(imgBin, vet):

  #Variáveis e limiares
  minimo_livre_inf = 200 #na parte de baixo da imagem
  minimo_livre_sup = 110 #na parte de cima da imagem
  num_perfis = 15 #quantidade de perfis a serem analisados na imagem

  largura, altura = imgBin.shape()

  print("Largura = {0} Altura = {1}".format(largura, altura))

  passo_vertical = altura/num_perfis

  linhas, colunas = 6, 50
  matriz_contagem[linhas][50]