#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:08:54 2020

@author: estanislau
"""

import cv2
import glob
import sys

numero_pasta = 0

caminho_pasta = '/home/estanislau/Projetos/TCC/frames_video_plc_'+str(numero_pasta)+'/*.jpg'


imagem = cv2.imread("/home/estanislau/Projetos/TCC/frames_video_plc_0/10000.jpg")

def define_pontos(imagem):
    for x in range(341, 679):
        B0_DIR, G0_DIR, R0_DIR = imagem[320, x] 
        if B0_DIR  <= 254 and G0_DIR  <= 254 and R0_DIR <= 254:
            imagem[320, x] = 255, 255, 255
        else:
            break
    
    
    for x in range(341, 679):
        B1_DIR, G1_DIR, R1_DIR = imagem[340, x]
        if B1_DIR  <= 254 and G1_DIR  <= 254 and R1_DIR <= 254:
            imagem[340, x] = 255, 255, 255
        else:
            break
      
        
    for x in range(341, 679):
        B2_DIR, G2_DIR, R2_DIR = imagem[360, x]   
        if B2_DIR  <= 254 and G2_DIR  <= 254 and R2_DIR <= 254:
            imagem[360, x] = 255, 255, 255
        else:
            break
    
    
    for x in range(341, 679):
        B3_DIR, G3_DIR, R3_DIR = imagem[380, x]
        if B3_DIR  <= 254 and G3_DIR  <= 254 and R3_DIR <= 254:
            imagem[380, x] = 255, 255, 255
        else:
            break
    
    
    for x in range(341, 679):
        B4_DIR, G4_DIR, R4_DIR = imagem[400, x]
        if B4_DIR  <= 254 and G4_DIR  <= 254 and R4_DIR <= 254:
            imagem[400, x] = 255, 255, 255
        else:
            break
    
    ######################################################################
    
    for x in range(339, 0, -1):
        B0_ESQ, G0_ESQ, R0_ESQ = imagem[320, x] 
        if B0_ESQ  <= 254 and G0_ESQ  <= 254 and R0_ESQ <= 254:
            imagem[320, x] = 255, 255, 255
        else:
            break
    
    
    for x in range(339, 0, -1):
        B1_ESQ, G1_ESQ, R1_ESQ = imagem[340, x]
        if B1_ESQ  <= 254 and G1_ESQ  <= 254 and R1_ESQ <= 254:
            imagem[340, x] = 255, 255, 255
        else:
            break
      
        
    for x in range(339, 0, -1):
        B2_ESQ, G2_ESQ, R2_ESQ = imagem[360, x]   
        if B2_ESQ  <= 254 and G2_ESQ  <= 254 and R2_ESQ <= 254:
            imagem[360, x] = 255, 255, 255
        else:
            break
    
    
    for x in range(339, 0, -1):
        B3_ESQ, G3_ESQ, R3_ESQ = imagem[380, x]
        if B3_ESQ  <= 254 and G3_ESQ  <= 254 and R3_ESQ <= 254:
            imagem[380, x] = 255, 255, 255
        else:
            break
    
    
    for x in range(339, 0, -1):
        B4_ESQ, G4_ESQ, R4_ESQ = imagem[400, x]
        if B4_ESQ  <= 254 and G4_ESQ  <= 254 and R4_ESQ <= 254:
            imagem[400, x] = 255, 255, 255
        else:
            break
    
    
    
    imagem[320, 340] = 0, 0, 255
    imagem[340, 340] = 0, 0, 255
    imagem[360, 340] = 0, 0, 255
    imagem[380, 340] = 0, 0, 255
    imagem[400, 340] = 0, 0, 255




try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
    
        define_pontos(imagem)
        
        cv2.imshow("Imagem Pista", imagem)
        cv2.waitKey(0)
            
        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()	

except KeyboardInterrupt:
    cv2.destroyAllWindows()
    sys.exit()
    
finally:
    cv2.destroyAllWindows()

    