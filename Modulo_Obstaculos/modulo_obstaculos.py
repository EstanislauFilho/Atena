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



Y0 = 350 
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





def detectaBordaEsqCMD0(img):
    xp, yp = xb, yb = x_Esq, y_Esq = 0, Y0 
    
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
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xb, yb
    elif(cont_b > 40) and (cont_p <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xp, yp
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        pass
    
    #print(cont_p, cont_b)
    #print(x_Esq, y_Esq)
    #print()
    return x_Esq, y_Esq


def detectaBordaDirCMD0(img):
    xp, yp = xb, yb = x_Dir, y_Dir = 679, Y0
      
    cont_p = 0
    cont_b = 0
    
    for x in range(679, 341, -1):
        canalCoresBordaDir0 = img[Y0, x]  
        if canalCoresBordaDir0 < 240:
            img[Y0, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y0
            for x in range(x, 341, -1):
                canalCoresBordaDir0 = img[Y0, x]  
                if canalCoresBordaDir0 > 240:
                    img[Y0, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y0
                    break
            break
    if(cont_b >= 25 and cont_b <= 40) and (cont_p <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Dir, y_Dir = xb, yb
    elif(cont_b > 40) and (cont_p <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Dir, y_Dir = xp, yp
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        pass
    
    #print(cont_p, cont_b)
    #print(x_Dir, y_Dir)
    #print()
    return x_Dir, y_Dir


def deteccaoObstaculosCamada0(img, x_esq0, y_esq0, x_dir0, y_dir0):
   
    for x in range(x_esq0, 339):
        canalCoresBordaEsq0 = img[Y0, x] 
        print(canalCoresBordaEsq0)
        
        img[Y0, x] = 255

    for x in range(x_dir0, 341, -1):
        #canalCoresBordaDir0 = img[Y0, x]
        img[Y0, x] = 255
        
    print()   
        
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
        
        deteccaoObstaculosCamada0(imagem_cinza, x_esq0, y_esq0, x_dir0, y_dir0)
        
        
        #cv2.imshow("Imagem Pista", imagem)
        cv2.imshow("Imagem Cinza", imagem_cinza)
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