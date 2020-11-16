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
    imagem[320, x] = 255, 255, 255
    imagem[340, x] = 255, 255, 255
    imagem[360, x] = 255, 255, 255
    imagem[380, x] = 255, 255, 255
    imagem[400, x] = 255, 255, 255


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
    