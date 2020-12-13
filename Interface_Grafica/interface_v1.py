#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:54:18 2020

@author: estanislau
"""

import pygame


largura, altura = 499, 325

corVermelhoForte = (255, 0, 0)
corVerdeForte = (0, 255, 0)
corAzulForte = (0, 0, 255)

corVermelhoFraco = (200, 0, 0)
corVerdeFraco = (0, 200, 0)
corAzulFraco = (0, 0, 200)


btnEntrarTelaInicial = [175, 150, 150, 35]
btnSairTelaInicial = [175, 195, 150, 35]

btnSelecionaFutebol = [15, 240, 150, 35]
btnSelecionaIgreja = [175, 240, 150, 35]
btnSelecionaTeatro = [335, 240, 150, 35]


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

imgFundoFutebol = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/futebol.png")
imgFundoIgreja = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/igreja.png")
imgFundoTeatro = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/teatro.png")



configTexto = pygame.font.Font('freesansbold.ttf', 25)


executaTelaSelecionaDestino = True
executaTelaConfirmaDestino = True
executaTelaCarregaConfiguracoes = True

destinoEstadio, destinoIgreja, destinoTeatro = False, False, False

def telaInicial():
    executaTelaInicial = True
    
    while(executaTelaInicial):      
        mouse = pygame.mouse.get_pos()
        clickMouse = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():       
            #print(event)
            
            if event.type == pygame.QUIT:
                executaTelaInicial = False
             
        #print(mouse)
                
        fundo.fill((0, 0, 0))
        fundo.blit(imgFundoTelaInicial, (0, 0))
        
        if 175+150 > mouse[0] > 175 and 150+35 > mouse[1] > 150:
            pygame.draw.rect(fundo, corVerdeForte, btnEntrarTelaInicial)
            if clickMouse[0] == 1:
                print("Clicando no botão entrar")
                TelaSelecionaDestino()
                executaTelaInicial = False
                #executaTelaInicial = False
        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnEntrarTelaInicial)
        
        if 175+150 > mouse[0] > 175 and 195+35 > mouse[1] > 195:
            pygame.draw.rect(fundo, corVermelhoForte, btnSairTelaInicial)
            if clickMouse[0] == 1:
                print("Clicando no botão sair")
                executaTelaInicial = False
        else:
            pygame.draw.rect(fundo, corVermelhoFraco, btnSairTelaInicial)
        
        if executaTelaInicial is True:
            textoEntrar = configTexto.render("Entrar", True, (0, 0, 0))
            fundo.blit(textoEntrar, (206, 154))
            
            textoSair = configTexto.render("Sair", True, (0, 0, 0))
            fundo.blit(textoSair, (220, 199))
            
            pygame.display.update()
            clock.tick(60)


def TelaSelecionaDestino():
    executaTelaSelecionaDestino = True
    
    while(executaTelaSelecionaDestino):      
        mouse = pygame.mouse.get_pos()
        clickMouse = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():       
            #print(event)
            
            if event.type == pygame.QUIT:
                executaTelaSelecionaDestino = False
                
        fundo.fill((0, 0, 0))
        fundo.blit(imgFundoSelecionaDestino, (0, 0))
        
        fundo.blit(imgFundoFutebol, (15, 30))
        
        
        if 15+150 > mouse[0] > 15 and 240+35 > mouse[1] > 240:
            pygame.draw.rect(fundo, corVerdeForte, btnSelecionaFutebol)
        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnSelecionaFutebol)
        
        
        if 175+150 > mouse[0] > 175 and 240+35 > mouse[1] > 240:
            pygame.draw.rect(fundo, corVerdeForte, btnSelecionaIgreja)
        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnSelecionaIgreja)
        
        
        if 335+150 > mouse[0] > 335 and 240+35 > mouse[1] > 240:
            pygame.draw.rect(fundo, corVerdeForte, btnSelecionaTeatro)
        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnSelecionaTeatro)
        
        
        if executaTelaSelecionaDestino is True:    
            textoFutebol = configTexto.render("Futebol", True, (0, 0, 0))
            fundo.blit(textoFutebol, (45, 245))
            
            textoIgreja = configTexto.render("Igreja", True, (0, 0, 0))
            fundo.blit(textoIgreja, (215, 245))
            
            textoTeatro = configTexto.render("Teatro", True, (0, 0, 0))
            fundo.blit(textoTeatro, (370, 245))
                      
            pygame.display.update()
            clock.tick(60)
        
telaInicial()
pygame.quit()
