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










def detectaBordaEsqCMD1(img):
    xp, yp = xb, yb = x_Esq, y_Esq = 0, Y1 
    
    cont_p = 0
    cont_b = 0
    
    for x in range(1, 339):
        canalCoresBordaEsq1 = img[Y1, x]  
        if canalCoresBordaEsq1 < 240:
            img[Y1, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y1
            for x in range(x, 339):
                canalCoresBordaEsq1 = img[Y1, x]  
                if canalCoresBordaEsq1 > 240:
                    img[Y1, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y1
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


def detectaBordaDirCMD4(img):
    xp, yp = xb, yb = x_Dir, y_Dir = 679, Y4
      
    cont_p = 0
    cont_b = 0
    
    for x in range(679, 341, -1):
        canalCoresBordaDir4 = img[Y4, x]  
        if canalCoresBordaDir4 < 240:
            img[Y4, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y4
            for x in range(x, 341, -1):
                canalCoresBordaDir4 = img[Y4, x]  
                if canalCoresBordaDir4 > 240:
                    img[Y4, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y4
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

def detectaBordaDirCMD3(img):
    xp, yp = xb, yb = x_Dir, y_Dir = 679, Y3
      
    cont_p = 0
    cont_b = 0
    
    for x in range(679, 341, -1):
        canalCoresBordaDir3 = img[Y3, x]  
        if canalCoresBordaDir3 < 240:
            img[Y3, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y3
            for x in range(x, 341, -1):
                canalCoresBordaDir3 = img[Y3, x]  
                if canalCoresBordaDir3 > 240:
                    img[Y3, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y3
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

def detectaBordaDirCMD2(img):
    xp, yp = xb, yb = x_Dir, y_Dir = 679, Y2
      
    cont_p = 0
    cont_b = 0
    
    for x in range(679, 341, -1):
        canalCoresBordaDir2 = img[Y2, x]  
        if canalCoresBordaDir2 < 240:
            img[Y2, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y2
            for x in range(x, 341, -1):
                canalCoresBordaDir2 = img[Y2, x]  
                if canalCoresBordaDir2 > 240:
                    img[Y2, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y2
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

def detectaBordaDirCMD1(img):
    xp, yp = xb, yb = x_Dir, y_Dir = 679, Y1
      
    cont_p = 0
    cont_b = 0
    
    for x in range(679, 341, -1):
        canalCoresBordaDir1 = img[Y1, x]  
        if canalCoresBordaDir1 < 240:
            img[Y1, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y1
            for x in range(x, 341, -1):
                canalCoresBordaDir1 = img[Y1, x]  
                if canalCoresBordaDir1 > 240:
                    img[Y1, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y1
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


def deteccaoObstaculosCamada1(img, x_esq0, y_esq0, x_dir0, y_dir0):
    pass

def deteccaoObstaculosCamada0(img, x_esq0, y_esq0, x_dir0, y_dir0):
    #print(x_esq0, y_esq0, x_dir0, y_dir0)
    cont_esq = 0
    cont_dir = 0
    
    auxEsq1 = 1000
    auxEsq2 = 0
    
    auxDir1 = 1000
    auxDir2 = 0

    for x in range(x_esq0, 339):
        canalCoresBordaEsq0 = img[Y0, x]   
        
        if canalCoresBordaEsq0 >= auxEsq2:
            auxEsq2 = canalCoresBordaEsq0
            
        if canalCoresBordaEsq0 < auxEsq1:
            auxEsq1 = canalCoresBordaEsq0
            
        if auxEsq2 > (auxEsq1*1.20):
            pass
        
        #print(auxEsq1, auxEsq2, canalCoresBordaEsq0)
        
        img[Y0, x] = 255
        cont_esq += 1

    
    if x_dir0 < 679:
        for x in range(x_dir0, 341, -1):
            canalCoresBordaDir0 = img[Y0, x]
            
            if canalCoresBordaDir0 >= auxDir2:
                auxDir2 = canalCoresBordaDir0
                
            if canalCoresBordaDir0 < auxDir1:
                auxDir1 = canalCoresBordaDir0
                
            if auxDir2 > (auxDir1*1.20):
                pass
            
            #print(auxDir1, auxDir2, canalCoresBordaDir0)
            
            img[Y0, x] = 255
            cont_dir += 1
   
        
    print()   
        
try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0)
        imagem_tresh = cv2.inRange(imagem_blur,  200, 255) 
                
        x_esq0, y_esq0 = detectaBordaEsqCMD0(imagem_tresh)
        x_esq1, y_esq1 = detectaBordaEsqCMD1(imagem_tresh)
        
        '''
        x_esq1, y_esq1 = detectaBordaEsqCMD1(imagem_tresh)
        x_esq2, y_esq2 = detectaBordaEsqCMD2(imagem_tresh)
        x_esq3, y_esq3 = detectaBordaEsqCMD3(imagem_tresh)
        x_esq4, y_esq4 = detectaBordaEsqCMD4(imagem_tresh)
        x_esq5, y_esq5 = detectaBordaEsqCMD5(imagem_tresh)
        '''
        
        x_dir0, y_dir0 = detectaBordaDirCMD0(imagem_tresh)
        x_dir1, y_dir1 = detectaBordaDirCMD1(imagem_tresh)
        '''
        x_dir2, y_dir2 = detectaBordaDirCMD2(imagem_tresh)           
        x_dir3, y_dir3 = detectaBordaDirCMD3(imagem_tresh)
        x_dir4, y_dir4 = detectaBordaDirCMD4(imagem_tresh)
        x_dir5, y_dir5 = detectaBordaDirCMD5(imagem_tresh)
        '''
        
        #deteccaoObstaculosCamada0(imagem_cinza, x_esq0, y_esq0, x_dir0, y_dir0)
        
        
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