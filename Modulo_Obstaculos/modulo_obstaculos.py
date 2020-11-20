#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:08:54 2020

@author: estanislau
"""

import cv2
import glob
import sys

numero_pasta = 13

caminho_pasta = '/home/estanislau/Projetos/TCC/frames_video_plc_'+str(numero_pasta)+'/*.jpg'


imagem = cv2.imread("/home/estanislau/Projetos/TCC/frames_video_plc_0/10000.jpg")



Y0 = 410 
Y1 = 390
Y2 = 370
Y3 = 350
Y4 = 330
Y5 = 310
Y6 = 290
Y7 = 270
Y8 = 250
Y9 = 230



def detectaBordaDirCMD1(img):
    x_Dir_CMD, y_Dir_CMD = 0, Y1
    for x in range(679, 339, -1):
        canalCoresBordaDir1 = img[Y1, x]  
        if canalCoresBordaDir1 < 240:
            img[Y1, x] = 255
        else:
            for x in range(x, 339, -1):
                canalCoresBordaDir1 = img[Y1, x]  
                if canalCoresBordaDir1 > 240:
                    img[Y1, x] = 0
                else:
                    x_Dir_CMD = x 
                    y_Dir_CMD = Y1
                    break
            break
    return x_Dir_CMD, y_Dir_CMD


def detectaBordaEsqCMD1(img):
    x_Esq_CMD, y_Esq_CMD = 0, Y1
    for x in range(1, 339):
        canalCoresBordaEsq1 = img[Y1, x]  
        if canalCoresBordaEsq1 < 240:
            img[Y1, x]  = 255
        else:
            for x in range(x, 339):
                canalCoresBordaEsq1 = img[Y1, x]  
                if canalCoresBordaEsq1 > 240:
                    img[Y1, x]  = 0
                else:
                    x_Esq_CMD = x
                    y_Esq_CMD = Y1
                    break
            break  
    return x_Esq_CMD, y_Esq_CMD


    
    
def detectaBordaDirCMD0(img):
    x_Dir_CMD, y_Dir_CMD = 0, Y0
    for x in range(679, 339, -1):
        canalCoresBordaDir0 = img[Y0, x]  
        if canalCoresBordaDir0 < 240:
            img[Y0, x] = 255
        else:
            for x in range(x, 339, -1):
                canalCoresBordaDir0 = img[Y0, x]  
                if canalCoresBordaDir0 > 240:
                    img[Y0, x] = 0
                else:
                    x_Dir_CMD = x 
                    y_Dir_CMD = Y0
                    break
            break
    return x_Dir_CMD, y_Dir_CMD


def detectaBordaEsqCMD0(img):
    x_Esq_CMD, y_Esq_CMD = 0, Y0
    for x in range(1, 339):
        canalCoresBordaEsq0 = img[Y0, x]  
        if canalCoresBordaEsq0 < 240:
            img[Y0, x]  = 255
        else:
            for x in range(x, 339):
                canalCoresBordaEsq0 = img[Y0, x]  
                if canalCoresBordaEsq0 > 240:
                    img[Y0, x]  = 0
                else:
                    x_Esq_CMD = x 
                    y_Esq_CMD = Y0
                    break
            break  
    return x_Esq_CMD, y_Esq_CMD


def detecta_obstaculos():
    pass

try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0)
        imagem_tresh = cv2.inRange(imagem_blur,  200, 255) 
                
        detectaBordaEsqCMD0(imagem_tresh)
        detectaBordaDirCMD0(imagem_tresh)
        
        detectaBordaEsqCMD1(imagem_tresh)
        detectaBordaDirCMD1(imagem_tresh)
    
        cv2.imshow("Imagem Pista", imagem)
        #cv2.imshow("Imagem Cinza", imagem_cinza)
        #cv2.imshow("Imagem Blur", imagem_blur)
        cv2.imshow("Imagem tresh", imagem_tresh)
        cv2.waitKey(0)
            
        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()	

except KeyboardInterrupt:
    cv2.destroyAllWindows()
    sys.exit()
    
finally:
    cv2.destroyAllWindows()


    
    
'''
imagem = cv2.imread("/home/estanislau/Projetos/TCC/frames_video_plc_0/10000.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0)
imagem_tresh = cv2.inRange(imagem_blur, 200, 255) 


     


cv2.imshow("Imagem tresh", imagem_tresh)
cv2.waitKey(0)

cv2.destroyAllWindows()
'''