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




tamanho_camada_0 = 0
tamanho_camada_1 = 0
tamanho_camada_2 = 0
tamanho_camada_3 = 0
tamanho_camada_4 = 0

Y_CMD_0 = 320
Y_CMD_1 = 340
Y_CMD_2 = 360
Y_CMD_3 = 380
Y_CMD_4 = 400 


def encontra_borda_dir(img):
    y_dir_cmd_0 = 0 
    x_dir_cmd_0 = 0
      
    y_dir_cmd_1 = 0 
    x_dir_cmd_1 = 0     
     
    y_dir_cmd_2 = 0 
    x_dir_cmd_2 = 0    
    
    y_dir_cmd_3 = 0 
    x_dir_cmd_3 = 0
     
    y_dir_cmd_4 = 0 
    x_dir_cmd_4 = 0
    
    cont_dir_cmd_0 = 0
    cont_dir_cmd_1 = 0
    cont_dir_cmd_2 = 0
    cont_dir_cmd_3 = 0
    cont_dir_cmd_4 = 0

    for x in range(341, 679):
        canal_borda_dir_0 = img[Y_CMD_0, x]
        if canal_borda_dir_0 <= 254:
            img[Y_CMD_0, x] = 255
            cont_dir_cmd_0 += 1
        else:
            y_dir_cmd_0 = Y_CMD_0
            x_dir_cmd_0 = x
            break
        
    for x in range(341, 679):
        canal_borda_dir_1 = img[Y_CMD_1, x]
        if canal_borda_dir_1 <= 254:
            img[Y_CMD_1, x] = 255
            cont_dir_cmd_1 += 1
        else:
            y_dir_cmd_1 = Y_CMD_1 
            x_dir_cmd_1 = x
            break
 
    for x in range(341, 679):
        canal_borda_dir_2 = img[Y_CMD_2, x]
        if canal_borda_dir_2 <= 254:
            img[Y_CMD_2, x] = 255
            cont_dir_cmd_2 += 1
        else:
            y_dir_cmd_2 = Y_CMD_2
            x_dir_cmd_2 = x
            break
        
    for x in range(341, 679):
        canal_borda_dir_3 = img[Y_CMD_3, x]
        if canal_borda_dir_3 <= 254:
            img[Y_CMD_3, x] = 255 
            cont_dir_cmd_3 += 1
        else:
            y_dir_cmd_3 = 380 
            x_dir_cmd_3 = x
            break
        
    for x in range(341, 679):
        canal_borda_dir_4 = img[Y_CMD_4, x]
        if canal_borda_dir_4 <= 254:
            img[Y_CMD_4, x] = 255
            cont_dir_cmd_4 += 1
        else:
            y_dir_cmd_4 = Y_CMD_4
            x_dir_cmd_4 = x
            break


    #print(cont_dir_cmd_0, cont_dir_cmd_1, cont_dir_cmd_2, cont_dir_cmd_3, cont_dir_cmd_4)
    return x_dir_cmd_0, y_dir_cmd_0, x_dir_cmd_1, y_dir_cmd_1, x_dir_cmd_2, y_dir_cmd_2, x_dir_cmd_3, y_dir_cmd_3, x_dir_cmd_4, y_dir_cmd_4, cont_dir_cmd_0, cont_dir_cmd_1, cont_dir_cmd_2, cont_dir_cmd_3, cont_dir_cmd_4 

    

def encontra_borda_esq(img):    
    y_esq_cmd_0 = 0 
    x_esq_cmd_0 = 0
    
    y_esq_cmd_1 = 0 
    x_esq_cmd_1 = 0
            
    y_esq_cmd_2 = 0 
    x_esq_cmd_2 = 0
            
    y_esq_cmd_3 = 0 
    x_esq_cmd_3 = 0   
            
    y_esq_cmd_4 = 0 
    x_esq_cmd_4 = 0

    cont_esq_cmd_0 = 0
    cont_esq_cmd_1 = 0
    cont_esq_cmd_2 = 0
    cont_esq_cmd_3 = 0
    cont_esq_cmd_4 = 0
          
    for x in range(339, 1, -1):
        canal_borda_esq_0 = img[Y_CMD_0, x]
        if canal_borda_esq_0 <= 254:
            img[Y_CMD_0, x] = 255 
            cont_esq_cmd_0 += 1
        else:
            y_esq_cmd_0 = Y_CMD_0 
            x_esq_cmd_0 = x
            break
        
        
    for x in range(339, 1, -1):
        canal_borda_esq_1 = img[Y_CMD_1, x]
        if canal_borda_esq_1 <= 254:
            img[Y_CMD_1, x] = 255 
            cont_esq_cmd_1 += 1
        else:
            y_esq_cmd_1 = Y_CMD_1
            x_esq_cmd_1 = x
            break
 

    for x in range(339, 1, -1):
        canal_borda_esq_2 = img[Y_CMD_2, x]
        if canal_borda_esq_2 <= 254:
            img[Y_CMD_2, x] = 255   
            cont_esq_cmd_2 += 1
        else:
            y_esq_cmd_2 = Y_CMD_2
            x_esq_cmd_2 = x
            break       
  

    for x in range(339, 1, -1):
        canal_borda_esq_3 = img[Y_CMD_3, x]
        if canal_borda_esq_3 <= 254:
            img[Y_CMD_3, x] = 255
            cont_esq_cmd_3 += 1
        else:
            y_esq_cmd_3 = Y_CMD_3
            x_esq_cmd_3 = x
            break 
        
    for x in range(339, 1, -1):
        canal_borda_esq_4 = img[Y_CMD_4, x]
        if canal_borda_esq_4 <= 254:
            img[Y_CMD_4, x] = 255
            cont_esq_cmd_4 += 1
        else:
            y_esq_cmd_4 = Y_CMD_4
            x_esq_cmd_4 = x
            break 
        
    #print(cont_esq_cmd_0, cont_esq_cmd_1, cont_esq_cmd_2, cont_esq_cmd_3, cont_esq_cmd_4)
    return x_esq_cmd_0, y_esq_cmd_0, x_esq_cmd_1, y_esq_cmd_1, x_esq_cmd_2, y_esq_cmd_2, x_esq_cmd_3, y_esq_cmd_3, x_esq_cmd_4, y_esq_cmd_4, cont_esq_cmd_0, cont_esq_cmd_1, cont_esq_cmd_2, cont_esq_cmd_3, cont_esq_cmd_4 



def detecta_obstaculos(img, x_esq_cmd_0, y_esq_cmd_0, x_esq_cmd_1, y_esq_cmd_1, x_esq_cmd_2, y_esq_cmd_2, x_esq_cmd_3, y_esq_cmd_3, x_esq_cmd_4, y_esq_cmd_4, x_dir_cmd_0, y_dir_cmd_0, x_dir_cmd_1, y_dir_cmd_1, x_dir_cmd_2, y_dir_cmd_2, x_dir_cmd_3, y_dir_cmd_3, x_dir_cmd_4, y_dir_cmd_4, cont_esq_cmd_0, cont_esq_cmd_1, cont_esq_cmd_2, cont_esq_cmd_3, cont_esq_cmd_4, cont_dir_cmd_0, cont_dir_cmd_1, cont_dir_cmd_2, cont_dir_cmd_3, cont_dir_cmd_4):
    for x in range(x_dir_cmd_0, x_esq_cmd_0, -1):
        print(img[Y_CMD_0, x])
        img[Y_CMD_0, x] = 255
    
    
    


try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0)
        imagem_tresh = cv2.inRange(imagem_blur,  200, 255) 
    
    
        st_esq_cmd_0 = False
        st_esq_cmd_1 = False
        st_esq_cmd_2 = False
        st_esq_cmd_3 = False
        st_esq_cmd_4 = False
        
        st_dir_cmd_0 = False
        st_dir_cmd_1 = False
        st_dir_cmd_2 = False
        st_dir_cmd_3 = False
        st_dir_cmd_4 = False

        [
        x_esq_cmd_0, y_esq_cmd_0,
        x_esq_cmd_1, y_esq_cmd_1,
        x_esq_cmd_2, y_esq_cmd_2,
        x_esq_cmd_3, y_esq_cmd_3,
        x_esq_cmd_4, y_esq_cmd_4,
        cont_esq_cmd_0, 
        cont_esq_cmd_1, 
        cont_esq_cmd_2, 
        cont_esq_cmd_3, 
        cont_esq_cmd_4 
        ]  = encontra_borda_esq(imagem_tresh)
        
        [
        x_dir_cmd_0, y_dir_cmd_0,
        x_dir_cmd_1, y_dir_cmd_1,
        x_dir_cmd_2, y_dir_cmd_2,
        x_dir_cmd_3, y_dir_cmd_3,
        x_dir_cmd_4, y_dir_cmd_4,
        cont_dir_cmd_0, 
        cont_dir_cmd_1, 
        cont_dir_cmd_2, 
        cont_dir_cmd_3, 
        cont_dir_cmd_4 
        ] = encontra_borda_dir(imagem_tresh)
        
        
        
        if cont_esq_cmd_0 > 10 and cont_esq_cmd_0 < 335: 
            cv2.line(imagem, (x_esq_cmd_0, y_esq_cmd_0), (340,419), (255,0,0), 2)
            st_esq_cmd_0 = True
        elif cont_esq_cmd_0 > 335:
            cv2.line(imagem, (x_esq_cmd_0, Y_CMD_0), (340,419), (255,0,0), 2)
            st_esq_cmd_0 = True
            
        if cont_esq_cmd_1 > 10 and cont_esq_cmd_1 < 335:    
           cv2.line(imagem, (x_esq_cmd_1, y_esq_cmd_1), (340,419), (255,0,0), 2)
           st_esq_cmd_1 = True
        elif cont_esq_cmd_1 > 335:
            cv2.line(imagem, (x_esq_cmd_1, Y_CMD_1), (340,419), (255,0,0), 2)
            st_esq_cmd_1 = True
        
        if cont_esq_cmd_2 > 10 and cont_esq_cmd_2 < 335: 
            cv2.line(imagem, (x_esq_cmd_2, y_esq_cmd_2), (340,419), (255,0,0), 2)
            st_esq_cmd_2 = True
        elif cont_esq_cmd_2 >= 335:
            cv2.line(imagem, (x_esq_cmd_2, Y_CMD_2), (340,419), (255,0,0), 2)
            st_esq_cmd_2 = True
        
        
        if cont_esq_cmd_3 > 10 and cont_esq_cmd_3 < 335:
            cv2.line(imagem, (x_esq_cmd_3, y_esq_cmd_3), (340,419), (255,0,0), 2)
            st_esq_cmd_3 = True
        elif cont_esq_cmd_3 > 335:
            cv2.line(imagem, (x_esq_cmd_3, Y_CMD_3), (340,419), (255,0,0), 2)
            st_esq_cmd_3 = True
        
        if cont_esq_cmd_4 > 10 and cont_esq_cmd_4 < 335:
            cv2.line(imagem, (x_esq_cmd_4, y_esq_cmd_4), (340,419), (255,0,0), 2)
            st_esq_cmd_4 = True
        elif cont_esq_cmd_4 > 335:
            cv2.line(imagem, (x_esq_cmd_4, Y_CMD_4), (340,419), (255,0,0), 2)
            st_esq_cmd_4 = True
        
        
        
        
        
        if cont_dir_cmd_0 > 10 and cont_dir_cmd_0 < 300: 
            cv2.line(imagem, (x_dir_cmd_0, y_dir_cmd_0), (340,419), (255,0,0), 2)
            st_dir_cmd_0 = True
        else:
            pass
        
        if cont_dir_cmd_1 > 10 and cont_dir_cmd_1 < 300: 
            cv2.line(imagem, (x_dir_cmd_1, y_dir_cmd_1), (340,419), (255,0,0), 2)
            st_dir_cmd_1 = True
            
        if cont_dir_cmd_2 > 10 and cont_dir_cmd_2 < 300: 
            cv2.line(imagem, (x_dir_cmd_2, y_dir_cmd_2), (340,419), (255,0,0), 2)
            st_dir_cmd_2 = True
            
        if cont_dir_cmd_3 > 10 and cont_dir_cmd_3 < 300: 
            cv2.line(imagem, (x_dir_cmd_3, y_dir_cmd_3), (340,419), (255,0,0), 2)
            st_dir_cmd_3 = True
            
        if cont_dir_cmd_4 > 10 and cont_dir_cmd_4 < 300: 
            cv2.line(imagem, (x_dir_cmd_4, y_dir_cmd_4), (340,419), (255,0,0), 2)
            st_dir_cmd_4 = True
        
        
        
        
        print()
        if ((st_esq_cmd_0 is True and st_esq_cmd_1 is True and st_esq_cmd_2 is True and st_esq_cmd_3 is True and st_esq_cmd_4 is True) and
            (st_dir_cmd_0 is True and st_dir_cmd_1 is True and st_dir_cmd_2 is True and st_dir_cmd_3 is True and st_dir_cmd_4 is True)):
            detecta_obstaculos(
                                imagem_cinza, 
                                x_esq_cmd_0, y_esq_cmd_0, 
                                x_esq_cmd_1, y_esq_cmd_1, 
                                x_esq_cmd_2, y_esq_cmd_2, 
                                x_esq_cmd_3, y_esq_cmd_3, 
                                x_esq_cmd_4, y_esq_cmd_4, 
                                x_dir_cmd_0, y_dir_cmd_0, 
                                x_dir_cmd_1, y_dir_cmd_1, 
                                x_dir_cmd_2, y_dir_cmd_2, 
                                x_dir_cmd_3, y_dir_cmd_3, 
                                x_dir_cmd_4, y_dir_cmd_4,
                                cont_esq_cmd_0, 
                                cont_esq_cmd_1, 
                                cont_esq_cmd_2, 
                                cont_esq_cmd_3, 
                                cont_esq_cmd_4, 
                                cont_dir_cmd_0, 
                                cont_dir_cmd_1, 
                                cont_dir_cmd_2, 
                                cont_dir_cmd_3, 
                                cont_dir_cmd_4 
                               )
            
   
        
        
        if (st_dir_cmd_0 is False and st_dir_cmd_1 is True and st_dir_cmd_2 is True and st_dir_cmd_3 is True and st_dir_cmd_4 is True):
           pass

            
            
            
       
    
        cv2.imshow("Imagem Pista", imagem)
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
imagem_tresh = cv2.inRange(imagem_blur,  220, 255) 


for x in range(341, 679):
    #camada_0 = imagem[320, x] 
    imagem_tresh[320, x] = 255



cv2.imshow("Imagem tresh", imagem_tresh)
cv2.waitKey(0)

cv2.destroyAllWindows()
'''