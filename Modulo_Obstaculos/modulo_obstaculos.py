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



def encontra_bordas(img):
    tam_cam_esq_0 = 0
    tam_cam_esq_1 = 0
    tam_cam_esq_2 = 0
    tam_cam_esq_3 = 0
    tam_cam_esq_4 = 0
    
    tam_cam_dir_0 = 0
    tam_cam_dir_1 = 0
    tam_cam_dir_2 = 0
    tam_cam_dir_3 = 0
    tam_cam_dir_4 = 0
    
    enc_borda_esq_cmd_0 = False
    enc_borda_dir_cmd_0 = False
    
    ref_y_borda_dir_cmd_0 = 0 
    ref_x_borda_dir_cmd_0 = 0
            
    ref_y_borda_esq_cmd_0 = 0 
    ref_x_borda_esq_cmd_0 = 0
    
    
    ref_y_borda_dir_cmd_1 = 0 
    ref_x_borda_dir_cmd_1 = 0
            
    ref_y_borda_esq_cmd_1 = 0 
    ref_x_borda_esq_cmd_1 = 0
    
    
    ref_y_borda_dir_cmd_2 = 0 
    ref_x_borda_dir_cmd_2 = 0
            
    ref_y_borda_esq_cmd_2 = 0 
    ref_x_borda_esq_cmd_2 = 0
    
    
    ref_y_borda_dir_cmd_3 = 0 
    ref_x_borda_dir_cmd_3 = 0
            
    ref_y_borda_esq_cmd_3 = 0 
    ref_x_borda_esq_cmd_3 = 0   
    
    
    ref_y_borda_dir_cmd_4 = 0 
    ref_x_borda_dir_cmd_4 = 0
            
    ref_y_borda_esq_cmd_4 = 0 
    ref_x_borda_esq_cmd_4 = 0
    ############ Direita ############
    for x in range(341, 679):
        canal_borda_dir_0 = img[320, x]
        if canal_borda_dir_0 <= 254:
            img[320, x] = 255   
        else:
            enc_borda_dir_cmd_0 = True
            ref_y_borda_dir_cmd_0 = 320 
            ref_x_borda_dir_cmd_0 = x
            break
        
    for x in range(341, 679):
        canal_borda_dir_1 = img[340, x]
        if canal_borda_dir_1 <= 254:
            img[340, x] = 255   
        else:
            enc_borda_dir_cmd_1 = True
            ref_y_borda_dir_cmd_1 = 340 
            ref_x_borda_dir_cmd_1 = x
            break
 
    for x in range(341, 679):
        canal_borda_dir_2 = img[360, x]
        if canal_borda_dir_2 <= 254:
            img[360, x] = 255   
        else:
            enc_borda_dir_cmd_2 = True
            ref_y_borda_dir_cmd_2 = 360 
            ref_x_borda_dir_cmd_2 = x
            break
        
    for x in range(341, 679):
        canal_borda_dir_3 = img[380, x]
        if canal_borda_dir_3 <= 254:
            img[380, x] = 255   
        else:
            enc_borda_dir_cmd_3 = True
            ref_y_borda_dir_cmd_3 = 380 
            ref_x_borda_dir_cmd_3 = x
            break
        
    for x in range(341, 679):
        canal_borda_dir_4 = img[400, x]
        if canal_borda_dir_4 <= 254:
            img[400, x] = 255   
        else:
            enc_borda_dir_cmd_4 = True
            ref_y_borda_dir_cmd_4 = 400 
            ref_x_borda_dir_cmd_4 = x
            break
        
    ############ Esquerda ################   
    for x in range(339, 1, -1):
        canal_borda_esq_0 = img[320, x]
        if canal_borda_esq_0 <= 254:
            img[320, x] = 255   
        else:
            enc_borda_esq_cmd_0 = True
            ref_y_borda_esq_cmd_0 = 320 
            ref_x_borda_esq_cmd_0 = x
            break
        
        
    for x in range(339, 1, -1):
        canal_borda_esq_1 = img[340, x]
        if canal_borda_esq_1 <= 254:
            img[340, x] = 255   
        else:
            enc_borda_esq_cmd_1 = True
            ref_y_borda_esq_cmd_1 = 340 
            ref_x_borda_esq_cmd_1 = x
            break
 

    for x in range(339, 1, -1):
        canal_borda_esq_2 = img[360, x]
        if canal_borda_esq_2 <= 254:
            img[360, x] = 255   
        else:
            enc_borda_esq_cmd_2 = True
            ref_y_borda_esq_cmd_2 = 360 
            ref_x_borda_esq_cmd_2 = x
            break       
  

    for x in range(339, 1, -1):
        canal_borda_esq_3 = img[380, x]
        if canal_borda_esq_3 <= 254:
            img[380, x] = 255   
        else:
            enc_borda_esq_cmd_3 = True
            ref_y_borda_esq_cmd_3 = 380 
            ref_x_borda_esq_cmd_3 = x
            break 
        
    for x in range(339, 1, -1):
        canal_borda_esq_4 = img[400, x]
        if canal_borda_esq_4 <= 254:
            img[400, x] = 255   
        else:
            enc_borda_esq_cmd_4 = True
            ref_y_borda_esq_cmd_4 = 400 
            ref_x_borda_esq_cmd_4 = x
            break 


    '''
    tamanho_camada_0 = tam_cam_dir_0 + tam_cam_esq_0
    tamanho_camada_1 = tam_cam_dir_1 + tam_cam_esq_1
    tamanho_camada_2 = tam_cam_dir_2 + tam_cam_esq_2
    tamanho_camada_3 = tam_cam_dir_3 + tam_cam_esq_3
    tamanho_camada_4 = tam_cam_dir_4 + tam_cam_esq_4
    
    
    camada_ORG_0 = imagem[320, 340]
    camada_ORG_1 = imagem[340, 340]
    camada_ORG_2 = imagem[360, 340]
    camada_ORG_3 = imagem[380, 340]
    camada_ORG_4 = imagem[400, 340]
    '''

    
    #print(tam_cam_esq_0, tam_cam_dir_0, enc_borda_esq_cmd_0, enc_borda_dir_cmd_0)
    #print("CMD_0: {0} \tCMD_1: {1} \tCMD_2: {2} \tCMD_3: {3} \tCMD_4: {4}".format(tamanho_camada_0, tamanho_camada_1, tamanho_camada_2, tamanho_camada_3, tamanho_camada_4))
    #print()

    return ref_x_borda_esq_cmd_0, ref_y_borda_esq_cmd_0, ref_x_borda_esq_cmd_1, ref_y_borda_esq_cmd_1, ref_x_borda_esq_cmd_2, ref_y_borda_esq_cmd_2, ref_x_borda_esq_cmd_3, ref_y_borda_esq_cmd_3, ref_x_borda_esq_cmd_4, ref_y_borda_esq_cmd_4, ref_x_borda_dir_cmd_0, ref_y_borda_dir_cmd_0, ref_x_borda_dir_cmd_1, ref_y_borda_dir_cmd_1, ref_x_borda_dir_cmd_2, ref_y_borda_dir_cmd_2, ref_x_borda_dir_cmd_3, ref_y_borda_dir_cmd_3, ref_x_borda_dir_cmd_4, ref_y_borda_dir_cmd_4

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

try:
    for i in sorted(glob.glob(caminho_pasta)):  
        imagem = cv2.imread(i)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0)
        imagem_tresh = cv2.inRange(imagem_blur,  220, 255) 
    

        [
        ref_x_borda_esq_cmd_0, ref_y_borda_esq_cmd_0,
        ref_x_borda_esq_cmd_1, ref_y_borda_esq_cmd_1,
        ref_x_borda_esq_cmd_2, ref_y_borda_esq_cmd_2,
        ref_x_borda_esq_cmd_3, ref_y_borda_esq_cmd_3,
        ref_x_borda_esq_cmd_4, ref_y_borda_esq_cmd_4,
        
        ref_x_borda_dir_cmd_0, ref_y_borda_dir_cmd_0,
        ref_x_borda_dir_cmd_1, ref_y_borda_dir_cmd_1,
        ref_x_borda_dir_cmd_2, ref_y_borda_dir_cmd_2,
        ref_x_borda_dir_cmd_3, ref_y_borda_dir_cmd_3,
        ref_x_borda_dir_cmd_4, ref_y_borda_dir_cmd_4
        ] = encontra_bordas(imagem_tresh)
        
        
        cv2.line(imagem, (ref_x_borda_esq_cmd_0, ref_y_borda_esq_cmd_0), (340,419), (255,0,0), 2)
        cv2.line(imagem, (ref_x_borda_dir_cmd_0, ref_y_borda_dir_cmd_0), (340,419), (255,0,0), 2)

        cv2.line(imagem, (ref_x_borda_esq_cmd_1, ref_y_borda_esq_cmd_1), (340,419), (255,0,0), 2)
        cv2.line(imagem, (ref_x_borda_dir_cmd_1, ref_y_borda_dir_cmd_1), (340,419), (255,0,0), 2)
    
        cv2.line(imagem, (ref_x_borda_esq_cmd_2, ref_y_borda_esq_cmd_2), (340,419), (255,0,0), 2)
        cv2.line(imagem, (ref_x_borda_dir_cmd_2, ref_y_borda_dir_cmd_2), (340,419), (255,0,0), 2)
    
        cv2.line(imagem, (ref_x_borda_esq_cmd_3, ref_y_borda_esq_cmd_3), (340,419), (255,0,0), 2)
        cv2.line(imagem, (ref_x_borda_dir_cmd_3, ref_y_borda_dir_cmd_3), (340,419), (255,0,0), 2)
    
        cv2.line(imagem, (ref_x_borda_esq_cmd_4, ref_y_borda_esq_cmd_4), (340,419), (255,0,0), 2)
        cv2.line(imagem, (ref_x_borda_dir_cmd_4, ref_y_borda_dir_cmd_4), (340,419), (255,0,0), 2)
        
    
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

    