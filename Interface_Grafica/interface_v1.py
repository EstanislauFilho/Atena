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


pygame.init()

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Atena v1")

executa = True

while(executa):
    
    for event in pygame.event.get():
        
        print(event)
        
        if event.type == pygame.QUIT:
            executa = False
    
    fundo.fill(cor_azul)
    pygame.draw.rect(fundo, cor_vermelho, [50, 50, 20, 20])
    
    pygame.display.update()


pygame.quit()
