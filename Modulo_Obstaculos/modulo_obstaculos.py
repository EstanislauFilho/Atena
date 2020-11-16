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


for x in range(340, 679):
    B0, G0, R0 = imagem[320, x] 
    if B0  <= 254 and G0  <= 254 and R0 <= 254:
        imagem[320, x] = 255, 255, 255
    else:
        break


for x in range(340, 679):
    B1, G1, R1 = imagem[340, x]
    if B1  <= 254 and G1  <= 254 and R1 <= 254:
        imagem[340, x] = 255, 255, 255
    else:
        break
  
    
for x in range(340, 679):
    B2, G2, R2 = imagem[360, x]   
    if B2  <= 254 and G2  <= 254 and R2 <= 254:
        imagem[360, x] = 255, 255, 255
    else:
        break


for x in range(340, 679):
    B3, G3, R3 = imagem[380, x]
    if B3  <= 254 and G3  <= 254 and R3 <= 254:
        imagem[380, x] = 255, 255, 255
    else:
        break


for x in range(340, 679):
    B4, G4, R4 = imagem[400, x]
    if B4  <= 254 and G4  <= 254 and R4 <= 254:
        imagem[400, x] = 255, 255, 255
    else:
        break


for x in range(340, 0, -1):
    B0, G0, R0 = imagem[320, x]
    B1, G1, R1 = imagem[340, x]
    B2, G2, R2 = imagem[360, x]
    B3, G3, R3 = imagem[380, x]
    B4, G4, R4 = imagem[400, x]
    
    if B0  >= 254 and G0  >= 254 and R0 >= 254:
        break

for x in range(340, 679):
    #imagem[320, x] = 255, 255, 255
    #imagem[340, x] = 255, 255, 255
    #imagem[360, x] = 255, 255, 255
    #imagem[380, x] = 255, 255, 255
    #imagem[400, x] = 255, 255, 255
    pass

for x in range(340, 0, -1):
    imagem[320, x] = 255, 255, 255
    imagem[340, x] = 255, 255, 255
    imagem[360, x] = 255, 255, 255
    imagem[380, x] = 255, 255, 255
    imagem[400, x] = 255, 255, 255

imagem[320, 340] = 0, 0, 255
imagem[340, 340] = 0, 0, 255
imagem[360, 340] = 0, 0, 255
imagem[380, 340] = 0, 0, 255
imagem[400, 340] = 0, 0, 255


cv2.imshow("Imagem Pista", imagem)
cv2.waitKey(0)
            
cv2.destroyAllWindows()	

'''
try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
    
        cv2.imshow("Imagem Pista", imagem)
        cv2.waitKey(0)
            
        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()	

except KeyboardInterrupt:
    cv2.destroyAllWindows()
    sys.exit()
    
finally:
    cv2.destroyAllWindows()
'''
    