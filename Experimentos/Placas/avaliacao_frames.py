#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:40:46 2020

@author: estanislau
"""


import cv2
import glob


numero_pasta = 10

caminho_pasta = '/home/estanislau/Projetos/Atena/Frames/frames_video_plc_'+str(numero_pasta)+'/*.jpg'

n_placa_1, c_placa_1 = "Pare", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_pare.xml')
n_placa_2, c_placa_2 = "Pedestre", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_pedestre.xml')
n_placa_3, c_placa_3 = "Desvio", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_desvio.xml')
n_placa_4, c_placa_4 = "80 Km/h", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_60.xml')
n_placa_5, c_placa_5 = "Obras", cv2.CascadeClassifier('/home/estanislau/Projetos/Atena/Modulo_Placas/Classificadores/cascade_obras.xml')

#classificadores = [(n_placa_1, c_placa_1), (n_placa_2, c_placa_2), (n_placa_3, c_placa_3), (n_placa_4, c_placa_4), (n_placa_5, c_placa_5)]

total_deteccao_plc_pare = 0
total_deteccao_plc_pedestre = 0
total_deteccao_plc_desvio = 0
total_deteccao_plc_velocidade = 0
total_deteccao_plc_obras = 0

def detecta_placa_pare(img, nome, classificador):
    global total_deteccao_plc_pare
    plc_pare = False
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_placa = classificador.detectMultiScale(img_gray, scaleFactor = 1.090, minNeighbors = 10, minSize=(25, 25), maxSize=(80, 80))
    
    for (x,y,w,h) in img_placa:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 191, 255), 2)
        cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 191, 255), 2)
        plc_pare = True
        total_deteccao_plc_pare += 1
                   
    return plc_pare


def detecta_placa_pedestre(img, nome, classificador):
    global total_deteccao_plc_pedestre
    plc_pedestre = False
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_placa = classificador.detectMultiScale(img_gray, scaleFactor = 1.090, minNeighbors = 7, minSize=(15, 15), maxSize=(85, 85))
    
    for (x,y,w,h) in img_placa:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 191, 255), 2)
        cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 191, 255), 2)
        plc_pedestre = True
        total_deteccao_plc_pedestre += 1
                   
    return plc_pedestre


def detecta_placa_desvio(img, nome, classificador):
    global total_deteccao_plc_desvio
    plc_desvio = False
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_placa = classificador.detectMultiScale(img_gray, scaleFactor = 1.099, minNeighbors = 10, minSize=(10, 5), maxSize=(120, 60))
    
    for (x,y,w,h) in img_placa:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 191, 255), 2)
        cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 191, 255), 2)
        plc_desvio = True
        total_deteccao_plc_desvio += 1
                   
    return plc_desvio


def detecta_placa_velocidade(img, nome, classificador):
    global total_deteccao_plc_velocidade
    plc_velocidade = False
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_placa = classificador.detectMultiScale(img_gray, scaleFactor = 1.095, minNeighbors = 10, minSize=(10, 10), maxSize=(80, 80))
    
    for (x,y,w,h) in img_placa:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 191, 255), 2)
        cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 191, 255), 2)
        plc_velocidade = True
        total_deteccao_plc_velocidade += 1         
          
    return plc_velocidade


def detecta_placa_obras(img, nome, classificador):
    global total_deteccao_plc_obras
    plc_obras = False
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_placa = classificador.detectMultiScale(img_gray, scaleFactor = 1.095, minNeighbors = 7, minSize=(25, 25), maxSize=(100, 100))
    
    for (x,y,w,h) in img_placa:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 191, 255), 2)
        cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 191, 255), 2)
        plc_obras = True
        total_deteccao_plc_obras += 1          
          
    return plc_obras



cont_imagem = 1000
try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        
        imagem_placas_esq = imagem.copy()
        imagem_placas_dir = imagem.copy()
        
        # Imagem das placas da esquerda
        imagem_placas_esq = imagem_placas_esq[160:420, 0:260] 
        
        # Imagem das placas da direita
        imagem_placas_dir = imagem_placas_dir[160:420, 420:680]
    
           
        plc_pare = detecta_placa_pare(imagem_placas_dir, n_placa_1, c_placa_1)
        
        plc_pedestre = detecta_placa_pedestre(imagem_placas_dir, n_placa_2, c_placa_2)
        
        plc_desvio = detecta_placa_desvio(imagem_placas_dir, n_placa_3, c_placa_3)
        
        plc_80 = detecta_placa_velocidade(imagem_placas_dir, n_placa_4, c_placa_4)
        
        plc_obras = detecta_placa_obras(imagem_placas_esq, n_placa_5, c_placa_5)
        plc_obras = detecta_placa_obras(imagem_placas_dir, n_placa_5, c_placa_5)
        
        print("{0} | {1} | {2} | {3} | {4} | Frame: {5}".format(plc_pare, plc_pedestre, plc_desvio, plc_80, plc_obras, cont_imagem))   
        #print("Frame: {0}".format(cont_imagem))   
        
        #cv2.imshow("Apresenta Imagens", imagem)
        cv2.imshow("Imagem das placas da esquerda", imagem_placas_esq)
        cv2.imshow("Imagem das placas da direita", imagem_placas_dir)
        cv2.waitKey(0)
        

        cont_imagem += 1
        
        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()	
        
        
    print(total_deteccao_plc_pare, total_deteccao_plc_pedestre, total_deteccao_plc_desvio, total_deteccao_plc_velocidade, total_deteccao_plc_obras)
except:
    cv2.destroyAllWindows()

finally:
    cv2.destroyAllWindows()