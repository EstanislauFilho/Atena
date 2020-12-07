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


Y0 = 280
Y1 = 310
Y2 = 340
Y3 = 370
Y4 = 400





x_dir0, y_dir0 = 0, 0
x_dir1, y_dir1 = 0, 0
x_dir2, y_dir2 = 0, 0
x_dir3, y_dir3 = 0, 0
x_dir4, y_dir4 = 0, 0

x_esq0, y_esq0 = 0, 0
x_esq1, y_esq1 = 0, 0
x_esq2, y_esq2 = 0, 0
x_esq3, y_esq3 = 0, 0
x_esq4, y_esq4 = 0, 0




def detectaBordaEsqCMD4(img):
    xp, yp = xb, yb = x_Esq, y_Esq = 0, Y4 
    
    cont_p = 0
    cont_b = 0
    
    for x in range(1, 339):
        canalCoresBordaEsq4 = img[Y4, x]  
        if canalCoresBordaEsq4 < 240:
            img[Y4, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y4
            for x in range(x, 339):
                canalCoresBordaEsq4 = img[Y4, x]  
                if canalCoresBordaEsq4 > 240:
                    img[Y4, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y4
                    break
            break
    
    if(cont_b >= 15 and cont_b <= 35) and (cont_p <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xb, yb
    elif(cont_b > 35) and (cont_b  < 50) and (cont_p <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xp, yp
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = 0, Y4
    
    #print(cont_p, cont_b)
    #print(x_Esq, y_Esq)
    #print()
    return x_Esq, y_Esq

def detectaBordaEsqCMD3(img):
    xp, yp = xb, yb = x_Esq, y_Esq = 0, Y3 
    
    cont_p = 0
    cont_b = 0
    
    for x in range(1, 339):
        canalCoresBordaEsq3 = img[Y3, x]  
        if canalCoresBordaEsq3 < 240:
            img[Y3, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y3
            for x in range(x, 339):
                canalCoresBordaEsq3 = img[Y3, x]  
                if canalCoresBordaEsq3 > 240:
                    img[Y3, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y3
                    break
            break
    
    if(cont_b >= 15 and cont_b <= 35) and (cont_p <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xb, yb
    elif(cont_b > 35) and (cont_b  < 50) and (cont_p <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xp, yp
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = 0, Y3
    
    #print(cont_p, cont_b)
    #print(x_Esq, y_Esq)
    #print()
    return x_Esq, y_Esq

def detectaBordaEsqCMD2(img):
    xp, yp = xb, yb = x_Esq, y_Esq = 0, Y2 
    
    cont_p = 0
    cont_b = 0
    
    for x in range(1, 339):
        canalCoresBordaEsq2 = img[Y2, x]  
        if canalCoresBordaEsq2 < 240:
            img[Y2, x]  = 255
            cont_p += 1
        else:
            xp = x 
            yp = Y2
            for x in range(x, 339):
                canalCoresBordaEsq2 = img[Y2, x]  
                if canalCoresBordaEsq2 > 240:
                    img[Y2, x] = 0
                    cont_b += 1
                else:
                    xb = x 
                    yb = Y2
                    break
            break
    if(cont_b >= 15 and cont_b <= 40) and (cont_p <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xb, yb
    elif(cont_b > 40) and (cont_b  < 50) and (cont_p <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = xp, yp
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        x_Esq, y_Esq = 0, Y2 
        
    #print(cont_p, cont_b)
    #print(x_Esq, y_Esq)
    #print()
    return x_Esq, y_Esq

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
    if(cont_b >= 15 and cont_b <= 40) and (cont_p <= 336):
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
    if(cont_b >= 15 and cont_b <= 40) and (cont_p <= 336):
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
    if(cont_b >= 15 and cont_b <= 40) and (cont_p <= 336):
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
    if(cont_b >= 15 and cont_b <= 40) and (cont_p <= 336):
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
    if(cont_b >= 15 and cont_b <= 40) and (cont_p <= 336):
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
    if(cont_b >= 15 and cont_b <= 40) and (cont_p <= 336):
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
      
   
def definePontosBordaEsq(img, x_esq0, x_esq1, x_esq2, x_esq3, x_esq4):
   
   if( (x_esq0 != 0 and x_esq1 == 0 and x_esq2 == 0 and x_esq3 == 0 and x_esq4 == 0) or
       (x_esq0 == 0 and x_esq1 != 0 and x_esq2 == 0 and x_esq3 == 0 and x_esq4 == 0) or
       (x_esq0 == 0 and x_esq1 == 0 and x_esq2 != 0 and x_esq3 == 0 and x_esq4 == 0) or
       (x_esq0 == 0 and x_esq1 == 0 and x_esq2 == 0 and x_esq3 != 0 and x_esq4 == 0) or
       (x_esq0 == 0 and x_esq1 == 0 and x_esq2 == 0 and x_esq3 == 0 and x_esq4 != 0)):
       x_esq0 = x_esq1 = x_esq2 = x_esq3 = x_esq4 = 0
   

   if(x_esq0 != 0 and x_esq1 != 0 and x_esq2 != 0 and x_esq3 != 0 and x_esq4 == 0):
        x_esq4 = int((x_esq0 + x_esq1 + x_esq2 + x_esq3)/4)
        
   if(x_esq0 != 0 and x_esq1 != 0 and x_esq2 != 0 and x_esq3 == 0 and x_esq4 != 0):
        x_esq3 = int((x_esq0 + x_esq1 + x_esq2 + x_esq4)/4)
        
   if(x_esq0 != 0 and x_esq1 != 0 and x_esq2 == 0 and x_esq3 != 0 and x_esq4 != 0):
        x_esq2 = int((x_esq0 + x_esq1 + x_esq3 + x_esq4)/4)  
        
   if(x_esq0 != 0 and x_esq1 == 0 and x_esq2 != 0 and x_esq3 != 0 and x_esq4 != 0):
        x_esq1 = int((x_esq0 + x_esq2 + x_esq3 + x_esq4)/4)  
  
   if(x_esq0 == 0 and x_esq1 != 0 and x_esq2 != 0 and x_esq3 != 0 and x_esq4 != 0):
        x_esq0 = int((x_esq1 + x_esq2 + x_esq3 + x_esq4)/4)


    
   if(x_esq4 > (x_esq0 + x_esq1 + x_esq2)):
       x_esq4 = int(((x_esq0 + x_esq1 + x_esq2)/3) - 15)
    
   
   if(x_esq3 > (x_esq0 + x_esq1 + x_esq2)):
       x_esq3 = int(((x_esq0 + x_esq1 + x_esq2)/3) - 15) 
   '''
   cv2.circle(img, (x_esq0, y_esq0), 5, (255, 0, 0), 2)
   cv2.circle(img, (x_esq1, y_esq1), 5, (255, 0, 0), 2)
   cv2.circle(img, (x_esq2, y_esq2), 5, (255, 0, 0), 2)
   cv2.circle(img, (x_esq3, y_esq3), 5, (255, 0, 0), 2)
   cv2.circle(img, (x_esq4, y_esq4), 5, (255, 0, 0), 2)
   '''
   '''
   print(x_esq4, y_esq4)
   print(x_esq3, y_esq3)
   print(x_esq2, y_esq2)
   print(x_esq1, y_esq1)
   print(x_esq0, y_esq0)
   print()
   '''
   return x_esq0, x_esq1, x_esq2, x_esq3, x_esq4

    
def definePontosBordaDir(img, x_dir0, x_dir1, x_dir2, x_dir3, x_dir4):
    
    if( (x_dir0 != 0 and x_dir1 == 0 and x_dir2 == 0 and x_dir3 == 0 and x_dir4 == 0) or
       (x_dir0 == 0 and x_dir1 != 0 and x_dir2 == 0 and x_dir3 == 0 and x_dir4 == 0) or
       (x_dir0 == 0 and x_dir1 == 0 and x_dir2 != 0 and x_dir3 == 0 and x_dir4 == 0) or
       (x_dir0 == 0 and x_dir1 == 0 and x_dir2 == 0 and x_dir3 != 0 and x_dir4 == 0) or
       (x_dir0 == 0 and x_dir1 == 0 and x_dir2 == 0 and x_dir3 == 0 and x_dir4 != 0)):
       x_dir0 = x_dir1 = x_dir2 = x_dir3 = x_dir4 = 0
    
    
    
    if(x_dir0 != 0 and x_dir1 != 0 and x_dir2 != 0 and x_dir3 != 0 and x_dir4 == 0):
        x_dir4 = int((x_dir0 + x_dir1 + x_dir2 + x_dir3)/4)
        
    if(x_dir0 != 0 and x_dir1 != 0 and x_dir2 != 0 and x_dir3 == 0 and x_dir4 != 0):
        x_dir3 = int((x_dir0 + x_dir1 + x_dir2 + x_dir4)/4)
        
    if(x_dir0 != 0 and x_dir1 != 0 and x_dir2 == 0 and x_dir3 != 0 and x_dir4 != 0):
        x_dir2 = int((x_dir0 + x_dir1 + x_dir3 + x_dir4)/4)  
        
    if(x_dir0 != 0 and x_dir1 == 0 and x_dir2 != 0 and x_dir3 != 0 and x_dir4 != 0):
        x_dir1 = int((x_dir0 + x_dir2 + x_dir3 + x_dir4)/4)  
  
    if(x_dir0 == 0 and x_dir1 != 0 and x_dir2 != 0 and x_dir3 != 0 and x_dir4 != 0):
        x_dir0 = int((x_dir1 + x_dir2 + x_dir3 + x_dir4)/4)
        
        
        
    if(x_dir4 > (x_dir0 + x_dir1 + x_dir2)):
       x_dir4 = int(((x_dir0 + x_dir1 + x_dir2)/3) - 15)
    
    if(x_dir3 > (x_dir0 + x_dir1 + x_dir2)):
       x_dir3 = int(((x_dir0 + x_dir1 + x_dir2)/3) - 15)
      
    '''
    cv2.circle(img, (x_dir0, y_dir0), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_dir1, y_dir1), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_dir2, y_dir2), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_dir3, y_dir3), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_dir4, y_dir4), 5, (255, 0, 0), 2)
    '''
    #print(x_esq0, x_esq1, x_esq2, x_esq3, x_esq4)
    #print()
    
    return x_dir0, x_dir1, x_dir2, x_dir3, x_dir4


def areaDeteccao(img, x_esq0, y_esq0, x_esq1, y_esq1, x_esq2, y_esq2, x_esq3, y_esq3, x_esq4, y_esq4, x_dir0, y_dir0, x_dir1, y_dir1, x_dir2, y_dir2, x_dir3, y_dir3, x_dir4, y_dir4):
      
    cv2.circle(img, (x_esq0, y_esq0), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_esq1, y_esq1), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_esq2, y_esq2), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_esq3, y_esq3), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_esq4, y_esq4), 5, (255, 0, 0), 2)
   
    cv2.circle(img, (x_dir0, y_dir0), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_dir1, y_dir1), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_dir2, y_dir2), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_dir3, y_dir3), 5, (255, 0, 0), 2)
    cv2.circle(img, (x_dir4, y_dir4), 5, (255, 0, 0), 2)
     
    
    cv2.line(img, (x_esq4, y_esq4), (x_dir4, y_dir4), (255, 0, 0), 2)
    cv2.line(img, (x_esq3, y_esq3), (x_dir3, y_dir3), (255, 0, 0), 2)
    cv2.line(img, (x_esq2, y_esq2), (x_dir2, y_dir2), (255, 0, 0), 2)
    cv2.line(img, (x_esq1, y_esq1), (x_dir1, y_dir1), (255, 0, 0), 2)
    cv2.line(img, (x_esq0, y_esq0), (x_dir0, y_dir0), (255, 0, 0), 2)
    
    
    cv2.line(img, (x_esq4, y_esq4), (x_esq3, y_esq3), (255, 0, 0), 2)
    cv2.line(img, (x_esq3, y_esq3), (x_esq2, y_esq2), (255, 0, 0), 2)
    cv2.line(img, (x_esq2, y_esq2), (x_esq1, y_esq1), (255, 0, 0), 2)
    cv2.line(img, (x_esq1, y_esq1), (x_esq0, y_esq0), (255, 0, 0), 2)
    
    cv2.line(img, (x_dir4, y_dir4), (x_dir3, y_dir3), (255, 0, 0), 2)
    cv2.line(img, (x_dir3, y_dir3), (x_dir2, y_dir2), (255, 0, 0), 2)
    cv2.line(img, (x_dir2, y_dir2), (x_dir1, y_dir1), (255, 0, 0), 2)
    cv2.line(img, (x_dir1, y_dir1), (x_dir0, y_dir0), (255, 0, 0), 2)
    
    
def definePontosVerticais(img):
    X_LIM_E = 300
    X_LIM_C = 340
    X_LIM_D = 380
    
    contPtE = contPtC = contPtD = 0
    tamanhoLinha = 280
    
    x_final, y_final = 340, 419
    
    for ye in range(419, 279, -1):
        canalCoresPtE = img[ye, X_LIM_E]      
        if canalCoresPtE <= 250:
            #img[ye, X_LIM_E] = 255
            contPtE += 1
        else:
            break
        
    for yc in range(419, 279, -1):
        canalCoresPtC = img[yc, X_LIM_C]
        if canalCoresPtC <= 250:
            #img[yc, X_LIM_C] = 255
            contPtC += 1
        else:
            break
        
    for yd in range(419, 279, -1):
        canalCoresPtD = img[yd, X_LIM_D]
        if canalCoresPtD <= 250:
            #img[yd, X_LIM_D] = 255
            contPtD += 1
        else:
            break
        
    if contPtE == 140 and contPtC == 140 and contPtD == 140:
        #print("Condições normais para detecção das bordas.")
        x_final, y_final = X_LIM_C, yc
        tamanhoLinha = contPtC
        
    elif(contPtE > contPtC and contPtC > contPtD):
        #print("Provável situação de curva para esquerda.")
        x_final, y_final = X_LIM_E, ye
        tamanhoLinha = contPtE
               
    elif(contPtE == 140 and contPtC == 140 and contPtD < 140):
        #print("E e C iguais. D diferente!")
        x_final, y_final = X_LIM_C, yc
        tamanhoLinha = contPtC
        
    elif(contPtE == 140 and contPtC < 140 and contPtD < 140):
        #print("Definindo com E")
        x_final, y_final = X_LIM_E, ye
        tamanhoLinha = contPtE
        
    elif(contPtE < 140 and contPtC == 140 and contPtD < 140):
        #print("Definindo com E")
        x_final, y_final = X_LIM_C, yc
        tamanhoLinha = contPtC
        
    elif(contPtE < 140 and contPtC < 140 and contPtD == 140):
        #print("Definindo com D")
        x_final, y_final = X_LIM_D, yd
        tamanhoLinha = contPtD
    else:
        #print("Falha!")
        x_final, y_final = 340, 419
        tamanhoLinha = 5
 
        
    if(contPtE <= 80 and contPtC <= 80 and contPtD <= 80):
        #print("Impossível criar area para detectar obstáculos!")
        x_final, y_final = 340, 419
        tamanhoLinha = 5
    
    
    #print(x_final, y_final)
    #print(contPtE, contPtC, contPtD)
    #print()
    
    return x_final, y_final, tamanhoLinha

def camadasEsqMetodo1(img, x, y0, y1, y2, y3, y4):  
    
    contCMD0 = contCMD1 = contCMD2 = contCMD3 = contCMD4 = 0
    
    for xe in range(x, 0, -1):
        canalCoresXE = img[y0, xe]    
        
        if canalCoresXE < 200 :
            img[y0, xe] = 255
            contCMD0 += 1
        else:
            break
        
    for xe in range(x, 0, -1):
        canalCoresXE = img[y1, xe]    
        
        if canalCoresXE < 200 :
            img[y1, xe] = 255
            contCMD1 += 1
        else:
            break
        
        
    for xe in range(x, 0, -1):
        canalCoresXE = img[y2, xe]    
        
        if canalCoresXE < 200 :
            img[y2, xe] = 255
            contCMD2 += 1
        else:
            break
        
    for xe in range(x, 0, -1):
        canalCoresXE = img[y3, xe]    
        
        if canalCoresXE < 200 :
            img[y3, xe] = 255
            contCMD3 += 1
        else:
            break
        
    for xe in range(x, 0, -1):
        canalCoresXE = img[y4, xe]    
        
        if canalCoresXE < 200 :
            img[y4, xe] = 255
            contCMD4 += 1
        else:
            break
   
def camadasDirMetodo1(img, x, y0, y1, y2, y3, y4): 
    
    xCMD0 = xCMD1 = xCMD2 = xCMD3 = xCMD4 = 340
    yCMD0 = yCMD1 = yCMD2 = yCMD3 = yCMD4 = 419
    
    contCMD0 = contCMD1 = contCMD2 = contCMD3 = contCMD4 = 0
    
    for xd in range(x, 680):
        canalCoresXD = img[y0, xd]    
        
        if canalCoresXD < 200 :
            img[y0, xd] = 255
            contCMD0 += 1
        else:
            xCMD0 = xd
            yCMD0 = y0
            break
        
    for xd in range(x, 680):
        canalCoresXD = img[y1, xd]    
        
        if canalCoresXD < 200 :
            img[y1, xd] = 255
            contCMD1 += 1
        else:
            xCMD1 = xd
            yCMD1 = y1
            break
        
        
    for xd in range(x, 680):
        canalCoresXD = img[y2, xd]    
        
        if canalCoresXD < 200 :
            img[y2, xd] = 255
            contCMD2 += 1
        else:
            xCMD2 = xd
            yCMD2 = y2
            break
        
    for xd in range(x, 680):
        canalCoresXD = img[y3, xd]    
        
        if canalCoresXD < 200 :
            img[y3, xd] = 255
            contCMD3 += 1
        else:
            xCMD3 = xd
            yCMD3 = y3
            break
        
    for xd in range(x, 680):
        canalCoresXD = img[y4, xd]    
        
        if canalCoresXD < 200 :
            img[y4, xd] = 255
            contCMD4 += 1
        else:
            xCMD4 = xd
            yCMD4 = y4
            break
        
    print(contCMD0, contCMD1, contCMD2, contCMD3, contCMD4)
    print(xCMD0, yCMD0)
    print(xCMD1, yCMD1)
    print(xCMD2, yCMD2)
    print(xCMD3, yCMD3)
    print(xCMD4, yCMD4)
    print()


def camadasEsqMetodo2(img):
    xp0, yp0 = xb0, yb0 = 0, Y0 
    xp1, yp1 = xb1, yb1 = 0, Y1 
    xp2, yp2 = xb2, yb2 = 0, Y2 
    xp3, yp3 = xb3, yb3 = 0, Y3 
    xp4, yp4 = xb4, yb4 = 0, Y4 
    
    cont_p0 = cont_p1 = cont_p2 = cont_p3 = cont_p4 = 0
    cont_b0 = cont_b1 = cont_b2 = cont_b3 = cont_b4 = 0
    
    for x in range(1, 339):
        canalCoresXE = img[Y0, x]  
        if canalCoresXE < 240:
            img[Y0, x]  = 255
            cont_p0 += 1
        else:
            xp0 = x 
            yp0 = Y0
            for x in range(x, 339):
                canalCoresXE = img[Y0, x]  
                if canalCoresXE > 240:
                    img[Y0, x] = 0
                    cont_b0 += 1
                else:
                    xb0 = x 
                    yb0 = Y0
                    break
            break
        
    for x in range(1, 339):
        canalCoresXE = img[Y1, x]  
        if canalCoresXE < 240:
            img[Y1, x]  = 255
            cont_p1 += 1
        else:
            xp1 = x 
            yp1 = Y1
            for x in range(x, 339):
                canalCoresXE = img[Y1, x]  
                if canalCoresXE > 240:
                    img[Y1, x] = 0
                    cont_b1 += 1
                else:
                    xb1 = x 
                    yb1 = Y1
                    break
            break
        
    for x in range(1, 339):
        canalCoresXE = img[Y2, x]  
        if canalCoresXE < 240:
            img[Y2, x]  = 255
            cont_p2 += 1
        else:
            xp2 = x 
            yp2 = Y2
            for x in range(x, 339):
                canalCoresXE = img[Y2, x]  
                if canalCoresXE > 240:
                    img[Y2, x] = 0
                    cont_b2 += 1
                else:
                    xb2 = x 
                    yb2 = Y2
                    break
            break
        
        
    for x in range(1, 339):
        canalCoresXE = img[Y3, x]  
        if canalCoresXE < 240:
            img[Y3, x]  = 255
            cont_p3 += 1
        else:
            xp3 = x 
            yp3 = Y3
            for x in range(x, 339):
                canalCoresXE = img[Y3, x]  
                if canalCoresXE > 240:
                    img[Y3, x] = 0
                    cont_b3 += 1
                else:
                    xb3 = x 
                    yb3 = Y3
                    break
            break
        
        
    for x in range(1, 339):
        canalCoresXE = img[Y4, x]  
        if canalCoresXE < 240:
            img[Y4, x]  = 255
            cont_p4 += 1
        else:
            xp4 = x 
            yp4 = Y4
            for x in range(x, 339):
                canalCoresXE = img[Y4, x]  
                if canalCoresXE > 240:
                    img[Y4, x] = 0
                    cont_b4 += 1
                else:
                    xb4 = x 
                    yb4 = Y4
                    break
            break
    
    if(cont_b0 >= 10 and cont_b0 <= 40) and (cont_p0 <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD0, yCMD0 = xb0, yb0
    elif(cont_b0 > 40) and (cont_b0 < 50) and (cont_p0 <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD0, yCMD0 = xp0, yp0
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD0, yCMD0 = 0, Y0 
        
        
    if(cont_b1 >= 15 and cont_b1 <= 40) and (cont_p1 <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD1, yCMD1 = xb1, yb1
    elif(cont_b1 > 40) and (cont_b1 < 50) and (cont_p1 <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD1, yCMD1 = xp1, yp1
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD1, yCMD1 = 0, Y1 
    
    
    if(cont_b2 >= 15 and cont_b2 <= 40) and (cont_p2 <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD2, yCMD2 = xb2, yb2
    elif(cont_b2 > 40) and (cont_b2 < 50) and (cont_p2 <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD2, yCMD2 = xp2, yp2
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD2, yCMD2 = 0, Y2 
        
    
    if(cont_b3 >= 15 and cont_b3 <= 35) and (cont_p3 <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD3, yCMD3 = xb3, yb3
    elif(cont_b3 > 35) and (cont_b3 < 50) and (cont_p3 <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD3, yCMD3 = xp3, yp3
    else:
        #print("n achou \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD3, yCMD3 = 0, Y3
        
    
    if(cont_b4 >= 10 and cont_b4 <= 40) and (cont_p4 <= 336):
        #print("achou b \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD4, yCMD4 = xb4, yb4
    elif(cont_b4 > 40) and (cont_p4 <= 336):
        #print("achou p \t{0} \t{1} \t{2} \t{3}".format(xp, yp, xb, yb))
        xCMD4, yCMD4 = xp4, yp4
    else:
        xCMD4, yCMD4 = 0, Y4
        
        
    print(xCMD0, xCMD1, xCMD2, xCMD3, xCMD4)
    print()
        
    if(xCMD0 != 0 and xCMD1 == 0 and xCMD2 == 0 and xCMD3 == 0 and xCMD4 == 0):
        xCMD0 = 0
    elif(xCMD0 == 0 and xCMD1 != 0 and xCMD2 == 0 and xCMD3 == 0 and xCMD4 == 0):
        xCMD1 = 0
    elif(xCMD0 == 0 and xCMD1 == 0 and xCMD2 != 0 and xCMD3 == 0 and xCMD4 == 0):
        xCMD2 = 0
    elif(xCMD0 == 0 and xCMD1 == 0 and xCMD2 == 0 and xCMD3 != 0 and xCMD4 == 0):
        xCMD3 = 0
    elif(xCMD0 == 0 and xCMD1 == 0 and xCMD2 == 0 and xCMD3 == 0 and xCMD4 != 0):
        xCMD4 = 0    

    print(xCMD0, yCMD0)
    print(xCMD1, yCMD1)
    print(xCMD2, yCMD2)
    print(xCMD3, yCMD3)
    print(xCMD4, yCMD4)
    print()
    
    return xCMD0, yCMD0, xCMD1, yCMD1, xCMD2, yCMD2, xCMD3, yCMD3, xCMD4, yCMD4



try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0)
        imagem_tresh = cv2.inRange(imagem_blur, 220, 255) 
          

        x, y, tamanhoLinha = definePontosVerticais(imagem_tresh)
       
        parte_y = int(tamanhoLinha/5)
        
        y0 = 419 - parte_y * 5 
        y1 = 419 - parte_y * 4
        y2 = 419 - parte_y * 3
        y3 = 419 - parte_y * 2
        y4 = 419 - parte_y
        
        #print( x, y, tamanhoLinha)
        #print(y0, y1, y2, y3, y4)
        
        camadasEsqMetodo2(imagem_tresh)
        
        
        '''
        if tamanhoLinha > 5:
            camadasEsqMetodo1(imagem_tresh, (x-1), y0, y1, y2, y3, y4)
            camadasDirMetodo1(imagem_tresh, (x+1), y0, y1, y2, y3, y4)
        else:
          pass
            
            x_esq0, y_esq0 = detectaBordaEsqCMD0(imagem_tresh)
            x_esq1, y_esq1 = detectaBordaEsqCMD1(imagem_tresh)
            x_esq2, y_esq2 = detectaBordaEsqCMD2(imagem_tresh)
            x_esq3, y_esq3 = detectaBordaEsqCMD3(imagem_tresh)
            x_esq4, y_esq4 = detectaBordaEsqCMD4(imagem_tresh)
            
    
            x_dir0, y_dir0 = detectaBordaDirCMD0(imagem_tresh)
            x_dir1, y_dir1 = detectaBordaDirCMD1(imagem_tresh)
            x_dir2, y_dir2 = detectaBordaDirCMD2(imagem_tresh)           
            x_dir3, y_dir3 = detectaBordaDirCMD3(imagem_tresh)
            x_dir4, y_dir4 = detectaBordaDirCMD4(imagem_tresh)
            
            x_esq0, x_esq1, x_esq2, x_esq3, x_esq4 = definePontosBordaEsq(imagem, x_esq0, x_esq1, x_esq2, x_esq3, x_esq4)
            x_dir0, x_dir1, x_dir2, x_dir3, x_dir4 = definePontosBordaDir(imagem, x_dir0, x_dir1, x_dir2, x_dir3, x_dir4)

            #areaDeteccao(imagem, x_esq0, y_esq0, x_esq1, y_esq1, x_esq2, y_esq2, x_esq3, y_esq3, x_esq4, y_esq4, x_dir0, y_dir0, x_dir1, y_dir1, x_dir2, y_dir2, x_dir3, y_dir3, x_dir4, y_dir4)
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