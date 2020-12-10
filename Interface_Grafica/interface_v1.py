#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:54:18 2020

@author: estanislau
"""

import pygame

largura, altura = 499, 325

pygame.init()

pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Atena v1")

executa = True

while(executa):
    
    for event in pygame.event.get():
        
        print(event)
        
        if event.type == pygame.QUIT:
            executa = False
    
    pygame.display.update()


pygame.quit()
