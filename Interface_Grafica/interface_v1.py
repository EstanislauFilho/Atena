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

btnEntrarTelaInicial = [175, 150, 150, 35]
btnSairTelaInicial = [175, 195, 150, 35]


pygame.init()

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Atena 2020")
clock = pygame.time.Clock()

imgFundoTelaInicial = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaInicial.png")
imgFundoSelecionaDestino = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaSelecionaDestino.png")
imgFundoConfirmaDestino = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaConfirmaDestino.png")
imgFundoCarregaConfiguracoes1 = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaConfig1.png")
imgFundoCarregaConfiguracoes2 = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaConfig2.png")
imgFundoCarregaConfiguracoes3 = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaConfig3.png")
imgFundoCarregaConfiguracoes4 = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaConfig4.png")
imgFundoCarregaConfiguracoes5 = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaConfig5.png")
imgFundoCarregaConfiguracoes6 = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaConfig6.png")


configTexto = pygame.font.Font('freesansbold.ttf', 25)

executaTelaInicial = True
executaTelaSelecionaDestino = True
executaTelaConfirmaDestino = True
executaTelaCarregaConfiguracoes = True

destinoEstadio, destinoIgreja, destinoTeatro = False, False, False

while(executaTelaInicial):
    
    for event in pygame.event.get():       
        print(event)
        
        if event.type == pygame.QUIT:
            executaTelaInicial = False
            pygame.quit()
            
            
    
    fundo.fill(cor_azul)
    fundo.blit(imgFundoTelaInicial, (0, 0))
    
    pygame.draw.rect(fundo, cor_verde, btnEntrarTelaInicial)
    pygame.draw.rect(fundo, cor_vermelho, btnSairTelaInicial)
    
    textoEntrar = configTexto.render("Entrar", True, (0, 0, 0))
    fundo.blit(textoEntrar, (206, 154))
    
    textoSair = configTexto.render("Sair", True, (0, 0, 0))
    fundo.blit(textoSair, (220, 199))
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()