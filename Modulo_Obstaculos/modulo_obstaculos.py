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



Y0 = 400
Y1 = 370
Y2 = 340
Y3 = 310
Y4 = 280

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

    
 
def camadasEsq(img, x, y0, y1, y2, y3, y4):   
    for xe in range(x, 0, -1):
        canalCoresXE = img[y0, xe]    
        
        if canalCoresXE < 200 :
            img[y0, xe] = 255
        else:
            break
        
    for xe in range(x, 0, -1):
        canalCoresXE = img[y1, xe]    
        
        if canalCoresXE < 200 :
            img[y1, xe] = 255
        else:
            break
        
        
    for xe in range(x, 0, -1):
        canalCoresXE = img[y2, xe]    
        
        if canalCoresXE < 200 :
            img[y2, xe] = 255
        else:
            break
        
    for xe in range(x, 0, -1):
        canalCoresXE = img[y3, xe]    
        
        if canalCoresXE < 200 :
            img[y3, xe] = 255
        else:
            break
        
    for xe in range(x, 0, -1):
        canalCoresXE = img[y4, xe]    
        
        if canalCoresXE < 200 :
            img[y4, xe] = 255
        else:
            break
      

try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0)
        imagem_tresh = cv2.inRange(imagem_blur,  215, 255) 
          
        '''
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

        areaDeteccao(imagem, x_esq0, y_esq0, x_esq1, y_esq1, x_esq2, y_esq2, x_esq3, y_esq3, x_esq4, y_esq4, x_dir0, y_dir0, x_dir1, y_dir1, x_dir2, y_dir2, x_dir3, y_dir3, x_dir4, y_dir4)
        '''
        

        x, y, tamanhoLinha = definePontosVerticais(imagem_tresh)
       
        parte_y = int(tamanhoLinha/5)
        
        y0 = 419 - parte_y 
        y1 = 419 - parte_y * 2
        y2 = 419 - parte_y * 3
        y3 = 419 - parte_y * 4
        y4 = 419 - parte_y * 5
        
        print( x, y, tamanhoLinha)
        #print(y0, y1, y2, y3, y4)
        

        camadasEsq(imagem_tresh, x, y0, y1, y2, y3, y4)

        
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