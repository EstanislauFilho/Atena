#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:54:18 2020

@author: estanislau
"""

import pygame
import time

largura, altura = 499, 325

corVermelhoForte = (255, 0, 0)
corVerdeForte = (0, 255, 0)
corAzulForte = (0, 0, 255)

corVermelhoFraco = (200, 0, 0)
corVerdeFraco = (0, 200, 0)
corAzulFraco = (0, 0, 200)


btnEntrarTelaInicial = [175, 150, 150, 35]
btnSairTelaInicial = [175, 195, 150, 35]

btnConfirmaSim = [75, 230, 150, 35]
btnConfirmaNao = [275, 230, 150, 35]


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
imgFundoTelaFim = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/telaFim.png")

imgFundoFutebol = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/futebol.png")
imgFundoIgreja = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/igreja.png")
imgFundoTeatro = pygame.image.load("/home/estanislau/Projetos/Atena/Interface_Grafica/Imagens_v1/teatro.png")

frameRate = 15

configTexto = pygame.font.Font('freesansbold.ttf', 25)


executaTelaSelecionaDestino = True
executaTelaConfirmaDestino = True
executaTelaCarregaConfiguracoes = True


def telaInicial():
    executaTelaInicial = True
    clickBtnEntrar = False
    
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
                executaTelaInicial = False
                clickBtnEntrar = True

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
            fundo.blit(textoEntrar, (210, 156))
            
            textoSair = configTexto.render("Sair", True, (0, 0, 0))
            fundo.blit(textoSair, (225, 201))
            
            pygame.display.update()
            clock.tick(frameRate)
            
    return clickBtnEntrar


def telaSelecionaDestino(executa):
    time.sleep(0.3)
    
    executaTelaSelecionaDestino = executa
    destino = "nda"
    
    while(executaTelaSelecionaDestino):      
        mouse = pygame.mouse.get_pos()
        clickMouse = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():       
            #print(event)
            
            if event.type == pygame.QUIT:
                executaTelaSelecionaDestino = False
                
        fundo.fill((0, 0, 0))
        fundo.blit(imgFundoSelecionaDestino, (0, 0))
        
        fundo.blit(imgFundoFutebol, (55, 130))
        fundo.blit(imgFundoIgreja, (215, 130))
        fundo.blit(imgFundoTeatro, (375, 130))
        
        
        if 15+150 > mouse[0] > 15 and 240+35 > mouse[1] > 240:
            pygame.draw.rect(fundo, corVerdeForte, btnSelecionaFutebol)
            if clickMouse[0] == 1:
                destino = "futebol"
                executaTelaSelecionaDestino = False
        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnSelecionaFutebol)
        
        
        if 175+150 > mouse[0] > 175 and 240+35 > mouse[1] > 240:
            pygame.draw.rect(fundo, corVerdeForte, btnSelecionaIgreja)
            if clickMouse[0] == 1:
                destino = "igreja"
                executaTelaSelecionaDestino = False
        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnSelecionaIgreja)
        
        
        if 335+150 > mouse[0] > 335 and 240+35 > mouse[1] > 240:
            pygame.draw.rect(fundo, corVerdeForte, btnSelecionaTeatro)
            if clickMouse[0] == 1:
                destino = "teatro"
                executaTelaSelecionaDestino = False
        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnSelecionaTeatro)
        
        
        if executaTelaSelecionaDestino is True:    
            textoFutebol = configTexto.render("Futebol", True, (0, 0, 0))
            fundo.blit(textoFutebol, (45, 246))
            
            textoIgreja = configTexto.render("Igreja", True, (0, 0, 0))
            fundo.blit(textoIgreja, (215, 246))
            
            textoTeatro = configTexto.render("Teatro", True, (0, 0, 0))
            fundo.blit(textoTeatro, (370, 246))
                      
            pygame.display.update()
            clock.tick(frameRate)

    return destino


def confirmaDestino(destino):
    time.sleep(0.3)
    
    destinoEstadio, destinoIgreja, destinoTeatro = False, False, False
    
    if destino == "nda":
        executaTelaConfirmaDestino = False
    else:
        executaTelaConfirmaDestino = True
    

    while(executaTelaConfirmaDestino):      
        mouse = pygame.mouse.get_pos()
        clickMouse = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():       
            #print(event)
            
            if event.type == pygame.QUIT:
                executaTelaConfirmaDestino = False
             
        #print(mouse)
                
        fundo.fill((0, 0, 0))
        fundo.blit(imgFundoConfirmaDestino, (0, 0))
        
        if destino == "futebol":
            fundo.blit(imgFundoFutebol, (210, 110))
            destinoEstadio, destinoIgreja, destinoTeatro = True, False, False
            
        if destino == "igreja":
            fundo.blit(imgFundoIgreja, (210, 110))
            destinoEstadio, destinoIgreja, destinoTeatro = False, True, False
            
        if destino == "teatro":
            fundo.blit(imgFundoTeatro, (210, 110))
            destinoEstadio, destinoIgreja, destinoTeatro = False, False, True
        
        
        
        if 75+150 > mouse[0] > 75 and 230+35 > mouse[1] > 230:
            pygame.draw.rect(fundo, corVerdeForte, btnConfirmaSim)
            
            if clickMouse[0] == 1 and destino == "futebol":
                print("Clicando no botão sim")
                destinoEstadio, destinoIgreja, destinoTeatro = True, False, False
                executaTelaConfirmaDestino = False
                
            if clickMouse[0] == 1 and destino == "igreja":
                print("Clicando no botão sim")
                destinoEstadio, destinoIgreja, destinoTeatro = False, True, False
                executaTelaConfirmaDestino = False
                
            if clickMouse[0] == 1 and destino == "teatro":
                print("Clicando no botão sim")
                destinoEstadio, destinoIgreja, destinoTeatro = False, False, True
                executaTelaConfirmaDestino = False
                
                
        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnConfirmaSim)
        
        if 275+150 > mouse[0] > 275 and 230+35 > mouse[1] > 230:
            pygame.draw.rect(fundo, corVermelhoForte, btnConfirmaNao)
            if clickMouse[0] == 1:
                print("Clicando no botão não")
                destinoEstadio, destinoIgreja, destinoTeatro = False, False, False
                destino = telaSelecionaDestino(True)
                destinoEstadio, destinoIgreja, destinoTeatro = confirmaDestino(destino)
                executaTelaConfirmaDestino = False

        else:
            pygame.draw.rect(fundo, corVermelhoFraco, btnConfirmaNao)
        
             
        if executaTelaConfirmaDestino is True:
            textoEntrar = configTexto.render("Sim", True, (0, 0, 0))
            fundo.blit(textoEntrar, (122, 236))
            
            textoSair = configTexto.render("Não", True, (0, 0, 0))
            fundo.blit(textoSair, (325, 236))
            
            pygame.display.update()
            clock.tick(frameRate)
            
    return destinoEstadio, destinoIgreja, destinoTeatro
  

def telaFim():
    executaTelaFim = True
    clickBtnOk = False
    
    while(executaTelaFim):      
        mouse = pygame.mouse.get_pos()
        clickMouse = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():       
            #print(event)
            
            if event.type == pygame.QUIT:
                executaTelaFim = False
             
        #print(mouse)
                
        fundo.fill((0, 0, 0))
        fundo.blit(imgFundoTelaFim, (0, 0))
        
        if 175+150 > mouse[0] > 175 and 150+35 > mouse[1] > 150:
            pygame.draw.rect(fundo, corVerdeForte, btnEntrarTelaInicial)
            if clickMouse[0] == 1:
                print("Clicando no botão entrar")
                executaTelaFim = False
                clickBtnOk = True

        else:
            pygame.draw.rect(fundo, corVerdeFraco, btnEntrarTelaInicial)
        

        
        if executaTelaFim is True:
            textoOk = configTexto.render("Ok", True, (0, 0, 0))
            fundo.blit(textoOk, (230, 156))
            
            pygame.display.update()
            clock.tick(frameRate)
            
    return clickBtnOk



telaFim()
             
#clickBtnEntrar = telaInicial()

#destino = telaSelecionaDestino(clickBtnEntrar)

#destinoEstadio, destinoIgreja, destinoTeatro = confirmaDestino(destino)

#print(destinoEstadio, destinoIgreja, destinoTeatro)

pygame.quit()
