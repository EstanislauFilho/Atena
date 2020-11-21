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


x_dir0, y_dir0 = 0, 0
x_dir1, y_dir1 = 0, 0
x_dir2, y_dir2 = 0, 0
x_dir3, y_dir3 = 0, 0
x_dir4, y_dir4 = 0, 0
x_dir5, y_dir5 = 0, 0

x_esq0, y_esq0 = 0, 0
x_esq1, y_esq1 = 0, 0
x_esq2, y_esq2 = 0, 0
x_esq3, y_esq3 = 0, 0
x_esq4, y_esq4 = 0, 0
x_esq5, y_esq5 = 0, 0


def detectaBordaDirCMD5(img):
    x_Dir_CMD, y_Dir_CMD = 0, Y5
    for x in range(679, 339, -1):
        canalCoresBordaDir5 = img[Y5, x]  
        if canalCoresBordaDir5 < 240:
            img[Y5, x] = 255
        else:
            for x in range(x, 339, -1):
                canalCoresBordaDir5 = img[Y5, x]  
                if canalCoresBordaDir5 > 240:
                    img[Y5, x] = 0
                else:
                    x_Dir_CMD = x 
                    y_Dir_CMD = Y5
                    break
            break
    return x_Dir_CMD, y_Dir_CMD


def detectaBordaEsqCMD5(img):
    x_Esq_CMD, y_Esq_CMD = 0, Y5
    for x in range(1, 339):
        canalCoresBordaEsq5 = img[Y5, x]  
        if canalCoresBordaEsq5 < 240:
            img[Y5, x]  = 255
        else:
            for x in range(x, 339):
                canalCoresBordaEsq5 = img[Y5, x]  
                if canalCoresBordaEsq5 > 240:
                    img[Y5, x]  = 0
                else:
                    x_Esq_CMD = x
                    y_Esq_CMD = Y5
                    break
            break  
    return x_Esq_CMD, y_Esq_CMD


def detectaBordaDirCMD4(img):
    x_Dir_CMD, y_Dir_CMD = 0, Y4
    for x in range(679, 339, -1):
        canalCoresBordaDir4 = img[Y4, x]  
        if canalCoresBordaDir4 < 240:
            img[Y4, x] = 255
        else:
            for x in range(x, 339, -1):
                canalCoresBordaDir4 = img[Y4, x]  
                if canalCoresBordaDir4 > 240:
                    img[Y4, x] = 0
                else:
                    x_Dir_CMD = x 
                    y_Dir_CMD = Y4
                    break
            break
    return x_Dir_CMD, y_Dir_CMD


def detectaBordaEsqCMD4(img):
    x_Esq_CMD, y_Esq_CMD = 0, Y4
    for x in range(1, 339):
        canalCoresBordaEsq4 = img[Y4, x]  
        if canalCoresBordaEsq4 < 240:
            img[Y4, x]  = 255
        else:
            for x in range(x, 339):
                canalCoresBordaEsq4 = img[Y4, x]  
                if canalCoresBordaEsq4 > 240:
                    img[Y4, x]  = 0
                else:
                    x_Esq_CMD = x
                    y_Esq_CMD = Y4
                    break
            break  
    return x_Esq_CMD, y_Esq_CMD


def detectaBordaDirCMD3(img):
    x_Dir_CMD, y_Dir_CMD = 0, Y3
    for x in range(679, 339, -1):
        canalCoresBordaDir3 = img[Y3, x]  
        if canalCoresBordaDir3 < 240:
            img[Y3, x] = 255
        else:
            for x in range(x, 339, -1):
                canalCoresBordaDir3 = img[Y3, x]  
                if canalCoresBordaDir3 > 240:
                    img[Y3, x] = 0
                else:
                    x_Dir_CMD = x 
                    y_Dir_CMD = Y3
                    break
            break
    return x_Dir_CMD, y_Dir_CMD


def detectaBordaEsqCMD3(img):
    x_Esq_CMD, y_Esq_CMD = 0, Y3
    for x in range(1, 339):
        canalCoresBordaEsq3 = img[Y3, x]  
        if canalCoresBordaEsq3 < 240:
            img[Y3, x]  = 255
        else:
            for x in range(x, 339):
                canalCoresBordaEsq3 = img[Y3, x]  
                if canalCoresBordaEsq3 > 240:
                    img[Y3, x]  = 0
                else:
                    x_Esq_CMD = x
                    y_Esq_CMD = Y3
                    break
            break  
    return x_Esq_CMD, y_Esq_CMD


def detectaBordaDirCMD2(img):
    x_Dir_CMD, y_Dir_CMD = 0, Y2
    for x in range(679, 339, -1):
        canalCoresBordaDir2 = img[Y2, x]  
        if canalCoresBordaDir2 < 240:
            img[Y2, x] = 255
        else:
            for x in range(x, 339, -1):
                canalCoresBordaDir2 = img[Y2, x]  
                if canalCoresBordaDir2 > 240:
                    img[Y2, x] = 0
                else:
                    x_Dir_CMD = x 
                    y_Dir_CMD = Y2
                    break
            break
    return x_Dir_CMD, y_Dir_CMD


def detectaBordaEsqCMD2(img):
    x_Esq_CMD, y_Esq_CMD = 0, Y2
    for x in range(1, 339):
        canalCoresBordaEsq2 = img[Y2, x]  
        if canalCoresBordaEsq2 < 240:
            img[Y2, x]  = 255
        else:
            for x in range(x, 339):
                canalCoresBordaEsq2 = img[Y2, x]  
                if canalCoresBordaEsq2 > 240:
                    img[Y2, x]  = 0
                else:
                    x_Esq_CMD = x
                    y_Esq_CMD = Y2
                    break
            break  
    return x_Esq_CMD, y_Esq_CMD


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
    xp, yp = 0, Y0
    xb, yb = 0, Y0
    x_Esq, y_Esq = 0, Y0
    
    cont_p = 0
    cont_b = 0
    
    for x in range(1, 339):
        canalCoresBordaEsq0 = img[Y0, x]  
        if canalCoresBordaEsq0 < 240:
            img[Y0, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y0
            for x in range(x, 339):
                canalCoresBordaEsq0 = img[Y0, x]  
                if canalCoresBordaEsq0 > 240:
                    img[Y0, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y0
                    break
            break
    if(cont_b >= 25 and cont_b <= 40) and (cont_p <= 336):
        print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xb, yb
    elif(cont_b > 40) and (cont_p <= 336):
        print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xp, yp
    else:
        print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = 0, Y0
    
    #print(cont_p, cont_b)
    print(x_Esq, y_Esq)
    print()
    return x_Esq, y_Esq


def detecta_obstaculos():
    pass

try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0)
        imagem_tresh = cv2.inRange(imagem_blur,  200, 255) 
                
        x_esq0, y_esq0 = detectaBordaEsqCMD0(imagem_tresh)
        
        '''
        x_esq1, y_esq1 = detectaBordaEsqCMD1(imagem_tresh)
        x_esq2, y_esq2 = detectaBordaEsqCMD2(imagem_tresh)
        x_esq3, y_esq3 = detectaBordaEsqCMD3(imagem_tresh)
        x_esq4, y_esq4 = detectaBordaEsqCMD4(imagem_tresh)
        x_esq5, y_esq5 = detectaBordaEsqCMD5(imagem_tresh)
        '''
        
        x_dir0, y_dir0 = detectaBordaDirCMD0(imagem_tresh)
        '''
        x_dir1, y_dir1 = detectaBordaDirCMD1(imagem_tresh)
        x_dir2, y_dir2 = detectaBordaDirCMD2(imagem_tresh)           
        x_dir3, y_dir3 = detectaBordaDirCMD3(imagem_tresh)
        x_dir4, y_dir4 = detectaBordaDirCMD4(imagem_tresh)
        x_dir5, y_dir5 = detectaBordaDirCMD5(imagem_tresh)
        '''
        
        
        
        #cv2.imshow("Imagem Pista", imagem)
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