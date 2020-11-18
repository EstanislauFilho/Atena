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


def define_pontos(imagem):
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
    
    
    ref_y_borda_dir_cmd_3 = 0 
    ref_x_borda_dir_cmd_3 = 0
            
    ref_y_borda_esq_cmd_3 = 0 
    ref_x_borda_esq_cmd_3 = 0
    
    
    ################################ camadas da direita ####################
    for x in range(341, 679):
        B0_DIR, G0_DIR, R0_DIR = imagem[320, x] 
        if B0_DIR  <= 254 and G0_DIR  <= 254 and R0_DIR <= 254:
            imagem[320, x] = 255, 255, 255
            tam_cam_dir_0 += 1
        else:
            enc_borda_dir_cmd_0 = True
            ref_y_borda_dir_cmd_0 = 320 
            ref_x_borda_dir_cmd_0 = x
            break
    
    
    for x in range(341, 679):
        B1_DIR, G1_DIR, R1_DIR = imagem[340, x]
        if B1_DIR  <= 254 and G1_DIR  <= 254 and R1_DIR <= 254:
            imagem[340, x] = 255, 255, 255
            tam_cam_dir_1 += 1
        else:
            break
      
        
    for x in range(341, 679):
        B2_DIR, G2_DIR, R2_DIR = imagem[360, x]   
        if B2_DIR  <= 254 and G2_DIR  <= 254 and R2_DIR <= 254:
            imagem[360, x] = 255, 255, 255
            tam_cam_dir_2 += 1
        else:
            break
    
    
    for x in range(341, 679):
        B3_DIR, G3_DIR, R3_DIR = imagem[380, x]
        if B3_DIR  <= 254 and G3_DIR  <= 254 and R3_DIR <= 254:
            imagem[380, x] = 255, 255, 255
            tam_cam_dir_3 += 1
        else:
            ref_y_borda_dir_cmd_3 = 380 
            ref_x_borda_dir_cmd_3 = x
            break
    
    
    for x in range(341, 679):
        B4_DIR, G4_DIR, R4_DIR = imagem[400, x]
        if B4_DIR  <= 254 and G4_DIR  <= 254 and R4_DIR <= 254:
            imagem[400, x] = 255, 255, 255
            tam_cam_dir_4 += 1
        else:
            break
    
    ############################## camadas da esquerda ########################   
    for x in range(339, 1, -1):
        B0_ESQ, G0_ESQ, R0_ESQ = imagem[320, x] 
        if B0_ESQ  <= 254 and G0_ESQ  <= 254 and R0_ESQ <= 254:
            imagem[320, x] = 255, 255, 255
            tam_cam_esq_0 += 1
        else:
            enc_borda_esq_cmd_0 = True
            ref_y_borda_esq_cmd_0 = 320 
            ref_x_borda_esq_cmd_0 = x
            break
    
    
    for x in range(339, 1, -1):
        B1_ESQ, G1_ESQ, R1_ESQ = imagem[340, x]
        if B1_ESQ  <= 254 and G1_ESQ  <= 254 and R1_ESQ <= 254:
            imagem[340, x] = 255, 255, 255
            tam_cam_esq_1 += 1
        else:
            break
      
        
    for x in range(339, 1, -1):
        B2_ESQ, G2_ESQ, R2_ESQ = imagem[360, x]   
        if B2_ESQ  <= 254 and G2_ESQ  <= 254 and R2_ESQ <= 254:
            imagem[360, x] = 255, 255, 255
            tam_cam_esq_2 += 1
        else:
            break
    
    
    for x in range(339, 1, -1):
        B3_ESQ, G3_ESQ, R3_ESQ = imagem[380, x]
        if B3_ESQ  <= 254 and G3_ESQ  <= 254 and R3_ESQ <= 254:
            imagem[380, x] = 255, 255, 255
            tam_cam_esq_3 += 1
        else:
            ref_y_borda_esq_cmd_3 = 380 
            ref_x_borda_esq_cmd_3 = x
            break
    
    
    for x in range(339, 1, -1):
        B4_ESQ, G4_ESQ, R4_ESQ = imagem[400, x]
        if B4_ESQ  <= 254 and G4_ESQ  <= 254 and R4_ESQ <= 254:
            imagem[400, x] = 255, 255, 255
            tam_cam_esq_4 += 1
        else:
            break
    
    tamanho_camada_0 = tam_cam_dir_0 + tam_cam_esq_0
    tamanho_camada_1 = tam_cam_dir_1 + tam_cam_esq_1
    tamanho_camada_2 = tam_cam_dir_2 + tam_cam_esq_2
    tamanho_camada_3 = tam_cam_dir_3 + tam_cam_esq_3
    tamanho_camada_4 = tam_cam_dir_4 + tam_cam_esq_4
    
    
    B0_ORG, G0_ORG, R0_ORG = imagem[320, 340]
    B1_ORG, G1_ORG, R1_ORG = imagem[340, 340]
    B2_ORG, G2_ORG, R2_ORG = imagem[360, 340]
    B3_ORG, G3_ORG, R3_ORG = imagem[380, 340]
    B4_ORG, G4_ORG, R4_ORG = imagem[400, 340]
    
    imagem[320, 340] = 0, 0, 255
    imagem[340, 340] = 0, 0, 255
    imagem[360, 340] = 0, 0, 255
    imagem[380, 340] = 0, 0, 255
    imagem[400, 340] = 0, 0, 255
    '''
    print(B0_ORG, G0_ORG, R0_ORG)
    print(B1_ORG, G1_ORG, R1_ORG)
    print(B2_ORG, G2_ORG, R2_ORG)
    print(B3_ORG, G3_ORG, R3_ORG)
    print(B4_ORG, G4_ORG, R4_ORG)
    
    #print(tam_cam_esq_0, tam_cam_dir_0, enc_borda_esq_cmd_0, enc_borda_dir_cmd_0)
    #print("CMD_0: {0} \tCMD_1: {1} \tCMD_2: {2} \tCMD_3: {3} \tCMD_4: {4}".format(tamanho_camada_0, tamanho_camada_1, tamanho_camada_2, tamanho_camada_3, tamanho_camada_4))
    print()
    '''
    
    #cv2.line(imagem, (ref_x_borda_esq_cmd_0,ref_y_borda_esq_cmd_0), (340,419), (255,0,0), 2)
    #cv2.line(imagem, (ref_x_borda_dir_cmd_0,ref_y_borda_dir_cmd_0), (340,419), (255,0,0), 2)

    
    #cv2.line(imagem, (ref_x_borda_esq_cmd_3,ref_y_borda_esq_cmd_3), (340,419), (255,0,0), 2)
    #cv2.line(imagem, (ref_x_borda_dir_cmd_3,ref_y_borda_dir_cmd_3), (340,419), (255,0,0), 2)


''''
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

    