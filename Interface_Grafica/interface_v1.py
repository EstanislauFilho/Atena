#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:54:18 2020

@author: estanislau
"""

import pygame


largura, altura = 499, 325

cor_vermelho = (255, 0, 0)
cor_verde = (0, 255, 0)
cor_azul = (0, 0, 255)

btn_entrar = [175, 150, 150, 35]
btn_sair = [175, 195, 150, 35]


pygame.init()

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Atena 2020")
clock = pygame.time.Clock()

imgFundoOriginal = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaInicial.png")


executa = True

while(executa):
    
    for event in pygame.event.get():
        
        print(event)
        
        if event.type == pygame.QUIT:
            executa = False
    
    fundo.fill(cor_azul)
    fundo.blit(imgFundoOriginal, (0, 0))
    
    pygame.draw.rect(fundo, cor_verde, btn_entrar)
    pygame.draw.rect(fundo, cor_vermelho, btn_sair)
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()
